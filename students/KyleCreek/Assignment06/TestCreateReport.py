# ----------------------------- #
# Title: TestCreateReport.py
# Desc: Tests the Functionality of the Create Report Function of Mailroom4
# Change Log: (Who, When, What)
# KCreek, 2/17/2019, Created Script
# ----------------------------- #

#-- Data --#
# Declare Variables and Constants
from mailroom4 import CreateReport
from mailroom4 import ReportInformation
import random
import datetime
#-- Processing --#
# Perform Tasks
# Grab line from text

def FileReader(strFileName):
    """
    Function creates a list of each line of information from provided file path
    :param strFileName: FilePath Contataining information
    :return: List of lists for each line in file path
    """
    # Empty List to store each line of names
    lstNames = []
    fileObj = open(strFileName,"r")

    # For Loop for each line in the file object
    for line in fileObj.readlines():
        line = line.strip()
        line = line.split("\n")
        lstNames.append(line)
    return lstNames

def ListMaker(lstNames):
    """
    Splits text in list to create list of names
    :param lstNames: List containing strings of texts
    :return: Returns list of comma separated names in list
    """
    lstNew = []
    for stringtext in lstNames:
        for text in stringtext:
            lst = text.split(",")
            lstNew.append(lst)

    return lstNew

def CreateDonations():
    """
    Function to generate random donations
    :return: List of simulated donations for users
    """
    # Create a random number of donations per Donor
    intNumDonation = random.randrange(2,10)


    intCount = 0
    lstDonation = []

    # 'while' loop to list of random donation amounts
    while intCount < intNumDonation:
        intRandInt = random.randint(1,100000)
        lstDonation.append(intRandInt)
        intCount += 1

    return lstDonation

def DictionaryMaker(lstNames):
    """
    Function to create a dictionary of donor names and donations
    :param lstNames: List of names
    :return: List containing dictionaries of donor names and donations.
    """
    # Empty Dictionary
    lstDic = []
    # 'for' loop to take each list and create a dictionary with random donations
    for list in lstNames:
        # Empty dictionary to store names in list
        dicNew = {}
        # Assigns  donations to each name within the list
        for name in list:
            dicNew[name.strip()] = CreateDonations()
        lstDic.append(dicNew)

    return lstDic

def FileWriter(strFileName,strText):
    """
    Writes string of text to File
    :param strFileName: String of Text for file path
    :param strText: Text to append to Written File
    :return: Saves text to file.
    """
    objFile = open(strFileName,'a')
    objFile.write(strText)
    objFile.close()

def TestCreateReport(lstDicInput, strFileName):
    """
    Tests the CreateReport function of Mailroom4.py
    :param lstDicInput: Dictionary of donor names and associated donations
    :param strFileName: String of file name output
    :return: Writes test results to system
    """
    for Dictionary in lstDicInput:
        # Create a time stamp for when this was written
        strTimeStamp = "\nTest Time Stamp: " + str(datetime.datetime.now().strftime('%m-%d-%Y, %H:%M:%S')) + "\n"
        # Writes timestamp to string
        FileWriter(strFileName, strTimeStamp)
        # Creates report for the dictionary
        lstReport = CreateReport(Dictionary)
        # Writes each line in dictionary to file
        for line in lstReport:
            FileWriter(strFileName,line + "\n")


# Presentation (Input/Output) --#
# Interact w/ the User

# Create a list of names from file
lstNames = FileReader("TestCreateReport.txt")
# Change list to make it more workable
lstNamesNew = ListMaker(lstNames)
# Create a file to write to
strFileName = "CreateReportResults.txt"
objFile = open(strFileName,'w')

# Create a list of Dictionaries
lstDic = DictionaryMaker(lstNamesNew)
# Test Dictionaries
TestCreateReport(lstDic,strFileName)
objFile.close()

