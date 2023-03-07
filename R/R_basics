# print is a function
print("Eluwiny")

# you have to use print() function if you want to use code in other functions
for (x in 1:5) {
	print(x)
}

# assign value to variable via <-
# ( = can be used too BUT it is forbidden in some contexts, so <- is better)
name <- "Mateusz"
crying <- "is not yet crying"
age <- 25
var1 <- var2 <- var3 <- "same value for thee variables"

#----------------------------- DATA TYPES --------------------------------
# numeric (10, 55.5)
# integer (1L, 55L) - L declares it's an integer
# character aka string ("4", "I like corn", "TRUE")
# logical aka boolean (TRUE or FALSE)
# complex (9 + 3i) - i is the imaginary part

# check data type with class()
class(var2)

# convert data type with as.numeric(), as.integer(), as.complex()
age2 <- "24"
as.numeric(age2) + 3
age2 <- as.numeric(age2)
age2 - 3


# math functions:
# min(), max(), sqrt() - square root, abs() - absolute value
# ceiling() - round-down to int, floor() - round-up to int


# str functions:
# in multiline string - newlines will be added as escape char "\n"
# (instead line breaks)
str <- "Jestem matka Witkacego
Zjadłam wczoraj klocki Lego"
str2 <- "We are the so-called \"Vikings\", from the north."
print(str)  # "Jestem matka Witkacego\nZjadłam wczoraj klocki Lego"
print(str2)  # "We are the so-called \"Vikings\", from the north."

# cat() - print output with interpreted escape characters
# (e.g. line breaks instead \n)
cat(str2)  # We are the so-called "Vikings", from the north.

# nchar() - str length
# grepl() - character or a sequence of characters present in a string -> boolean
grepl("matka", str)  # TRUE
# paste() - concatenate&print vars
paste(name, crying, "bro")

# ------------------------------- OPERATORS --------------------------
# Arithmetic (+, -, *, /, ^, %% - modulus/remainder of division, %/% - integer division/discard remainder of division) 
# Assignment (<-, <<-, ->, ->>)
# Comparison (==, !=, >, <, >=, <=)
# Logical (& - element-wise "AND" operator, &&, | - element-wise "OR", ||, ! - "NOT")
# Miscellaneous (: - creates series of nrs in a sequence, %in% - find out if an element belong in a vector, %*% - matrix multiplication)

# ------------------------------- if else -----------------------------
if (age > age2 & age > 10) {
	paste(age,"is greater than", age2)
} else if (age == age2 | age2 == 25) {
	paste(age, "and", age2, "are equal")
} else {
	paste(age, "is lower than", age2)
}

# ------------------------------- LOOPS --------------------------------
i <- 1
while (i<8) {
    i <- i+1
    if (i == 3){
    next
    }
    print(i)
    if (i == 6){
    break
    }
}

colors <- list("red", "yellow", "cherry")
fruits <- list("apple", "banana", "cherry")
for (x in colors) {
	for (y in fruits) {
    print(paste(x,y))
    }
} 


# ------------------------------ FUNCTIONS  --------------------------------
my_function <- function(fname="John", age3=1) {  # create a function with a name my_function, fname is an parameter (you pass argument to make it a value of the parameter) with default value "John"
	print(paste("Hello", fname))
    return (5 * age3)  #
}

print(my_function())
print(my_function("Ceftolozan/tazobactam", 3))
