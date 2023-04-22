`nanopolish index -d fast5_files/ output.fastq`
	create an index file that links read IDs with their signal-level data in the FAST5 files


`docker run -it --rm --name nanopolish14 -v "$PWD":/data aokad/nanopolish:0.14.0_debug bash` - works



najnowszy
`docker run -v "$PWD":/data -it aokad/nanopolish /nanopolish/nanopolish eventalign --reads covid_rna1/covid_rna1.fq.gz --bam covid_rna1/covid_rna1.fq.bam --genome Human_reference/human_ref.fa --scale-events --signal-index --summary covid_rna1/final_summary.txt  --threads 40 > OUTPUT_nano_pre_m6anet/eventalign.txt`

LUB 
```
(m6anet) twardovsky@twardovsky:/media/twardovsky/big_data/Mateusz_Kurzyński_covid/Repos/nanopolish$ ./nanopolish --version
nanopolish version 0.14.0
Written by Jared Simpson.

Copyright 2015-2017 Ontario Institute for Cancer Research
```












`docker run -v "$PWD":/data -it carrce/nanopolish nanopolish eventalign --reads covid_rna1/covid_rna1.fq.gz --bam covid_rna1/covid_rna1.fq.bam --genome Human_reference/human_ref.fa --scale-events --signal-index --summary covid_rna1/final_summary.txt  --threads 40 > OUTPUT_nano_pre_m6anet/eventalign.txt`



hidden Markov models (HMMs) can be used to analyze nanopore sequencing data
HMM computes the probability of observing a sequence of signal-level events, given a specific nucleotide sequence (e.g. for methylation discovery sake)