import keyboard

while True:
    if keyboard.read_key() == "a":
        print("A")
    
    if keyboard.read_key() == "b":
        print("B")
    if keyboard.read_key() == "esc":
        break
print("finalizado")