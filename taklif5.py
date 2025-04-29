# this program checks if a number is a palindrome
number = input("enter a number: ")

# create an empty string to store the reversed number
reversed_number = ""

#loop through each charecter of the orginal number from last to first
for i in range(len(number)-1, -1, -1):
    reversed_number += number[i]

#compare the orginal number with the reversed one 
if number == reversed_number:
    print("this is a palindrome !")
else:
    print("this  not palindrome !")    