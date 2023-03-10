for methylation calling

you can train `remora` module OR use pretrained


fast5 -> pod5 (contain signal data)
bam (with basecalls from pod5) - must contain the `move table` - default in Bonito, `--moves_out` in Gruppy






alignment - checking where reads (fastq) best match on reference
bam - store info about how well reads match reference
pod5 - store signal data (good for methylation basecalling)
index file - links read IDs with their signal-level data

typical workflow:
`some_aligner --reads reads.fastq --reference reference.fasta > read_alignments.bam`
	aligner/mapper to compare reads to reference and extract how well does it match
	
`some_variant_caller --reads read_alignments.bam --reference reference.fasta > variants.vcf`
	caller to compare alignment reads  with reference (again) to find sth specific