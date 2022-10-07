OPTS=-shell-restricted --interaction=batchmode

outputs := $(patsubst %.tex,%.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_notes.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_notes_h.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_h.pdf,$(wildcard *.tex))

all:	$(outputs)

%.pdf:	%.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer}\usepackage[final]{pdfcomment} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer}\usepackage[final]{pdfcomment} \input{$<}"

%_notes.pdf: %.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass[notheorems]{beamer}\usepackage[draft]{pdfcomment} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass[notheorems]{beamer}\usepackage[draft]{pdfcomment} \input{$<}"

%_notes_h.pdf: %.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[handout,notheorems]{beamer}\usepackage[draft]{pdfcomment} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[notes=only,handout,notheorems]{beamer}\usepackage[draft]{pdfcomment} \input{$<}"

%_h.pdf: %.tex Makefile
	pdflatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer}\usepackage[final]{pdfcomment} \input{$<}"
	pdflatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer}\usepackage[final]{pdfcomment} \input{$<}"

clean:
	rm -f *.upa
	rm -f *.snm
	rm -f *.toc
	rm -f *.out
	rm -f *.fls
	rm -f *.nav
	rm -f *.pdf
	rm -f *.log
	rm -f *.aux
	rm -f *.fdb_latexmk

.PHONY:	clean all
