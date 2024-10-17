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
    profiles = {'zen': profile_zen, 'angry': profile_angry, "smart": profile_smart, 'obsessed': profile_obsess, 'dependent': profile_dependent}
    winner = max(profiles, key=profiles.get)
    return analisis[winner]

def dice_throw(per):
    percentage = random.random() * 100
    return percentage <= per

def obsession():
    global current_situation
    if dice_throw(5):
        current_situation = 'success'
        return situations[current_situation]
    else:
        current_situation = 'obsess'
        return "Still Nothing...Crap! continue y / n ?"

def sleeping():
    global current_situation
    if dice_throw(55):
        current_situation = 'nap success'
        return situations[current_situation]
    else:
        current_situation = 'start'
        return situations["start"]

# Define other game actions like cursing, slap, hammer, explain similarly...

@app.get("/")
async def read_root():
    return {"message": "Welcome to the 'A Coder's Rhapsody Game'! Type your command to begin."}

@app.post("/command")
async def process_command(request: Request):
    global current_situation, profile_zen, profile_angry, profile_smart, profile_obsess, profile_dependent
    body = await request.json()
    command = body.get("command").lower()

    if command in solutions[current_situation]:
        current_situation = solutions[current_situation][command]
        return {"situation": situations[current_situation]}
    
    elif command == "get to work":
        return {"situation": situations[current_situation]}
    
    elif command == "study":
        current_situation = 'study'
        profile_smart += 1
        return {"situation": situations["study"], "additional_info": "Although you feel smarter, dinner time approaches..."}
    
    elif command == "obsess":
        current_situation = 'obsess'
        profile_obsess += 2
        return {"situation": obsession()}
    
    elif command == "y":
        profile_obsess += 1
        return {"situation": obsession()}
    
    elif command == "n":
        profile_smart += 1
        current_situation = 'abandon'
        return {"situation": situations['abandon']}
    
    # Handle more commands like friend, colleague, chatgpt, sleep, scream, f-word, slap, hammer, explain...
    
    elif command == "profile":
        return {"situation": profiling()}
    
    elif command == "help":
        return {"help": "Try typing keywords like: duck, fridge, stack overflow... 'exit' to end the game or 'profile' to check your profile!"}
    
    elif command == "quit":
        return {"message": '👿 Yeah, just what I thought 😈'}
    
    elif command == "exit":
        return {"message": 'Thanks and hope to see you soon!'}
    
    else:
        return {"message": "Say Whaaaat???🫣"}

# Run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
