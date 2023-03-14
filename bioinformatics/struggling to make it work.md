
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
2. try to correct `Epinano_Variants.py` code (ideas below)
3. basecall with `Gruppy 3.1.5` ->  `EpiNano-SVM`
4. [novoalab best practices](https://github.com/novoalab/Best_Practices_dRNAseq_analysis) (for `dRNA`)




`sudo docker run -it --rm --name epivar2 -v /home/arco/Workspace/:/Workspace epi12 python3 /Workspace/EpiNano/Epinano_Variants.dev.py -r /Workspace/align/data/ref.fa -b /Workspace/align/data/reads_noF_noq.bam -c 3`
``` python
multiprocessing.pool.RemoteTraceback:
"""
Traceback (most recent call last):
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 119, in worker
    result = (True, func(*args, **kwds))
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 47, in starmapstar
    return list(itertools.starmap(args[0], args[1]))
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 74, in bam_to_var
    out = open (outfn, 'w')
FileNotFoundError: [Errno 2] No such file or directory: '/Workspace/align/data/reads_noF_noq.tmp//Workspace/align/data/reads_noF_noq.fwd.4.per.site.csv'
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 153, in <module>
    main ()
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 143, in main
    multi_processes_bam2var(fafn, ref_names, bam, strands[i], ncpus,  outdir)
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 109, in multi_processes_bam2var
    files = pool.starmap (bam_to_var,conditions)
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 274, in starmap
    return self._map_async(func, iterable, starmapstar, chunksize).get()
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 644, in get
    raise self._value
FileNotFoundError: [Errno 2] No such file or directory: '/Workspace/align/data/reads_noF_noq.tmp//Workspace/align/data/reads_noF_noq.fwd.4.per.site.csv'
```
`/Workspace/align/data/reads_noF_noq.tmp/` exist -.-
`/Workspace/align/data/reads_noF_noq.fwd.4.per.site.csv'` don't

`docker exec -it docker_ID bash`
`python3 /Workspace/EpiNano/Epinano_Variants.dev.py -r /Workspace/align/data/ref.fa -b /Workspace/align/data/reads_noF_noq.bam -c 3`
```python
multiprocessing.pool.RemoteTraceback:
"""
Traceback (most recent call last):
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 119, in worker
    result = (True, func(*args, **kwds))
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 47, in starmapstar
    return list(itertools.starmap(args[0], args[1]))
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 74, in bam_to_var
    out = open (outfn, 'w')
FileNotFoundError: [Errno 2] No such file or directory: '/Workspace/align/data/reads_noF_noq.tmp//Workspace/align/data/reads_noF_noq.fwd.4.per.site.csv'
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 153, in <module>
    main ()
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 143, in main
    multi_processes_bam2var(fafn, ref_names, bam, strands[i], ncpus,  outdir)
  File "/Workspace/EpiNano/Epinano_Variants.dev.py", line 109, in multi_processes_bam2var
    files = pool.starmap (bam_to_var,conditions)
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 274, in starmap
    return self._map_async(func, iterable, starmapstar, chunksize).get()
  File "/usr/local/bin/Python-3.6.3/Lib/multiprocessing/pool.py", line 644, in get
    raise self._value
FileNotFoundError: [Errno 2] No such file or directory: '/Workspace/align/data/reads_noF_noq.tmp//Workspace/align/data/reads_noF_noq.fwd.4.per.site.csv'
```


# **The input BAM file may not have any reads mapped to the reference sequence(s) specified.**







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