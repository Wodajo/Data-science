PARENT_DIRS=($(find "$PWD" -type d -printf '%f\n'))
for d in "${PARENT_DIRS[@]}"; do
check_find=$(find "$PWD/$d" -type d \( -name "*fastq_fail" \) -o \( -name "*fastq_pass" \))
if [ -z $check_find ]; then
	echo "No fastq dirs"
else
	echo "fastq found"
fi
done
