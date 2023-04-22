`minimap2 -ax map-ont -L --split-prefix=tmp ../ref.fa covid1.fq.gz | samtools view -bh | samtools sort -O bam > covid1.bam`

`samtools index covid1.bam`

`samtools faidx ref.fa` - raz, dla wszystkich


to samo tylko oneliner:
```
minimap2 -ax map-ont -L --split-prefix=tmp ../ref.fa.gz covid2.fq.gz | samtools view -bh | samtools sort -O bam > covid2.bam; samtools index covid2.bam
```

`gzip -d covid1.fq.gz` - na potrzeby nanopolish index

`./nanopolish index -d /media/twardovsky/sda/Mateusz_Kurzyński/covid1/fast5_pass -d /media/twardovsky/sda/Mateusz_Kurzyński/covid1/fast5_fail /media/twardovsky/sda/Mateusz_Kurzyński/covid1/covid1.fq`
	check it
	wee certainly need it.
	IT WORKS
	BUT - reads db is mapped to fast5 location - it MUST have the same path in the docker
		
	would be cool to run this from the same docker as eventalign (**not checked!**)


`docker run -it -v "$PWD":/media/twardovsky/sda/Mateusz_Kurzyński ca64a695154d bash`
	(**mount pwd as the real pwd**)

`./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/patient11.fq --bam /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/patient11.bam --genome /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/final_summary.txt > /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/eventalign.txt`



- `whatshap` in `clair3` for phasing haplotypes (divide diploidal material into 2)
	- how does it work?
- `clair3` pileup and full-alignment (for fast&reliable variant calling)
	and maybe more

- do `m6anet` for m6a
- do `Epinano` for the rest of mods

- your own model?


training labels are provided for a set of reads at the site level, but not for each individual read. Existing methods address this problem by averaging read-based features

read-level (5mer) probability -> pool-layer (per site probablity)

IT SEEMS that nucleotides in certain locations of 5-mers are more frequently methylated.
DRACH motif (D=A,G,U, R=A,G A=A, C=C H=A,C,U) - impact RNA structure, stability, splicing, and translation.

NIE przetrenujesz samemu m6anet, bo nie ma kontroli (mod/unmod).
CHYBA ZE https://trace.ncbi.nlm.nih.gov/Traces/index.html?view=study&acc=SRP174366

Trzeba uzyc ich modelu.
Mozliwe, ze ich wyniki EpiNano sa zanizone, poniewaz uzyto gotowych modeli NIE koniecznie w tych samych wersjach basecallerow (3.1.5)

NanoPolish ejst na tej samej linii komorkowej (HEK293T)
m6anet twierdzi, ze nie ma zasadniczych roznic miedzy basecallerami
SVM w epinano domaga sie wersji 

https://sci-hub.se/10.1016/j.jplph.2014.10.017
```
To the best of our knowledge, there is only one report on the
negative effect of DNA methylation on DNA amplification during
PCR (Bunyan et al., 2011). Multiple protocols of plant DNA extrac-
tion or commercial DNA extraction kits do not involve treatment
with proteinase K (e.g. in Edwards et al., 1991; Echt et al., 1992;
Bekesiova et al., 1999; Li et al., 2010; Ahmed et al., 2009; Amani
et al., 2011). Since DNA methylation is very common in plant
genomes (Finnegan et al., 1998; Vanyushin and Ashapkin, 2011)
and a large portion of all cytosines within a plant genome were
found to be methylated (Gehring and Henikoff, 2007; Zhang et al.,
2010; Capuano et al., 2014), we suggest that proteinase K treat-
ment should be considered as a mandatory step of DNA purification
before PCR of those regions, whose methylation status is not known,
in order to prevent false-negative results
```

jak dobrze rozumiem - ponoc same sekwencje CG koreluja z zawyzonym pcr, metylacja niezbyt ALE to stare badania (konsensus z ~2014)
