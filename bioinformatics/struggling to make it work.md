
### empty dataframe for /project/reads_noF_noq.plus_strand.per.site.csv

what not ok?
	- code
	- .fa/.fai/.bam/.bai/.dict
	- dependency (not installed? wrong version? e.g. java)

1. try the `Epinano_Variants.py` & `Epinano_Variants.dev.py` with cDNA `ref.fa`
2. check java in container !!!!!!
3. [m6anet](https://m6anet.readthedocs.io/en/latest/installation.html#installation-from-our-github-repository)
4. try to correct `Epinano_Variants.py`/`Epinano_VAriants.dev.py` code (ideas below)
5. basecall with `Gruppy 3.1.5` ->  `EpiNano-SVM`
6. 
7. [novoalab best practices](https://github.com/novoalab/Best_Practices_dRNAseq_analysis) (for `dRNA`)



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
`/Workspace/align/data/reads_noF_noq.tmp/` exist
`/Workspace/align/data/reads_noF_noq.fwd.4.per.site.csv'` don't -.-



`docker exec -it docker_ID bash`    OR     `sudo docker run -it docker_name bash`
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
(doe
s `samtools view -h -F 3860 read.bam | java -jar sam2tsv` output make sense?)



# cDNA as ref.fa !!!!




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




`mv FAU81678_pass_351f87f2_0.fastq.gz reads.fq.gz`
`mv Homo_sapiens.GRCh38.cdna.all.fa.gz ref.fa.gz`
`gzip -d ref.fa.gz` (for `samtools faidx` sake)
`samtools faidx ref.fa`

`minimap2 -a -L --split-prefix=tmp ref.fa reads.fq.gz | samtools view -bh | samtools sort -O bam > reads.bam`
`samtools index reads.bam`




`sudo docker run -it --name epivar -v "$PWD/":/project/ epi12 python3 /usr/local/bin/EpiNano/Epinano_Variants.py -R /project/ref.fa -b /project/reads.bam -s /usr/local/bin/EpiNano/misc/sam2tsv.jar -n 10`