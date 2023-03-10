```R
# ---------------------------- Vectors ---------------------------
# Vectors - list of items of the same type
# c() - funtion to concatenate items (can be used to create vectors)
fruits <- c("banana", "apple", "orange")
numbers <- 1:5
numbers2 <- 1.5:4.4  # 1.5 2.5 3.5
log_values <- c(TRUE, FALSE, TRUE, FALSE)
# lenght() - length of a vector
# sort() - sort numerically or alphabetically
# append() - by default append at the end. Use parameter after=index_nr
append(fruits, "tomato", after = 2)  # it also prints the output o.O

#     INDEX VALUES START FORM 1
fruits[1]  # "banana"
fruits[c(1,3)]  # "banana" "orange"
fruits[c(-1)]  # access all except 1  # "apple" "orange"
fruits[1] <- "cherry"

# rep() - repeat...
 repeat_each <- rep(c(1,2,3), each = 3)  # each value  # 1 1 1 1 2 2 2 3 3 3
 repeat_times <- rep(c(1,2,3), times = 3)  # sequence of vector  # 1 2 3 1 2 3 1 2 3
 repeat_independent <- rep(c(1,2,3), times=c(3,2,1))  # each value independently  # 1 1 1 2 2 3
 
# seq() - generate sequenced vectors
# parameters: from - sequence start, to - sequence stop, by - interval of the sequence
numbers3 <- seq(0, 100, 25)  # 0 25 50 100

# %in% - check is item exist
"cherry" %in% fruits  # TRUE

# ------------------------------- Lists ----------------------------------
# List - ordered & changeable collection of items (can contain different data types)
list1 <- list(1, "cherry", "pizza", "burger", "sushi", "czarcie", "soup")  # wierdly printed. # [[1]] [1] 1  [[2]] [1] "cherry"  [[3]] [1] "pizza"
list1[1] <- 31
list1 <- list1[-1]  # remove first item (doesn't have to mark what data structure it is like in c())
list1[3:5]  # both 3 & 5 are INCLUDED
list2 <- list(43, "Mario", "Luigi", "Pacino")
list3 <- c(list1, list2)  # to join lists

# length(), %in%, append(), rep()

# -------------------------------- Matrices --------------------------------
# matrix() - create matrix with nrow rows and ncol columns
matrix1 <- matrix(c(1,2,3,4,5,6,7,8,9), nrow = 3, ncol = 3)
matrix1[1,2]  # [row, cloumn]
matrix1[,2]  # whole column (analogically for whole row)
matrix1[c(1,2),]  # rows 1 & 2

# dim() - find nr of rows & columns
dim(matrix1)
# nrow() - nr of rows, ncol() - nr of columns
# cbind() - add more columns (must be the same length as existing colums)
matrix2 <- cbind(matrix1, c(0,1,2))
# rbind() - add more rows (must be the same length as existing rows)
matrix2 <- rbind(matrix2, c("pika", "guts", "slan", "SK"))
matrix2 <- matrix2[c(-1),c(-1)]  # remove first row&column
matrix_combined <- rbind(matrix1,matrix2)  # or with cbind()
# length() - dimension of the matrix (rowsxcolums)

"guts" %in% matrix2  # TRUE

for (rows in 1:nrow(matrix1)){
	for (columns in 1:ncol(matrix1)){
    	print(matrix1[rows,columns])
    }
}

# ---------------------------------- Arrays ----------------------------------
# Array can have > 2 dimensions, only one data type.
array1 <- c(1:24)  # array with 1 dimenstion (vector)
# array() - create an array, dim() - parameter to specify dimensions
multiarray <- array(array1, dim = c(4,3,2))  # dim=c(rowns, columns, dimensions)
multiarray[2,3,2]  # array[row, column, matrix level]
multiarray[,c(1),1]  # access all items from first column from matrix 1
2 %in% multiarray  # TRUE
# dim() - rows & columns of array, length() - dimension of array(rowsxcolumnsxdims?)
for (x in multiarray){
	print(x)
}

# ------------------------------- Data frames ---------------------------
# Can have different data types, BUT each column should have the same
Data_frame <- data.frame(
	Training = c("Stamina", "Strength", "Other"),
    Pulse = c(100, 150, 120),
    Duration = c(60, 30, 45)    
)
Data_frame2 <- data.frame (
  Training = c("Stamina", "Stamina", "Strength"),
  Pulse = c(140, 150, 160),
  Duration = c(30, 30, 20)
)
Data_frame3 <- data.frame (
  Steps = c(3000, 6000, 2000),
  Calories = c(300, 400, 300)
)
# summary() - info about data frame liek median, mean, 3rd Qu., max
summary(Data_frame)

# To access items:
Data_frame[1]  # Training Stamina Strength Other (in table fasion)
Data_frame[["Training"]]  # Stamina Strength Other Levels: Other Stammina Strength
Data_frame$Training  # same as above

# rbind() - add a new row / bind data frames vertically
New_row_DF <- rbind(Data_frame, c("Strength", 110, 110))
New_DF_rbind <- rbind(Data_frame, Data_frame2)
# cbind() - add a new column / bind data frames horizontally
New_col_DF <- cbind(Data_frame, Steps = c(1000, 6000, 2000))
New_DF_cbind <- cbind(Data_frame, Data_frame3)
# c() to remove rows/columns
New_DF <- Data_frame[c(-1), c(-1)]  # delete first row & column

# dim() - rows&columns, nrow(), ncol(), length() - similar to ncol()

# ---------------------------- factors -----------------------------------
# used to categorise data
# Create a factor
# factor() - add vector as argument
music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"))
# levels() - shows categories (levels)
levels(music_genre)  # "Classic" "Jazz"    "Pop"     "Rock"

# you can also add levels manually (parameter levels)
 music_genre <- factor(c("Jazz", "Rock", "Classic", "Classic", "Pop", "Jazz", "Rock", "Jazz"), levels = c("Classic", "Jazz", "Pop", "Rock", "Other"))
 
 music_genre[1]  # Jazz
 music_genre[1] <- "Disco-polo"  # ERROR - you can't specify sth that doesn't exist there at all (there is no such level)
 music genre[1] <- "Pop"  # works just fine (there is other "Pop" in the factor)
 
# length(), 
```