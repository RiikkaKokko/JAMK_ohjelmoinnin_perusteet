import datetime

def my_function(x):

    """Purpose of this function is to increase given parameter by one

    Parameters
    ___________

    x : int
        a numeric value that will be increased by one

    Returns
    __________

    int
        increases parameter 'x' by one and returns the result from the function
    """

    return x+1

# Print current date and time
print(datetime.datetime.now())

#declare a variable as 'name' and assign some text into it
name= "Riikka Kokko"

# Print the contents of the 'name' variable
print(name)

# call the function
value = my_function(100)
print(value)
