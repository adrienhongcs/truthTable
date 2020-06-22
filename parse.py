import Helper
from Queue import LifoQueue



def removeSpace(expr):
    result=[]
    for char in expr:
        if (char!=' '): result.append(char)
    if (len(result)==0): Helper.error("You entered an empty expression")
    return result

def validNGetVar(expr):
    '''
    takes as input an expression with spaces removed and checks if it is a valid boolean expression
    if valid, returns a list of the variables 
    ''' 
    var = []
    numOfParentheses = 0 
    end = len(expr)-1
    prevIsVar = False
    valid = True
    # loop iterates over every character in the expression and checks its validity with its neighbors
    for i in range(len(expr)):
        char = expr[i]
        if (char=='('):
            numOfParentheses += 1
            if (i!=0):
                if (not Helper.isOp(expr[i-1]) and not expr[i-1]=='!'): 
                    valid = Helper.error("Missing operator <br>")
                    break
            if (i==end): 
                valid = Helper.error("Missing parenthesis <br>")
                break
            if (Helper.isOp(expr[i+1])):
                valid = Helper.error("Missing operand <br>")
                break
            prevIsVar = False
        elif (char==')'):
            numOfParentheses -= 1
            if (i==0): 
                valid = Helper.error("Missing parenthesis <br>")
                break
            if (Helper.isOp(expr[i-1])):
                valid = Helper.error("Missing operand <br>")
                break
            prevIsVar = False
        elif (Helper.isOp(char)):
            if (i==0 or i==end): 
                valid = Helper.error("Missing operand <br>")
                break
            if (Helper.isOp(expr[i-1]) or Helper.isOp(expr[i+1])): 
                valid = Helper.error("Missing operand <br>")
                break
            prevIsVar = False
        elif (char=='!'):
            if (i==end): 
                valid = Helper.error("Missing operand <br>")
                break
            if (Helper.isOp(expr[i+1]) or expr[i+1]==')'): 
                valid = Helper.error("Missing operand <br>")
                break
            if (not i==0):
                if (not Helper.isOp(expr[i-1]) and not expr[i-1]=='('): 
                    valid = Helper.error("Missing operand <br>")
                    break
            prevIsVar = False
        else:
            if (prevIsVar==True): 
                valid = Helper.error("Missing operator <br>")
                break
            if (char not in var): var.append(char)
            prevIsVar = True
    if (not numOfParentheses==0): valid = Helper.error("Missing parenthesis <br>")
    if (not valid): var = [None]
    return var          

def inToPost(expr):
    ''' 
    takes as input an infix expression and outputs a post fix expression
    '''
    result = []
    stack = LifoQueue(maxsize = len(expr))
    #loop iterates over every character in the expression
    for char in expr:
        # non variables are put on a stack where their precedence will determine the order of transfer onto the result queue
        if (Helper.isOp(char) or char=='!'):
            if (stack.empty() or Helper.peek(stack)=='('): stack.put(char)
            elif (Helper.precedence(Helper.peek(stack)) > Helper.precedence(char)): 
                result.append(stack.get())
                stack.put(char)
            elif (Helper.precedence(Helper.peek(stack)) == Helper.precedence(char)): result.append(char)
            else: stack.put(char)
        elif (char=='('): stack.put(char)
        # consecutively adding operators between operators on result
        elif (char==')'):
            while (not Helper.peek(stack)=='('): result.append(stack.get())
            stack.get()
        # Variables are directly put on result
        else: result.append(char)
    # remaining character on the stack are consecutively added to result
    while(not stack.empty()): 
        result.append(stack.get()) 
    return result

def evalExpr(row, postFix, var): 
    '''
    evaluates a post fix boolean expression
    '''
    stack = LifoQueue(len(postFix))
    for char in postFix:
       # operators removes the top two variables of the stack and output their result onto the stack
        if (Helper.isOp(char)):
            operand2 = stack.get()
            if (operand2 in var): operand2 = row[var.index(operand2)]
            operand1 = stack.get()
            if (operand1 in var): operand1 = row[var.index(operand1)]
            stack.put(Helper.evaluate(operand1, char, operand2))
        # ! removes the top of the stack and puts its boolean opposite on the stack
        elif (char=='!'): 
            operand = stack.get()
            if (operand in var): operand = row[var.index(operand)]
            stack.put(Helper.notGate(operand))
        # variables are directly added to the stack
        else: stack.put(char)
    return stack.get()

