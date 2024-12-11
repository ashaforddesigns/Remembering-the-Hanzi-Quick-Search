import json

with open("rsh_flashcards.json","r") as json_file:
    data = json.load(json_file)

def hanziSearch(hanzi):
#spit out keyword and allow to edit quick notes
    print(f"Searching for '{hanzi}'...")
    #logic
    for index, details in data.items():
        if details["hanzi"] == hanzi:
            print(f"Keyword: {details['keyword']}")
            print(f"Additional notes: {details["notes"]}")
            task = input("Press [N] to update a Note, [Q] to quit or hit Enter to make a new search ").capitalize()
            if task == "N":
                myNote = input("Enter your note now: ")
                noteAdded = addNote(hanzi, myNote)  # addNote will return True if successful
                if noteAdded: # is True
                    print(f"Your note '{myNote}' was successfully updated!")
                else:
                    print("Something went wrong, try again.")
                    break
            if task == "Q":
                print("Exiting...")
                break
            else:
                NewSearch()
            
        

def keywordSearch(keyword):
#spit out hanzi and allow to edit quick notes
    print(f"Searching for '{keyword}'")
    #logic
    for index, details in data.items():
        if keyword in details['keyword']:
            print(f"Hanzi: {details['hanzi']}")
            print(f"Additional notes: {details["notes"]}")
            task = input("Press [N] to update a Note, [Q] to quit or hit Enter to make a new search ").capitalize()
            if task == "N":
                myNote = input("Enter your note now: ")
                noteAdded = addNote(keyword, myNote)  # addNote will return True if successful
                if noteAdded: # is True
                    print(f"Your note '{myNote}' was successfully updated!")
                else:
                    print("Something went wrong, try again.")
                    break
            if task == "Q":
                print("Exiting...")
                break
            else:
                NewSearch()

    
def addNote(searchTerm, myNote):
    # Checks if the note is empty
    if myNote == "":
        confirm = input("You entered nothing. This will erase the existing entry PERMANENTLY. Would you like to erase your existing entry? Enter [Y] or [N]").capitalize()
        if confirm == "N":
            return  # Exits so no override occurs
        # if Y, empty string overrides the existing data
        for index, details in data.items():
            if details["hanzi"] == searchTerm or searchTerm in details["keyword"]:
                details["notes"] = ""  # erases the note
        with open("rsh_flashcards.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True  # Return True to indicate that the note was erased
    
    # if myNote is not empty, it goes ahead and adds the note
    for index, details in data.items():
        if details["hanzi"] == searchTerm or searchTerm in details["keyword"]:
            details["notes"] = myNote  
            with open("rsh_flashcards.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
            return True #it was a success
    return False #it failed (should not happen)


def NewSearch():
    print("Welcome to Asha's Remembering the Hanzi Quick Search!!!")
    print("Are you searching by [H]anzi or a [K]eyword?")
    searchType = input("Please select [H] or [K] ").capitalize()

    if searchType == "H" or searchType == "HANZI":
        userEntry = input("Enter the hanzi now: ")
        hanziSearch(userEntry)
    elif searchType == "K" or searchType == "KEYWORD":
        userEntry = input("Enter the keyword now: ")
        keywordSearch(userEntry)
    else:
        print("You did not enter [H] or [K]. Let's try again.")
        NewSearch()

NewSearch()




    



    





