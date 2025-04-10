situations = {
    "instructions": """You are currently playing a text adventure game with multiple possible endings.§\
                Choices you make will sometimes trigger 'dice rolls' that end up in success or failure.§\
                Meanwhile, the game punctuates your every moves and writes a coder 'profile' in the background.§\
                Explore your options by typing the uppercase keywords in the text (as: WORK, CODE, DUCK, FRIDGE, PROFILE....).§§\
                Get it? Jump right in by typing START.§\
                No time for this? Type EXIT or QUIT§->""",
    "start": "So, here you are again, laptop in hands. You start to WRITE CODE.§->",
    "start_next_day": "§§The next day ...§$So, here you are again, laptop in hands. You start to WRITE CODE.§->",
    "first options": "You gather your focus and put your mind to work with confidence. §Right away, your flow gets interrrupted by this damn 'meanError' again.§\
... What do you do? §STUDY all your notes from school, open your browser and GOOGLE the issue, check STACK overflow, query CHATGPT?§ Or maybe get your eyes off the screen and start talking to the DUCK\
, move to the KITCHEN? §Also, how about asking a senior COLLEAGUE for a quick fix?§->",
 #STACK-----------------------------  
    "stack overflow": "You end up scrolling again on Stack Overflow, your most trusted friend on the web. §There are tons of solutions \
exposed on many pages but, at first glance, it's all gibberish, nothing seems applicable ...§At this point, be honest: you start building internal FRUSTRATION §or \
you calmly start to INVESTIGATE deeper, consulting multiple resources, STUDY some more and see what sticks? §Maybe you ask a coder FRIEND (#COLLEAGUE) §or turn to some CHATGPT consulting? §(You could always SLEEP on it ...)§->",
 #DUCK----------------------------------
    "duck": "You look around and make eye contact with the rubber duck on your desk. §You are well aware of the magic involved in \
RUBBER DUCKING. §The question is: do you really believe in it? §The duck looks back at you faithfully, listening ...§What are you going to do: try to EXPLAIN your coding problems \
to Donald §or don't be a fool and reconsider your OPTIONS?§->",
    "rubber ducking": "[ In software engineering, rubber duck debugging (or 'rubberducking') is a method of debugging code by articulating a \
problem in spoken or written natural language. The name is a reference to a story in the book The Pragmatic Programmer in which a programmer \
would carry around a rubber duck and debug their code by forcing themselves to explain it, line by line, to the duck. ] § Now that you know, please reconsider your options by pressing B+A+C+K, in that order with a finger \
on the keyboard. Then, with the same finger or another press <enter> ...)§->",
    "duck_explain_txt": "You confess to the rubber duck ... <key>$§He seems rather perplexed ...$\
§",
    "duck success": "Incredible! §Confessional Programming IS an actual working method for debugging and you are now \
living proof of it. §Going back to the code, you find that hidden bug and make everything run smoothly again. §You feel smart \
and adequate. §TODO: Celebrate fully and check for updates on your coder PROFILE? §Or on to the NEXT challenge?§->",
    "duck_explain_no": "You unfold the layers of your coding conundrum, but still can't connect those dots.§\
... so sad!§EXPLAIN in more detail, check your OPTIONS or just STRANGLE the rubber duck?§->",
    "strangle duck": "You put your hands around the duck's neck. §You start squeezing until you hear a \
'Kwaaaakkk'. §Playing the rubber duck murderer makes you giggle and releases a bit of accumulated tension. §You squeeze some more, \
and realize how childish you have become§(...or have you? You're considering turning to the DARK side ...) §§Now, where were we? \
Ah yeah! Donald ... §Try to EXPLAIN your code again line by line, §reconsider your OPTIONS §or accept defeat and ABANDON?§->",
 #KITCHEN----------------   
    "kitchen": "Let's get some air in the lungs and refill your energy levels. §What's the rush anyways? §You walk \
to the kitchen slowly, thinking about what you will find there ...§You take the opportunity to drink a bit of water. \
Your eyes catch a glimmer coming from a box on the counter with a big 'Merci' written on it... §Steal a bite of CHOCOLATE or \
BACK to work?§->",
    "chocolate_intro": "The chocolate <enter>s your watering mouth.$§'Mmmmmh, Delicious!",
    "tea": "§You wipe away all traces of chocolate from the corners of your smile and notice that the kettle was already filled and plugged in. §Now, how about making \
yourself a nice cup of TEA? §Maybe eat another piece of CHOCOLATE? §... or BACK to work for some reason ...???§->",
    "tea_intro": "You press <key> on the kettle ...$§",
    "sandwich": "Waiting for the water to boil, you prepare your cup and check the fridge for some cream while you \
are planning your next move: §going BACK to work ...   §Also, you can't help but notice all the necessary ingredients to make yourself \
your favorite SANDWICH. §Again: 'What's the rush, right? Very tempting. It would surely take your belly out of the equation during your next coding session ...§->",
    "sandwich_intro": "You insert all those wonderful ingredients between integral slices of bread ...<key>$§Best Sandwich Ever!§",
    "break": "§There it is: true pleasure. A Happy brain in a Happy body. What more? §Well, how about a little BREAK for \
digestion purposes? §(Or BACK to work ... Really??)§->",
    "break_intro": "Press <key> to pause and check the news on your phone ...$§La la laaa ... Hey, what's up with that? ...§",
    "after break": "§Oh! Time passes so fast when you're looking for new shoes on amazon!§§Fine, let's go BACK to coding, \
but not before you pass by the WC, check your hair and your teeth in the mirror, put on a warm shirt, make yourself \
another TEA, and/or grab some more CHOCOLATE ...§->",
    "wc": "Right!§Of course you had to type 'WC'!§Very, very thorough ... like a bot! Too bad I do not have a 'verify if you are human' in my program.\
§ Alright, whatever. Back to the KITCHEN or to your CODE issues?§->",
 #FRIEND---COLLEAGUE-------------------------   
    "call_colleague": "Your self esteem takes a hit as you push through the: §'Pffffff', 'yeah, yeah' and 'I'm too busy right now'...§ \
Anyways, you end up pushing your problematic code and, later, you receive that much needed gitHub get request from a more advanced coder colleague.§ \
§Smart move, buddy, You congratulate yourself for not wasting time and/or not learning much ...§\
§(Press <key> to swallow some of your coder pride ...)$",
    "call_colleague_not": "Oooops! Not now it seems.§It's been crunch time every day for a lot of your co-workers lately, and you really get \
the sensation that your cries for help are annoying them.§Most colleagues don't even bother reading your messages right now. But once they do, you know it will not reflect good on you.§\
How about giving your CODE issue another GO?§\
Or would you rather ask a coder FRIEND for tips?§->",
    "call_friend": "After a couple of calls, someone from the inner circle picks up and laughs at you a little.§ \
You do your best to explain the matter at hand ... and your friend gets half of it. §During the exchange, he refers you to an obscure webChat \
where some similar issues to yours are being discussed. §You thank your friend for nothing and start pasting every line of code \
from the forum until one of them sticks! §Lucky for you, those coders are geniuses and the 'meanError' seems to have disappeared ... for the moment. \
§Hallelujah!! §You praise the coding community and swear to your future self that you will one day take the time to understand that pasted code ...§\
§§Press <key> to celebrate and do a little dance ...$§",
    "call_friend_not": "Nobody picks up ... §What?? Today of all days!§Pfffffff! You decide to leave messages all over your social apps ...§\
Press <key> to check your messages.$§§Nothing. Time passes ... Check again (<key>)$§I guess it's just one of those days, buddy ...§\
Well then, are you going to WASTE the whole day waiting?§... or will you TRY SOMETHING ELSE?§->",
 #CHATGPT------------------------------------   
    "chatgpt": "(Press <key> and may the omnipotent AI one day rule the World!)$§\
After a couple of tweaks to the prompt, the Truth appears before your eyes: §Pure Code§ Perfect: \
devoid of unuseful console loggings, full of //#Comments and generic variable names. §The code is undoubtedly clean and, once pasted, runs smooth like butter. \
§Smart move. Just don't tell anyone what you've done and earn yourself some time to spend on more entertaining stuff! \
§Life doesn't have to be that hard, right? §So, will you ever CODE again, §QUIT this nonsensical absurdity of a mini game, §or check updates \
on your coder PROFILE?§->",
    "chatgpt_not": "(Press <key> and may the omnipotent AI one day rule the World!)$§\
Oops, weird answer. Let's formulate that query more adequately$§Nope! Doesn't work!§The pasted code creates more \
issues than it solves.§Is that it? Have you reached 'Chat's endpoint?§§Press <key> with the full weight of what that would mean for humanity ...$\
§You feel incredible for 5 seconds; then you realize how much this failure just underscores your inability to expose your coding issues to a more efficient being.§\
And, by the way, that 'meanError' hasn't been solved yet!§\
§How about something more tangible? A coder FRIEND or COLLEAGUE?§A rubber DUCK or a search on GOOGLE?§\
Getting some SLEEP or snacks in the KITCHEN?§->",
 #FRUSTRATION--------------------------------------   
    "frustration": "HOOOOOOLLLY COW!!! Computers are so incredibly AUTISTIC! §You realize at this instant how much you were NOT \
made to work in a mental institution ...§but you might become a patient if you let all this anger control you! \
§You take a second to contemplate the issue: do you decide to come BACK and evaluate this situation calmly, §or turn to \
the DARK side and express some of that accumulated tension physically?§->",
    "dark": "Something's got to give and various options are rapidly presenting themselves: §you can SCREAM in a pillow, §let out a very long and very loud F-WORD, \
SLAP something on the desk §or just PUNCH that wall with all you've got ...§->",
    "pillow": "(Press <key> to scream into that pillow and cry it out a little ...)$§After this mini crisis episode, you go and refresh your face in the bathroom. §Once the mirror-check \
reflects your normal 'OK' face again, you come back to your post, take a deep breath and start to CODE again ...§->",
    "curse_intro": "(Fffffffff......)$§",
    "cursing": "You breathe in all the air your lungs can admit and let out a magnificent angry FUUUUUUUUUUUU#%!!!<key>$§WAouuuuuh that felt good! §Sometimes, cursing is all you've got ...§\
For now, you're 'OK'. (Are you? Let us know if you had ENOUGH?) §Also, you can't shake the feeling that \
you might have been noticed by someone else, and that makes you want to curse even more. §Will you risk another very loud 'FUUU'??§->",
    "cursing_success": "   !!! FU%**😤§§   FU*^&#**#🤬§§   FUuuuuUUUU*%#*#^#%🤯   !!!§§Double down with FUUU or feel BETTER now?§->",
    "punch": "You turn to that ugly wall next to the desk and hit it with your right fist. §AOUCH! ... §Damn, \
you have hit precisely where the supporting beam was! §Your hand hurts a little and the wall is somehow mocking you. \
§What is this unfortunate experience teaching you? §That you need to 'CALM DOWN'? §... or go the toolbox, get the HAMMER and bring that \
stupid wall down?§->",
    "hammer_intro": "You grab the hammer with both hands and hit as hard as you can ... <key>$§KAAABOUUUUUMMMMM, KRRAAAKKK, schling schlingg ...$§",
    "hammer_success": "The wall still stands but it's getting weaker. Any moment now ...§Go full Thor with the HAMMER this time, explore more of the DARK side?§... or are you feeling BETTER now?§->",
    "slap_intro": "You raise your hand and hit <key> the table in frustration ...$§SHHLLPPLAAAAKKK!!!$§",
    "slap_success": "... silence ...§§Ouf! You just realized that you could have hit some sensitive equipment. \
(Maybe not do that again?)§SLAP harder, explore more of your DARK side?§ ... Or come BACK to CODING?§->",
    "slap endgame": "OUch!!! §The slapping went uncontrolled and your laptop gets a big hit. §Screen of Death and broken glass, \
you are also bleeding at the wrist. §What a mess!!! §§Seriously?? This couldn't have gone worse. \
§You have just been labeled 'dangerous' to all synthetic life. §This mini game is booting you out as to avoid further material destruction. §Good luck with your temper issues Pal!§@",
    "angry endgame": "With so much noise, someone has called the autorities on you. §You get a serious warning and find yourself in such a state of \
anger and despair that you are rendered inoperable. §You need to CALM DOWN! Seriously. \
§This mini game is booting you out as to avoid further material and/or psychic destruction. §Have a nice Life, Buddy!§@",
    "autism": "Autism, also called autism spectrum disorder (ASD) or autism spectrum condition (ASC), is a neurodevelopmental disorder \
marked by restricted and repetitive patterns of behavior and deficits in reciprocal social communication. Other common signs include perseverative \
interests, stereotypic body movements (stimming), rigid routines, hyper- or hyporeactivity to sensory input, and difficulty with social interaction \
and verbal and nonverbal communication. §(type 'BACK' exactly, without any mistake or I will not understand!)§->",
 #STUDY-----------------------------------------   
    "study": "Zen as a bonsai, you turn to research mode, grab your notes and try not to deviate from the path too much.§Time passes ...$\
more time passes ...§$Although you feel like you are getting smarter by the minute, §dinner time approaches \
and you are still nowhere close to resolving your coding issues ...§\
You take a couple of minutes to ponder your options: §you can always let it go and SLEEP on it, \
see what tomorrow brings. §You can also OBSESS and stay on course until you make the code work, §or \
look inward and see if you are not, in fact, building up some kind of FRUSTRATION.§->",
    "obsess_intro": "OK, you got this. §Knife between your teeth you try to make it work using the sheer power of your Will.$",
    "success": "§Hey! It's functioning! You're not yet sure exactly why, but it runs. Flawlessly! §WOW! Impressive.\
§You do a little dance ... and just between us, you know it's passed 3 a.m., right? \
§Oh! And did you miss that call from your mother? §You will probably be coding in bed too. Good luck sleeping! \
§§START again because you are a maniac? §Or check updates on your coder PROFILE together?§->",
 #SLEEP-----------------------------------   
    "sleep_txt": "Time to get your Mojo back, meditate, and experience the cycle of life again. §Breathing in and out. \
§This is how the experienced thinker acts: trusting one's brain to classify all the data during its 'reboot phase' and eventually reveal the missing links ...§\
    Press <key> to wake up.$",
    "nap_success": "§What a difference a power nap makes! §You haven't touched the keyboard and yet, you are already \
formulating solutions smiling from one ear to the other. §Your refreshed self is winning, the reset bears its fruits. §You feel wiser and a little more proficient at coding. How about that?\
§Hopefully, it will work NEXT TIME. §Or maybe you would like to check updates on your coder PROFILE?§->",
 #ABANDON------------------------------   
    "abandon": "You are failing and you know it. There must be a simple explanation, but it is out of reach for the moment. \
§Time to lick your wounds, admit defeat, and gather your strength for the next fight. §§Another day, another code to write ... What will you do? \
§START AGAIN, meditate on your coder PROFILE §or just QUIT?§->",
#TODO---------------------------------
    "todo": "'To do', get it?§(BACK?)->"
}
 
solutions = {
    "instructions": {"start": "start"},
    "start": {"write code": "first options", "code": "first options", "write": "first options", "why": "instructions", "goal": "instructions"},
    "start_next_day": {"write code": "first options", "code": "first options", "write": "first options"},
    "first options": {"google": "stack overflow", "stack overflow": "stack overflow", "stack": "stack overflow", "duck": "duck", "kitchen": "kitchen"},
    "stack overflow": {"frustration": "frustration", "investigate": "study", "study": "study"},
    "study": {"obsess": "obsess", "frustration": "frustration"},
    "nap_success": {"next time": "start_next_day", "next": "start_next_day", "time": "start_next_day"},
    "call_friend_not": {"waste": "start_next_day", "try": "first options", "something": "first options", "else": "first options", "something else": "first options", "try something else": "first options"},
    "call_colleague_not": {"start": "first options", "start again": "first options", "code": "first options", "go": "first options"},
    "chatgpt": {"code": "start_next_day"},
    "frustration": {"autistic": "autism", "not": "autism","back": "first options", "dark": "dark"},
    "dark": {"punch": "punch"},
    "autism": {"back": "frustration"},
    "cursing": {"ok": "first options", "enough": "first options", "better": "start", "write code": "first options", "code": "first options"},
    "obsess": {"abandon": "abandon", "start": "start"},
    "abandon": {"start again": "start", "start": "start"},
    "pillow": {"code": "first options", "ok": "first options"},
    "f-word": {"write code": "first options"},
    "slap": {"write code": "first options","dark": "dark", "back": "start", "coding": "first options"},
    "punch": {"write code": "first options", "better": "start", "calm down": "first options", "calm": "first options","dark": "dark"},
    "todo": {"back": "duck success", "todo": "todo"},
    "duck": {"rubber ducking": "rubber ducking", "next": "start", "options": "first options", "strangle": "strangle duck", "start": "start", "todo": "todo"},
    "rubber ducking": {"back": "duck"},
    "duck_explain_no": {"options": "first options", "strangle": "strangle duck", "strangle duck": "strangle duck"},
    "strangle duck": {"options": "first options", "abandon": "abandon", "dark": "dark", "donald": "duck"},
    "duck success": {"next": "start_next_day", "todo": "todo"},
    "kitchen": {"back": "first options", "wc": "wc", "w.c.": "wc", "kitchen": "kitchen", "code": "first options"},
    "profile": {"start": "start"},
    "success": {"start": "start"},
    "wc": {"kitchen": "kitchen", "code": "first options"},
    "help": {"start": "start", "back": "start"},
}

analisis ={
    "zen":"Your definition of being Zen is borderline between 'My body is a Temple' and 'fulfilling every little \
bodily impulse of mine'. §As Bobby said: it is your prerogative. And after all, we don't want you complaining, or \
stressed, unhappy, sick, hungry ...§It's just not good for business! §However, you also need a roof over your head. \
Have you done any work today?§§EXIT or START again?§->",
    "angry":"Terrible! Intimidating. §You're a constant menace to colleagues and any sensitive electrical devices around you \
when you are coding. §Anger issues? §We all have them, especially when driving during rush hour. §Someday, you will realize that \
we are all angry inside. Some are just better at managing/hiding it, that's all. §Now, careful next time you spin out of \
control: you might open the cage for an angrier beast ... §and/or just get a bad rep!§§EXIT or START again?§->",
    "smart":"It is not enough to have the best bike, you need to maintain and tune it to your \
preferences. §Well, my friend, that bike is your brain and you are very aware of it. §There's nothing we can tell you here \
that you don't already know. §Keep on making the right decisions and soon you will see them mortals, miles away on your \
rearview mirror.§§EXIT or START again?§->",
    "obsessed":"You are definitely very confident in your own capacities. §But, you end up sooooo tired, soooo exhausted ...\
and after a while, so does everyone around you. §Not sure you can keep this up for long. How about tomorrow? \
§It kind of begs the question: §Wouldn't it be more productive to take a breather sometimes? Fill up the tank?§§EXIT or START again?§->",
    "dependent": "Asking for help is fine and respecting deadlines is fundamental. Good point. §Hopefully, you are aware that \
abusing the people around you is not a viable carreer plan. §Unless your only friend is an AI on the web and fellow humans start avoiding your calls, you should be fine.§ \
Oh! And also, NEVER ask yourself: How's my coding going? Any notable progress lately?§§EXIT or START again?§->",
}

#------TEXT ADAPTED FOR MOBILE----------------------------------------------------------------------

mobile_situations = {
    "start": "So, here you are again, laptop in hands. You start to [WRITE CODE].",
    "start_next_day": "§§The next day ...§$So, here you are again, laptop in hands. You start to [WRITE CODE].§ (Or would you rather consult your coder [PROFILE] first?)",
    "first options": "You gather your focus and put your mind to work with confidence. §Right away, your flow gets interrrupted by this damn 'meanError' again.§\
... What do you do? §[STUDY] all your notes from school, open your browser and [GOOGLE] the issue, check [STACK] overflow, query [CHATGPT]?§ Or maybe get your eyes off the screen and start talking to the [DUCK]\
, move to the [KITCHEN]? §Also, how about asking a senior [COLLEAGUE] for a quick fix?",
 #STACK-----------------------------  
    "stack overflow": "You end up scrolling again on Stack Overflow, your most trusted friend on the web. §There are tons of solutions \
exposed on many pages but, at first glance, it's all gibberish, nothing seems applicable ...§At this point, be honest: you start building internal [FRUSTRATION] §or \
you calmly start to [INVESTIGATE] deeper, consulting multiple resources, [STUDY] some more and see what sticks? §Maybe you ask a coder [FRIEND] (#[COLLEAGUE]) §or turn to some [CHATGPT] consulting? §(You could always [SLEEP] on it ...)",
 #DUCK----------------------------------
    "duck": "You look around and make eye contact with the rubber duck on your desk. §You are well aware of the magic involved in \
[RUBBER DUCKING]. §The question is: do you really believe in it? §The duck looks back at you faithfully, listening ...§What are you going to do: try to [EXPLAIN] your coding problems \
to Donald §or don't be a fool and reconsider your [OPTIONS]?",
    "rubber ducking": "--In software engineering, rubber duck debugging (or 'rubberducking') is a method of debugging code by articulating a \
problem in spoken or written natural language. The name is a reference to a story in the book The Pragmatic Programmer in which a programmer \
would carry around a rubber duck and debug their code by forcing themselves to explain it, line by line, to the duck.-- § Now that you know, come [BACK] and please reconsider your options",
    "duck_explain_txt": "You confess to the rubber duck ...$§He seems rather perplexed ...$\
§",
    "duck success": "§Incredible! §Confessional Programming IS an actual working method for debugging and you are now \
living proof of it. §Going back to the code, you find that hidden bug and make everything run smoothly again. §You feel smart \
and adequate. §[TODO]: Celebrate fully and check for updates on your coder [PROFILE]? §Or on to the [NEXT] challenge?",
    "duck_explain_no": "You unfold the layers of your coding conundrum, but still can't connect those dots.§\
... so sad!§[EXPLAIN] in more detail, check your [OPTIONS] or just [STRANGLE] the rubber duck?",
    "strangle duck": "You put your hands around the duck's neck. §You start squeezing until you hear a \
'Kwaaaakkk'. §Playing the rubber duck murderer makes you giggle and releases a bit of accumulated tension. §You squeeze some more, \
and realize how childish you have become§(...or have you? You're considering turning to the [DARK] side ...) §§Now, where were we? \
Ah yeah! Donald ... §Try to [EXPLAIN] your code again line by line, §reconsider your [OPTIONS] §or accept defeat and [ABANDON]?",
 #KITCHEN----------------   
    "kitchen": "Let's get some air in the lungs and refill your energy levels. §What's the rush anyways? §You walk \
to the kitchen slowly, thinking about what you will find there ...§You take the opportunity to drink a bit of water. \
Your eyes catch a glimmer coming from a box on the counter with a big 'Merci' written on it... §Steal a bite of [CHOCOLATE] or \
[BACK] to work?",
    "chocolate_intro": "TOUCH ME to let the chocolate enter your watering mouth.$§'Mmmmmh, Delicious!",
    "tea": "§You wipe away all traces of chocolate from the corners of your smile and notice that the kettle was already filled and plugged in. §Now, how about making \
yourself a nice cup of [TEA]? §Maybe eat another piece of [CHOCOLATE]? §... or [BACK] to work for some reason ...???",
    "tea_intro": "You press the ON switch on the kettle ...$",
    "sandwich": "§Waiting for the water to boil, you prepare your cup and check the fridge for some cream while you \
are planning your next move: §going [BACK] to work ...   §Also, you can't help but notice all the necessary ingredients to make yourself \
your favorite [SANDWICH]. §Again: 'What's the rush, right? Very tempting. It would surely take your belly out of the equation during your next coding session!",
    "sandwich_intro": "You insert all those wonderful ingredients between integral slices of bread ...$§Best Sandwich Ever!",
    "break": "§There it is: true pleasure. A Happy brain in a Happy body. What more? §Well, how about a little [BREAK] for \
digestion purposes? §(Or [BACK] to work ... Really??)",
    "break_intro": "Touch THIS APP to pause and check the news on your phone ...$§La la laaa ... Hey, what's up with that? ...§",
    "after break": "§Oh! Time passes so fast when you're looking for new shoes on amazon!§§Fine, let's go [BACK] to coding, \
but not before you pass by the [WC], check your hair and your teeth in the mirror, put on a warm shirt, make yourself \
another [TEA], grab some more [CHOCOLATE] or first check on your coedr [PROFILE]?",
    "wc": "Right!§Of course you had to touch 'WC'!§Very, very thorough ... like a bot! Too bad I do not have a 'verify if you are human' in my program.\
§ Alright, whatever. Back to the [KITCHEN] or to your [CODE] issues?",
 #FRIEND---COLLEAGUE-------------------------   
    "call_colleague": "Your self esteem takes a hit as you push through the: §'Pffffff', 'yeah, yeah' and 'I'm too busy right now'...§ \
Anyways, you end up pushing your problematic code and, later, you receive that much needed gitHub get request from a more advanced coder colleague.§ \
§Smart move, buddy, You congratulate yourself for not wasting time and/or not learning much ...§\
§(Touch HERE to swallow some of your coder pride ...)$",
    "call_colleague_not": "§Oooops! Not now it seems.§It's been crunch time every day for a lot of your co-workers lately, and you really get \
the sensation that your cries for help are annoying them.§Most colleagues don't even bother reading your messages right now. But once they do, you know it will not reflect good on you.§\
How about giving your [CODE] issue another [GO]?§\
Or would you rather ask a coder [FRIEND] for tips?",
    "call_friend": "§After a couple of calls, someone from the inner circle picks up and laughs at you a little.§ \
You do your best to explain the matter at hand ... and your friend gets half of it. §During the exchange, he refers you to an obscure webChat \
where some similar issues to yours are being discussed. §You thank your friend for nothing and start pasting every line of code \
from the forum until one of them sticks! §Lucky for you, those coders are geniuses and the 'meanError' seems to have disappeared ... for the moment. \
§Hallelujah!! §You praise the coding community and swear to your future self that you will one day take the time to understand that pasted code ...§\
§§Touch ME to celebrate and do a little dance ...$",
    "call_friend_not": "§Nobody picks up ... §What?? Today of all days!§Pfffffff! You decide to leave messages all over your social apps ...§\
Press THIS APP to check your messages.$§§Nothing. Time passes ... CHECK again$§I guess it's just one of those days, buddy ...§\
Well then, are you going to [WASTE] the whole day waiting?§... or will you [TRY SOMETHING ELSE]?",
 #CHATGPT------------------------------------   
    "chatgpt": "(Press ANYWHERE and may the omnipotent AI one day rule the World!)$§\
After a couple of tweaks to the prompt, the Truth appears before your eyes: §Pure Code§ Perfect: \
devoid of unuseful console loggings, full of //#Comments and generic variable names. §The code is undoubtedly clean and, once pasted, runs smooth like butter. \
§Smart move. Just don't tell anyone what you've done and earn yourself some time to spend on more entertaining stuff! \
§Life doesn't have to be that hard, right? §So, will you ever [CODE] again, §[QUIT] this nonsensical absurdity of a mini game, §or check updates \
on your coder [PROFILE]?",
    "chatgpt_not": "(Press ANYWHERE and may the omnipotent AI one day rule the World!)$§\
Oops, weird answer. Let's formulate that query more adequately$§Nope! Doesn't work!§The pasted code creates more \
issues than it solves.§Is that it? Have you reached 'Chat's endpoint?§§Touch this SCREEN with the full weight of what that would mean for humanity ...$\
§You feel incredible for 5 seconds; then you realize how much this failure just underscores your inability to expose your coding issues to a more efficient being.§\
And, by the way, that 'meanError' hasn't been solved yet!§\
§How about something more tangible? A coder [FRIEND] or [COLLEAGUE]?§A rubber [DUCK] or a search on [GOOGLE]?§\
Getting some [SLEEP] or snacks in the [KITCHEN]?",
 #FRUSTRATION--------------------------------------   
    "frustration": "HOOOOOOLLLY COW!!! Computers are so incredibly [AUTISTIC]! §You realize at this instant how much you were NOT \
made to work in a mental institution ...§but you might become a patient if you let all this anger control you! \
§You take a second to contemplate the issue: do you decide to come [BACK] and evaluate this situation calmly, §or turn to \
the [DARK] side and express some of that accumulated tension physically?",
    "dark": "Something's got to give and various options are rapidly presenting themselves: §you can [SCREAM] in a pillow, §let out a very long and very loud [F-WORD], \
[SLAP] something on the desk §or just [PUNCH] that wall with all you've got ...§->",
    "pillow": "(HERE, scream into that pillow and cry it out a little ...)$§After this mini crisis episode, you go and refresh your face in the bathroom. §Once the mirror-check \
reflects your normal '[OK]' face again, you come back to your post, take a deep breath and start to [CODE] again ...§->",
    "curse_intro": "(Fffffffff......)$",
    "cursing": "§You breathe in all the air your lungs can admit and let out a magnificent angry FUUUUUUUUUUUU#%!!!$§WAouuuuuh that felt good! §Sometimes, cursing is all you've got ...§\
For now, you're '[OK]'. (Are you? Let us know if you had [ENOUGH]?) §Also, you can't shake the feeling that \
you might have been noticed by someone else, and that makes you want to curse even more. §Will you risk another very loud '[FUUU]'??",
    "cursing_success": " §  !!! FU%**😤§§   FU*^&#**#🤬§§   FUuuuuuuuuuUUUU*%#*#^#%🤯   !!!§§Double down with [FUUU] or feel [BETTER] now?",
    "punch": "You turn to that ugly wall next to the desk and hit it with your right fist. §AOUCH! ... §Damn, \
you have hit precisely where the supporting beam was! §Your hand hurts a little and the wall is somehow mocking you. \
§What is this unfortunate experience teaching you? §That you need to '[CALM DOWN]'? §... or go the toolbox, get the [HAMMER] and bring that \
stupid wall down?",
    "hammer_intro": "You grab the hammer with both hands and HIT as hard as you can ...$§KAAABOUUUUUMMMMM, KRRAAAKKK, schling schlingg ...$",
    "hammer_success": "§The wall still stands but it's getting weaker. Any moment now ...§Go full Thor with the [HAMMER] this time, explore more of the [DARK] side?§... or are you feeling [BETTER] now?",
    "slap_intro": "You raise your hand and HIT the table in frustration ...$§SHHLLPPLAAAAKKK!!!$",
    "slap_success": "§... silence ...§§Ouf! You just realized that you could have hit some sensitive equipment. \
(Maybe not do that again?)§[SLAP] harder, explore more of your [DARK] side?§ ... Or come [BACK] to [CODING]?",
    "slap endgame": "§OUch!!! §The slapping went uncontrolled and your laptop gets a big hit. §Screen of Death and broken glass, \
you are also bleeding at the wrist. §What a mess!!! §§Seriously?? This couldn't have gone worse. \
§You just have been labeled 'dangerous' to all synthetic life. §This mini game is booting you out as to avoid further material destruction. §Good luck with your temper issues Pal!§@",
    "angry endgame": "§With so much noise, someone has called the autorities on you. §You get a serious warning and find yourself in such a state of \
anger and despair that you are rendered inoperable. §You need to CALM DOWN! Seriously. \
§This mini game is booting you out as to avoid further material and/or psychic destruction. §Have a nice Life, Buddy!§@",
    "autism": "--Autism, also called autism spectrum disorder (ASD) or autism spectrum condition (ASC), is a neurodevelopmental disorder \
marked by restricted and repetitive patterns of behavior and deficits in reciprocal social communication. Other common signs include perseverative \
interests, stereotypic body movements (stimming), rigid routines, hyper- or hyporeactivity to sensory input, and difficulty with social interaction \
and verbal and nonverbal communication.-- §(This game will continue when you touch the following word: -> '[BACK]' <-)",
 #STUDY-----------------------------------------   
    "study": "Zen as a bonsai, you turn to research mode, grab your notes and try not to deviate from the path too much.§Time passes ...$\
more time passes ...§$Although you feel like you are getting smarter by the minute, §dinner time approaches \
and you are still nowhere close to resolving your coding issues ...§\
You take a couple of minutes to ponder your options: §you can always let it go and [SLEEP] on it, \
see what tomorrow brings. §You can also [OBSESS] and stay on course until you make the code work, §or \
look inward and see if you are not, in fact, building up some kind of [FRUSTRATION].",
    "obsess_intro": "OK, you got this. §Knife between your teeth you try to make it work using the sheer power of your WILL.$",
    "success": "§Hey! It's functioning! You're not yet sure exactly why, but it runs. Flawlessly! §WOW! Impressive.\
§You do a little dance ... and just between us, you know it's passed 3 a.m., right? \
§Oh! And did you miss that call from your mother? §You will probably be coding in bed too. Good luck sleeping! \
§§[START] again because you are a maniac? §Or check updates on your coder [PROFILE] together?",
 #SLEEP-----------------------------------   
    "sleep_txt": "Time to get your Mojo back, meditate, and experience the cycle of life again. §Breathing in and out. \
§This is how the experienced thinker acts: trusting one's brain to classify all the data during its 'reboot phase' and eventually reveal the missing links ...§\
    Open your EYES to wake up.$",
    "nap_success": "§What a difference a power nap makes! §You haven't touched the keyboard and yet, you are already \
formulating solutions smiling from one ear to the other. §Your refreshed self is winning, the reset bears its fruits. §You feel wiser and a little more proficient at coding. How about that?\
§Hopefully, it will work [NEXT TIME]. §Or maybe you would like to check updates on your coder [PROFILE]?",
 #ABANDON------------------------------   
    "abandon": "You are failing and you know it. There must be a simple explanation, but it is out of reach for the moment. \
§Time to lick your wounds, admit defeat, and gather your strength for the next fight. §§Another day, another code to write ... What will you do? \
§[START AGAIN], meditate on your coder [PROFILE] §or just [QUIT]?",
#TODO---------------------------------
    "todo": "'To do', get it?§([BACK]?)"
}

mobile_analisis ={
    "zen":"Your definition of being Zen is borderline between 'My body is a Temple' and 'fulfilling every little \
bodily impulse of mine'. §As Bobby said: it is your prerogative. And after all, we don't want you complaining, or \
stressed, unhappy, sick, hungry ...§It's just not good for business! §However, you also need a roof over your head. \
Have you done any work today?§§[EXIT] or [START] again?",
    "angry":"Terrible! Intimidating. §You're a constant menace to colleagues and any sensitive electrical devices around you \
when you are coding. §Anger issues? §We all have them, especially when driving during rush hour. §Someday, you will realize that \
we are all angry inside. Some are just better at managing/hiding it, that's all. §Now, careful next time you spin out of \
control: you might open the cage for an angrier beast ... §and/or just get a bad rep!§§[EXIT] or [START] again?",
    "smart":"It is not enough to have the best bike, you need to maintain and tune it to your \
preferences. §Well, my friend, that bike is your brain and you are very aware of it. §There's nothing we can tell you here \
that you don't already know. §Keep on making the right decisions and soon you will see them mortals, miles away on your \
rearview mirror.§§[EXIT] or [START] again?",
    "obsessed":"You are definitely very confident in your own capacities. §But, you end up sooooo tired, soooo exhausted ...\
and after a while, so does everyone around you. §Not sure you can keep this up for long. How about tomorrow? \
§It kind of begs the question: §Wouldn't it be more productive to take a breather sometimes? Fill up the tank?§§[EXIT] or [START] again?",
    "dependent": "Asking for help is fine and respecting deadlines is fundamental. Good point. §Hopefully, you are aware that \
abusing the people around you is not a viable carreer plan. §Unless your only friend is an AI on the web and fellow humans start avoiding your calls, you should be fine.§ \
Oh! And also, NEVER ask yourself: How's my coding going? Any notable progress lately?§§[EXIT] or [START] again?",
}