# Example Alignment

The Original and Aligned detector global position and orientations
were extracted from their detector GDMLs at SLAC S3DF and then
copied here for further plot development.

- Original.csv : unaligned (survey-only) 2016 HPS detector
- Aligned.csv : aligned (Pass2) 2016 HPS detector

I then use the plotting tools of JeffersonLab/hps-align
to plot these detectors.

```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install ./hps-align
