import os, re, datetime
from OOP import Reference, Sample


# try to do this in a OOP way
# each sample as object

# function for data prep & check if averything is in order for analysis

def now():
    return datetime.datetime.now().strftime('%D:%H:%M:%S')


def get_raw_dirs_paths_list():
    script_dir_path = os.path.dirname(
        os.path.abspath(__file__))  # get absolute path of dir form which the script is run
    raw_dir_path = f'"{os.path.join(script_dir_path, "dump", "raw")}"'  # ./dump/raw
    raw_dirs_paths_list = os.popen(f"find {raw_dir_path} -mindepth 1 -maxdepth 1 -type d | sort").read().splitlines()
    return raw_dirs_paths_list


def set_samples_names_and_main_dir_to_dict(raw_dirs_paths_list):
    # sample_list = []  # I don't really care about order here
    sample_dict = {}  # name should be a unique identifier
    for sample in raw_dirs_paths_list:
        sample_name = str(sample.split('/')[-1])
        if sample_name == "ref":
            continue
        sample_instance = Sample(name=sample_name, sample_main_dir_path=sample)
        sample_dict[sample_name] = sample_instance
    # for name, sample_instance in sample_dict.items():  # check print(f'Kay: {name}, Sample name: {
    # sample_instance._name}, Sample dir: {sample_instance._sample_main_dir_path}')
    return sample_dict


def get_set_fast5_dirs_paths(sample_dict):  # there HAVE TO be _pass and failed dirs. Otherwise 
    for name, sample_instance in sample_dict.items():
        command = f'find "{sample_instance._sample_main_dir_path}" -type d -name "fast5*" | sort'
        sample_instance._fast5_dirs_paths_list = os.popen(command).read()
        # -- extract fast5 dirs from fast5_dirs_paths_list
        fast5_dirs_list = sample_instance._fast5_dirs_paths_list  # working copy
        for fast5_dir in fast5_dirs_list:
            try:
                if "_pass" in fast5_dir:
                    sample_instance._fast5_pass_dir_path = str(fast5_dir)
                elif "_fail" in fast5_dir:
                    sample_instance._fast5_pass_dir_path = str(fast5_dir)
                else:
                    print(f'[+] Warning - detected fast5 dirs not named "_pass" or "_fail"\n'
                          f'[+] {fast5_dir}')
            except:
                print(f'[+] Error in get_set_fast5_dirs_paths() - fast5')
        command = f'find "{sample_instance._sample_main_dir_path}" -type d -name "fastq*" | sort'
        sample_instance._fastq_dirs_paths_list = os.popen(command).read()
        # -- extract fastq dirs from fastq_dirs_paths_list
        fastq_dirs_list = sample_instance._fastq_dirs_paths_list
        for fastq_dir in fastq_dirs_list:
            try:
                if "_pass" in fastq_dir:
                    sample_instance.__fastq_pass_dir_path = str(fastq_dir)
                elif "_fail" in fastq_dir:
                    sample_instance._fast5_fail_dir_path = str(fastq_dir)
                else:
                    print(f'[+] Warning - detected fastq dirs not named "_pass" or "_fail"\n'
                          f'[+] {fastq_dir}')
            except:
                print(f'Error in get_set_fast5_dirs_paths() - fastq')
    for key, value in sample_dict.items():  # check
        print(
            f'Kay: {key}, Sample name: {value._name}\nSample fast5 list: {value._fast5_dirs_paths_list}\nSample main dir path: {value._sample_main_dir_path}\n\n')


'''
        command = f'find {sample_instance._sample_main_dir_path} -mindepth 2 -type f -name "fast5_pass*" | sort'

    command = f'find {RAW_DIR} -mindepth 2 -type f -name "fast5_pass*" | sort'
    RAW_FAST5_FILES_PASS_ALL = os.popen(command).read()
    get_paths.RAW_FAST5_FILES_PASS_ALL_list = RAW_FAST5_FILES_PASS_ALL.splitlines()
    command = f'find {RAW_DIR} -mindepth 2 -type f -name "fast5_fail*" | sort'
    RAW_FAST5_FILES_FAIL_ALL = os.popen(command).read()
    get_paths.RAW_FAST5_FILES_FAIL_ALL_list = RAW_FAST5_FILES_FAIL_ALL.splitlines()
    get_paths.RAW_FAST5_FILES_ALL_list = get_paths.RAW_FAST5_FILES_PASS_ALL_list + get_paths.RAW_FAST5_FILES_FAIL_ALL_list
    get_paths.RAW_FAST5_FILES_ALL_SAMPLE_list = []
    get_paths.RAW_FAST5_FILES_ALL_CONTROL_list = []
    get_paths.RAW_FAST5_FILES_ALL_NOT_MATCHED_list = []
    command = f'find {RAW_DIR} -mindepth 1 -maxdepth 1 -type d -name "ref"'
    get_paths.RAW_REF_DIR = os.popen(command).read()
    command = f'find "{get_paths.RAW_REF_DIR.rstrip()}" -type f'
    get_paths.RAW_REF_ALL = os.popen(command).read()
    get_paths.RAW_REF_ALL_list = get_paths.RAW_REF_ALL.splitlines()





def set_sample_fast5_paths(sample_dict):
    pass




def get_paths():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # get absolute path of dir form which the script is run
    RAW_DIR = f'"{os.path.join(script_dir, "dump", "raw")}"'  #  ./dump/raw
    command = f"find {RAW_DIR} -mindepth 1 -maxdepth 1 -type d | sort"
    RAW_SAMPLE_DIRS = os.popen(command).read()
    get_paths.RAW_SAMPLE_DIRS_list = RAW_SAMPLE_DIRS.splitlines()  # list created that way, so that functions outside
    # get_paths() recognize this list (and could modify it!)
    get_paths.RAW_SAMPLE_NAMES_ALL_list = []
    get_paths.RAW_SAMPLE_NAMES_SAMPLE_list = []
    get_paths.RAW_SAMPLE_NAMES_CONTROL_list = []
    # ----- declaring fast5 vars
    command = f'find {RAW_DIR} -mindepth 2 -type d -name "fast5*" | sort'
    RAW_FAST5_DIRS = os.popen(command).read()
    get_paths.RAW_FAST5_DIRS_list = RAW_FAST5_DIRS.splitlines()
    command = f'find {RAW_DIR} -mindepth 2 -type f -name "fast5_pass*" | sort'
    RAW_FAST5_FILES_PASS_ALL = os.popen(command).read()
    get_paths.RAW_FAST5_FILES_PASS_ALL_list = RAW_FAST5_FILES_PASS_ALL.splitlines()
    command = f'find {RAW_DIR} -mindepth 2 -type f -name "fast5_fail*" | sort'
    RAW_FAST5_FILES_FAIL_ALL = os.popen(command).read()
    get_paths.RAW_FAST5_FILES_FAIL_ALL_list = RAW_FAST5_FILES_FAIL_ALL.splitlines()
    get_paths.RAW_FAST5_FILES_ALL_list = get_paths.RAW_FAST5_FILES_PASS_ALL_list + get_paths.RAW_FAST5_FILES_FAIL_ALL_list
    get_paths.RAW_FAST5_FILES_ALL_SAMPLE_list = []
    get_paths.RAW_FAST5_FILES_ALL_CONTROL_list = []
    get_paths.RAW_FAST5_FILES_ALL_NOT_MATCHED_list = []
    command = f'find {RAW_DIR} -mindepth 1 -maxdepth 1 -type d -name "ref"'
    get_paths.RAW_REF_DIR = os.popen(command).read()
    command = f'find "{get_paths.RAW_REF_DIR.rstrip()}" -type f'
    get_paths.RAW_REF_ALL = os.popen(command).read()
    get_paths.RAW_REF_ALL_list = get_paths.RAW_REF_ALL.splitlines()
    # ------ declaring fastq vars
    command = f'find {RAW_DIR} -mindepth 2 -type d -name "fastq*" | sort'
    RAW_FASTQ_DIRS = os.popen(command).read()
    get_paths.RAW_FASTQ_DIRS_list = RAW_FASTQ_DIRS.splitlines()
    command = f'find {RAW_DIR} -mindepth 2 -type f -name "fastq_pass*" | sort'
    RAW_FASTQ_FILES_PASS_ALL = os.popen(command).read()
    get_paths.RAW_FASTQ_FILES_PASS_ALL_list = RAW_FASTQ_FILES_PASS_ALL.splitlines()
    command = f'find {RAW_DIR} -mindepth 2 -type f -name "fastq_fail*" | sort'
    RAW_FASTQ_FILES_FAIL_ALL = os.popen(command).read()
    get_paths.RAW_FASTQ_FILES_FAIL_ALL_list = RAW_FASTQ_FILES_FAIL_ALL.splitlines()
    get_paths.RAW_FASTQ_FILES_ALL_list = get_paths.RAW_FASTQ_FILES_PASS_ALL_list + get_paths.RAW_FASTQ_FILES_FAIL_ALL_list
    get_paths.RAW_FASTQ_FILES_ALL_SAMPLE_list = []
    get_paths.RAW_FASTQ_FILES_ALL_CONTROL_list = []
    get_paths.RAW_FASTQ_FILES_ALL_NOT_MATCHED_list = []
    # -------- control prints
    print("#############################")
    print("[+] detected raw directories:")
    for dir in get_paths.RAW_SAMPLE_DIRS_list:
        print(f"{dir}")
    print("------------------------------")
    print("[+] detected fast5 directories:")
    for dir in get_paths.RAW_FAST5_DIRS_list:
        print(f"{dir}")
    print("------------------------------")
    print("[+] detected fast5_pass files:")
    for fast5 in get_paths.RAW_FAST5_FILES_PASS_ALL_list:
        print(f"{fast5}")
    print("------------------------------")
    print("[+] detected fast5_fail files:")
    for fast5 in get_paths.RAW_FAST5_FILES_FAIL_ALL_list:
        print(f"{fast5}")
    print("------------------------------")
    print("[+] detected fastq directories:")
    for dir in get_paths.RAW_FASTQ_DIRS_list:
        print(f"{dir}")
    print("------------------------------")
    print("[+] detected fastq_pass files:")
    for fastq in get_paths.RAW_FASTQ_FILES_PASS_ALL_list:
        print(f"{fastq}")
    print("------------------------------")
    print("[+] detected fastq_fail files:")
    for fastq in get_paths.RAW_FASTQ_FILES_FAIL_ALL_list:
        print(f"{fastq}")
    print("------------------------------")
    # ------- sample/control&reference selection
    print(f'[+] names of samples for further analysis:')
    for sample in get_paths.RAW_SAMPLE_DIRS_list:
        sample = str(sample.split('/')[-1])
        get_paths.RAW_SAMPLE_NAMES_ALL_list.append(sample)
        print(f'{sample}')
    naming_scheme()
    print("---------------------------------")
    print(f'[+] samples/batch1 {get_paths.RAW_SAMPLE_NAMES_SAMPLE_list}\n'
          f'[+] controls/batch2 {get_paths.RAW_SAMPLE_NAMES_CONTROL_list}')
    print("---------------------------------")
    for fast5 in get_paths.RAW_FAST5_FILES_ALL_list:
        check1 = fast5.split('/')[-3]
        check2 = fast5.split('/')[-4]
        if (naming_scheme.batch1 in check1) or (naming_scheme.batch1 in check2):
            get_paths.RAW_FAST5_FILES_ALL_SAMPLE_list.append(fast5)
        elif (naming_scheme.batch2 in check1) or (naming_scheme.batch2 in check2):
            get_paths.RAW_FAST5_FILES_ALL_CONTROL_list.append(fast5)
        else:
            get_paths.RAW_FAST5_FILES_ALL_NOT_MATCHED_list.append(fast5)
    for fastq in get_paths.RAW_FASTQ_FILES_ALL_list:
        check1 = fastq.split('/')[-3]
        check2 = fastq.split('/')[-4]
        if (naming_scheme.batch1 in check1) or (naming_scheme.batch1 in check2):
            get_paths.RAW_FASTQ_FILES_ALL_SAMPLE_list.append(fastq)
        elif (naming_scheme.batch2 in check1) or (naming_scheme.batch2 in check2):
            get_paths.RAW_FASTQ_FILES_ALL_CONTROL_list.append(fastq)
        else:
            get_paths.RAW_FASTQ_FILES_ALL_NOT_MATCHED_list.append(fastq)
    print(f'[+] samples fast5 {get_paths.RAW_FAST5_FILES_ALL_SAMPLE_list}\n'
          f'[+] controls fast5 {get_paths.RAW_FAST5_FILES_ALL_CONTROL_list}\n'
          f'[+] not matched fast5 {get_paths.RAW_FAST5_FILES_ALL_NOT_MATCHED_list}')
    print(f'[+] samples fastq {get_paths.RAW_FASTQ_FILES_ALL_SAMPLE_list}\n'
          f'[+] controls fastq {get_paths.RAW_FASTQ_FILES_ALL_CONTROL_list}\n'
          f'[+] not matched fastq {get_paths.RAW_FASTQ_FILES_ALL_NOT_MATCHED_list}')
def naming_scheme():  # strictly codependent with get_paths()
    naming_scheme.batch1 = str(input(f"[+] enter sample/batch1 prefix/pattern: "))
    # print(f"[+] selected samples/batch1:")
    for sample in get_paths.RAW_SAMPLE_NAMES_ALL_list:
        if re.search(naming_scheme.batch1, sample):
            # print(sample)
            get_paths.RAW_SAMPLE_NAMES_SAMPLE_list.append(sample)
    naming_scheme.batch2 = str(input(f"[+] enter control/batch2 prefix/pattern: "))
    # print(f"[+] selected controls/batch2:")
    for sample in get_paths.RAW_SAMPLE_NAMES_ALL_list:
        if re.search(naming_scheme.batch2, sample):
            # print(sample)
            get_paths.RAW_SAMPLE_NAMES_CONTROL_list.append(sample)
    print(f"[+] ref dir contents:")
    for ref in get_paths.RAW_REF_ALL_list:
        print(f"{ref}")
    naming_scheme.TRANSCRIPT_REFERENCE = str(input(f"[+] enter path to transcript reference: "))

def dec_gate(dec):
    if dec == "" or dec.lower().strip() == "y" or dec.lower().strip() == "yes":
        dec = True
    else:
        dec = False
    return dec


def map_and_index(dec):
    # ------ index transcript ref
   if dec:
       command = f'samtools faidx {naming_scheme.TRANSCRIPT_REFERENCE}'
       os.popen(command)
   minimap_flags = "-ax map-ont -L --split-prefix=tmp"



    # # ------ concatenate fq -> byłoby łatwiej OOP
    # for sample in get_paths.RAW_FASTQ_FILES_ALL_SAMPLE_list:
    #     check1 = sample.split('/')[-3]
    #     check1 = sample.split('/')[-3]
    #     if sample in :
    # command = f'cat {}'
    # get_paths.RAW_SAMPLE_NAMES_ALL_list
    #
    # for fastq_prefix in x:
    # command = (f'minimap2 {minimap_flags} {naming_scheme.TRANSCRIPT_REFERENCE} '
    #            f'{fastq_prefix}.fq.gz | samtools view -bh | samtools sort -O bam > {fastq_prefix}.bam;'
    #            f'samtools index {fastq_prefix}.bam')

# functions for:
# - aligning
# - indexing
#- basecalling
'''
