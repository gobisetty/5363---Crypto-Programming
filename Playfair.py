###############################################
# Name: Sai Rahul Gobisetty
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################

import pprint
import re
def generateAlphabet():
    #Create empty alphabet string
    alphabet = ""
    
    #Generate the alphabet
    for i in range(0,26):
        alphabet = alphabet + chr(i+65)
        
    return alphabet

def cleanString(s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
    """
    Cleans message by doing the following:
    - up            - uppercase letters
    - spLetters     - split double letters with some char
    - reSpaces      - replace spaces with some char or '' for removing spaces
    - reNonAlphaNum - remove non alpha numeric
    - reDupes       - remove duplicate letters

    @param   string -- the message
    @returns string -- cleaned message
    """
    if 'up' in options:
        s = s.upper()
        
    if 'spLetters' in options:
        #replace 2 occurrences of same letter with letter and 'X'
        s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
        
    if 'reSpaces' in options:
        space = options['reSpaces']
        s = re.sub(r'[\s]', space, s)
    
    if 'reNonAlphaNum' in options:
        s = re.sub(r'[^\w]', '', s)
        
    if 'reDupes' in options:
        s= ''.join(sorted(set(s), key=s.index))
    
     #removing numbers
    s=re.sub('[0-9]+', '',s)
    return s

def generateSquare(key):
    """
    Generates a play fair square with a given keyword.

    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #uppercase key (it may be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})
    
    print(key)
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair
    
def transpose(playFair):
    """
    Turns columns into rows of a cipher square

    @param   list2D -- playFair square
    @returns list2D -- square thats transposed
    """
    #Create empty 5x5 matrix 
    trans = [[0 for i in range(5)] for i in range(5)]
    
    for col in range(5):
        for row in range(5):
           trans[col][row] = playFair[row][col] 
           
    return trans

def getCodedDigraph(graph,square,a):
    """
    Turns a given digraph into its encoded digraph 

    @param   list -- graph
    @returns list -- encoded digraph
    """
    #creating arrays
    digraph = [[0 for i in range(2)] for i in range(len(graph)//2)]
    newDigraph = [0 for i in range(len(graph))]
    
    row = 0     #row index for sqaure
    col = 0     #col index for square
    #assigning the array
    for i in range(len(graph)):
        digraph[row][col] = graph[i]
        col = col + 1
        if col >= 2:
            col = 0
            row = row + 1
    
    
    r=0
    for rows in range(len(graph)//2):   
        ifnot=0    
        # Checking out if the codes are present in the same row
        for row in square:
            if digraph[rows][0] in row and digraph[rows][1] in row:
                # % 5 if the value exceeds more than 5
                newDigraph[r] = row[((row.index(digraph[rows][0])+a)%5)]
                newDigraph[r+1] = row[((row.index(digraph[rows][1])+a)%5)]
                ifnot=1
               
        transSquare=transpose(square)
        # Checking out if the codes are present in the same col
        for col in transSquare:
            if digraph[rows][0] in col and digraph[rows][1] in col:
                # % 5 if the value exceeds more than 5
                newDigraph[r] = col[((col.index(digraph[rows][0])+a)%5)]
                newDigraph[r+1] = col[((col.index(digraph[rows][1])+a)%5)]
                ifnot=1
        #If codes are present in different rows and columns    
        if ifnot==0:     
            for cols in range(2):
                for row in range(5):
                    for col in range(5):
                        if cols==0:
                            if square[row][col] == digraph[rows][0]:
                                i1 = row
                                j1 = col
                        elif cols==1:
                            if square[row][col] == digraph[rows][1]:
                                i2 = row
                                j2 = col
                if cols==1:
                    newDigraph[r]=square[i1][j2]
                    newDigraph[r+1]=square[i2][j1]
        r=r+2
     
    return newDigraph
    

###########################################################################

while True:
    # providing the options
    
    print("Playfair Tool (P.T)")
    print("Written By: Sai Rahul Gobisetty ")
    print("*************************************")
    print("1. Encipher")
    print("2. Decipher")
    print("3. Quit")
    Choice=input("Enter the choice: ")
    print("*************************************")
    print()
    #for encryption the message
    if(Choice == '1'):
        
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: Sai Rahul Gobisetty ")
        print("*************************************")
        message=input("Please enter a message:  ")
        print("*************************************")
        print()
        
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: Sai Rahul Gobisetty ")
        print("*************************************")
        key=input("Please enter a keyword: ")
        print("*************************************")
        print()
        #creating square using key 
        playFair = generateSquare(key)
        print()
        for list in playFair:
            print(list)
        print()
        #transpose the square
        transPlayFair = transpose(playFair) 
        print()
        for list in transPlayFair:
            print(list)
           
        message=cleanString(message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':'X'})
        
        if (len(message)%2) !=0:
            message= message+"X"
        
        print()
       
        message=getCodedDigraph((message),transPlayFair,1)
        message = ''.join(message)
        
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: Sai Rahul Gobisetty ")
        print("*************************************")
        print("Your encrypted message is:")
        print(message)
        print("*************************************") 
        print()
    #for decryption
    elif(Choice == '2'):
        
        print("Playfair Decryption Tool (P.D.T)")
        print("Written By: Sai Rahul Gobisetty ")
        print("*************************************")
        message=input("Your decrypted message is:  ")
        print("*************************************")
        print()
        
        print("Playfair Decryption Tool (P.D.T)")
        print("Written By: Sai Rahul Gobisetty ")
        print("*************************************")
        key=input("Please enter a keyword: ")
        print("*************************************")
        print()
        #creating square using key
        playFair = generateSquare(key)
        print()
        #printing the square
        for list in playFair:
            print(list)
        print()
        #transpose the square
        transPlayFair = transpose(playFair) 
        print()
        #printing the transpose square
        for list in transPlayFair:
            print(list)
        
        print()
        #Decrypting the message
        message=getCodedDigraph((message),transPlayFair,4)
        message = ''.join(message)
        
        print("Playfair Decryption Tool (P.D.T)")
        print("Written By: Sai Rahul Gobisetty ")
        print("*************************************")
        print("Your decrypted message is:")
        print(message)
        print("*************************************") 
        
    else:
        # breaking the loop if the value it is error
        break
    