technologies used for sequencing (e.g. nanopore - fast5, illumina) have different primary, raw-data formats -> processed into secondary, common formats


fasta -  just hold genomes (e.g. for reference genomes)
```
>ch20  # chromosome
ATGCCATGTGAACCCGATGACGGACATAC ...
```

fastq - reads (info taken out of primary data)
```
@A007:48:HV820381VDF:2:2421:1315462  # name of a read
CCCCAATGCATGCTTATTGGCAATCCGTCTCC...  # sequence
+  # optional info line
FFFFFFFFFFF:FF:FFFFFFFFFFF:FFFFFFFF  # quality score of each base in sequence
```

mapping/alignment - checking where reads (fastq) best match on reference genome (fasta)
	are there variations like insertions/deletions? etc.

bam - store info about how well reads match reference (alignment file)
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



`CIGAR` (Concise Idiosyncratic Gapped Alignment Report) string - compressed representation of an alignment in `SAM` files
	A CIGAR string is made up of <integer><op> pairs, e.g. 76H130M. Here, "op" is an operation specified as a single character, usually an upper-case letter (see table below). An operation is usually a type of column that appears in the alignment, e.g. a match or gap. The integer specifies a number of consecutive operations. In some CIGAR variants, the integer may be omitted if it is 1
	ops e.g. "M" (match), "D" (deletion), "I" (insertion), "X" mismatch