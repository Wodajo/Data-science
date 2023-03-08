```R
data$death_dummy <- as.integer(data$death != 0)  # create column death_dummy (wierd). If in column death sth is not 0 - type 1. That way if there are different ways of saying "someone died" in data you can easly clean it up
unique(data$death_dummy)  # 0 1  # check ifonly this values are there

```

`less -S` - turn off line wrapping