#Python program that uses bubble sort to sort a list of names input by user

#Prompts the user to enter five names and store them in a list
names = []
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

#Utilizes Bubble Sort algorithm to sort the names alphabetically
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:  #Compares adjacent elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  #Swaps if out of order

#Creates a copy of the original list to preserve input order
sorted_names = names.copy()
bubble_sort(sorted_names)  #Sorts the copied list

#Reverses the sorted list
reversed_names = sorted_names.copy()
reversed_names.reverse()

#Prints final results of sorted and reverse sorted names
print("\nSorted List (Ascending):", sorted_names)
print("Reversed List (Descending):", reversed_names)