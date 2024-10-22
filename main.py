from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import random
from game_data import situations, solutions, analisis

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# Global variables to hold the game state
current_situation = 'start'
profile_zen = 0
profile_angry = 0
profile_smart = 0
profile_obsess = 0
profile_dependent = 0

# Functions from the original game
def profiling():
    global current_situation
    profiles = {'zen': profile_zen, 'angry': profile_angry, "smart": profile_smart, 'obsessed': profile_obsess, 'dependent': profile_dependent}
    winner = max(profiles, key=profiles.get)
    current_situation = 'profile'
    return analisis[winner]

def dice_throw(per):
    percentage = random.random() * 100
    return percentage <= per

def effort_noise():
    effort = ["Arrrrghh!!$", "Pfffff!$", "Mmmmmmmhhhhh!$", "Let's GO!$", "C'mon buddy!$", "Jeeeeeeeez!$", "Oummmpppffff!$",\
               "(You try another A.I. study sounds list...)$", "Sssslurrrp (You take a sip from a now very cold tea that was made agess ago)$",\
              "More Caffeine!!!$", "Hhhmmmmfff! (You shake your legs to bring back the normal flow of blood)$"]
    res = random.choice(effort)
    print(res)
    return res

def obsession():
    global current_situation
    if dice_throw(5):
        current_situation = 'success'
        return {"situation": effort_noise() + situations[current_situation]}
    else:
        current_situation = 'obsess'
        return {"situation": effort_noise() + "Still Nothing...Crap! continue Y / N ?§->"}


# Define other game actions like cursing, slap, hammer, explain similarly...

@app.get("/")
async def read_root():
        global current_situation, profile_zen, profile_angry, profile_smart, profile_obsess, profile_dependent
        current_situation = 'start'
        return {"message": """*Welcome*§
    (type your command)§->"""}

    # return {"message": """*Welcome to the 'A Coder's Rhapsody Game'*§
    # <.press a key.>$
    # A plausible situational and psychological analysis§
    # (Based on personal and shared experience)§
    # <..>$
    # Please type 'GET TO WORK' when you feel ready to start.§
    # (type 'HELP' in case you are blocked or in need of instructions)$"""}

@app.post("/command")
async def process_command(request: Request):
    global current_situation, profile_zen, profile_angry, profile_smart, profile_obsess, profile_dependent
    body = await request.json()
    command = body.get("command").lower()

    if command in solutions[current_situation]:
        current_situation = solutions[current_situation][command]
        print(current_situation)
        print("zen=", profile_zen)
        print("angry=", profile_angry)
        print("smart=", profile_smart)
        print("obsess=", profile_obsess)
        print("dependent=", profile_dependent)


        return {"situation": situations[current_situation]}

    elif command == "work":
        return {"situation": situations[current_situation]}
        
    elif command == "get to work":
        return {"situation": situations[current_situation]}
    
    elif command == "study":
        current_situation = 'study'
        profile_smart += 1
        return {"situation": situations["study"]}
    
    elif command == "will":
        current_situation = 'obsess'
        profile_obsess += 2
        return obsession()
    
    elif command == "y":
        profile_obsess += 1
        return obsession()
    
    elif command == "n":
        profile_smart += 1
        current_situation = 'abandon'
        return {"situation": situations['abandon']}
    
    elif command == "sleep":
        profile_smart += 1
        if dice_throw(55):
            current_situation = 'nap_success'
            return {"situation": situations["sleep_txt"] + situations[current_situation]}
        else:
            current_situation = 'start'
            return {"situation": situations["sleep_txt"] + situations["start"]}
    
    elif command == "friend":
        profile_dependent += 1
        if dice_throw(20):
            current_situation = 'call_friend_not'
            return {"situation": situations['call_friend_not']}
        else:
            current_situation = 'start_next_day'
            return {"situation": situations['call_friend'] + situations['start_next_day']}
    
    elif command == "colleague":
        profile_dependent += 1
        if dice_throw(20):
            current_situation = 'call_colleague_not'
            return {"situation": situations['call_colleague_not']}
        else:
            current_situation = 'start_next_day'
            return {"situation": situations['call_colleague'] + situations['start_next_day']}

    elif command == "chatgpt":
        current_situation = 'chatgpt'
        profile_dependent += 2
        if dice_throw(15):
            current_situation = 'chatgpt_not'
            return {"situation": situations['chatgpt_not']}
        else:
            return {"situation": situations['chatgpt']}
        
    elif command == "explain":
        profile_smart += 1
        if dice_throw(40):
            current_situation = 'duck success'
            return {"situation": situations['duck_explain_txt'] + situations['duck success']}
        else:
            current_situation = 'duck_explain_no'
            return {"situation": situations['duck_explain_txt'] + situations['duck_explain_no']}

    elif command == "scream":
            profile_angry += 0.5
            current_situation = 'pillow'
            return {"situation": situations['pillow']}
    
    elif command == "f-word":
            profile_angry += 1
            current_situation = 'cursing'
            return {"situation": situations[current_situation]}
    
    elif command == "fuuu":
        profile_angry += 2
        if dice_throw(20):
            current_situation = 'endgame'
            return {"situation": situations['curse_intro'] + situations['angry endgame']}
        else:
            current_situation = 'cursing'
            return {"situation": situations['curse_intro'] + situations['cursing_success']}

    elif command == "fuck":
        profile_angry += 2
        if dice_throw(20):
            current_situation = 'endgame'
            return {"situation": situations['curse_intro'] + situations['angry endgame']}
        else:
            current_situation = 'cursing'
            return {"situation": situations['curse_intro'] + situations['cursing_success']}
        
    elif command == "slap":
        profile_angry += 1
        if dice_throw(20):
            current_situation = 'slap endgame'
            return {"situation": situations['slap_intro'] + situations['slap endgame']}
        else:
            current_situation = 'slap'
            return {"situation": situations['slap_intro'] + situations['slap_success']}

    elif command == "hammer":
        profile_angry += 3
        if dice_throw(50):
            current_situation = 'endgame'
            return {"situation": situations['hammer_intro'] + situations['angry endgame']}
        else:
            current_situation = 'punch'
            return {"situation": situations['hammer_intro'] + situations['hammer_success']}

    elif command == "chocolate":
            profile_zen += 1
            current_situation = 'kitchen'
            return {"situation": situations['chocolate_intro'] + situations['tea']}
    
    elif command == "tea":
            profile_zen += 1
            current_situation = 'kitchen'
            return {"situation": situations['tea_intro'] + situations['sandwich']}
    
    elif command == "sandwich":
            profile_zen += 2
            current_situation = 'kitchen'
            return {"situation": situations['sandwich_intro'] + situations['break']}
    
    elif command == "break":
            profile_zen += 2
            current_situation = 'kitchen'
            return {"situation": situations['break_intro'] + situations['after break']} 
    
    elif command == "profile":
        return {"situation": profiling()}
    
    elif command == "help":
        current_situation = 'help'
        return {"message": "Try typing the uppercase keywords in the text. (work, code, duck, fridge, stack overflow...) §\
                'exit' to end the game or 'profile' to see updates on your coder's profile!§\
                Now, try typing START or BACK§->"}
    
    elif command == "quit":
        return {"message": 'Of course... just what I thought!))'}
    
    elif command == "exit":
        return {"message": 'Thanks and hope to see you again soon!'}
    
    else:
        return {"message": "Say Whaaaat?§->"}

# Run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
