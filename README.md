# Closures
Explanation of closures in python.

To better understand closures you should know first class objects very well. So,
First class functions allow  any function to be treated as an object i.e..
1. We can pass functions as an aruguements to another functions
2. We can assign a function to a variable or return a function as a result of a function 

A closure is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally but defined 
in an enclosing scope) with the value or reference to which the name was bound when the closure was created.A closure—unlike a plain function—allows the function to access 
those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.

In my example I used logging into a file so that when we work on big projects it will help us find error ,running whenever 
