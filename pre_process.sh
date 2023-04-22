#! /usr/bin/env bash
# Start me inside a docker run -it
# ctl-p ctl-q to detach
# docker attach container_id

# cd nanopolish

echo "[+] nanopolish eventalign covid1"
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzyński/covid1/covid1.fq --bam /media/twardovsky/sda/Mateusz_Kurzyński/covid1/covid1.bam --genome /media/twardovsky/sda/Mateusz_Kurzyński/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzyński/covid1/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzyński/covid1/eventalign.txt;\

echo "[+] nanopolish eventalign covid2"
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzyński/covid2/covid2.fq --bam /media/twardovsky/sda/Mateusz_Kurzyński/covid2/covid2.bam --genome /media/twardovsky/sda/Mateusz_Kurzyński/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzyński/covid2/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzyński/covid2/eventalign.txt;\

echo "[+] nanopolish eventalign patient11"
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzyński/patient11/patient11.fq --bam /media/twardovsky/sda/Mateusz_Kurzyński/patient11/patient11.bam --genome /media/twardovsky/sda/Mateusz_Kurzyński/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzyński/patient11/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzyński/patient11/eventalign.txt;\

echo "[+] nanopolish eventalign patient14"
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.fq --bam /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.bam --genome /media/twardovsky/sda/Mateusz_Kurzyński/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzyński/patient14/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzyński/patient14/eventalign.txt

echo "[+] pre_process.sh completed (MATEUSZ KURZYŃSKI JEST SUPER)"
touch /media/twardovsky/sda/Mateusz_Kurzyński/pre_process_DONE
```
./nanopolish index -d /media/twardovsky/sda/Mateusz_Kurzyński/covid2/fast5_pass -d /media/twardovsky/sda/Mateusz_Kurzyński/covid2/fast5_fail /media/twardovsky/sda/Mateusz_Kurzyński/covid2/covid2.fq
./nanopolish index -d /media/twardovsky/sda/Mateusz_Kurzyński/patient14/fast5_pass -d /media/twardovsky/sda/Mateusz_Kurzyński/patient14/fast5_fail /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.fq
```
