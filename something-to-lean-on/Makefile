OPTS=-shell-restricted

outputs := $(patsubst %.tex,%.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_notes.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_notes_h.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_h.pdf,$(wildcard *.tex))

all:	img/ $(outputs)

%.pdf:	%.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer} \input{$<}"

%_notes.pdf: %.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass[notes=only,notheorems]{beamer} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass[notes=only,notheorems]{beamer} \input{$<}"

%_notes_h.pdf: %.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[notes=only,handout,notheorems]{beamer} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[notes=only,handout,notheorems]{beamer} \input{$<}"

%_h.pdf: %.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer} \input{$<}"

clean:
	rm -f *.pdf
	rm -f *.log
	rm -f *.aux
	rm -f *.fdb_latexmk

.PHONY:	clean all
