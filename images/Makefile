PDFS := $(wildcard *.pdf)

all: $(PDFS:.pdf=.svg)

%.svg: %.pdf
	pdf2svg $< $@
