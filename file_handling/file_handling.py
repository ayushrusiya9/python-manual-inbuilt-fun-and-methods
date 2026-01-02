## FILE HANDLING

# file handling -> used to store data permanently in a file
# and read data from a file when needed.
# Example:
# save data in a text file instead of variables.


# open() -> opens a file and returns a file object.
# Syntax:
# file = open('file.extension', 'mode')
# Example:
# f = open('data.txt', 'r')


# close() -> closes the file and releases system resources.
# Always close the file after use.
# Example:
# f.close()


## FILE MODES

# 'r' (read) -> reads data from file.
# Error if file does not exist.
# Example:
# open('data.txt', 'r')


# 'w' (write) -> writes data to file.
# Creates file if not exists.
# Overwrites existing data.
# Example:
# open('data.txt', 'w')


# 'a' (append) -> adds data at the end of file.
# Creates file if not exists.
# Example:
# open('data.txt', 'a')


# 'x' (exclusive create) -> creates a new file.
# Error if file already exists.
# Example:
# open('data.txt', 'x')


## FILE OPERATIONS

# write() -> writes string data into file.
# Example:
# f.write("Hello World")


# writelines() -> writes multiple strings at once.
# Example:
# f.writelines(["Hello\n", "Python\n"])


# read() -> reads complete file content as a string.
# Example:
# data = f.read()


# readline() -> reads one line at a time.
# Example:
# line = f.readline()


# readlines() -> reads all lines and returns a list.
# Example:
# lines = f.readlines()


## FILE POINTER 

# tell() -> returns current position of file pointer.
# Example:
# f.tell()


# seek() -> moves file pointer to a specific position.
# Example:
# f.seek(0)   # move to start of file


## WITH KEYWORD

# with keyword -> used to open file safely.
# It automatically closes the file after block execution.
# No need to call close().
# Example:
# with open('data.txt', 'r') as f:
#     data = f.read()


## FILE METHODS

# closed -> returns True if file is closed, else False.
# Example:
# f.closed


# name -> returns file name.
# Example:
# f.name


# mode -> returns file open mode.
# Example:
# f.mode