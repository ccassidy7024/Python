#Python program that opens downloaded file and makes adjustments and saves file

#Creates main function that reads downloaded text file and makes adjustments
def main():
    try:
        with open('processing_files/sales_totals.txt', 'r') as file: #opens downloaded file in read mode
            lines = file.readlines() #reads through all lines of the file
            total = 0 #sets the initial total to 0
            count = 0 #sets the initial count of lines to 0
        for lines in file:
                file.write(lines) #allows new lines to be written to file
                lines = lines.strip() #strips the \n from the established line
                number = float(lines) #converts numbers to float
                print(number)
                total += number #adds each float number to total
                count += 1 #increased the line count number by 1
                average = total / count #calculates the average 
        #prints total, count, and average
        print("Total: ", total)
        print("Count: ", count)
        print("Average: ", average)
        file.close() #saves and closes file
    #except blocks handle different possible errors
    except IOError:
        print("An IOError has occurred")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)
#calls main function
main()

