# repeats from 1 to 100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:

#if the multiple was 3 and 5 
        print("FizzBuzz")  
    elif num % 3 == 0:
        
        #if only it were a multiple of 3
        print("Fizz")  
    elif num % 5 == 0:

        #if only it were a multiple of 3
        print("Buzz") 

        #otherwise , print the number ourselves
    else:
        print(num) 
