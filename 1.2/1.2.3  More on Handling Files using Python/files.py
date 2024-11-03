import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

# learnt read and write




# Append
# try:
#     # Open file in 'a+' mode for both appending and reading
#     file = open('Files/names.txt', 'a+')

#     file.write('Ali Usman Zaidan')
    
#     # # Move the pointer to the start of the file to read its content
#     file.seek(0)  # start reading from the beginning
#     print(file.read())  # Now this will work without an exception
# except Exception as e:
#     # Print the specific exception message
#     print(f"Issues with appending to file: {e}")
# finally:
#     file.close()

# Creating a file 2- ways

# option 1(create if it doesnt exist and open it)
with open('Files/this_didnt_exist.txt','w'):
    print('dn')


# option 2(create if it doesnt exist and open using the os module)

file_path='Files/zaidan.txt'
# if not os.path.exists(file_path):
#     new_file=open(file_path,'x')
#     new_file.close()
    
# deleting a file
if  os.path.exists(file_path):
    os.remove(file_path)
else:
    print('The file does not exist')
