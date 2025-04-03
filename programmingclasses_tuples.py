#Python programs that uses tuple to contain list of six necessary classes to take for a programming certificate 

#Uses a main function to create tuple list of required classes
def main():
    #defines 'programming_classes' tuple with class titles
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')
    print("There are", len(programming_classes), "classes required for a programming certificate:") #lists and prints the number of classes contained in the tuple using len function
    for item in programming_classes:
        print(item) #prints each item of tuple list
#calls main function        
main()
