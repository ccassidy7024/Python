#Python program that takes user input of 10 book titles and uses string methods to sort and format the list

#Creates main function to run while loop and create list to store entered book titles.
def main():
    book_titles = [] #creates list to store book titles in
    print("Please enter a total of 10 book titles..")
    titles = 0 #sets the amount of titles entered to 0 before incrementing each time a title is entered
    while titles < 10: #while loop prompts the user to continue adding book titles until the amount of entries reaches 10
        user_input = input("\nPlease enter a book title: ").title() #this string method formats titles to correct capitalization for proper titles
        book_titles.append(user_input) #append function adds the entry to the book_titles list 
        titles += 1 #this adds to the count of the amount of entires the user has made to ensure we collect 10 titles
    else: 
        ("Thank you for entering 10 book titles!")
    sorted_titles = sorted(book_titles) #sorted function takes newly created list of titles and sorts them alphabetically
    print("Here are your book titles sorted in alphabetical order:")
    for title in sorted_titles: #iterates through and prints each title in the book list in order
        print(title) 
#Calls main function
main()
    
