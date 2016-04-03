#!/usr/bin/python

import re
import argparse
from pdfrw import PdfReader, PdfWriter

def main():

    parser = argparse.ArgumentParser(description="Strip ResearchGate additions from a PDF")
    parser.add_argument("infile", metavar="input-filename", type=str, nargs=1,
                        help="PDF file to process")
    parser.add_argument("outfile", metavar="output-filename", type=str, nargs=1,
                        help="name for processed output file")
    args = parser.parse_args()

    # This regular expression matches the form of the ResearchGate
    # underlinings in the content streams. We match against a truncated form
    # of the distinctive RGB triplet because it's not always given with
    # the same accuracy.
    # "0.3333333333 0.6941176471 0.9607843137"
    regex = re.compile(r"""(0\.33333[0-9]+ 0\.694117[0-9]+ 0\.960784[0-9]+ RG
\d+\.?\d* w
\d+\.?\d* \d+\.?\d* m
\d+\.?\d* \d+\.?\d* )l
S""")

    dict_pages = PdfReader(args.infile[0]).pages

    def fix_stream(contents):
        # Look for underlinings and make them invisible.
        if not hasattr(contents, "stream"):
            return
        s = contents.stream
        # We identify RG underlinings by their (hopefully unique)
        # RGB colour triplet.
        if s is not None and regex.search(s):
            # Minimal change: change the line draw commands to
            # moves, so no line is drawn. It would be more
            # satisfying to remove the stream entirely, but it's
            # simpler and safer to preserve the file structure
            # (in particular, the stream length) wherever possible.
            contents.stream = regex.sub("\\1m\nS", s)        

    for page in dict_pages:
        if "/Annots" in page:
            # Remove all annotations. This may of course cause some
            # collateral damage, but PDFs of articles don't usually have
            # annotations so probably this will just strip ResearchGate
            # links. If this becomes a problem, it should be easy to
            # identify RG annotations and remove only them.
            page.pop("/Annots")
        # There may be a stream in the Contents object and/or in its
        # children, so we check for both.
        fix_stream(page.Contents)
        for contents in page.Contents:
            fix_stream(contents)
    
    writer = PdfWriter()

    # Start at the second page to remove the ResearchGate cover sheet.
    for page in dict_pages[1:]:
        writer.addpage(page)
    writer.write(args.outfile[0])

if __name__ == "__main__":
    main()
