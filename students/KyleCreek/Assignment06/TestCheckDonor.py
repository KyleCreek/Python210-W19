# ----------------------------- #
# Title: TestCheckDonor
# Desc: Tests the CheckDonor function of mailroom4.py
# Change Log: (Who, When, What)
# KCreek, 2/16/2019, Created Script
# ----------------------------- #


#-- Data --#
# Declare Variables and Constants

# File Location
filename = "TestCheckDonor.txt"

# Empty list to store Test Results
lstResults = []

# Output file write location
strFileOut = "CheckDonorResults.txt"


#-- Processing --#
# Perform Tasks

def TestCheckDonor(strDonor, dicDonorDB, intExpectedDiff):
    """
    Tests the Check Donor Function  of Mailroom4 to Ensure new names append
    Dictionary and exiting names do not increase length
    :param strDonor: String of Text for Donor Name
    :param dicDonorDB: Dictionary containing Donor Indormation
    :param intExpectedDiff: Expected Difference in dictionary after being passed through
    function
    :return: Writes Test results to system
    """
    # Counts the number of Names in dictionary prior to passing function
    counter1 = 0

    # Counts the number of Names in Dictionary after processing through Function
    counter2 = 0

    # 'for' loop to count number of names in Original Dictionary
    for key in dicDonorDB.keys():
        counter1 += 1
    tplReturn = CheckDonor(strDonor,dicDonorDB)
    strNew, dicNew = tplReturn

    # 'for' loop to count the number of names in dictionary after passing
    for key in dicNew.keys():
        counter2 += 1
    counterdiff = counter2 - counter1

    # Pass/Fail Statement pending the difference in names and expected difference
    if counterdiff == intExpectedDiff:
        return "Pass"
    else:
        return "Fail"

# Presentation (Input/Output) --#
# Interact w/ the User



from mailroom4 import CheckDonor
import DataProcessor
import datetime
# Create initial file to write text
objFile = open(strFileOut, 'w')

# Import list of Text From File
lstTestText = DataProcessor.FileProcessor.filereader(filename)

# Create TimeStamp for Test 
time = "Time of Test: " + datetime.datetime.now().strftime('%m-%d-%Y, %H:%M:%S')
strHeader = '{:^30}{:^30}'.format("Test Input", "Test Result")
lstResults.append(time)
lstResults.append(strHeader)

# Process the text in the notepad through the function
for item in lstTestText:
    dicDonorDB = {"William Gates, III": [653772.32, 12.17],
                  "Jeff Bezos": [877.33],
                  "Paul Allen": [663.23, 43.87, 1.32],
                  "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]}
    lstSplit = item.split(",")
    # Creates a string of text after processing through CheckDonor Function
    strTestResult = TestCheckDonor(lstSplit[0],dicDonorDB,int(lstSplit[1]))
    strTestOutput = "{:^30}{:^30}".format(lstSplit[0],strTestResult)

    # Appends list for string of text
    lstResults.append(strTestOutput)




# Write Each Line of Test Results to File Path Location
for line in lstResults:
    objFile.write(line +"\n")
    
objFile.close()



