from nanopore_basic_func import get_paths,dec_gate

# ------------------- Methylation
get_paths()  # establish paths and sample groups
# NOT DONE fq! - ask if you want to basecall.
# If not - select fq dir

dec = str(input("Skaner ICMP? [Y/n]: "))
dec = dec_gate(dec)