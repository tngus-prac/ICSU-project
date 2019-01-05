import random

def mainMenu():
    print("1. All Words")
    print("2. Quiz")
    print("3. Flashcard")
    print("4. My words")
    print("5. exit")
    while True:
        try:
            selection = int(input("Enter choice: "))
            if selection == 1:
                words()
                break
            elif selection == 2:
                quiz()
                break
            elif selection == 3:
                print("Flashcard")
                break
            elif selection == 4:
                print("Flashcard")
            elif selection == 5:
                break
            else:
                print("Invalid choice. Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-3")
    exit
def words():
    my_word = {}
    ieltswords = {'daunt':'기죽게하다 \nIf something daunts you, it makes you feel slightly afraid or worried about dealing with it.', 'venerate':'존경하다', 'discepant':'일치하지 않은/모순된', 'discretion':'신중, 분별','predicament':',곤경, 분별'}

    for k,v in ieltswords.items():
        print("**", k, "**")
        print("1. I know\n2. I don't know")
        selection = int(input("Enter choice: "))
        if selection == 1: pass
        elif selection == 2:
            print(v)
            my_word[k] = v
    anykey = input("** Enter anything to return to main menu **")
    mainMenu()




def quiz():
    for k,v in my_word.items():
        kmeaning = ieltswords.values()
        option = random.sample(kmeaning,4)
        if v not in option: option[0] = v
        option = random.shuffle(option)
        answer = option.index(v)
        def question():
            question = input(f"What is the meaning of {k}\n1){option[0]}\n2){option[1]}\n3){option[2]}\n4){option[3]}\nAnswer: ")
            if int(question) == answer+1:
                print("@@@ Correct! @@@")
            else:
                print("### Wrong answer! ###")


    anykey = input("Enter anything to return to main menu")
    mainMenu()
# main routine
