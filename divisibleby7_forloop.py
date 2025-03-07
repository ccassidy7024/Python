#Program that finds and prints all numbers divisible by 7 between 1-30
#range starts at 1 and ends at 300
for i in range(1, 300): 
    if i % 7 == 0:  # % 7 divides the number by 7 to see if it meets for loop requirements
        print(i)