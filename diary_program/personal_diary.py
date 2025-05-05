#Python program that opens a text file and appends user input diary entries into file without overwriting existing content
#Creates main function that will open and add user input entries to text file
def main():
    date_time = input("Enter today's date and current time: ") #takes user input for date and time
    entry = input("Enter your diary entry: ") #takes user input for data entry all to be added to text file
    #opens existing diary.txt file and 'a' opens the file in append mode
    try:
        with open("diary_program/diary.txt", 'a') as file: #establishes the folder and file path to open
            file.write(date_time  + '\n' + entry + "\n") #Adds a new line and takes user input of date, time, and diary entry with line breaks 
            file.close() #closes the file when complete with entries
    except FileNotFoundError:
        print("File not found!") #try except block to handle error if file is not found or spelled correctly
#Calls main function
main()