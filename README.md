clean-rg-pdf 
============

A tool to strip ResearchGate modifications from a PDF file.

Background
----------

ResearchGate provides a useful repository for PDFs of research articles.
However, articles uploaded to ResearchGate are subjected to some
processing before being made available for download: a cover page is
inserted with links to ResearchGate pages for the authors. This is easy
to remove using a tool such as pdftk. More recently, a more pervasive
modification has been applied: the text of the entire paper is
processed, and any citation or reference is turned into a link to the
corresponding ResearchGate page for the article (or, when ResearchGate
doesn't have a page for the article, a link to ResearchGate's home
page). For these links to work, the user must have a ResearchGate
account and be logged in. They are distractingly marked with a thick
blue underline, producing a particularly striking effect in the list of
references. They supplant any original links to which the same text
originally pointed (for example, a DOI link to a referenced article, or
a link from citation to reference). The process also deactivates
non-citation links within the article -- so, for instance, internal
links to figures and URL links to websites stop working.

In short: ResearchGate damages PDFs uploaded to their website. This
program attempts to undo some of the damage.

What clean-rg-pdf does
----------------------

clean-rg-pdf removes the cover page, blue underlining, and ResearchGate
links from a PDF processed by ResearchGate. Unfortunately it's difficult
or impossible to fully undo the damage: links in the original PDF are
probably gone for good. clean-rg-pdf should at least make the document
*look* like the original, even if it doesn't work quite as well.

Usage
-----

    clean-rg-pdf.py <input-file> <output-file>

Details
-------

clean-rg-pdf is an extremely short Python script. The heavy lifting is
done by Patrick Maupin's pdfrw library. clean-rg-pdf depends on some
fairly specific internal formatting to find the underlinings, so will
probably stop working if ResearchGate change their PDF munging system.
It's only been tested with a small number of documents, so may even
fail on some current PDFs.

Copyright and license
---------------------

clean-rg-pdf is Copyright 2016 Pontus Lurcock (pont at talvi dot net)
and released under the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
