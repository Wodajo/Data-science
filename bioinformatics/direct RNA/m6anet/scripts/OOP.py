import os
import re

class Reference:
    def __init__(self):
        self.__ref_transcriptome_path = ""
        self.__ref_genome_path = ""
        self.__ref_gtf_path = ""
        self.__ref_transcriptome_index_path = ""
        pass


class Sample:  # add per-sample relevant semiproducts
    def __init__(self, id="", name=""):
        self.__id = id  # id of sample - for sake of creating them in range() loop. Obsolete?
        self.__batch = ""  # sample/control
        self.__name = name  # name of particular sample (e.g. covid1)
        self.__project_raw_dir_paths_list = []
        self.__sample_main_dir_path = ""
        self.__fast5_pass_dir_path = ""
        self.__fast5_fail_dir_path = ""
        self.__fast5_dirs_paths_list = []  # path to fast5 pass&fail dirs
        self.__slow5_dir_path = ""  # one, bcos for now only for m6anet sake
        self.__fastq_pass_dir_path = ""
        self.__fastq_fail_dir_path = ""
        self.__fastq_dirs_paths_list = []
        self.__fastq_pass_merged_path = ""
        self.__fastq_fail_merged_path = ""
        self.__fastq_all_merged_dir_path = ""
        self.__bam_path = ""
        self.__bam_index_path = ""







''''

        # def create_instances_of_Sample_class(self):
    #     sample_list = []
    #     for i in range(1,len(self.RAW_DIRS_PATHS_LIST)):  # exclude last - we want it bcos ref
    #         sample_id = f"sample{i}"
    #         sample = Sample(id=sample_id)
    #         sample_list.append(sample)





def get_paths():


print(f'[+] names of samples for further analysis:')
    for sample in RAW_SAMPLE_DIRS_list:
        sample = str(sample.split('/')[-1])
        RAW_SAMPLE_NAMES_ALL_list.append(sample)
        print(f'{sample}')





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
    '''
