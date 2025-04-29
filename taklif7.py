#empty list for save couple numbers
even_numbers = [] 

#of 1 up to 100 checking
for num in range(1,101): 
    
    #if number is couple
    if num % 2 == 0:

        #add number to list
        even_numbers.append(num)

#print courple number 
print(even_numbers)

    