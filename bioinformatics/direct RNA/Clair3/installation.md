`docker pull hkubal/clair3`
or from [github](https://github.com/HKU-BAL/Clair3)

```
docker run -it \
  -v ${INPUT_DIR}:${INPUT_DIR} \
  -v ${OUTPUT_DIR}:${OUTPUT_DIR} \
  hkubal/clair3:latest \
  /opt/bin/run_clair3.sh \
  --bam_fn=${INPUT_DIR}/input.bam \    ## samtools indexed
  --ref_fn=${INPUT_DIR}/ref.fa \       ## samtools indexed
  --threads=${THREADS} \               ## maximum threads to be used
  --platform="ont" \                   ## options: {ont,hifi,ilmn}
  --model_path="/opt/models/${MODEL_NAME}" \  ## e.g. r941_prom_hac_g360+g422
  --output=${OUTPUT_DIR}               ## absolute output path prefix
```
e.g.
`docker run -v /media/twardovsky/big_data/Mateusz_Kurzyński_covid/INPUT_calir3:/INPUT -v /media/twardovsky/big_data/Mateusz_Kurzyński_covid/OUTPUT_calir3:/OUTPUT -it hkubal/clair3 /opt/bin/run_clair3.sh --bam_fn=/INPUT/covid_rna1_aligned_reads.bam --ref_fn=/INPUT/human_ref.fa --threads=39 --platform="ont" --model_path="/opt/models/rna_r9.4.1_minion_96_b3af299f" --output=/OUTPUT
`


`  --bed_fn=FILE` - call variants only in the provided bed regions.
`.bed` example:
```
# define 0-based "ctg start end" if at specific sites
CONTIGS="[YOUR_CONTIGS_NAME]"          # e.g. chr22
START_POS="[YOUR_START_POS]"           # e.g. 0
END_POS="[YOUR_END_POS]"               # e.g 10000
echo -e "${CONTIGS}\t${START_POS}\t${END_POS}" > /home/user1/tmp.bed ## change directory accordingly
```