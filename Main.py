from pynput import keyboard
from SRC.Global import GlobalState
from SRC.Phases import CurrentPhases

KeyCombo = [
    {keyboard.Key.shift, keyboard.KeyCode(char = "a")},
    {keyboard.Key.shift, keyboard.KeyCode(char = "A")},
    {keyboard.Key.alt_l, keyboard.KeyCode(char = "1")},
    {keyboard.KeyCode(char = "b")},
    {keyboard.KeyCode(char = "B")}
]
current = set()

def execute():
    print("Tecla Pulsada")

def on_press(key):
    if any({key in Combo for Combo in KeyCombo}):
        current.add(key)
        if any(all(k in current for k in Combo)for Combo in KeyCombo):
            execute()

def on_release(key):
    if any({key in Combo for Combo in KeyCombo}):
        current.remove(key)

while True:
    if GlobalState.GlobalPhase == CurrentPhases.MENU:
        print("<--KeyLogger-->\nExecute\t > 1\nSettings\t > 2")
        Option = input()
        if Option == "1":
            GlobalState.GlobalPhase = CurrentPhases.PLAY
        else:
            pass


    elif GlobalState.GlobalPhase == CurrentPhases.PLAY:
        with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
            listener.join()
            
