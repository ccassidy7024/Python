#Python program that creates a Madlib based on the song "Dreams" by Fleetwood Mac using functions and user inputs

#Creates a function that takes 8 or more parameters corresponding to variables
def custom_song(emotion, noun, sound, weather, people, verb1, animal, noun2, verb2):
    print("\n\n")
    print(f"Like a heartbeat drives you {emotion}")
    print(f"In the {noun} of rememberin'")
    print(f"What you had and what you lost")
    print(f"Oh, what you had, oh what you lost")
    print(f"{sound} only happens when it's {weather}")
    print(f"{people} only love you when they're {verb1}")
    print(f"{animal}, they will come and they will go")
    print(f"When the {noun2} {verb2} you clean, you'll know")


#Defines variables to take user input to create madlib within song lyrics
input_emotion = input("Enter an emotion: ")
input_noun = input("Enter a noun: ")
input_sound = input("Enter a sound: ")
input_weather = input("Enter a form of weather: ")
input_people = input("Enter a group of people: ")
input_verb1 = input("Enter a verb: ")
input_animal = input("Enter an animal(plural): ")
input_noun2 = input("Enter another noun: ")
input_verb2 = input("Enter another verb(present tense): ")

#Calls custom_song function which inputs provided user data into song lyrics to create custom madlib
custom_song(emotion=input_emotion, noun=input_noun, sound=input_sound, weather=input_weather, people=input_people, verb1=input_verb1, animal=input_animal, noun2=input_noun2, verb2=input_verb2)
