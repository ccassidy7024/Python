#Python program using basic file operations with the os module to organize files in newly created directories
import os #imports os module to use to create directories
def main():
    os.mkdir("MyFiles") #creates main directory MyFiles
    os.mkdir("MyFiles/Docs") #creates three separate subdirectories Docs, Images, and Videos within MyFiles main directory
    os.mkdir("MyFiles/Images")
    os.mkdir("MyFiles/Videos")
main()