# Closures
Explanation of closures in python.

To better understand closures you should know first class objects very well. So,
First class functions allow  any function to be treated as an object i.e..
1. We can pass functions as an aruguements to another functions
2. We can assign a function to a variable or return a function as a result of a function 

A closure is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally but defined 
in an enclosing scope) with the value or reference to which the name was bound when the closure was created.A closure—unlike a plain function—allows the function to access 
those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.

In my code example I used logging module that lets you track events when your code runs so that when the code crashes you can check the logs and identify what caused it. Log messages have a built-in hierarchy – starting from debugging, informational, warnings, error and critical messages. You can include traceback information as well. It is designed for small to large python projects with multiple modules and is highly recommended for any modular python programming.

Using logging, you can:

1.Control message level to log only required ones
2.Control where to show or save the logs
3.Control how to format the logs with built-in message templates
4.Know which module the messages is coming from

so thats all !
Have a good day
