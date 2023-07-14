`conda create -n NanoCount python=3.6`
`conda activate NanoCount`
`conda install -c aleg nanocount`

`minimap2 -ax map-ont -L --split-prefix=tmp ../ref.fa covid1.fq.gz | samtools view -bh | samtools sort -O bam > covid1.bam`
	ref to transkryptom

`mkdir nanocount_out`
```NanoCount -i covid1/patient11.bam --extra_tx_info -o nanocount_out/cov1_counts.tsv;\
NanoCount -i covid2/patient14.bam --extra_tx_info -o nanocount_out/cov2_counts.tsv;\
NanoCount -i covid3/covid3.bam --extra_tx_info -o nanocount_out/cov3_counts.tsv;\
```
`i` sorted&aligned bam
`--extra_tx_info` - add transcript lenght&zero coverage transcripts
`-o` output











