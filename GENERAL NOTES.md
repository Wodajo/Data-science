 1. Sprawdz czy jest zerowa ekspresja w illuminie tam, gdzie niezerowa w nanoporze

Illumina ma wieksza przepustowosc niz nano
Dlatego potrzebujemy jakeijs normalizacji pozwalajacej ocenic, czy zero w nanoporze to konsekwencja nizszej przepustowosci nano, czy nie

2. Znajdz najbardziej ekpresowane transkrypty, zestaw ja na scatterplocie (tpm od transkryptu) i zrob regresje
(trend posluzy dla oceny punktu odciecia tpm dla illuminy ORAZ oceny foldu)

Pod stringtie:
`minimap2 -ax splice -L --split-prefix=tmp ../genome.fa covid1.fq | samtools view -bh | samtools sort -O bam > covid1_genome.bam`


 
