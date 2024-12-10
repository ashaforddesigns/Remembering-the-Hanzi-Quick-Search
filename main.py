import json



with open("rsh_flashcards.json","r") as json_file:
    data = json.load(json_file)

def hanziSearch(hanzi):
#spit out keyword and allow to edit quick notes
    print(f"Searching for {hanzi}: ")
    #logic
    for index, details in data.items():
        if details["hanzi"] == hanzi:
            print(f"Keyword: {details['keyword']}")
            print(f"Additional notes: {details["notes"]}")
            print("Press [N] to add a Note or <return> to make a new search")
        else:
            print(f"{hanzi} was not found")
#make it loop somehow?
        

def keywordSearch(keyword):
#spit out hanzi and allow to edit quick notes
    print(keyword)
    


def NewSearch()
print("Welcome to Asha's Remembering the Hanzi Quick Search!")
print("Are you searching by [H]hanzi or a [K]keyword?")
searchType = input("Please select [H] or [K]").capitalize()

if searchType == "H" or searchType == "HANZI":
    userEntry = input("Enter the hanzi now: ")
    hanziSearch(userEntry)

if searchType == "K" or searchType == "KEYWORD":
    userEntry = input("Enter the keyword now: ")
    keywordSearch(userEntry)




    



    





