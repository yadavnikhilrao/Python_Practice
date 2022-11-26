# Return in function
# A return statement ends the execution of a function, and returns control to the calling function.

def table(n):
    for i in range(1,11):
        return i*n
    
table(int(input('Enter the number: ')))  # calling function
