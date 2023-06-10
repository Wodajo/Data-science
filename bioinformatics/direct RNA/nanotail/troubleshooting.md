- f5c index
- minimap align
	`minimap2 -a -x splice data/reference.fa data/polyA.fastq | samtools view -b - -o data/polyA.bam`
	`-x splice` for splice-aware setting for mRNA
	`cd data && samtools sort -T tmp -o polyA.sorted.bam 30xpolyA.bam && samtools index 30xpolyA.sorted.bam && cd ..`

- nanopolish polya
	`nanopolish polya --threads=8 --reads=data/polyA.fastq --bam=data/polyA.sorted.bam --genome=data/reference.fa > polya_results.tsv`

- `grep 'PASS' polya_results.tsv > polya_results.pass_only.tsv`