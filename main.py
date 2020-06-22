#!/usr/bin/python
import cgi
import cgitb
from truthTable import TruthTable
import parse

def main():
    print("Content-type:text/html\n\n")
    form = cgi.FieldStorage()
    expr = form.getvalue('myExpression')        #fetching the boolean expression into value expr
    result = open("/home/2019/ahong6/public_html/truthTable/result.html","r")
    for line in result:
        if ("<!--HERE-->" in line):

            expr = parse.removeSpace(expr)              # removing spaces from the expression
            seperator=' '
            print("You entered: "+seperator.join(expr)+"<br>")
            var = parse.validNGetVar(expr)              # checks if the expression is valid, if valid returns a list of the variables       
            if ( var[0]==None): print("Try again")
            else:
                truthTable = TruthTable(len(var))           # creates a table with 2^N columns and N+1 rows leaving the last row empty for the result
                postFix = parse.inToPost(expr)              # convert the in-fix expression to a post-fix expression (precedence of operators=>easier)
                for i in range(truthTable.getRows()):       # loops through every row of the table
                    row = truthTable.table[i]
                    truthTable.table[i][len(var)] = parse.evalExpr(row, postFix, var)   # evaluates and fills the result of the row
                truthTable.display(var)
        else:
             print(line)
    result.close()


main()
