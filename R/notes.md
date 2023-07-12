- Moze przypisac proby do nowej col "próba"? (na potrzeby ggplot)
  Wtedy potrzebne byloby wieele rzędów prób - pojednym rzędzie na każdy
  transkrypt danego typu.
- Może lepiej boxplot niz scatter (dla rozkladu proba vs transkrypt)


confidence interval (se = T)
categorical var distribution
	bar plot
numerical/quantitative var
	histogram (experiment with binwidth/bins)
	geom_density (smoothed version of the histogram)
cat-num relation
	boxplot
		interquartile range (IQR) - distance between 25-75
		points out of 1.5 IQR noted as a single dot
cat-cat relation
	stacked bar plot (showing distribution)
	frequency bar plot (showing percentage - not affected by unequal distribution)
		`position = 'fill' `
many relations
	e.g. `facet_wrap(~island)`

