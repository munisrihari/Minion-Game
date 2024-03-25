def minion_game(string):
    print("your word is : ",string)
    player1,scores=[],0
    payer2,score=[],0
    owels="AEIOUaeiou"
    stop="//"
    print("if you stop giving substrings please enter: //")
    player1=input("enter first player name : ")
    def player_1():
        nonlocal scores
        while True: 
            n=input("enter only consonant substrings : ")
            if n == stop:
                break
            else:
                if not n[0] in owels:
                    if n in string:
                        if n == n[::-1]:
                            if len(n)>2:
                                subs=""
                                pali=string[string.index(n[0]):string.rindex(n[0])+1:]
                                for i in range(len(pali)):
                                    if n == subs:
                                        scores+=1
                                        subs=pali[i-1]+pali[i]
                                    else:
                                        subs+=pali[i]
                                if n == subs:
                                    scores+=1
                            else:
                                scores+=string.count(n)
                        else:
                            scores+=string.count(n)
                    else:
                        print("only enter characters in given word !")
                else:
                    print("please enter consonants only ! ")
    player_1()
    player2=input("enter second player name : ")
    def player_2():
        nonlocal score
        while True: 
            n=input("enter owel sub strings :  ")
            if n == stop:
                break
            else:
                if n[0] in owels:
                    if n in string:
                        if n == n[::-1]:
                            if len(n)>2:
                                subs=""
                                pali=string[string.index(n[0]):string.rindex(n[0])+1:]
                                for i in range(len(pali)):
                                    if n == subs:
                                        score+=1
                                        subs=pali[(i-1)]+pali[i]
                                    else:
                                        subs+=pali[i]
                                if n == subs:
                                    score+=1
                            else:
                                score+=string.count(n)
                        else:
                            score+=string.count(n)
                    else:
                        print("only enter characters in given word !")
                else:
                    print("please enter owels only ! ")    
                    
                
                            
    player_2()
    print(player1,"score is :",scores,",",player2,"score is :",score)
    print((player1+" is win") if scores > score else (player2+" is win"))
minion_game(input("enter which word you are taking : "))
