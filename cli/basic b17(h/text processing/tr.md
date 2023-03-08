translate or delete characters

###### find&replace chars
`echo "This is a line of text" | tr 'aeio' 'AEIO'` - find char -> replace with what's mapped
```
ThIs Is A lInE Of tExt
```

can take classes
`echo "This is a line of text" | tr '[[:lower:]]' '[[:upper:]]'`
```
THIS IS A LINE OF TEXT
```


###### delete chars
`echo "This is a line of text" | tr -cd 'aeio'`
	`-d` delete
```
Ths s  ln f txt
```

`echo "This is a line of text" | tr -cd 'aeio'`
	`-c` delete everything that NOT...
```
iiaieoe
```


###### squeeze chars
`echo "Thiiis iiiis  aaa     lineeee oof  teeext" | tr -s 'aeio '`
	`-s` squeeze
```
This is a line of text
```


###### generate random passwds
`head -n 3 /dev/urandom | tr -cd [[:print:]] | cut -c 1-16`
```
kue4ZbI6oml4K%6
```