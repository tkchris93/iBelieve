import numpy as np
from Entry import Entry
import os

################################################################################
root = "C:\\Users\\Tanner\\Documents\\\"Python Scripts\"\\iBelieve\\data.txt"

help_text = '''
add - (applied to current entry)
    author
    file
    source
    tag
backup -
    create
    restore - (make sure there is a confirmation message)
current - 
    print the ID of the current Entry
echo - print echo. (temp)
edit - 
    author -
    body -  
    file - 
    source - 
    summary -
    tag -	
new - create a new Entry
open - (applied to current Entry)
    file - (if it exists)
    source - (if it's a website)
quit - exit the program. You will be asked if you want to save the session 
remove - (make sure there is a confirmation message)
    author -
    body - 
    file - 
    source -
    summary -
    tag -
search - 
    author - 
    date - 
    keyword - (search everything.  This will take a while)
    tag - 
    ID - 
select ID - make the Entry of with matching ID the current Entry. Prints the ID
            and the summary of the current Entry.

set - change the directory to the new location.  Move the whole folder to 
      that new location.  (make sure there is a confirmation message)
      (also ask if the user would like to save their session first)
show all - print the ID and summary for all entries
view - (for debugging)
write - 
'''

current_entry = 0
master_dictionary = {} #pairs IDs and Entries

# confirmation message
def confirmed():
    response = raw_input("Are you sure? (Y/n)")
    if response in ("Y", "y", ""):
        return True
    else:
        return False

def init_data():
    file = open("data.txt",'r')
    my_list = []

    doit = True
    while doit:
        summary = file.readline().strip()
        author = file.readline().strip()
        body = file.readline().strip()
        tags = file.readline().strip().split()
        source = file.readline().strip()
        date = file.readline()
        link = file.readline().strip()
        files = file.readline().strip()
        
        master_dictionary[len(master_dictionary) + 1] = Entry(
            summary,author,body,tags,source,date,link=link,files=files)
        
        peek = peek_line(file)
        if peek == "end":
            doit = False
            
    return my_list
        
# add a new entry to the master_list
def new_entry():
    summary = raw_input("Summary: ")
    author = raw_input("Author: ")
    body = raw_input("Body: ")
    tags = raw_input("Tags: ")
    source = raw_input("Source: ")
    
    entry = Entry(summary, author, body, tags.split(), source, "date") #TODO
    master_dictionary[len(master_dictionary) + 1] = entry

    return len(master_dictionary)

def peek_line(f):
    pos = f.tell()
    line = f.readline().strip()
    f.seek(pos)
    return line

def write_file():
    file = open("data.txt","w")
    for i in master_dictionary.values():
        file.write(i.print_write())
    
if __name__ == "__main__":
    file = open("data.txt", 'r')
    data = init_data()

    while True:
        print ""
        command = raw_input(">>> ")
        
        # current
        if command == "current":
            print current_entry
        
        # echo
        elif command == "echo":
            print "echo"

        # new
        elif command == "new":
            current_entry = new_entry() #sets the ID of the new entry to current_entry
        
        # quit
        elif command == "quit":
            if confirmed():
                save = raw_input("Save current session? (Y/n) ")
                if save in ("Y", "y", ""):
                    #call saving function
                    print "saving..."
                break
        
        # view (for debug)
        elif command == "view":
            print data
            print master_dictionary
        
        elif command == "write":
            write_file()
            
            
        # ?
        elif command == "?":
            print help_text
        else:
            print "invalid command"