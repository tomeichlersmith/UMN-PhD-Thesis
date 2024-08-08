_default:
    @just --list

latexmk := "denv texfot latexmk"
latexmk_opts := "-pdf -shell-escape -bibtex -f"

# compile thesis pdf into repo root directory
build:
    {{ latexmk }} {{ latexmk_opts }} thesis.tex

# have latexmk watch for changes and rebuild
watch:
    {{ latexmk }} -pvc {{ latexmk_opts }} thesis.tex

# open compiled pdf
view:
    open thesis.pdf
