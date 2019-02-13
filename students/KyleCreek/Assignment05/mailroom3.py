# ----------------------------- #
# Title: mailroom3.py
# Desc: Program Written to Complete Assignments of Python210
# Change Log: (Who, When, What)
# KCreek, 2/5/2019, Revised docstrings and simplified parts of code.
#                   "#***" Signifies location of Revision
# KCreek, 2/6/2019, Checked each function for consistent Varable naming
#                   "#***" Signifies Location of Revision
# ----------------------------- #


# -- Data --#
# Declare Variables and Constants

# Database list containing Tuples of donators and their associated donations.
dicDonorDB = {"William Gates, III": [653772.32, 12.17],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]}


# -- Processing --#
# Perform Tasks

# --- Main --- #
def main():
    """
    Main Program Loop
    :return:
    """
    if __name__ == '__main__':
        flag = True
    else:
        flag = False

    dicSwitchCase = {1: SendThankYouSingle,
                     2: CreateReport,
                     3: SendLettersAllDonors}
    while flag:

        # Obtain User's Choice
        intUserChoice = MenuDisplay()

        # Use Switch Statement to Call Function
        if intUserChoice <= 3:
            dicSwitchCase.get(intUserChoice)(dicDonorDB)

        # Case Statement to Exit the Program
        else:
            break


def MenuDisplay():
    # *** Revised existing Docstring Information
    """
    Return a list of Mailroom Options to the user to direct input choices.
    :return: User Choice of available options
    """
    print("""
    Please Choose from the Available Options:
    1: Send a Thank You to a Single Donor
    2: Create a Report
    3: Send Letters to ALL Donors
    4: Quit""")

    # 'While' loop queries user until the program is provided with an acceptable input.
    while True:
        try:
            intMenuChoice = int(input("\nChoose Option Here: "))
            if intMenuChoice < 1 or intMenuChoice > 4:
                # *** Corrected spelling error
                # print("That is our of Range, Please Try Again")
                print("That is out of Range, Please Try Again")
            else:
                return intMenuChoice

        except ValueError:
            print("That is not an acceptable input")


def DonorNameInput():
    # *** Added Information to Function DocString
    """
    Returns a properly formatted name of a user provided input
    :return Donors name stripped of whitespace in "Title" format.
    """
    # Note, 'try-except' Block was not used here to ensure string as 'input' will always return a string
    strDonorName = input('''Please Provide Donor Full Name, or 'list' to display all donors: ''').strip()
    #strDonorName = strDonorName.strip()
    #strDonorName = strDonorName.title()
    # *** Removed line to return title form.
    return strDonorName.title()


# --- Case Statement 1 --- #

def StringFormatter(strText):
    # *** Added Information to Function DocString
    """
    Returns a properly formatted string to meet processing requirements
    :param strText: Input string that will subsequently be processed.
    :return Text string w/ removed punctuation, stripped of L/R white space, and in lowercase
    """
    import string

    # Strip Punctuation

    # *** Replaced variable 'c' with "Character" to better name variable
    #for c in string.punctuation:
    #    strText = strText.replace(c, "").strip()

    for Character in string.punctuation:
        strText = strText.replace(Character, "").strip()

    # Strip White Space
    #strText = strText.strip()
    # Make Name a title
    #strText = strText.lower()
    # *** Reduced stripping to one line and returned text with lower formatting
    return strText.lower()


def DonorListView(dicDonorDB):
    # *** Revised information in Function DocString
    """
    Prints keys of provided dictionary to screen.
    :param dicDonorDB: Dictionary to be printed to screen
    :return Prints keys in provided dictionary
    """
    # 'for' loop printing each of the items in the provided list
    for key, value in dicDonorDB.items():
        print(key)


def CheckDonor(strDonorName, dicDonorDB):
    # *** Revised information in existing DocString
    """
    Checks for Donor's existence in database and returns donors name and revised DataBase
    :param strDonorName: String consisting of Donor's Name
    :param dicDonorDB: Dictionary containing DataBase of Donors Information
    :return: String of DonorName in title format and revised Dictionary
    """
    import string

    # *** Simplified function to reduce lines of code
    #strDonorNameCheck = StringFormatter(strDonorName)

    # ---  Extract Donor Names from Database --- #
    # 'for' loop to evaluate the keys of the dictionary
    for strName in dicDonorDB.keys():
        # Format the name to remove punctuation and make all lower case

        # *** Simplified Function to Reduce Lines of Code
        #strDBNameCheck = StringFormatter(strName)
        #if strDBNameCheck == strDonorNameCheck:

        if StringFormatter(strName) == StringFormatter(strDonorName):
            print("This name is in the DataBase")
            # Note, This will return the Key to the dictionary

            return strName, dicDonorDB

    # *** Note Attempted to simplify function to only return (1) value, but needed revised
    # *** revised dictionary in the instance donor is not currently in DataBase
    # *** Note: Can likely use 'Global" statement, but this breaks encapsulation.
    else:
        print("This is not in the database")
        # Note, This wil return the new Key Entry
        dicDonorDB[strDonorName.title()] = []

        return strDonorName.title(), dicDonorDB


def AddDonation(strDonorName, dicDonorDB):
    # *** Revised information in existing DocString
    """
    Returns a revised dictionary to include new donations from Donor
    :param strDonorName: String of Donor Name who has recently donated
    :param dicDonorDB: Dictionary containing all donor information
    :return: Dictionary of updated donor DataBase
    """
    # 'while' loop continuously queries users for information until an acceptable response
    # has been obtained
    while True:
        try:
            fltDonationAmount = float(input("Provide amount Donated: "))
            break
        except ValueError:
            print("That is not an acceptable input, please try again")

    dicDonorDB[strDonorName] += [fltDonationAmount]

    return dicDonorDB


def SendThankYouSingle(dicDonorDB):
    # *** Updated information in existing DocString
    """
    Obtains Donor Name from user and updates Donor DataBase Accordingly
    :param dicDonorDB: Dictionary containing all donor information
    :return: Prints thank you message to screen
    """
    import string

    while True:

        strDonorName = DonorNameInput()

        if strDonorName == 'List':
            # Lists the Donors in the Donor Database to the Screen
            DonorListView(dicDonorDB)
        else:
            # Determine if donor is in database, otherwise create
            # New Donor and update database
            strDonorName, dicDonorDB = CheckDonor(strDonorName, dicDonorDB)


            # Adds the Donors contribution to their history
            dicDonorDB = AddDonation(strDonorName, dicDonorDB)

            # Prints a Thank you note to the Donor for their contribution
            # PrintThankYou(tplDonor,fltDonationAmount)
            PrintThankYou(strDonorName, dicDonorDB)

            break


def PrintThankYou(strDonorName, dicDonorDB):
    # *** Updated information in existing DocString
    """
    Prints a thank you letter to a donor for their most recent donation to the screen
    :param strDonorName is a string consisting of the Donor's Name
    :param dicDonorDB: Dictionary containing all donor information
    :return: Prints thank you letter to the screen for most recent donation
    """

    lstDonations = dicDonorDB[strDonorName]

    # *** Moved this step to Format statement
    #strRecentDonation = lstDonations[-1]

    strThankYouText = 'Dear {},\nThank you for your kind donation of ${}. ' \
                      'With help of your donation a poor Engineer at Boeing ' \
                      'will be able to pass Python 210 and continue' \
                      'to persue their dream of becoming dirty rich.' \
                      'Thank you!'.format(strDonorName, lstDonations[-1])

    print(strThankYouText)


# --- Case Statement 2 --- #

# *** Eliminated Need for Float Formatter Function
#def FloatFormatter(fltInput):
    #*** Revised existing DocString Information and Variable Name
    # *** Ultimately Eliminated Function
#    """
#    Returns floating point number as string formatted to 2 decimals.
#    :param intFloat: floating point integer
#    :return: String of Floating Point to two decimals
#    """
#    return '{0:.2f}'.format(fltInput)


def ReportInformation(strDonorName, dicDonorDB):
    # *** Updated information in Existing DocString
    """
    Returns multiple strings of the Donation history of a given donor

    :param dicDonorDB: Dictionary containing all donor information
    :param strDonorName: Donor Name to associate to key in dicDonorDB
    :return Gift Total Amount, Number of Gifts, and Average Gift Cost in two decimal strings"""

    fltGiftTotal = 0
    lstDonations = dicDonorDB.get(strDonorName)

    # Calculate gift total by summing list
    for donation in lstDonations:
        fltGiftTotal += donation

    # *** Removed Statement and added to return
    #strGiftTotal = FloatFormatter(fltGiftTotal)

    # Calculate the number of donations given
    # *** Note: Tried to condense strNumGift to one Operation but need integer
    # *** to determine the average gift amount
    fltNumGift = len(lstDonations)
    strNumGift = str(fltNumGift)

    # Calculate the average cost per donation
    try:
        fltAverageGift = fltGiftTotal / fltNumGift
    except ZeroDivisionError:
        fltAverageGift = 0

    # *** Removed Statement and Addded to Return
    #strAverageGift = FloatFormatter(fltAverageGift)

    return '{0:.2f}'.format(fltGiftTotal), strNumGift, '{0:.2f}'.format(fltAverageGift)


def CreateReport(dicDonorDB):
    # *** Revised information in existing DocString
    """
    Prints donor information from provided Dictionary to the screen
    :param dicDonorDB: Dictionary containing all donor information
    :return: Prints report of donor and donor statistics to the screen
    """
    intColumnWidth = 0
    # Determine the Maximum Column Width
    for person in dicDonorDB.keys():
        if len(person) > intColumnWidth:
            intColumnWidth = len(person)

    # Create a Table Header
    strHeaderName = '{name:<{width}}'.format(name='Donor Name', width=intColumnWidth + 5)
    strHeaderAmtGiven = '{name:>{width}}'.format(name='Total Given', width=15)
    strHeaderNumGift = '{name:>{width}}'.format(name='Num Gifts', width=15)
    strHeaderAvgGift = '{name:>{width}}'.format(name='AVG Gift', width=12)
    strHeader = strHeaderName + strHeaderAmtGiven + strHeaderNumGift + strHeaderAvgGift
    print(strHeader)
    print('-' * (len(strHeader) + 5))

    # Create a 'for' loop to write information in dictionary into text format
    for person in dicDonorDB.keys():
        strGiftTotal, strNumGift, strAverageGift = ReportInformation(person, dicDonorDB)
        strNameText = '{name:<{width}}'.format(name=person, width=intColumnWidth + 5)
        strTotalGiven = '${total:>{width}}'.format(total=strGiftTotal, width=15)
        strNumGift = '{num:^{width}}'.format(num=strNumGift, width=15)
        strAvgGift = '${avg:>{width}}'.format(avg=strAverageGift, width=12)

        strOutPut = strNameText + strTotalGiven + strNumGift + strAvgGift
        print(strOutPut)


# --- Case Statement 3 --- #

def FileNameFormatter(strText):
    # *** Revised existing DocString Information
    """
    Returns a string of text in a filename format
    :param strText: String of text to be formatted
    :return: Input text with all special characters stripped + '.txt'
    """
    import string

    # *** There might be ability to comprehend list here
    # Strip text of punctuation
    for c in string.punctuation:
        strText = strText.replace(c, "")
    # Strip WhiteSpaces from FileName
    if " " in strText:
        strText = strText.replace(" ", "_") + ".txt"
    return strText


def SendLettersAllDonors(dicDonorDB):
    # *** Revised existing DocString Information
    """
    Writes and Saves file thanking Donors for their contributions
    :param dicDonorDB: Dictionary containing all Donors Information
    :return: Saves Thank you letters to all donors in database to file.
    """
    for person, donations in dicDonorDB.items():
        # Create File Name
        strFileName = FileNameFormatter(person)
        strFileText = LetterTemplate(person, donations)

        # Write Letter to text file
        with open(strFileName, 'w') as f:
            f.write(strFileText)
            f.close()


def FormatAlign(strAlignment, strText, intWidth=100):
    # *** Revised existing DocString Information
    """
    Returns text formatted to a desired alignment
    :param strAlignment: String alignment option
    :param strText:  String of text to be formatted
    :param intWidth = 100: An optional parameter that sets the # of characters in the line of text
    :return String of text formatted to match desired alignment
    """
    return '{strText:{strAlignment}{intWidth}}'.format(strText=strText, strAlignment=strAlignment, intWidth=intWidth)


def LetterTemplate(strDonorName, lstDonations):
    """
    Function written to creat template letter to donors
    :param dicDonorDB is a database containing donors and their donation amounts
    :return a string of text displaying gratification.
    """
    strNumGift = ''
    strGiftAverage = ''
    # Text for greeting
    strGreeting = "Dear {},\n".format(strDonorName)
    strGreeting = FormatAlign('<', strGreeting)

    # Text for most Recent donation
    strBodyText1 = "Thank you for your very generous Donoation of {intDonation:.2f}".format(
        intDonation=lstDonations[-1])
    strBodyText1 = FormatAlign("^", strBodyText1)

    # Calculate Donation Information
    # *** Removed Float Formatter Function
    #strNumGift = FloatFormatter(len(lstDonations))
    strNumGift = '{0:.2f}'.format(len(lstDonations))
    intGiftTotal = 0
    for donation in lstDonations:
        intGiftTotal += donation
    # *** Removed Float Formatter Function
    # strGiftTotal = FloatFormatter(intGiftTotal)
    # strGiftAverage = FloatFormatter((intGiftTotal / len(lstDonations)))
    strGiftTotal = '{0:.2f}'.format(intGiftTotal)
    strGiftAverage = '{0:.2f}'.format((intGiftTotal / len(lstDonations)))

    # Build Transition Text
    strBodyText2 = "Since we're on the topic of giving, lets talk about your entire history donating with us!"
    strBodyText2 = FormatAlign('^', strBodyText2)

    # Stats
    strBodyText3 = "You have donated {} number of gifts for a total of ${} and average of ${}".format(strNumGift,
                                                                                                      strGiftTotal,
                                                                                                      strGiftAverage)
    strBodyText3 = FormatAlign("^", strBodyText3)

    # Talk about Giving Habits
    if intGiftTotal < 100 and len(lstDonations) < 2:
        strBodyText4 = "Those are pretty pathetic donations, you CAN and SHOULD do better"
        strBodyText4 = FormatAlign("^", strBodyText4)
    elif intGiftTotal > 100000 and len(lstDonations) > 2:
        strBodyText4 = "Wow, you are so generous! You've donated more than most make in a year!"
        strBodyText4 = FormatAlign("^", strBodyText4)
    elif intGiftTotal > 50000 and len(lstDonations) < 2:
        strBodyText4 = "Be honest, you're rich and need a tax write off, don't mask this as charity"
        strBodytext4 = FormatAlign("^", strBodyText4)
    else:
        strBodyText4 = "We are proud of your average work and appreciate all that you can give."
        strBodyText4 = FormatAlign("^", strBodyText4)

    # Closing
    strClosing1 = "Sincerely"
    strClosing1 = "\n" + FormatAlign(">", strClosing1, 75)

    strClosing2 = "-The Team"
    strClosing2 = "\n" + FormatAlign(">", strClosing2, 80)

    # Join text and maintain formatting
    lstOutPut = [strGreeting, strBodyText1, strBodyText2, strBodyText3, strBodyText4, strClosing1, strClosing2]

    # *** Revised Variable Names to be more descriptive

    strTextOutput = "\n"
    strTextOutput = strTextOutput.join(lstOutPut)
    return strTextOutput


# Presentation (Input/Output) --#
# Interact w/ the User
main()