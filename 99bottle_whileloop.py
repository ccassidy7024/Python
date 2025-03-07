# Program uses while loop to cycle through '99 bottles of  beer' song counting down from 99-0 bottles
#while loop is starting at 99 and descending
bottle = 99
#states that as the numbers cycle down through the while loop, the song will print with 
# number decreasing by one at the end of every verse
while bottle > 1:
    print(bottle, "bottles of beer on the wall,")
    print(bottle, "bottles of beer.")
    print("Take one down, pass it around,")
    bottle = bottle - 1
    print(bottle, " bottles of beer on the wall")
    print()
#once while loop fully cycles through and gets to 0, this will print to console to end song with no bottles
print("1 bottle of beer on the wall,\n1 bottle of beer.\nTake it down, pass it around,\nNo more bottles of beer on the wall!")
