# game_data.py

scene_office = {
    "description": f"""
    {
    """
       _,-._
      / \_/ \
      >-(_)-<
      \_/ \_/
         `-'
    """
    }

    Rain lashes against the grimy windows of your office...
    You're Anya, a private investigator in the magical city of Veiled City.
    Your desk is cluttered with case files, and the air smells of stale coffee.
    """,
    "interactive_elements": [
        {
            "name": "desk",
            "actions": ["examine", "search"],
            "description": "Your trusty desk, piled high with case files and overflowing ashtrays."
        },
        {
            "name": "whiskey bottle",
            "actions": ["take a swig", "ignore"],
            "description": "A half-empty bottle of cheap whiskey sits precariously on a stack of old newspapers."
        },
        {
            "name": "case files",
            "actions": ["read", "ignore"],
            "description": "A mountain of case files, each a testament to the bizarre and dangerous underbelly of Veiled City."
        },
        {
            "name": "window",
            "actions": ["look out", "ignore"],
            "description": "A grimy window offering a glimpse into the rain-swept streets below."
        },
        {
            "name": "old gramophone",
            "actions": ["examine", "play"],
            "description": "A vintage gramophone sits in the corner, collecting dust. A single record rests on the turntable."
        },
        {
            "name": "your pockets",
            "actions": ["check"],
            "description": "You instinctively pat your pockets, feeling for anything useful."
        }
    ],
    "events": [
        {
            "trigger": "examine desk",
            "action": """print('''You find a crumpled cigarette butt with lipstick stains - a reminder of your last client, 
a succubus with a gambling problem.  There's also a half-eaten takeout container from that 
questionable goblin diner down the street. The food still smells vaguely of sulfur and despair.'''); anya.clues.append('cigarette butt')"""
        }, 
        {
            "trigger": "search desk",  # Added this event
            "action": """print('''You rummage through the drawers, pushing aside old receipts, crumpled notes, and a dried 
fairy wing. Finally, your fingers brush against something cold and metallic. You pull out a dusty box of enchanted bullets.  
Might come in handy when dealing with creatures that don't respond well to reason.'''); anya.clues.append('enchanted bullets')"""
        },
                {
            "trigger": "take a swig",  # Added this event
            "action": """anya.update_sync('charisma', -1); print('''You grimace as the cheap whiskey burns your throat.  Maybe not the best choice for this early in the morning... 
or maybe it is, considering the day you're likely to have.''')"""
        },
                {
            "trigger": "ignore whiskey bottle",  # Added this event
            "action": "print('You decide to leave the whiskey for now.  Perhaps later...')"
        },
        {
            "trigger": "read case files",  # Added this event
            "action": """anya.update_sync('intelligence', 1); print('''You skim through the files, each one a bizarre tale 
of magic, mayhem, and betrayal. A missing imp, a stolen grimoire, a werewolf divorce... the usual Veiled City chaos. You can't 
help but feel a sense of grim satisfaction knowing you're the one who brings a semblance of order to this madness.''')"""
        },
        {
            "trigger": "ignore case files",  # Added this event
            "action": "print('You glance at the towering stack of case files and decide to tackle them later. There's always another mystery brewing in Veiled City.')"
        },
        {
            "trigger": "look out window",
            "action": """print('''
        .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
''')
print('The city stretches out before you, a labyrinth of neon-lit streets and towering buildings that disappear into the haze. Rain splatters against the glass, blurring the lights and casting a shimmering sheen over the bustling sidewalks.')  # Added description
"""
        },
        {
            "trigger": "ignore window",  # Added this event
            "action": "print('The rain-streaked window doesn\'t offer much of a view. You turn your attention back to the cluttered office.')"
        },
    ],
    "exits": [{
        "direction": "out",
        "destination": "scene_street"
    }],
}

# ... (rest of the game data)