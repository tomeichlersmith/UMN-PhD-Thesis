_default:
    @just --list

use_denv := env("USE_DENV", "true")
use_texfot := env("USE_TEXFOT", "false")

latexmk_prefix := if use_denv == "true" {
  "denv texfot "
} else if use_texfot == "true" {
  "texfot "
} else { 
  ""
}

latexmk_opts := "-pdf -shell-escape -bibtex -f"
latexmk := latexmk_prefix + "latexmk " + latexmk_opts

# compile thesis pdf into repo root directory
build:
    {{ latexmk }} thesis.tex

# have latexmk watch for changes and rebuild
watch:
    {{ latexmk }} -pvc thesis.tex

# open compiled pdf
view:
    open thesis.pdf
