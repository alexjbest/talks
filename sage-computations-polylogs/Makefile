OPTS=-shell-restricted --interaction=batchmode -synctex=1

outputs := $(patsubst %.tex,%.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_notes.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_notes_h.pdf,$(wildcard *.tex)) $(patsubst %.tex,%_h.pdf,$(wildcard *.tex))

all:	$(outputs)

%_fast.pdf:	%.tex Makefile
	lualatex $(OPTS) -jobname=$(basename $<) "\documentclass{beamer}\usepackage[final]{pdfcomment} \input{$<}"

%.pdf:	%.tex Makefile
	lualatex $(OPTS) -jobname=$(basename $<) "\documentclass{beamer}\usepackage[final]{pdfcomment} \input{$<}"
	sage $(basename $<).sagetex.sage
	lualatex $(OPTS) -jobname=$(basename $<) "\documentclass{beamer}\usepackage[final]{pdfcomment} \input{$<}"

%_notes.pdf: %.tex Makefile
	lualatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass{beamer}\usepackage[draft]{pdfcomment} \input{$<}"
	sage $(basename $<)_notes.sagetex.sage
	lualatex $(OPTS) -jobname=$(basename $<)_notes "\documentclass{beamer}\usepackage[draft]{pdfcomment} \input{$<}"

%_notes_h.pdf: %.tex Makefile
	lualatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[handout]{beamer}\usepackage[draft]{pdfcomment} \input{$<}"
	sage $(basename $<)_notes_h.sagetex.sage
	lualatex $(OPTS) -jobname=$(basename $<)_notes_h "\documentclass[notes=only,handout]{beamer}\usepackage[draft]{pdfcomment} \input{$<}"

%_h.pdf: %.tex Makefile
	lualatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout]{beamer}\usepackage[final]{pdfcomment} \input{$<}"
	sage $(basename $<)_h.sagetex.sage
	lualatex $(OPTS) -jobname=$(basename $<)_h "\documentclass[handout]{beamer}\usepackage[final]{pdfcomment} \input{$<}"

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
