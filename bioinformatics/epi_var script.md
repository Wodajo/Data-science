
pocwicz wlaczanie/wylaczanie/usuwanie/dodawanie/laczenie sie z dockerowymi kontenerami

`minimap2`
	is `-F 2324` neccessary?
	is `-q 10` helpful

**n is NECCESSARY (but maybe it could be max nr of threads and kernel will take care of the rest?)**

epi-error
****
`.fa` -> `.fa.fai` (samtools) & `fa.dict` (picard)  - same for all human (unless newer genome release)
`.fq` -> `.bam`(minimap2&samtools), `.bam.bai` (samtools)
  
****
- `time command`
- `Epinano_Variants.py` szuka indeksow `ref` w oparciu o `ref.fa`, szuka indeksow `bam` w oparciu o `read.bam`
- `MasterOFPores` workflow uses `Epinano1.1`

```bash
#! /usr/bin/env bash
# assume fa, fa.fai and fa.dict exist in /path/to/ref
# let's we've got dirs of patients containing i.a. fastq_pass & fastq_fail dirs

# I want this script to concatenate fastq files of patients -> create bam -> create bai -> create .csv | than repeat for the next patient

# I will create a functions that will - concatenate, create bam&bai, create csv
# I will use a loop iterating through dirs of patients- only first dir -> find fastq_pass&fail dirs
# It doesn't matter if thats WT or KO :D 

# arguments needed at start: ref dir, reads dir (dir with patient dirs)
# read -p 'Username: ' uservar

# read -sp 'Password: ' passvar
# ----------------------------------------------------------------------------
echo "[+] Scirpt assume:
- human cDNA reference files (human_ref.fa, human_ref.fa.fai, human_ref.fa.dict) are in one dir and have exactly the same filename
- script is started in directory containing each patient directory which contain dirs with basecalled .fq.gz
(e.g. here_start_script/patient1/sth/*fastq_pass/*fastq.gz)
- proper docker container (with Epinano_Variant.py dependencies) was build, and it's image name is epi12
- it has root privilege (for docker sake)
- spaces in filenames could result in errors"

read -p "[+] Path to dir with human_ref.fa, human_ref.fa.fai, human_ref.fa.dict: " REF_DIR
# echo '[+] In dir typed below - shouldn\'t have any other dirs than "patient dirs"'
# read -p "[+] Path to dir with patient dirs of basecalled .fq (e.g. /parent/fq_pass/fq.gz): " READ_DIR
PWD=$(pwd)
PARENT_DIRS=($(find "$PWD" -mindepth 1 -maxdepth 1 -type d -printf '%f\n'))  # store parent dirs in an array. '-printf '%f\n'' so not to store whole path
echo "[+] There are ${#PARENT_DIRS[@]} dirs in current dir"

# create bam&bai - invoke  INSIDE concatenate!
bambai () {
FQ_BAM=$d/"$d.fq.bam"
echo "[+] control - bambai for $FQ_BAM started"
minimap2 -ax map-ont -L --split-prefix=tmp "$REF_DIR"/human_ref.fa "$FQ_GZ" | samtools view -bh | samtools sort -O bam > "$FQ_BAM"  # create reads.bam
samtools index "$FQ_BAM"  # create reads.bam.bai in the same dir that bam is
}

# concatenate fastq.gz & invoke bambai func
concatenate () {
FQ_DIR_F=$(find "$PWD/$d" -type d -name "*fastq_fail")  # fastq_pass dir
FQ_DIR_P=$(find "$PWD/$d" -type d -name "*fastq_pass")  # fastq_fail dir
FQ_GZ=$d/"$d.fq.gz"
mv $FQ_DIR_F/*.fastq.gz $FQ_DIR_P/
cat $FQ_DIR_P/*.fastq.gz > $FQ_GZ
bambai


# start docker containers with Epinano_Variants.py for every dir
# MUST run from concatenate
epivar12 () {
docker run -it -d --rm --name "$d" -v "$d/":/fq_dir/ -v "$REF_DIR/":ref_dir/ epi12 python3 /usr/local/bin/EpiNano/Epinano_Variants.py -R /ref_dir/human_ref.fa -b /fq_dir/"$d.fq.bam" -s /usr/local/bin/EpiNano/misc/sam2tsv.jar -n 30  # n is NECCESSARY (but maybe it could be max nr of threads and kernel will take care of the rest?)
}


# invocation of functions
for d in "${PARENT_DIRS[@]}"; do
	echo "[+] Directory: $PWD/$d"
	concatenate
	epivar12
done


```

1. skrypt jako root dla dockera - ale wszystkie pliki maja roota jako wlasciciela
2. dodaj usera do grupy docker - mozna puszczac dockera bez sudo - ALE mozna uzyc do eskalacji uprawnien
3. inne opcje zbyt upierdliwe w utrzymaniu