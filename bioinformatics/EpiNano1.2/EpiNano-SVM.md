`SVM` (support vector machine) learning - classifier powerful at recognizing subtle patterns in complex datasets

- pre-trained(must be basecalled with `Guppy 3.1.5`)/self-trained models for a given RNA mod
	training with:
	- "raw" base-calling 'error' features
	- capture differences in mismatch, rather than absolute mismatch frequency (better performance)
- direct RNA sequencing reads has error-rich nature- matched control (e.g. `KO` or `KD`) recommended
	without control we could't be sure if the results are truly methylations or not
	(but in comparative COVID it should be fine)

**`Epinano-Variants`** per-site&per-kmer
	quality, insertion, deletion, mismatch
**`Epinano_Current`** (optional)
	current intensity
**`EpiNano_Predict`**
	- train SVM models
	- predict RNA mods using pretrained models (`ProbM`)

`m6A` SVM models has been trained and tested upon a set of 'unmodified' and 'modified' sequences containing `m6A` at known sites or `A`

SVM models with `delta features` - capturing difference between modified and un-modified samples. Detect other RNA modifications apart from `m6A` (tested on `pseudouridine`)

`/test_data/make_predictions` - commands to make predictions with pre-trained models
`test_data/train_models/train_test.sh` - commands to train models & assess prediction accuracies