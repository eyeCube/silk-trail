'''
    ui.py
        console UI. Will be converted into GUI
'''

def get(message=None):
    if message:
        print(message)
    return input('> ')

def show(message):
    print(message)
    
def show_menu(items:dict):
    string = ''
    string += '~\n'
    for k,v in items.items():
        string += '    {}       {}\n'.format(k,v)
    string += '~'
    show(string)

# GUI -- draw an image representing game state
def draw(event, *args):
    if event=='travel':
        location = args[0]
        #location.name
        #location.region
        #location.terrain
        pass
    elif event=='settlement':
        location = args[0]
        #location.name
        #location.region
        #location.terrain
        pass
    elif event=='event_thief':
        terrain = args[0]
        pass
    elif event=='event_find':
        terrain = args[0]
        pass
    elif event=='event_character_contract':
        character = args[0]
        pass
    elif event=='event_character_ill':
        character = args[0]
        pass
    elif event=='event_character_critical':
        character = args[0]
        pass
    elif event=='event_character_death':
        character = args[0]
        cause = args[1]
        # temporary:
        ui.show("{} died of {}.".format(character.name, cause))
        pass


#show_menu({'t':'take', 'l':'leave',})
#get()
