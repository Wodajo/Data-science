from nanopore_basic_func import get_raw_dirs_paths_list,create_samples_to_list

# ------------------- Methylation

RAW_DIRS_PATHS_LIST = get_raw_dirs_paths_list()
create_samples_to_list(RAW_DIRS_PATHS_LIST)


'''

get_paths()  # establish paths and sample groups

dec = str(input("Index transcriptome? [Y/n]: "))
dec = dec_gate(dec)
map_and_index(dec)


# opcjonalne checki w get_paths
# If not - select fq dir
# - add option to run basecaller


'''