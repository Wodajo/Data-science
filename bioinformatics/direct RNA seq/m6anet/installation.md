I used pull from docker hub
`docker pull dsaha0295/m6anet`


#### data prep
"nanopolish does not support `R10.4` flowcells as variant and methylation calling is accurate enough to not require signal-level analysis"

`minimap2 -a -L Human_reference/human_ref.fa covid_rna1/covid_rna1.fq.gz | samtools view -bh -F 2324 | samtools sort -O bam > covid_rna1_aligned_reads.bam` - for aligned&sorted


`docker run -v "$PWD":/data/ -it carrce/nanopolish bash`
	ID of nanopolish container





`nanopolish/nanopolish eventalign --reads /data/covid_rna1/covid_rna1.fq.gz --bam /data/covid_rna1_aligned_reads.bam --genome /data/Human_reference/human_ref.fa --scale-events --signal-index --summary /data/covid_rna1/final_summary.txt  --threads 40 > /data/OUTPUT_nano_pre_m6anet/eventalign.txt`


`nanopolish eventalign --reads /data/covid_rna1/covid_rna1.fq.gz --bam /data/covid_rna1_aligned_reads.bam --genome /data/Human_reference/human_ref.fa --scale-events --signal-index --summary /data/covid_rna1/final_summary.txt  --threads 40 > /data/OUTPUT_nano_pre_m6anet/eventalign.txt`






`docker run -v "$PWD":/data -it carrce/nanopolish /nanopolish/nanopolish eventalign --reads covid_rna1/covid_rna1.fq.gz --bam covid_rna1/covid_rna1.fq.bam --genome Human_reference/human_ref.fa --scale-events --signal-index --summary covid_rna1/final_summary.txt  --threads 40 > OUTPUT_nano_pre_m6anet/eventalign.txt` - segments raw fast5 signals to each position within the transcriptome, allowing m6Anet to predict modification based on the segmented signals

PROBLEM - bash nie daje odpalic komendy, bo porownuje ze swoim srodowiskiem (nie chce zroibic przekierowania sdout do lokalizacji ktora nie istnieje poza kontenerem)

