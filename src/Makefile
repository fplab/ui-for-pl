SPHINX_SOURCES := index.rst conf.py
RST_SOURCES := $(filter-out $(SPHINX_SOURCES),$(wildcard *.rst))
MATHJAX_URL := https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML
SPHINX_OUT_DIR := ../html
PDF_OUT_FILE := $(SPHINX_OUT_DIR)/eecs490notes.pdf
BUILD_DIR := ../build
SPHINX_TEX_FILE := $(wildcard $(BUILD_DIR)/*.tex)
GIT_COMMIT_HASH := $(shell git rev-parse HEAD)

default: sphinx

all: sphinx sphinx-pdf

sphinx: svg
	sphinx-build . $(SPHINX_OUT_DIR)

sphinx-pdf:
	mkdir -p $(BUILD_DIR)
	sphinx-build -b latex . $(BUILD_DIR)
	cp ../images/*.pdf $(BUILD_DIR)
	sed -i -E 's/\.svg/\.pdf/g' $(BUILD_DIR)/*.tex
	$(MAKE) sphinx-build-pdf

sphinx-build-pdf:
	$(MAKE) -C $(BUILD_DIR)
	cp $(SPHINX_TEX_FILE:.tex=.pdf) $(PDF_OUT_FILE)

pdf: $(RST_SOURCES:.rst=.pdf)

html: $(RST_SOURCES:.rst=.html) svg

svg:
	$(MAKE) -C ../images

%.html: %.rst
	rst2html.py --math-output="MathJax $(MATHJAX_URL)" --stylesheet=..//style/style.css --syntax-highlight=short $< > $@

%.pdf: %.rst
	rst2latex.py --stylesheet=../style/style.sty $< $(<:.rst=.tex)
	sed -i -E 's/\(images[^"]*\)svg/\1pdf/g' $(<:.rst=.tex)
	pdflatex $(@:.pdf=.tex)
	pdflatex $(@:.pdf=.tex)
	pdflatex $(@:.pdf=.tex)

# https://www.reddit.com/r/learnpython/comments/8dinw8/sphinx_github_pages_and_matplotlib/
publish: all
	ghp-import -n -m "publish-to-github from $(GIT_COMMIT_HASH)" -b gh-pages -p $(SPHINX_OUT_DIR)

clean:
	rm -vf *.html *.tex *.pdf *.aux *.log *.out *.toc *-E
	rm -rvf $(BUILD_DIR) $(SPHINX_OUT_DIR)
