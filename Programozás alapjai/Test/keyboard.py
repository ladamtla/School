import keyboard


def on_key_event(e):
    if e.name == 'up':
        print('Fel nyíl lenyomva')
        # Ide írd be azt a kódot, amit a fel nyíl lenyomására akarsz végrehajtani
    elif e.name == 'down':
        print('Le nyíl lenyomva')
        # Ide írd be azt a kódot, amit a le nyíl lenyomására akarsz végrehajtani
    elif e.name == 'left':
        print('Balra nyíl lenyomva')
        # Ide írd be azt a kódot, amit a balra nyíl lenyomására akarsz végrehajtani
    elif e.name == 'right':

        print('Jobbra nyíl lenyomva')
        # Ide írd be azt a kódot, amit a jobbra nyíl lenyomására akarsz végrehajtani


keyboard.hook(on_key_event)
keyboard.wait('esc')  # Vár, amíg a felhasználó megnyomja a "Esc" billentyűt, majd kilép
