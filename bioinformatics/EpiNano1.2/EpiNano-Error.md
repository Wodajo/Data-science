
- combines base-calling errorsbase-calling errors (insertions, deletions, mismatch) & per-base-calling qualities -> **predictions based on differences in error patterns in two matched samples**
	(base-calling algorithm independent)
- can only be run in pairwise mode (e.g. `WT`(2wildtype/modified sample) and `KO` (knockout/unmodified sample) or `KD`)

**`Epinano_variants`** - per-site&per-kmer
	quality, insertion, deletion, mismatch
`sample.per.site.var.csv` - basecalling error info for each ref. position

**`Epinano_Diff_Error`**:
	- sum of errors
	- outlier detection
	- `WT-KO` (per-transcript plots) 
	- `WT` vs `KO` (features scatterplots)
- draws linear regression model between paired unmodified and modified samples -> detects outliers
  (deviance -> z-score with user-defined treshold)
- large residuals(szczątki/resztki) -> probably underlined(podkreślone) by base modifications

