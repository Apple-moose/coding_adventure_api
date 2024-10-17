import random
from game_data import situations
from game_data import solutions
from game_data import analisis


def main(): 


 current_situation = 'start'

 profile_zen = 0
 profile_angry = 0
 profile_smart = 0
 profile_obsess = 0
 profile_dependent = 0

 def profiling():
     profiles = {'zen':profile_zen, 'angry':profile_angry, "smart":profile_smart, 'obsessed':profile_obsess, 'dependent':profile_dependent}
     winner = max(profiles, key=profiles.get)
     print(analisis[winner])
     

 def dice_throw(per):
        percentage = random.random() * 100
        if percentage <= per:
           return True
        else:
           return False 
        
 def obsession():
     if dice_throw(5):
        current_situation = 'success'
        print(situations[current_situation])
     else:
        current_situation = 'obsess'
        print("Still Nothing...Crap! continu y / n ?")

 def sleeping():
     if dice_throw(55):
        current_situation = 'nap success'
        print(situations[current_situation])
     else:
        current_situation = 'start'
        print(situations["start"])

 def cursing():
     if dice_throw(20):
        print("\033c", end="")
        print(situations['angry endgame'])
        exit()
     else:
        print("   !!! FU$%$😤    FU@^**#🤬    FU*%*@*#$^$#$%🤯   !!!")
        print("")
        print("(Double down with FUUU or feel BETTER now?)")

 def slap():
     if dice_throw(35):
        print("\033c", end="")
        print(situations['slap endgame'])
        exit()
     else:
        print("...silence...")
        print("")
        print("You just realized that you could have hit some sensitive equipment. \
(Maybe not do that again?)")
        print("SLAP harder, explore more of the DARK side or come BACK to CODING?)")  

 def hammer():
     if dice_throw(50):
        print("\033c", end="")
        print(situations['angry endgame'])
        exit()
     else:
        print("")
        print("The wall still stands but it's getting weaker. Any moment....")
        print("")
        print("HAMMER further, explore more of the DARK side or feel BETTER now?)")

 def explain():
     if dice_throw(40):
         print(situations['duck success'])
     else:
         print("You unfold the layers of your coding conundrum, but still can't connect those dots...")
         print("")
         print("...so sad!...EXPLAIN in more detail, check your OPTIONS or just STRANGLE the rubber duck")

 print("\033c", end="")
 print("")
 print("Welcome to the 'A Coder's Rhapsody Game'!")
 input("Press <enter> to start...")
 print(" ")
 print("A plausible situational and psychological analysis")
 input("(Based on personal and shared experience)<enter>")
 print(" ")
 print("Please type 'GET TO WORK' when you feel ready to start!")
 print("(type 'HELP' in case you are blocked)")

 while True:
        command = input("👉 ").lower()
        if command in solutions[current_situation]:
             current_situation = solutions[current_situation][command]
             print(situations[current_situation])
        elif command == "get to work":
            print(f"{situations[current_situation]}.")
        elif command == "work":
            print(f"{situations[current_situation]}.")
        elif command == "study":
            current_situation = 'study'
            profile_smart += 1
            print(situations["study"])
            input("time passes....<enter>")
            input("more time passes...")
            print("")
            print("Although you feel like you are getting smarter by the minute, dinner time approaches \
and you are still nowhere close to resolving your coding issues...")
            print("")
            print(situations["study2"])
            print("")
        elif command == "obsess":
            current_situation = 'obsess'
            profile_obsess += 2
            print(situations['obsess'])
            input("Aaaaaarrrgh!!! ....")
            obsession()
        elif command == "y":
            profile_obsess += 1
            obsession()
        elif command == "n":
            profile_smart += 1
            current_situation = 'abandon'
            print(situations['abandon'])
        elif command == "friend":
            current_situation = 'call_friend'
            profile_dependent += 1
            print(situations['call_friend'])
            input("(Press <enter> to celebrate and do a little dance...)")
            print("")
            current_situation = 'start'
            input("The next day...")
            print(situations['start'])
        elif command == "colleague":
            current_situation = 'call_colleague'
            profile_dependent += 1
            print(situations['call_colleague'])
            print("")
            input("(Press <enter> to swallow some of your coder's pride...)")
            print("")
            current_situation = 'start'
            input("The next day...")
            print(situations['start'])
        elif command == "chatgpt":
            current_situation = 'chatgpt'
            profile_dependent += 2
            input("(Press <enter> and may the omnipotent A.I. one day rule the World!)")
            print("")
            input("Oops, weird answer. Let's formulate that query more adequately...")
            print("")
            print(situations['chatgpt'])
        elif command == "sleep":
            current_situation = 'sleep'
            profile_smart += 1
            print(situations['sleep'])
            print("")
            input('Press <enter> to wake up')
            sleeping()
        elif command == "scream":
            profile_angry += 0.5
            input("(Press <enter> to scream into that pillow and cry it out a little...)")
            current_situation = 'pillow'
            print(situations['pillow'])
        elif command == "f-word":
            profile_angry += 1
            input("You breathe in all the air your lungs can admit and let out a magnificent angry FUUUUUUUUUUUU@#$% !!!<enter>")
            current_situation = 'cursing'
            print("")
            print(situations[current_situation])
        elif command == "fuuu":
            profile_angry += 2
            input("(Fffffffff......)")
            current_situation = 'cursing'
            cursing()
        elif command == "slap":
            profile_angry += 1
            current_situation = 'slap'
            input("You raise your hand and hit <enter> the table in frustration...")
            input("SHHLLPPLAAAAKKK!!!")
            slap()
        elif command == "hammer":
            profile_angry += 3
            current_situation = 'punch'
            input("You grab the hammer with both hands and hit as hard as you can...<enter>")
            input("KAAABOUUUUUMMMMM, KRRAAAKKK, Schling schlingg...")
            hammer()
        elif command == "explain":
            profile_smart += 1
            current_situation = 'duck'
            input("You confess to the rubber duck...<enter>")
            input("He seems rather perplexed...")
            print("")
            explain()
        elif command == "chocolate":
            profile_zen += 1
            current_situation = 'kitchen'
            input('the chocolate <enter>s your watering mouth')
            print("")
            print("Mmmmmh, Delicious!")
            print("")
            print(situations['tea'])
        elif command == "tea":
            profile_zen += 1
            current_situation = 'kitchen'
            input('You press <enter> on the water boiler...')
            print("")
            print(situations['sandwich'])
        elif command == "sandwich":
            profile_zen += 2
            current_situation = 'kitchen'
            input('You insert all those wonderful ingredients between integral slices of bread...')
            print("")
            print("Best Sandwich Ever!")
            print("")
            print(situations['break'])
        elif command == "break":
            profile_zen += 2
            current_situation = 'kitchen'
            input('Press <enter> to pause and check the news on your phone...')
            print("")
            print("La la lah...ouh, what's up with that...")
            print("")
            print(situations['after break'])
        elif command == "profile":
            current_situation = "profile"
            input('Please take a deep breath and press <enter> to accept some constructive criticism...')
            print("\033c", end="")
            print('')
            profiling()
            print("")
            print("Keep on CODING, QUIT or EXIT this mini game")
        elif command == "help":
            print(" ")
            print("Try typing keywords from the text, such as: duck, fridge, stack overflow...")
            print("...'exit' to end the game or 'profile' to watch over your coder's profile! ")
        elif command == "quit":
            print('👿 Yeah, just what I thought 😈')
            break
        elif command == "exit":
            print('Thanks and hope to see you soon!')
            break
        else:
            print("Say Whaaaat???🫣")

if __name__ == "__main__":
    main()