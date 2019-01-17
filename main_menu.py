import random
import pyglet


ieltswords = {'daunt':'기죽게하다', 'venerate':'존경하다', 'discepant':'일치하지 않은/모순된','discretion':'신중, 분별','predicament':'곤경, 분별','nocturnal':'야행성의','troop':'군대','inconspicuous':'눈에 띄지않는','penetrate':'투과하다','hydrothermal':'열수의','arithmometer':'계산기','dormant':'휴면(동면)중인, 움직이지 않는','recruitment':'모집','membrane':'막','derive':'추출하다','kingfisher':'물총새','tepee':'천막집','thrive':'번성하다','intricate':'복잡한','microorganism':'미생물','descendant':'계승자','intimacy':'친밀도','affluence':'풍족함','mock':'조롱하다'}
chap_1 = {'daunt':'기죽게하다', 'venerate':'존경하다', 'discepant':'일치하지 않은/모순된','discretion':'신중, 분별','predicament':'곤경, 분별','nocturnal':'야행성의'}
chap_2 = {'troop':'군대','inconspicuous':'눈에 띄지않는','penetrate':'투과하다','hydrothermal':'열수의','arithmometer':'계산기','dormant':'휴면(동면)중인, 움직이지 않는'}
chap_3 = {'recruitment':'모집','membrane':'막','derive':'추출하다','kingfisher':'물총새','tepee':'천막집','thrive':'번성하다'}
chap_4 = {'intricate':'복잡한','microorganism':'미생물','descendant':'계승자','intimacy':'친밀도','affluence':'풍족함','mock':'조롱하다'}

music = ['music/daunt', 'music/venerate', 'music/discepant','music/discretion','music/predicament','music/nocturnal','music/troop','music/inconspicuous','music/penetrate','music/hydrothermal','music/arithmometer','music/dormant','music/recruitment','music/membrane','music/derive','music/kingfisher','music/tepee','music/thrive','music/intricate','music/microorganism','music/descendant','music/intimacy','music/affluence','music/mock']


def mainMenu():

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("1. All Words")
    print("2. Quiz")
    print("3. My words")
    print("4. My words")
    print("5. exit")
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n")

    while True:
        try:
            selection_01 = int(input("Enter choice: "))
            if selection_01 == 1:
                words()
                break
            elif selection_01 == 2:
                quiz(ieltswords)
                break
            elif selection_01 == 3:
                while True:
                    print("\n1. Add new words")
                    print("2. Review my words")
                    print("3. Main menu\n")
                    selection_04 = int(input("Enter choice: "))
                    if selection_04 == 1:
                        addwords()
                    if selection_04 == 2:
                        review()
                        break
                    if selection_04 == 3:
                        mainMenu()
                        break
                break
            elif selection_01 == 4:
                print("Flashcard")
            elif selection_01 == 5:
                break
            else:
                print("Invalid choice. Enter 1-5")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-5")



def words():
    """ Save the words users don't know to my words """
    my_word = {}
    for k,v in ieltswords.items():
        while True:
            print("\n**", k, "**\n")
            print("1. I know\n2. I don't know\n")

            try:
                selection_02 = int(input("Enter choice: "))

                if selection_02 == 1:break
                elif selection_02 == 2:
                    print(v)
                    my_word[k] = v
                    break
                else:print("Invalid choice. Enter 1-2")
            except:
                print("Invalid choice. Enter 1-2")

    print(my_word)
    anykey = input("** Enter anything to return to main menu **")
    mainMenu()



def quiz(words):

    reviewwords = {}
    wcount = 0
    ccount = 0
    kmeaning = list(ieltswords.values())

    for k,v in words.items():
        while True:
            option = list(random.sample(kmeaning,4))
            if v not in option: option[0] = v
            option = random.sample(option, len(option))
            answer = option.index(v)

            try:
                question = int(input(f"\nWhat is the meaning of {k}?\n\n1){option[0]}\n2){option[1]}\n3){option[2]}\n4){option[3]}\n\nAnswer: "))


                if int(question) == answer+1:
                    print("@@@@@@ Correct! @@@@@@\n")
                    ccount += 1
                    break
                elif 1 <= question <= 4:
                    print(f"@@@@@@ Wrong answer! @@@@@@\nThe answer is >> {answer+1} <<\n")
                    wcount += 1
                    reviewwords[k] = v
                    break
                else:
                    print("Invalid choice. Enter 1-4")
            except ValueError:
                print("Invalid choice. Enter 1-4")

    print(f"@@@@@@ {ccount} Correct, {wcount} Wrong @@@@@@\n")

    if wcount == 0:
        print("@@@@@@ Good Job @@@@@@")
        anykey = input("Enter anything to return to main menu ")
        mainMenu()
    else:
        print("1. Review the words you got wrong\n2. Main menu")
    while True:
        try:
            selection_03 = int(input("Enter choice: "))

            if selection_03 == 1:
                savewords = reviewwords
                quiz(savewords)
                break

            elif selection_03 == 2:
                mainMenu()
                break

            else:
                print("Invalid choice. Enter 1-2")
        except ValueError:
            print("Invalid choice. Enter 1-2")


def addwords():
    """ Add the words users put """
    userword = input("Enter word: ")
    usermean = input("Enter the meaning of the word: ")
    print(f"the word '{userword} : {usermean}' is added.\n")

    ieltswords[userword] = usermean

def review():
    """ Review my words with pronunciation\nPress P to listen"""
    for k,v,i in ieltswords.items(), music:
        print("\n**** ",k, v," ****\n")
        pronounce = input("Press p(pronunciation), press n(next word)")
            if pronounce.lower() == "p":
                pygame.mixer.init(22050,-16,2,4096)
                pygame.mixer.music.load(i)
                pygame.mixer.music.play()
            elif pronounce.lower() == "n":
                break






mainMenu()
