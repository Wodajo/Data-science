`./Epinano_DiffErr.sh -x ko1.plus_strand.per.site.var.csv -y wt1.plus_strand.per.site.var.csv -p c -m 0  -c 30 -t 5 -q`
	`-x` sample1 csv (ko?)
	`-y` sample2 csv (wt?)
	`-p` plot type
		`c` scatterplot
		`b` bar plot
	`-m` 0 - no labeling, 1- label outliers
	`-t` treshold \* sd - used to determine `OLS` (Ordinary Least Squares regression) outliers/candidates of modification sites
		5 by default
	`-c` minimum depth ????????????????
		30 by default
	`-q`  - include quality scores to compute summed errors (or not if not used)


