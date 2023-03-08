`awk '{print $0}'`- print every field
`awk -F":" '{print $1 "/t" $3}' ~/text`

`awk -F"," '{print $(NF)}'
	`$NF` - last field

`awk 'BEGIN{FS=":"; OFS="-"} {print $1,$6,$7}' /etc/passwd`
	input field separator is ':' -> i want output field separator '-'
	if arguments not comma-separated - field separator won't be printed


`awk '($3 == "Toyota") {print}' names.txt` - where $3 eq 'Toyota' -> print line

`awk '($5 < 1945) {print $2}' names.txt` - where $5 < 1945 -> print $2
