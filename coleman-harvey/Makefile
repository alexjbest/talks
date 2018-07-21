OPTS=-shell-restricted

outputs := $(patsubst %.tex,%.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_h.pdf,$(wildcard *.tex))

all:	$(outputs)

%.pdf:	%.tex
	pdflatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer} \input{$<}"

%_h.pdf: %.tex
	pdflatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer} \input{$<}"

clean:
	rm -f *.pdf
	rm -f *.log
	rm -f *.aux
	rm -f *.fdb_latexmk

.PHONY:	clean
