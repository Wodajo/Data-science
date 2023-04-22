##### CUPS

1. app sends PDF to CUPS (if it's not PDF it's changed into PDF)
2. CUPS looks at the printer's PPD file (printer description file) and figures out what filters it needs to use to convert the PDF file to a language that the printer understands (like PJL, PCL, bitmap or native PDF)
3. filter converts the PDF file to a format understood by the printer
4. it is sent to the back-end. For example, if the printer is connected to a USB port, it uses the USB back-end

`pacman -S cups foomatic-db ghostscript gsfonts gutenprint foomatic-db-gutenprint-pdds`
	`cups` - current standards-based, open source printing system, `foomatic` - provides PPDs for many printer drivers, `ghostscript` - for non-PDF printers, `gutenprint` - drivers for Canon, Epson, Lexmark, Sony, Olympus, and PCL printers for use with CUPS and GIMP  
	**You might have to check for PDD on producer site or in AUR**

`vim /etc/cups/cups-files.conf`
```
SystemGroup root lpadmin  # add `lpadmin` group
```

`usermod -aG lpadmin arco`
`sudo systemctl enable cups`
`127.0.0.1:631` CUPS web interface


#### cli printing
`lpq` - show the printing queue
	(you can lookup job numbers here)
`lpr` - print
	e.g.
	`echo "This is going to print so hard" | lpr`
	`lpr document_for_printing.txt`
`lprm NUMBER_OF_JOB` - rm job from printing queue