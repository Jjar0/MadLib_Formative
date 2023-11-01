import random

def main():

    print ("Would you like to:")
    selection = input ("A: Play Mad-Lib?\nB: Create Mad-Lib stories?\n[A/B]>") # Main menu for the game, IF statements to choose gamemode.
    print (selection)

    if selection == "A":
        print ("Select your gamemode!")
        setup()
    if selection == "B":
        print ("Welcome to the story creator!")
        stories()
    else:
        print ("Please make sure you choose either option A or B.")
        main()

def setup():

    gameType = input ("Do you want to play with,\nA: Default stories,\nB: User created stories?\nC: Return to the main menu?\n[A/B/C]>") # Player chooses between using built in stroies or custom stories.

    print(gameType)

    if gameType == "C":
        main()

    if gameType == "A": 
        print ("using default stories.") # DEFAULT STORIES.

        default1 = ("I get # when I @ a &.")
        default2 = ("That was #, I've never seen anyone @ like that, destroyed the & though.")
        default3 = ("Thats one ugly &, we might need to @ it in a # kind of way.")

        roulette = [default1,default2,default3] # Selects a stroy at random.

        template = random.choice(roulette)

        game(template)

        storyList = [] # Creating a list of characters from the txt file string.
        for char in template:
            storyList.append(char) # 'storyList' holds custom story as a list for editing during the game.
            
        game(storyList) # Calls the game function and carries the chosen story through.
                    
    if gameType == "B":
        print ("Using custom stories.\n") # CUSTOM STORIES.

        with open("templates.txt", "r",) as f: # Read and print txt file by line to display story options to player.
            for line in f:
                print (line.rstrip())
        f.close()

        print ("\n")

        chosenLine = input ("enter the linenumber of the template you wish to use.\n[123...]>") # Player chooses which template they wish to use by entering line number.
        while True:
            try:
                chosenInt = int(chosenLine) # Integer validation.       
            except ValueError:
                print("Not an integer! Try again.")
                chosenLine = input ("[123...]>")
                continue
            else:
                break

        print (chosenLine)
        chosenLine = int(chosenLine)

        f = open("templates.txt", "r")
        lines = f.readlines()
        f.close()

        totalLines = len(lines) # Input validiation for Index errors.
        if (chosenLine > totalLines):
            print (str(totalLines))
            print ("there are " + (str(totalLines)) + " lines in the file") # Prevents player from entering line numbers that dont have data.
            setup() # This validation is lazy.

        else:
            template = lines[chosenLine - 1].rstrip('\n') # removes newline on lines for better data redability, also makes sure first line is not skipped.
            print ("\n")
            print (template + "\n")
            
        game(template) # Calls the game function and carries the chosen story through.

    else:
        print ("Please make sure you choose either option A or B.")
        setup()    


def game(template):

    print ("Lets play!")
 
    adjective = input ("Please enter an Adjective.\n>")
    print (adjective)

    verb = input ("Please enter a Verb.\n>")
    print (verb)

    noun = input ("Please enter a Noun.\n>")
    print (noun)

    storyList = [] # Creating a list of characters from the custom/default template string.
    for char in template:
        storyList.append(char) # 'storyList' holds custom story as a list for editing during the game.
        
    for i in range(len(storyList)):  # Locates adjective, verb and noun markers. replaces them with user entered strings.
        if storyList[i] == "#":
            storyList[i] = (adjective)

    for i in range(len(storyList)):
        if storyList[i] == "@":
            storyList[i] = (verb)

    for i in range(len(storyList)):
        if storyList[i] == "&":
            storyList[i] = (noun)

    madLib = ""

    for i in storyList: # Replacing delimiters with spaces, turning list into string.
        madLib += i+""


    print ("\n")
    print (madLib + "\n") #printing madlib string!

    epilogue = input ("Would you like to,\nA: Play again with new words,\nB: Choose a different story,\nC: Return to the menu.\n[A/B/C]>")
    while epilogue != "A" or epilogue != "B" or epilogue != "C": # Validated menu to return to different functions of the game.
        print ("Please enter either A, B or C.")
        epilogue = input ("[A/B/C]>")

        if epilogue == "A":
            game()
        if epilogue == "B":
            setup()
        if epilogue == "C":
            main()
        


def stories(): 
        
    print ("When creating your story use,\n'#' to place an adjective,\n'@' for a verb,\n'&' for a noun.\nEnter 'ESC' to return the main menu.") 
    userStory = input ("\nplease enter your user story:\n>")

    while userStory.find('#')==-1 or userStory.find('@')==-1 or userStory.find('&')==-1: # Validation for madlib markers, searches for markers and loops if not present.
        print ("Please make sure you entered all 3 special characters!")
        stories()

    if userStory == "ESC": # Exit to main
        main()

    print ("\n" + userStory + "\n") # Shows player their own story after entering.
 
    saveChoice = input ("Do you wish to save this user story?\n[Y/N]>")
    print (saveChoice)

    while saveChoice != "Y" or saveChoice != "N":
        saveChoice = input ("[Y/N]>")
        print (saveChoice)


        if saveChoice == "Y":                           # Player appends their story string to a newline in the txt.   
            print ("This story has been saved.")
            templateFile = open('templates.txt', 'a')
            templateFile.write('\n' + userStory)
            templateFile.close()
            print ("Story saved to templates.txt")
            stories()
            
        if saveChoice == "N":
            stories()

    



print ("Welcome to the Mad-Lib word game!") 
main()