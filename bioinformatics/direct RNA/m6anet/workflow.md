## CURRENT (m6anet 2.0.1)

###
`samtools faidx ref.fa` - raz, dla wszystkich
`gzip -d` - might be neccessairy for `ref.fa` & `read.fq` (not really checked which tool need and which don't)

`minimap2 -ax map-ont -L --split-prefix=tmp ../ref.fa covid1.fq.gz | samtools view -bh | samtools sort -O bam > covid1.bam`

`samtools index covid1.bam`

to samo tylko oneliner:
```
minimap2 -ax map-ont -L --split-prefix=tmp ../ref.fa covid2.fq | samtools view -bh | samtools sort -O bam > covid2.bam; samtools index covid2.bam
```

### fast5->slow5
move fast5_fail to fast5_pass
`docker run -it --rm --name slow5tools -v "$PWD":/patient14 --log-driver none slow5tools bash`
	- `./scripts/install-vbz.sh` - install plugin for `hdf5` `VBS` compression
	- `export HDF5_PLUGIN_PATH=/root/.local/hdf5/lib/plugin` - export plugin to path
		**ctl-p ctl-q** to detach `run -it` container :D
		`docker attach container_id` to reattach

`./slow5tools f2s /patient14/fast5_pass/ -d /patient14/blow5_dir -p 10`
	`BLOW5` files (default compression: zlib+svb-zd)
	`-p` nr of I/O processes

`./slow5tools merge /patient14/blow5_dir -o /patient14/signals.blow5 -t15`
	merge into one file
	`-t` 15 threads


### index fq&blow5
`conda create -n f5c -c bioconda -c conda-forge f5c`
`conda activate f5c`

`f5c index /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.fq --slow5 /media/twardovsky/sda/Mateusz_Kurzyński/patient14/signals.blow5`
	reads db is mapped to blow5 location - from now on paths can't be relative

### eventalign
`f5c eventalign -r /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.fq -b /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.bam -g /media/twardovsky/sda/Mateusz_Kurzyński/ref.fa --slow5 /media/twardovsky/sda/Mateusz_Kurzyński/patient14/signals.blow5 --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzyński/patient14/final_summary.txt -t 15 --rna > /media/twardovsky/sda/Mateusz_Kurzyński/patient14/eventalign.txt`

##### explanation eventalign
MinION detect events per 5-mers passing through.
That means 1024 combinations for ~40-70pA range
- normal distribution of 5-mers overlap BUT solution must respect overlaps between subsequent 5-mers
`eventalign` - nanopolish module (used by `f5c`) takes in a set of nanopore reads aligned according to base sequence of reference sequence (what read is where in reference) and re-aligns the reads in event space (what read was infered from that signal)
```
contig                         position  reference_kmer  read_index  strand  event_index  event_level_mean  event_length  model_kmer  model_mean  model_stdv
gi|556503834|ref|NC_000913.3|  10000     ATTGC           1           c       27470        50.57             0.022         ATTGC       50.58       1.02
gi|556503834|ref|NC_000913.3|  10001     TTGCG           1           c       27471        52.31             0.023         TTGCG       51.68       0.73
gi|556503834|ref|NC_000913.3|  10001     TTGCG           1           c       27472        53.05             0.056         TTGCG       51.68       0.73
gi|556503834|ref|NC_000913.3|  10001     TTGCG           1           c       27473        54.56             0.011         TTGCG       51.68       0.73
gi|556503834|ref|NC_000913.3|  10002     TGCGC           1           c       27474        65.56             0.012         TGCGC       66.96       2.91
gi|556503834|ref|NC_000913.3|  10002     TGCGC           1           c       27475        69.97             0.071         TGCGC       66.96       2.91
gi|556503834|ref|NC_000913.3|  10004     GCGCT           1           c       27476        67.11             0.017         GCGCT       68.08       2.20
```
- output has one row for every event. If a reference 5-mer was skipped, there will be a gap in the output where no signal was observed
event 27470
	- had a measured current level of 50.57 pA
	- aligns to the reference 5-mer ATTGC at position 10,000 of the reference
	- pore model indicates that events measured for 5-mer ATTGC should come from N(50.58,1.022) -> matches the observed data very well
events 27471, 27472, 27473
	- all aligned to the same reference 5-mer (TTGCG) -> event detector erroneously called 3 events where only one should have been emitted
	- expected distribution N(51.68,0.732) -> not really accurate match

### install m6anet
`conda update -n base -c conda-forge conda`
`conda create --name m6anet2 python=3.8; conda activate m6anet; pip3 install m6anet==2.0.1`
`conda activate m6anet2`


### infering m6a
`nohup m6anet inference --input_dir /media/twardovsky/sda/Mateusz_Kurzyński/covid1/m6anet_dataprep --out_dir /media/twardovsky/sda/Mateusz_Kurzyński/covid1/m6anet_infer  --n_processes 4 --num_iterations 1000 2> /media/twardovsky/sda/Mateusz_Kurzyński/covid1/error_infer.txt`


### further analysis
`data.indiv_proba.csv` - probability of mod for **`each read`**
	-   `transcript_id`: The transcript id of the predicted position
	-   `transcript_position`: The transcript position of the predicted position
	-   `read_index`: The read identifier from nanopolish that corresponds to the actual `read_id` from nanopolish `summary.txt`
	- ---------------------------
	-   `probability_modified`: The probability that a given read is modified


`data.site_proba.csv` - probability of mod at each individual position for **`each transcript`**
	-   `transcript_id`: The transcript id of the predicted position
	-   `transcript_position`: The transcript position of the predicted position
	-   `n_reads`: The number of reads for that particular position 
	- ---------------------------
	-   `probability_modified`: The probability that a given site is modified     <---
		devs recommend a threshold of 0.9 to select m6A sites
	-   `kmer`: The 5-mer motif of a given site
	-   `mod_ratio`: The estimated percentage of reads in a given site that is modified
