```R
data$death_dummy <- as.integer(data$death != 0)  # create column death_dummy (wierd). If in column death sth is not 0 - type 1. That way if there are different ways of saying "someone died" in data you can easly clean it up
unique(data$death_dummy)  # 0 1  # check ifonly this values are there

# alt + - create <- with surrounding spaces
# "cov" ctl + arrow - show all commands starting thatway in history 
# ctl + shift + M - |>
```



`less -S` - turn off line wrapping


```R
filter(dst=="NYC")  # keep rows with matching value
arrange()  # sort rows, by col values. arrange(desc(colname)) for descending
distinct()  # unique rows.
distinct(src, dst) # unique src-dst pairs
distinct(src, dst, .keep_all=TRUE) # unique src-dst paired rows
count(src, dst, sort=TRUE)  # all src-dst pairs, sorted by nr. occurence (descending)
mutate(
	speed = distance/time  # create new col
	.before = 1  # paste col at beggining
	.after = year  # paste after col year
	.keep = "used"  # keep only col used inside mutate()
)
select(
	dep = departure_time,  # rename col while selecting
    src:dst,  # cols from  src to dst
    !year:day,  # all except cols from year to day
    where(is.character),  # cols with chars
    any_of(c(year,day,sth))  # c() could be passed as var. all_of() would throw an error if anything was missing
    starts_with("abc"), 
    ends_with("xyz"),
    contains("sth")
)
relocate(
    src:dst,
    starts_with("abc"), 
	.before = year
	.after = 1
)
group_by(month) |>  # output grouped by month
	summarize(  # grouped operation, only requested values of group
	avg_delay = mean(dep_delay, na.rm = T),  # avg_delay of each month
	# na.rm = T - ignore NA
	n = n()  # nr of rows in each group
	) |>
	slice_head(n=1),  # first row from each group
	slice_head(prop=0.25)  # first 25% of rows from each group
	slice_tail(n=4),  # last 4 rows from each group
	slice_min(x, n=1, with_ties = F),  # row with smallest value in col x
	# jeżeli pare ma najwieksza wartosc - moze zwrocic pare rows.
	# with_ties = F - zwróci tylko jeden row
	slice_max(x, n=1),  # row with largest value in col x
	slice_sample(n=1)  # random row
```


EWR, IAH, MIA, LGA
1. Wszystkie loty z EWR z kwietnia 2013. Od najszybszych do najwolniejszych. Z dodatkową kolumną speed, położoną jako trzecia od lewej.
2. Scatterplot z regresja liniowa pokazujacy zaleznosc czas - speed, color - carrier.
3. Wszystkie miasta src i origin, tabela ze zmieniona nazwa column dla src i dst. Dodatkowa kolumna na src i dst BEZ litery A. 
4. tabela w ktorej pingwiny maja przydzielone wlasne loty w zaleznosci od miesiecy
5. zgrupuj loty miesiacami. Ocen srednie predkosci w poszczegolnych miesiacach. Nowe columny z najwiekszymi i najmniejszymi predkoscimi danego miesiaca.
6. 