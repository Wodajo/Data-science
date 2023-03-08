`wget -qO - https://deb.ubuntu.com/archive.key | sudo apt-key add -`
	`-q` quiet
	`-O -` output to stdout (great for scripting)
	`add` add new to key to list of trusted keys. Normally it reads file, but `add -` read ftom `stdin`