import os
import re

# try to do this in a OOP way
# each sample as object

# use python3 for scripts
# - no wierd escaping rules
# - usefull for later (ML libraries)


# extract raw subdirs
# declare important paths:
# - fast5 dirs
# - reference transcriptome

def dec_gate(dec):
    if dec == "" or dec.lower().strip() == "y" or dec.lower().strip() == "yes":
        dec = True
    else:
        dec = False
    return dec

def get_paths():
    RAW_DIR = f"~+/dump/raw"
    command = f"find {RAW_DIR} -mindepth 1 -maxdepth 1 -type d | sort"
    RAW_SAMPLE_DIRS = os.popen(command).read()
    get_paths.RAW_SAMPLE_DIRS_list = RAW_SAMPLE_DIRS.splitlines()  # list created that way, so that functions outside
    # get_paths() recognize this list (and could modify it!)
    get_paths.RAW_SAMPLE_NAMES_ALL_list = []
    get_paths.RAW_SAMPLE_NAMES_SAMPLE_list = []
    get_paths.RAW_SAMPLE_NAMES_CONTROL_list = []
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
    print(f'[+] samples fast5 {get_paths.RAW_FAST5_FILES_ALL_SAMPLE_list}\n'
          f'[+] controls fast5 {get_paths.RAW_FAST5_FILES_ALL_CONTROL_list}\n'
          f'[+] not matched fast5 {get_paths.RAW_FAST5_FILES_ALL_NOT_MATCHED_list}')

def naming_scheme():
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

def map_and_index():
    minimap_flags = "-ax map-ont -L --split-prefix=tmp"

    os.popen(command)
    command = f'minimap2 {minimap_flags} {}'

# functions for:
# - basecalling
# - aligning
# - indexing
# - ...
