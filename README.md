# University of Minnesota PhD Thesis

This repository contains the LaTeX code for my UMN PhD Thesis.

### Build Locally

One can also build this thesis with a container that already has all the latex
tools we need. I use [denv](tomeichlersmith.github.io/denv) to interact with
containers in this way, a config for `denv` is already in this repository so
one can just run the commands above without having to install anything else
if a container runner `denv` supports is already installed (e.g. docker).
```
# omit -pvc if you just want to build it once and not watch for changes
denv latexmk -pvc -pdf thesis.tex
# also given an alias within the denv
denv build_and_watch
```

## Additional Packages

The thesis template comes with some useful additional packages. They are
described below.

### `cleveref`

[`cleveref`](https://www.ctan.org/pkg/cleveref?lang=en) is a package designed
to make cross referencing easier. Unlike `\ref`, `\cref` automatically adds
the prefix required for the object being referenced. For example,
`\cref{fig:my_fig}` will produce text like "figure 1" whereas
`\ref{fig:my_fig}` would simply produce "1" and require you to fill in the
"figure".

Additionally, `cleveref` can handle multiple references at once.
`\cref{fig:my_fig,fig:my_fig2}` produces "figures 1 and 2".

In the [main thesis file](thesis_masters.tex), the following is set:

```latex
\newcommand{\creflastconjunction}{, and } % Always use the serial comma
```

This includes the serial comma in lists, so that
`\cref{fig:my_fig,fig:my_fig2,fig_other_fig}` produces "figures 1, 2, and 3"
instead of "figures 1, 2 and 3".

Additionally, the package is passed the option `noabbrev` which causes it to
print the full prefix instead of an abbreviation ("figure" vs "fig.").

### `SIunitx`

[`SIunitx`](https://www.ctan.org/pkg/siunitx?lang=en) formats SI units. It
provides the `\SI{}` command, which is used as follows:

```latex
\SI{3.8}{\tesla}
\SI{14}{\kilo\tonne}
\SI{14.6}{\meter\squared}
\SI{8}{\tera\eV}
```

There are various abbreviations for units (such as `\SI{8}{\TeV}`) and the
formatting of the numbers can be controlled in detail. Additionally, it
provides `\SIrange{1}{5}{\meter}` which produces "1m to 5m" and
`\SIlist{1;2;3}{\kelvin}` which produces "1K, 2K, and 3K".

The package also provides `\num{12345}` which will format numbers (just like
`\SI`) but without adding units. The previous example produces "12,345" for
instance.

In the [main thesis file](thesis_masters.tex), the following default options
are set:

```latex
% Configure the siunitx package
\sisetup{
    group-separator = {,}, % Use , to separate groups of digits, like 12,345
    list-final-separator = {, and } % Always use the serial comma in \SIlist
}
```

`group-separator` makes the package separate groups of digits with commas (so
12,345.0), and `list-final-separator` uses the serial comma in lists ("1K, 2K,
and 3K", not "1K, 2K and 3K").

The way in which units are displayed can also be redefined, as has been done
`\electronvolt` in [the macros file](my_definitions.tex):

```latex
% Define a better looking eV by moving the V slightly left
\DeclareSIUnit\electronvolt{e\hspace{-0.08em}V}
```

### `booktabs`

[`booktabs`](https://www.ctan.org/pkg/booktabs?lang=en) adds options to make
nicer tables. It defines `\toprule`, `\midrule`, and `\bottomrule` which add
rules of varying thickness and with additional vertical space.

An example table using these commands is shown below. The `@{}` removes extra
space on the end of the tables (so that the rules start and end flush with the
text instead of hanging over) and the `\spacerows{1.2}` command is defined in
[the macros file](my_definitions.tex) and adds extra space between the rows.

```latex
\begin{table}[h]
    \centering
    \spacerows{1.2}
    \begin{center}
        \begin{tabular}{@{}l r@{}}
            \toprule
            Mode         & Fraction $\left( \Gamma_{i} / \Gamma \right)$ \\
            \midrule
            $\Ztoqq$     & $69.91 \pm 0.06\%$ \\
            $\Ztoee$     & $3.363 \pm 0.004\%$ \\
            $\Ztomumu$   & $3.366 \pm 0.007\%$ \\
            $\Ztotautau$ & $3.370 \pm 0.008\%$ \\
            $\Ztonunu$   & $20.00 \pm 0.06\%$ \\
            \bottomrule
        \end{tabular}
        \caption{
            Selected decay modes of the Z boson.
        }
        \label{table:z_decays}
    \end{center}
\end{table}
```
