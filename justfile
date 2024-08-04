_default:
    @just --list

# compile thesis pdf into obj/
build:
    denv texfot latexmk -pdf -shell-escape -bibtex -f thesis.tex

# open compiled pdf
view:
    open obj/thesis.pdf
