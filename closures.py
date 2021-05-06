# Closures

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):# We have a function  named logger which takes in a function as its arguement
    def log_func(*args):# '*' here show we can pass any number of arguemrnts
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))#executing the function with args and printing that to console
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)# Here func is 'add' and we are assigning inner function 'log_func' to variable add_logger so it will work same as function 
sub_logger = logger(sub)

# Now we are passing args in and printing out in console
add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)


