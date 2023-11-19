from nanopore_basic_func import get_raw_dirs_paths_list,set_samples_names_and_main_dir_to_dict,get_set_fast5_dirs_paths

# ------------------- Methylation

raw_dirs_paths_list = get_raw_dirs_paths_list()
sample_dict = set_samples_names_and_main_dir_to_dict(raw_dirs_paths_list)
get_set_fast5_dirs_paths(sample_dict)

'''

get_paths()  # establish paths and sample groups

dec = str(input("Index transcriptome? [Y/n]: "))
dec = dec_gate(dec)
map_and_index(dec)


# opcjonalne checki w get_paths
# If not - select fq dir
# - add option to run basecaller


'''