import random, sys
liw = ["Bauer ", "Pferd ", "Läufer", "Turm  ", "Dame  ", "König "]
lib = ["Bauer ", "Pferd ", "Läufer", "Turm  ", "Dame  ", "König "]
turn = True

while True:
    result = []
    
    if turn == True:
        l = liw
        print("White Move: ")
    else: 
        l = lib
        print("Black Move: ")


    random.shuffle(l)
    result.append(l[0])
    result.append(l[1])
    result.append(l[2])

    print(" | ".join(result))
    

   
    if turn == True:
        l = lib
    else: 
        l = liw

    inp = "NO"

    while len(inp) >= 1 :
        inp = input("")
        if inp == "leng":
            print(len(l))
        elif inp == "listb":
            print(lib)
        elif inp == "listw":
            print(liw)
        elif inp == "b":
            l.remove('Bauer ')
        elif inp == "p":
            l.remove('Pferd ')
        elif inp == "l":
            l.remove('Läufer')
        elif inp == "t":
            l.remove('Turm  ')
        elif inp == "d":
            l.remove('Dame  ')
        elif inp == "D":
            l.append('Dame  ')
    

    if turn == True:
        lib = l
    else: 
        liw = l
     
    turn = not turn
