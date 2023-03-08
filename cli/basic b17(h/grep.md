`grep OPTIONS PATTERN FILES`


#### options
`-l` list files with a match of pattern
	e.g. `grep -l copyright *.html` - all `.html` with string "copyright"
`-L` list files without a match of pattern

`-B NUM` lines **before** match
`-A NUM` lines **after** match
`-C NUM` lines **circling** match
	e.g. `grep -B 4 "dhcp" /var/log/syslog`

`-i` case insensitive

`-E` extended regex
`-G` basic  regex

