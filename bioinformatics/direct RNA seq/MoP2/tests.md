```
params {
    input_path         = "/media/twardovsky/big_data/Mateusz_Kurzyński_covid/"
    comparison         = "$baseDir/comparison.tsv"

    reference           = "/media/twardovsky/big_data/Mateusz_Kurzyński_covid/Human_reference/human_ref.fa"

    output             = "/media/twardovsky/big_data/Mateusz_Kurzyński_covid/OUTPUT_mop_mod"

    pars_tools         = "$baseDir/tools_opt.tsv"

    // flows
    epinano       = "YES"
    nanocompore   = "YES"
    tombo_lsc     = "YES"
    tombo_msc     = "YES"

    // epinano plots
    epinano_plots = "YES"

    email              = ""
```

- let's assume `wt` and ko `in` `comparison.tsv` are `dirs` - good
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     No such dirs :/   !!!!!!!!!!!!!!!!!!!!!!!!!!!1
```
patient11 -> /media/twardovsky/big_data/Mateusz_Kurzyński_covid/fast5_files/patient11
patient11_final_summary.stats -> /media/twardovsky/big_data/Mateusz_Kurzyński_covid/QC_files/patient11_final_summary.stats
patient11.fq.gz -> /media/twardovsky/big_data/Mateusz_Kurzyński_covid/fastq_files/patient11.fq.gz
```
`QC_files/patient11_final_summary.stats` !

`fastqc -o /media/twardovsky/big_data/Mateusz_Kurzyński_covid/QC_files/ --noextract /media/twardovsky/big_data/Mateusz_Kurzyński_covid/patient11/*fq.gz`
	`--noextract`     don't uncompress the output file after creating it
	`--memory 2048` or more
	(if `Terminating due to java.lang.OutOfMemoryError: Java heap space`)