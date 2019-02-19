# ----------------------------- #
# Title: TestSendLettersAllDonors.py
# Desc: Tests the SendLettersAllDonors Function  and Ensures Files are Written
# Change Log: (Who, When, What)
# KCreek, 2/18/2019, Script Created
# ----------------------------- #

# --- Data --- # 
import mailroom4
import os
import TestCreateReport
import datetime

# --- Processing --- #
# Write Text to File
def TestSendLettersAllDonors(lstDic):
    """
    Tests the SendLettersAllDonors funciton of mailroom4.py
    :parm lstDic: List containing Dictionary of information
    :Return Saves Text File to working folder, ensuring SendLettersAllDonors
    saved files to system. 
    """
    # 'for' loop passes through each Dictionary and saves a letter to Working Folder
    for dictionary in lstDic:
        mailroom4.SendLettersAllDonors(dictionary)
    
    # 'for' Loop for each dictionary within the list
    for dictionary in lstDic:
        # Writes a Time Stamp for when data is passed to file
        strTimeStamp = "\nTest Time Stamp: " + str(datetime.datetime.now().strftime('%m-%d-%Y, %H:%M:%S')) + "\n"
        TestCreateReport.FileWriter(strFileName,strTimeStamp)
        
        # 'for' loop tests each name in the list
        for name in dictionary.keys():
            name = mailroom4.FileNameFormatter(name)
            # Checks to ensure the SendLettersAllDonors wrote the file to the disk
            # Result is written to the file in formatted text 
            if os.path.exists(name) == True:
                strTextOutPut = "Test Name: {}, Test Results: {}".format(name,'Pass') + "\n"
                TestCreateReport.FileWriter(strFileName=strFileName, strText=strTextOutPut)
            else:
                strTextOutPut = "Test Name: {}, Test Results: {}".format(name,'Fail') + "\n"
                TestCreateReport.FileWriter(strFileName=strFileName, strText= strTextOutPut)

# --- Presentation --- #

# File Name for writing file Results. 
strFileName = "TestSendLettersAllDonorsResults.txt"
# Create an an output file to which Results can be written.
objFile = open(strFileName, 'w')
# Obtain a List of Names from a Test File
# Note: Each Line is imported as string in a list w/ len = 1
# Each name in line is separated by Comma
lstNames = TestCreateReport.FileReader("TestSendLetters.txt")
# Create new list to separate each line in string of text by ","
lstNamesNew = TestCreateReport.ListMaker(lstNames)
# Create a list of dicitonaries by assigning random donations to each name
# in the new list of names. 
lstDic = TestCreateReport.DictionaryMaker(lstNamesNew)
TestSendLettersAllDonors(lstDic)



