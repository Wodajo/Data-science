
### empty dataframe for /project/reads_noF_noq.plus_strand.per.site.csv

what not ok?
	- code
	- .fa/.fai/.bam/.bai/.dict
	- dependency (not installed? wrong version? e.g. java)

1. lear how to get into docker container
	while inside:
		- check if `Epinano_Variants.dev.py` works (install dependecies ofc)
		- `pip list` (check if correct versions&eveything)
			if neccessary `pip3 install -r requirements.txt`
			python3.6.8 pysam0.18.0
		- does `samtools view -h -F 3860 read.bam | java -jar sam2tsv` output make sense?
1. check out `nanoRMS`
2. try to correct `Epinano_Variants.py` code (ideas below)
3. check out `Dorado`
4. basecall with `Gruppy 3.1.5` ->  `EpiNano-SVM`
5. [novoalab best practices](https://github.com/novoalab/Best_Practices_dRNAseq_analysis) (for `dRNA`)





#### change df_is_not_empty(df)
change    (assumin that `df.iterrows()` works other way)
``` python
def df_is_not_empty(df):

'''

input df is a df filtred on reference id

if is is empty: next (df.iterrows()) does not work

otherwise it returns a row of df

'''

try:

next (df.iterrows())

return True

except:

return False
```
to 
```python
if not df.empty:
    for index, row in df.iterrows():
        print(index, row)

```

#### mnrusimh idea
```python
def has_reads_mapped(bam)
	return int(pysam.flagstat(bam).split('\n')[1][0]) > 0
```