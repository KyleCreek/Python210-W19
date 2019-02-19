# ----------------------------- #
# Title: AddDonationTest
# Desc: Tests the AddDonation Function of Mailroom4.py
# Change Log: (Who, When, What)
# KCreek, 2/16/2019, Created Script
# ----------------------------- #


#-- Data --#
# Declare Variables and Constants
# Database list containing Tuples of donators and their associated donations.
dicDonorDB = {"William Gates, III": [653772.32, 12.17],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]}


#-- Processing --#
# Perform Tasks

# Presentation (Input/Output) --#
# Interact w/ the User

from mailroom4 import AddDonation

count1 = 0
count2 = 0

for key,value in dicDonorDB.items():
    count1 += len(value)

print(count1)

funAddDonation = AddDonation

funAddDonation("KYLE CREEK", dicDonorDB)

for key,value in dicDonorDB.items():
    count2 += len(value)

print(count2)


