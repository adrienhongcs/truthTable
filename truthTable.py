'''
Created on Jun 8, 2020

@author: adrienhong
'''
import Helper

class TruthTable(object):
    '''
    Instance of TruthTable has rows, columns, and a table containing the values of the truthTable
    The last column represents the output of a given boolean expression, the others represent the boolean value of a variable
    '''
    def __init__(self, numOfVar):
        '''
        Constructor
        '''
        self.__rows = 2**numOfVar
        self.__cols = numOfVar+1 
        self.table = self.createTable()
        self.setTable(numOfVar)
        
    def createTable(self):
        '''
        returns a 2D list representing a table
        '''
        table = []
        for i in range(self.__rows):
            row = [None]*self.__cols
            table.append(row)
        return table 
    
    def setTable(self,numOfVar):
        '''
        sets the values of all the columns representing the value of a variable
        '''
        modulo = 2**(numOfVar-1)
        # loops iterates over every columns
        for i in range(self.__cols-1):
            value = 0
            for j in range(self.__rows):
                self.table[j][i]=value
                if ((j+1)%(modulo)==0):     # determines the interval at which a column alternates values of a variable
                    value = Helper.notGate(value)
            # the next column will alternate values at twice the rate 
            modulo /= 2     
            
    def getRows(self):
        return self.__rows
    
    def display(self,var):
        print("<table>")
        print("<tr>")
        for x in var:
            print("<th>"+str(x)+"</th>")
        print("<th>Result</th>")    
        print("</tr>")
        for i in range(self.__rows):
            print("<tr>")
            for j in range(self.__cols):
                print("<th>"+str(self.table[i][j])+"</th>")
            print("</tr>")
        print("</table>")
