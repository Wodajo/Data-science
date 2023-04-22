### 1. find basecalling error for each ref. position
`Epinnano_Variants.py`  ---> `sample.per.site.var.csv` - basecalling error info for each ref. position
```shell
python Epinano_Variants.py -h
usage: Epinano_Variants.py [-h] [-R REFERENCE] [-b BAM] [-s SAM2TSV]
                           [-n NUMBER_CPUS] [-T TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_CPUS, --number_cpus NUMBER_CPUS
                        number of CPUs
  -T TYPE, --type TYPE  reference types, which is either g(enome) or
                        t(ranscriptome);

Required Arguments:
  -R REFERENCE, --reference REFERENCE
                        reference file indexed with samtools faidx and with
                        sequence dictionary created using picard
                        CreateSequenceDictionary
  -b BAM, --bam BAM     bam file; if given; no need to offer reads file;
                        mapping will be skipped
  -s SAM2TSV, --sam2tsv SAM2TSV
                        /path/to/sam2tsv.jar; needed unless a sam2tsv.jar
                        produced file is already given```
e.g.
	`python $EPINANO_HOME/Epinano_Variants.py -n 6 -R reference.fasta -b sample.reads.bam -s  $EPINANO_HOME/misc/sam2tsv.jar --type t`
	`-R` reference (genome? transcriptome? which for what?) - `samtools faidx` indexed reference file with `sequence dictionary` created using picard `CreateSequenceDictionary` !!!!
	`-b` BAM (is it prepared ok? make copies with different options and check results)
	`-s` path to sam2tsv
	`-T` or `--type` - reference type (g)nome or (t)ranscryptome
	
organize the variants in any kmer length using `$EPINANO_HOME/misc/Slide_Variants.py`

### 2. (optional) extract current intensity values
`Epinano_Current` - current intensities and duration time  (you might be intrested in it e.g. for SVM sake)
```shell
$ sh Epinano_Current.sh -h

Epinano_Current.sh [-h] [-b bam -r reads -f genome/transriptome reference -d fast5dir -t threads -m bam_file_mapping_type]

        it runs nanopolish eventalign; aggreagets current intensity values associated with single positions

        nanopolish, samtools have to be installed and added to environmental paths!!

        -h [this help text]
        -b [bam file]
        -d [fast5 folder]
        -r [fastq reads file]
        -f [reference file used to produce bam file]
        -t [number of threads]
        -m [t: reads mapping performed using reference transcriptome; g: reads mapping performed with reference genome]```
add `/path/to/nanopolish` to `$PATH` env

### 3. detect outliers
`Epinano_DiffErr.R` - draws linear regression model between paired unmodified and modified samples -> detects outliers
- large residuals(szczątki/resztki) -> probably underlined(podkreślone) by base modifications
```shell
$ Rscript Epinano_DiffErr.R -h

Usage:
        DiffErr.R v0.1 compares a given feature between two samples. It predicts potential modified sites mainly through two methods:
                1. Compute deviance of selected featuers between samples and then calculate z-scores. Outliers or potential modified sites will then
                be determined based on user-defined threshold. Note that this is not suited for 'curlcake' data because they are highly modified (~25% of the bases 
		in the RNA molecules are modified bases).
                2. Fit a linear regression model between two samples.
                        1) detect residuals outliers of the given linear model.
                        2) compute z-scores of residuals for each observation and determine outliers using user-defined z-score threshold.
                Examples:
                        1 compare sum_err between two samples
                        Rscript Epinano_DiffErr.R -k ko.csv -w wt.csv -t 3 -o Test -c 30 -f sum_err  -d 0.1
                        2 same as above, but generate plots, one for each reference.
                        Rscript Epinano_DiffErr.R -k ko.csv -w wt.csv -t 3 -o Test -c 30 -f sum_err  -d 0.1 -p

Options:
        -c COVERAGE, --coverage=COVERAGE
                minimum coverage/depth; default: 30

        -t THRESHOLD, --threshold=THRESHOLD
                minimum z-score (i.e., number of standard deviation from mean) to determine modified sites; default: 3

        -d DEVIANCE, --deviance=DEVIANCE
                minimum deviance of selected feature between two samples; default: 0.1

        -f FEATURE, --feature=FEATURE
                the feature (column name(s) in from input file) to use to predict modifications

        -k KO_SAMPLE, --ko_sample=KO_SAMPLE
                knockout/unmodified sample

        -w WT_SAMPLE, --wt_sample=WT_SAMPLE
                wildtype/modified sample

        -o OUT_PREFIX, --out_prefix=OUT_PREFIX
                output prefix

        -p, --plot
                whether or not generate plots;  default: no plots will be generated because Epinano_Plot.R can do the job

        -h, --help
                Show this help message and exit```
- independent types of errors&the combined error - performed when running `Epinano_ErrDiff.R`
- different types of RNA base modification -> distinct biases toward the spefic types of errors -> `Epinano_sumErr.py` combine mismatches, indels and even quality scores


minimap2 -ax map-ont -L {transcriptome_fasta} {basecalled_fastq} | samtools view -bh -F 2324 -q 10 | samtools sort -O bam > {aligned_reads_bam}

samtools index {aligned_reads_bam}