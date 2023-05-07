- `whatshap` in `clair3` for phasing haplotypes (divide diploidal material into 2)
	- how does it work?
- `clair3` pileup and full-alignment (for fast&reliable variant calling)
	and maybe more

- do `m6anet` for m6a
- do `Epinano` for the rest of mods



Training labels are provided for a set of reads at the site level, but not for each individual read.
Existing methods address this problem by averaging read-based features

read-level (5mer) probability -> pool-layer (per site probablity)

IT SEEMS that nucleotides in certain locations of 5-mers are more frequently methylated.
DRACH motif (D=A,G,U, R=A,G A=A, C=C H=A,C,U) - impact RNA structure, stability, splicing, and translation.

NIE przetrenujesz samemu m6anet, bo nie ma kontroli (mod/unmod).
CHYBA ZE https://trace.ncbi.nlm.nih.gov/Traces/index.html?view=study&acc=SRP174366

Trzeba uzyc ich modelu.
Mozliwe, ze ich wyniki EpiNano sa zanizone, poniewaz uzyto gotowych modeli NIE koniecznie w tych samych wersjach basecallerow (3.1.5)

NanoPolish jest na tej samej linii komorkowej (HEK293T)
m6anet twierdzi, ze nie ma zasadniczych roznic miedzy basecallerami
SVM w epinano domaga sie wersji 
