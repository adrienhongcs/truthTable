# Truth Table Generator
Created by Adrien Hong to help with boolean arithmetic and discrete mathematics homework.
The website is hosted at https://www.cs.mcgill.ca/~ahong6/truthTable/
 
This website takes as input a boolean expression and outputs a truth table with all possible values of the variables and their results. The user enters a boolean expression and sends the form. Using python, the expression is checked for its validity. If not valid, a message is outputted pointing out the error. If valid, the truthTable is outputted.

key concepts: in to post-fix expression, operators precedence, stack algorithms

index.html: creates the content of the main page. 

result.html: creates the content of the result page.

style.css: styles index.html and result.html.

main.py: called by index.html, prints the content of result.html and adds the given expression and its truthTable.

parse.py: contains functions that parse through the expression to remove spaces, evaluate it...

truthTable.py: creates and fills the variable values of the truthTable.

Helper.py: contains helper functions for truthTable.py and parse.py.
