stream editor

###### find&replace
`sed 's/find/replace/ < oldfile > newfile'` - at every line find first instance of 'find' -> replace with 'replace'
	`s` substitution
`sed 's_find_replace_g < oldfile > newfile'` - at every line find every instance of 'find' -> replace with 'replace'
	`g` global

`sed -i 's/find/replace/g' filename`
	`-i` write changes in-place
`cat /etc/shells | sed -e 's|usr|u|g' -e 's#bin#b#g'`
	`-e` pass additional searches
`sed -i 's/[[:space:]]*$//' test.sh` - delete any whitespace char at the end of a line


###### find a line with a match and...
`cat .zshrc | sed '/Replace/s/no/NO/g'` - find all lines having 'Replace' -> substitute every 'no' at this line with 'NO'
`cat .zshrc | sed '/line_pattern/d'` - find all lines having "line_pattern" -> delete them
	`-d` delete line


##### prepend&append lines
`sed '4 i #THIS is an extra line' test.txt`
	`i` insert text before line nr 4

`sed '/Pattern/ a #This line is appended after pattern'`
	`a` append text after