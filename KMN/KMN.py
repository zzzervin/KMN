from random import*

player1=[]
win1=[]
lose1=[]
    
draw=[]

player2=[]
win2=[]
lose2=[]

playerB=[]
winB=[]
loseB=[]


while 1:
    try:
        name=[""]
        KNB=["k","n","b","yes"]
        start=["start","top","bot"]
        S=str(input("(start) plays, (top) players or (bot) :").lower())
        ST=start.index(S)
    
        p1w=0
        p2w=0
        p1l=0
        p2l=0
        pd=0
        pbd=0
        pbl=0
        pbw=0
        if ST==0:
            while 1:
                try:
                    print("To finish the game Write (Yes)")
                    print("Вы можете выбрать:Камень-k,Ножницы и Бумагу-b")
                    a=str(input("player1>>>").lower())
                    m=KNB.index(a)
                    for i in range(30):
                            print()
                    print("To finish the game Write (Yes)")
                    print("Вы можете выбрать:Камень-k,Ножницы и Бумагу-b")
                    a2=str(input("player2>>>").lower())
                    m2=KNB.index(a2)
   
            
                    if m==3 and m2==3:
                        player1.append(input("your name player1"))
                        player2.append(input("your name player2"))
                        win1.append(p1w)
                        lose1.append(p1l)
                        win2.append(p2w)
                        lose2.append(p2l)
                        draw.append(pd)

                        break
                    elif m==m2 :
                        print()
                        print("draw")
                        pd+=1
                    elif m==2 and m2==0 or m==0 and m2==1 or m==1 and m2==2 :
                        print()
                        print("player1 win")
                        p1w=+1
                        p2l+=1                        
                        print()
                        
                    else:
                        print()
                        print("player2 win")
                        p2w=+1
                        p1l+=1                  
                        print()
                        
                except ValueError:
                    print("Oops somethin goes wrong=)")
        elif ST==1:
            S=str(input("(top) 2 plays or (bot) :"))
            ST=start.index(S)
            if ST==1 :
                pt1=str(input("player name>>>"))
                p1=player1.index(pt1)           
                print("player1 ","name ",player1[p1],"win ",win1[p1],"lose ",lose1[p1],"draw",draw[p1])           
                print("player2 ","name ",player2[p1],"win ",win2[p1],"lose ",lose2[p1],"draw",draw[p1])   
                                 
            elif ST==2 :
                pt=str(input("plaer>>>"))

                p1=playerB.index(pt)
                print(p1)
                print("player1","name ",playerB[p1],"win ",winB[p1],"lose ",loseB[p1],"draw",draw[p1])
            


        elif ST==2:
                print("Вы можете выбрать:Камень-k,Ножницы и Бумагу-b")  
                print()
                while 1:

                    print()
                    a=str(input("player1>>>").lower())
                    m=KNB.index(a)
                    print()
                    BOT=randint(0,2)
                    print("BOT кидает:",KNB[BOT])
                    print()
                    if m==BOT :
                        print("ничья")
                        pbd+=1
                        print("To finish the game Write (Yes)")
                    elif m==2 and BOT==0 or m==0 and BOT==1 or m==1 and BOT==2 :
                        print("player1 win")
                        print()
                        pbw=+1
                        print("To finish the game Write (Yes)")
                    elif m==3:
                        playerB.append(input("your name player1"))
                        winB.append(pbw)
                        loseB.append(pbl)
                        draw.append(pbd)
                        break
                        print()
                    else:
                        print("BOT win")
                        pbl+=1
                        print("To finish the game Write (Yes)")
    except ValueError:
                print("Oops somethin goes wrong=)")
