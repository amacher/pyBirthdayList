import csv
import os

# This is very heavy commented, it's used to help show a simple program and the whys behind the code.

# The path to the CSV file
csvFile='<path to csv file>'
# User input for beginning and end dates
startDate = input("Start Date: ") 
endDate = input("End Date: ") 

# testing dates
# startDate = "0125" 
# endDate = "0202"

# Setting a value to endList, this will be used going through list to find when start of new day
endList = '0'

# Add dates to a list and if not there have it create the starting date
dates = []

# list of the months, the spacer to fill so Jan will start in the 1 location
months = ['spacer', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# Break the date appart have the first 2 check and conver to month spelled out then the date, remove begin '0'
def dateFormat(date):
    #pulls the first 2 digits from the date pasted
    month = int(date[:2])
    # prints to terminal on a new line, the month pulled from the list a space and then the day removing any leading zeros.
    print('\n' + months[month] + ' ' + date[-2:].lstrip('0'))

def checkDate(line):
    #looks at the dates list to see if that date is already present, if not add to the ist
    if data[0] not in dates:
        date = data[0]
        # calls the dateFormat to get and print the month and day to start that days list
        dateFormat(date)
        dates.append(data[0])
    # Prints the persons name
    print(data[1])

# Do To: Need way to loop back through for end of year
f = open( csvFile, "r" )
read = f.readlines()
#going through file line by line (row by row)
for line in read:
    # since this is a CSV file this is breaking the line down to each col and putting it into a list
    data = line.split(',')
    #looking for the first date to start pulling names
    if startDate in line:
        checkDate(line)
        # assigns endList to 'PRINT' meaning to continue on with printing the names
        endList = 'PRINT'
    #This will check if we have the last date for the list, but still get the people who all have that birthday
    # will continue to pull since endDate will be in those last ones.
    elif endDate in line:
        checkDate(line)
        # This is to stop the last elif from running and when its past the endDate will continue through the list 
        endList = 'END'
    # will continue to pull
    elif endList =='PRINT':
        checkDate(line)
    # To break out of a huge list
    elif endList == 'END':
        break
# This is to show the file  is done running
print('###')