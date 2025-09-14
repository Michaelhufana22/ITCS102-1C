print("Welcome to Manga Recommender")
print("Choose what you want🥰")
print("A. Horror")
print("B. Action")
print("C. Romance")

manga_choice = input("Choose one: (A, B, C) ")

if manga_choice == 'A':
    manga = 'Horror'
    print("\nYou chose", manga)
    
    duration_choice = input("How long would it be? (short, long) ")
    era_choice = input("What era? (90s, 2000s) ")

    if era_choice == '90s':
        era = '90s'
        if duration_choice == 'short':
            print("My recommendations are:")
            print("The Laughing Vampire")
            print("Uzumaki")
            print("Hell Baby")
        elif duration_choice == 'long':
            print("Here are my recommendations:")
            print("Pet Shop of Horrors")
            print("Kyoufu Shinbun")
            
    elif era_choice == '2000s':
        if duration_choice == 'short':
            print("My recommendations are:")
            print("Fuan no Tane")
            print("Abstraction")
            print("Museum of Terror")
            print("Emerging")
        elif duration_choice == 'long':
            print("I have no recommendations")

elif manga_choice == 'B':
    manga = 'Action'
    print("\nYou chose", manga)
    
    duration_choice = input("How long would it be? (short, long) ")
    era_choice = input("What era? (90s, 2000s) ")

    if era_choice == '90s':
        era = '90s'
        if duration_choice == 'short':
            print("My recommendations are:")
            print("Rurouni Kenshin")
            print("Yu Yu Hakusho")
            print("Berserk")
        elif duration_choice == 'long':
            print("Here are my recommendations:")
            print("Dragon Ball Z")
            print("One Piece")
            print("Slam Dunk")
            
    elif era_choice == '2000s':
        if duration_choice == 'short':
            print("My recommendations are:")
            print("Hellsing")
            print("Bleach")
            print("Black Lagoon")
        elif duration_choice == 'long':
            print("Here are my recommendations:")
            print("Naruto")
            print("Attack on Titan")
            print("Fullmetal Alchemist")

elif manga_choice == 'C':
    manga = 'Romance'
    print("\nYou chose", manga)
    
    duration_choice = input("How long would it be? (short, long) ")
    era_choice = input("What era? (90s, 2000s) ")

    if era_choice == '90s':
        era = '90s'
        if duration_choice == 'short':
            print("My recommendations are:")
            print("Slam Dunk (Romantic Subplot)")
            print("Kimi no Na wa (Your Name) - OVA")
        elif duration_choice == 'long':
            print("Here are my recommendations:")
            print("Fruits Basket")
            print("Paradise Kiss")
            print("Sailor Moon")

    elif era_choice == '2000s':
        if duration_choice == 'short':
            print("My recommendations are:")
            print("Lovely★Complex")
            print("Ao Haru Ride")
            print("Nodame Cantabile")
        elif duration_choice == 'long':
            print("Here are my recommendations:")
            print("Ouran High School Host Club")
            print("Honey and Clover")
            print("Kimi ni Todoke")

else:
    print ("Invalid : please choose again(A/B/C)")