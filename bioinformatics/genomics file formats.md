technologies used for sequencing (e.g. nanopore, illumina) have different primary, raw-data formats -> processed into secondary, common formats


fasta -  just hold genomes (e.g. for reference genomes)
```
>ch20  # chromosome
ATGCCATGTGAACCCGATGACGGACATAC ...
```

fastq - reads (info taken out of primary data)
```
@A007:48:HV820381VDF:2:2421:1315462  # name of a read
CCCCAATGCATGCTTATTGGCAATCCGTCTCC...  # sequence
+  # linebreak?
FFFFFFFFFFF:FF:FFFFFFFFFFF:FFFFFFFF  # base qualities (somehow info about quality scores)
```

mapping aka alignment - checking where reads (fastq) best match on reference genome (fasta)
	are there variations like insertions/deletions? etc.

bam - store info about how well reads match reference
	binary - you need `samtools view`
	compressed version of sam file
	i.a. name of read, chromosome, position, mapping quality

vcf - conclusions from comparing
	e.g. in few of reads there were A insted of G (reference) - that might be a variant

bed - regions of intrest
```
chr20 1000023 1000233  # chromosome, start, end
chr20 1000254 1000432
```
can also have name, quality etc.

typical workflow:
`some_aligner --reads reads.fastq --reference reference.fasta > read_alignments.bam`
	aligner/mapper to compare reads to reference and extract how well does it match
	
`some_variant_caller --reads read_alignments.bam --reference reference.fasta > variants.vcf`
	caller to compare alignment reads  with reference (again) to find sth specific



T2T genome