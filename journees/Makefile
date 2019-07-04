OPTS=-shell-restricted

outputs := $(patsubst %.tex,%.pdf,$(wildcard *es.tex)) $(patsubst %.tex,%_notes.pdf,$(wildcard *es.tex)) $(patsubst %.tex,%_notes_h.pdf,$(wildcard *es.tex)) $(patsubst %.tex,%_h.pdf,$(wildcard *es.tex))

all:	$(outputs)

%.pdf:	%.tex Makefile
	xelatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer} \input{$<}"
	xelatex $(OPTS) -jobname=$(basename $<) "\documentclass[notheorems]{beamer} \input{$<}"

%_notes.pdf: %.tex Makefile
	xelatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass[notes=only,notheorems]{beamer} \input{$<}"
	xelatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass[notes=only,notheorems]{beamer} \input{$<}"

%_notes_h.pdf: %.tex Makefile
	xelatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[notes=only,handout,notheorems]{beamer} \input{$<}"
	xelatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[notes=only,handout,notheorems]{beamer} \input{$<}"

%_h.pdf: %.tex Makefile
	xelatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer} \input{$<}"
	xelatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout,notheorems]{beamer} \input{$<}"

clean:
	rm -f *.pdf
	rm -f *.log
	rm -f *.aux
	rm -f *.fdb_latexmk

.PHONY:	clean all

abstract.tex:	abstract.md
	pandoc -f markdown -t latex -o abstract.tex abstract.md
