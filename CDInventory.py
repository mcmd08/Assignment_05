#------------------------------------------#
# Title: CDInventory.py
# Desc: Add, Delete, Load and Display CD Inventory (Assignment 05)
# Change Log: (Who, When, What)
# Maria Dacutanan, 2020-Aug-09, Drafted pseudo code for the load data from file option
# Maria Dacutanan, 2020-Aug-09, Finalized code for loading data from file option
# Maria Dacutanan, 2020-Aug-10, Updated code for storing data into dictionary
# Maria Dacutanan, 2020-Aug-10, Updated code for displaying inventory - unpacking a dictionary
# Maria Dacutanan, 2020-Aug-10, Added code for deleting inventory
# Maria Dacutanan, 2020-Aug-10, Refined logic for deleting inventory so that duplicate ID values are also deleted
# Maria Dacutanan, 2020-Aug-11, Updated code for saving inventory into file
# Maria Dacutanan, 2020-Aug-12, Added check for file not existing
# Maria Dacutanan, 2020-Aug-12, Removed Debug Statements
# Maria Dacutanan, 2020-Aug-12, Updated comments
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dictRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program
        break
    if strChoice == 'l':
        # Loading existing data
        while True:
            objfile='Error'
            try:
                objfile=open(strFileName, 'r') #open CDInventory.txt and store in objfile
            except:
                print('Problem loading ' + strFileName + '.\n') #if unable to load file, return error msg and break out of loop
                break
            linectr=0
            for row in (objfile): #iterate thru each each line entry of objfile
                if row.strip(): #ignore blank lines
                    lstRow=row.strip().split(',') #remove leading and trailing spaces, and separate elements by comma
                    dictRow={'id':lstRow[0], 'song': lstRow[1], 'artist':lstRow[2]}
                    lstTbl.append(dictRow) #append dictionary entries to lstTbl
                    linectr+=1            #count number of lines loaded
            objfile.close()
            print (str(linectr) + ' line(s) loaded into memory.\n')
            break
    elif strChoice == 'a':
        # Add data to the inventory
        while True: #user is re-prompted for null ID
            strID = input('Enter an ID: ')
            if (strID):
                break
        while True: #user is re-prompted for null CD Title
            strTitle = input('Enter the CD\'s Title: ')
            if (strTitle):
                break
        while True: #user is re-prompted for null Artist's Name
            strArtist = input('Enter the Artist\'s Name: ')
            if (strArtist):
                break
        dictRow = {'id':strID, 'song':strTitle, 'artist':strArtist} #store new data into dictionary variable
        lstTbl.append(dictRow) #append to list lstTbl
        print ()
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        if (lstTbl):
            for row in lstTbl:
                print(*row.values(), sep = ',') #unpack list elements, separated by comma
        else:
            print('Inventory is empty.\n')
        print ()
    elif strChoice == 'd':
        # Delete an entry from Inventory
        while True:
            keyID=input('Please enter an ID number to delete: ')
            if (keyID): #checks for null ID
                lstID=[]
                delctr=0
                for cd in lstTbl:                   
                    for row in cd['id']:
                       lstID.append(row) #store all IDs from lstTbl to a variable
                
                if lstID.count(keyID) > 0: #check if ID provided by user exists in list of IDs
                    ctr=0
                    while ctr < len(lstTbl): #iterate thru lstTbl elements and match against user input
                        var=(lstTbl[ctr]['id']) #store ID from lstTbl
                        
                        if str(var)==keyID: #compare value in var against user input
                            del lstTbl[int(ctr)] #delete element from lstTbl if found
                            delctr+=1 #counts number of deleted elements from lstTbl
                            ctr+-1 #decrease counter since lstTbl has shifted after deletion
                        else:
                            ctr+=1
                else:
                    print ('Sorry, either inventory is empty or ID ' + str(keyID) +\
                           ' is not in the inventory.\n')
                    break
                print (str(delctr) + ' row(s) deleted.\n')
                break
            else:
                 continue
    elif strChoice == 's':
        # Save the data to CDInventory.txt
        counter=0
        if (lstTbl): #check for null list
            objFile = open(strFileName, 'a') #open file
            for row in lstTbl: #iterate thru lstTbl
                counter+=1
                strRow = ''
                for item in row.values(): #capture dictionary values
                    strRow += str(item) + ',' #store dictionary values to variable
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow) #write stored dictionary values
            objFile.close() # close file
        else:
            print('Inventory is empty.')
        print('Saved ' + str(counter) + ' new item(s) to the inventory.\n')
    else:
        print('Please choose either l, a, i, d, s or x!\n')

