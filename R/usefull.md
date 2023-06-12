```R
data$death_dummy <- as.integer(data$death != 0)  # create column death_dummy (wierd). If in column death sth is not 0 - type 1. That way if there are different ways of saying "someone died" in data you can easly clean it up
unique(data$death_dummy)  # 0 1  # check ifonly this values are there

# alt + - create <- with surrounding spaces
# "cov" ctl + arrow - show all commands starting thatway in history 
```



`less -S` - turn off line wrapping


```R
filter()  # keep rows with matching value
arrange()  # sort rows, by col values. arrange(desc(colname)) for descending
distinct()  # unique rows.
### Finds first occurrence of unique row in the dataset and discard the rest ###
distinct(src, dst) # src-dst pairs
distinct(src, dst, .keep_all=TRUE) # src-dst paired rows
count(src, dst, sort=TRUE)  # src-dst pairs, sorted by nr. occurence (descending)
```