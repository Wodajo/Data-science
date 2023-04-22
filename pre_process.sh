#! /usr/bin/env bash
docker run -it --rm -v "$PWD":/media/twardovsky/sda/Mateusz_Kurzyński --log-driver none ca64a695154d bash;\
\
cd nanopolish;\
\
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid1/covid1.fq --bam /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid1/covid1.bam --genome /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid1/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid1/eventalign.txt;\
\
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid2/covid2.fq --bam /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid2/covid2.bam --genome /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid2/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/covid2/eventalign.txt;\
\
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/patient11.fq --bam /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/patient11.bam --genome /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient11/eventalign.txt;\
\
./nanopolish eventalign --reads /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient14/patient14.fq --bam /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient14/patient14.bam --genome /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/ref.fa --scale-events --signal-index --summary /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient14/final_summary.txt -t 35 > /media/twardovsky/sda/Mateusz_Kurzy\305\204ski/patient14/eventalign.txt

```
./nanopolish index -d /media/twardovsky/sda/Mateusz_Kurzyński/covid2/fast5_pass -d /media/twardovsky/sda/Mateusz_Kurzyński/covid2/fast5_fail /media/twardovsky/sda/Mateusz_Kurzyński/covid2/covid2.fq
./nanopolish index -d /media/twardovsky/sda/Mateusz_Kurzyński/patient14/fast5_pass -d /media/twardovsky/sda/Mateusz_Kurzyński/patient14/fast5_fail /media/twardovsky/sda/Mateusz_Kurzyński/patient14/patient14.fq
```
