`cut -c 1-10 .bashrc` - print first 10 characters of every line of `.bashrc`
	`-c` characters
`cut -c 11- .bashrc` - print every char from 11 char to the end of each line

`cut -d '' -f 5` - print 5th word
	`-d` delimiter
		if leading spaces between words - `awk` is better
		e.g.
		`echo "abc    def" | cut -f 2 -d ' '`  - print ' '
		`echo "abc    def" | awk -F' ' '{print $2}'` - print 'def'
