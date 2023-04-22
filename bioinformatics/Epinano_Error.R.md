
- combines base-calling errorsbase-calling errors (insertions, deletions, mismatch) & per-base-calling qualities -> **predictions based on differences in error patterns in two matched samples**
	(base-calling algorithm independent)
- can only be run in pairwise mode (e.g. `WT`(2wildtype/modified sample) and `KO` (knockout/unmodified sample) or `KD`)

`sample.per.site.var.csv` - basecalling error info for each ref. position

**`Epinano_Diff_Error`**:
	- sum of errors
	- outlier detection
	- `WT-KO` (per-transcript plots) 
	- `WT` vs `KO` (features scatterplots)
- draws linear regression model between paired unmodified and modified samples -> detects outliers
  (deviance -> z-score with user-defined treshold)
- large residuals(szczątki/resztki) -> probably underlined(podkreślone) by base modifications


- independent types of errors&the combined error - performed when running `Epinano_DiffErr.R`
- different types of RNA base modification -> distinct biases toward the spefic types of errors -> `Epinano_sumErr.py` combine mismatches, indels and even quality score


`Rscript ../Epinano_DiffErr.R -k ko.csv -w wt.csv -t 3 -o Test -c 30 -f sum_err  -d 0.1`
	`-k` KO/unmodified sample
	`-w` WT/modified sample
	`-t` treshold - minimal z-score (standard deviation from mean) ????
		3 by default
	`-d` deviance - minimum deviance of selected feature between two samples
		0.1 by default
	`-o` output prefix
	`-c` coverage - minimal coverage/depth ????????
		30 by default
	`-f` feature - column name(s) in input file to use for modification prediction
		`sum_err`  rowSums(input[,c("mis", "ins", "del")])
		


`Rscript ../Epinano_DiffErr.R -w ../covid_rna1/covid_rna1_reads.plus_strand.per.site.csv -k ../patient11/patient11_reads.plus_strand.per.site.csv -t 3 -o Test -c 30 -f sum_err  -d 0.1`
```
BŁĄD: nieoczekiwane '/' w "!/"
Wykonywanie wstrzymane
```

