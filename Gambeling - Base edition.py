import random
import time
import math
money = 100
insert = 0
luck = 0
cashout = 0
winprize = 0
loan = 0
loanpayment = 0
loans = 0
fired = False
strikes = 0
def asciislots(a,b,c):
    up = [int(random.randint(0, 3)),int(random.randint(0, 3)),int(random.randint(0, 3))]
    mid = [a,b,c]
    dwn = [int(random.randint(0, 3)),int(random.randint(0, 3)),int(random.randint(0, 3))]
    row = [[[["  .--.  "," /    | "," |    / ","  '--'  "],["   /|   ","  /  |  "," /    | ","'------'"],
             [".------.","/      /","/      /","'------'"],["  |  /  ","   |/   ","   /|   ","  /  |  "]],
             
             [["    .   ","  /  ' /","  /   / ","    .   "],
             ["    /   "," /  /'  "," '  /   ","  |'  | "],
             ["  /  .  ","  /   / ","  '.  / "," |    ' "]]],
    
             [[["  .--.  "," /    \ "," \    / ","  '--'  "],["   /\   ","  /  \  "," /    \ ","'------'"],
              [".------.","|      |","|      |","'------'"],["  \  /  ","   \/   ","   /\   ","  /  \  "]],
              
              [["  .   | ","  ' | | "," | .  | "," | .  ' "],
              [" |      "," . |  | ","   |. ' ","  .'| . "],
              [" |   ' |"," ' ||  |","|  |' . ","'  |  ' "]]],
    
             [[["  .--.  "," |    \ "," \    | ","  '--'  "],["   |\   ","  |  \  "," |    \ ","'------'"],
              [".------.","\      \\","\      \\","'------'"],["  \  |  ","   \|   ","   |\   ","  |  \  "]],
              
              [["    | ' "," .      ","   \ .  ","   \  ' "],
              ["  |  '. ","    \  '","  . \ ' ","  \ .   "],
              [" |  |   "," \ '  \ ","  . \   ","\   \   "]]]]
    
    upmidrow = ["  / '   "," /  .   ","./ ' / "]
    creators = ["m /at \ě /j ,  n| ov/ á\ k ,\ p ,/ |e \tr , h /a, ,v \rl | a . nt"]
    dwnmidrow = ["    | ' ","  |  '. "," |  |   "]
    lm = lambda a,b: up[b] if a==0 else mid[b] if a==1 else dwn[b]
    st = lambda x,a,b,c: row[a][1][x%3][c] if x<((b+1)*3) else row[a][0][lm(a,b)][c]
    for x in range(0, 10):
        print(f'''


                                                           
                      ____________________________         
                _____/____________________________\____
            ___/_____/                            \_____\   
        ___/___/___________________               ____/_\\ 
       /___________________________\______    ___/____/  \\
      ||                           \______\__/___/       ||
     //                                   \\ /           ||
     ||    ____________________________    \\            ||  
     ||   /{st(x,0,0,0)}/{st(x,0,1,0)}/{st(x,0,2,0)}/ \    \\           ||  
    //   /{st(x,0,0,1)}/{st(x,0,1,1)}/{st(x,0,2,1)}/  |    ||           ||  
    ||  /{st(x,0,0,2)}/{st(x,0,1,2)}/{st(x,0,2,2)}/   |    ||           //  
    || |{st(x,0,0,3)}|{st(x,0,1,3)}|{st(x,0,2,3)}|    |    //          ||  
   //  /        /        /        /    |    ||          ||  
   || |{st(x,1,0,0)}|{st(x,1,1,0)}|{st(x,1,2,0)}|     |    ||          ||  
   || |{st(x,1,0,1)}|{st(x,1,1,1)}|{st(x,1,2,1)}|     |    ||          //  
   || |{st(x,1,0,2)}|{st(x,1,1,2)}|{st(x,1,2,2)}|     |   //          ||  
   || |{st(x,1,0,3)}|{st(x,1,1,3)}|{st(x,1,2,3)}|     |   ||          ||  
   //  \        \        \        \    |   ||          ||  
  ||   |{st(x,2,0,0)}|{st(x,2,1,0)}|{st(x,2,2,0)}|    |   ||          ||  
  ||    \{st(x,2,0,1)}\{st(x,2,1,1)}\{st(x,2,2,1)}\   |   ||          ||  
  ||     \{st(x,2,0,2)}\{st(x,2,1,2)}\{st(x,2,2,2)}\  |   ||          ||  
  //      \{st(x,2,0,3)}\{st(x,2,1,3)}\{st(x,2,2,3)}\ /   ||         / |   
 ||        ͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞    ||        / /    
 ||                                        || _____/__/      
 ||________________________________________||/_____/         
  \__________________________________________/                


                                                           
''')
        time.sleep(0.2)
    time.sleep(1)
input('''
████████████████████████████████████████████████████████████












        Calibrate the window size then press enter

















████████████████████████████████████████████████████████████
''')
input('''
████████████████████████████████████████████████████████████












        Enter "functions" to open functions list

















████████████████████████████████████████████████████████████
''')
input('''






 _      _______  _______     
| | /| / /  _/ |/ / __(_)    
| |/ |/ // //    /\ \_       
|__/|__/___/_/|_/___(_)      
                                         ___  ____
  .--.    .--.    .--.     ____  __ __  <  / / __/
 /    \  /    \  /    \   /___/  \ \ /  / / /__ \ 
 \    /  \    /  \    /  /___/  /_\_\  /_( )____/ 
  '--'    '--'    '--'                    |/___     
   /\       /\       /\      ____  __ __   |_  |    
  /  \     /  \     /  \    /___/  \ \ /  / __/     
 /    \   /    \   /    \  /___/  /_\_\  /____/     
'------' '------' '------'                  ____    
.------. .------. .------.   ____  __ __   |_  /    
|      | |      | |      |  /___/  \ \ /  _/_ <     
|      | |      | |      | /___/  /_\_\  /____/     
'------' '------' '------'
       




        


''')
def asciilist(x):
    global money
    global insert
    global winprize
    global loan
    global loanpayment
    asci = [f"""










   ____                 __                         
  /  _/__  ___ ___ ____/ /_                        
 _/ // _ \(_-</ -_) __/ __/                        
/___/_//_/___/\__/_/  \__/  __                     
 ___ ___ _  ___  __ _____  / /_                    
/ _ `/  ' \/ _ \/ // / _ \/ __/                    
\_,_/_/_/_/\___/\_,_/_//_/\__/                     
  __                           __   __       _ ___ 
 / /____      ___ ____ ___ _  / /  / /__    (_) _ \ 
/ __/ _ \    / _ `/ _ `/  ' \/ _ \/ / -_)  _ / // /
\__/\___/    \_, /\_,_/_/_/_/_.__/_/\__/  (_)____/ 
            /___/                                  

you have: {money}$










""",f"""









  ______              __            __      
 /_  __/__  ___      / /  _______  / /_____ 
  / / / _ \/ _ \    / _ \/ __/ _ \/  '_/ -_)
 /_/  \___/\___/   /_.__/_/  \___/_/\_\\\\__/









you have: {money}$









""",f"""









    __       __                       
   / /  ___ / /____     ___ ____      
  / /__/ -_) __(_-<    / _ `/ _ \     
 /____/\__/\__/___/    \_, /\___/     
                      /___/           
                    __   ___          
   ___ ____ ___ _  / /  / (_)__  ___ _
  / _ `/ _ `/  ' \/ _ \/ / / _ \/ _ `/
  \_, /\_,_/_/_/_/_.__/_/_/_//_/\_, / 
 /___/                         /___/  



you have: {money}$









""",f"""









   ___              __                  _ __  __
  / _ |_    __  ___/ /__ ____  ___ _   (_) /_/ /
 / __ | |/|/ / / _  / _ `/ _ \/ _ `/  / / __/_/ 
/_/ |_|__,__/  \_,_/\_,_/_//_/\_, /  /_/\__(_)  
                             /___/








you have: -{insert}$








                             
""",f"""









 ______              __            __         __      
/_  __/__  ___      / /  _______  / /_____   / /____  
 / / / _ \/ _ \    / _ \/ __/ _ \/  '_/ -_) / __/ _ \ 
/_/  \___/\___/   /_.__/_/  \___/_/\_\\\\__/  \__/\___/ 
         __                           _               
   ___  / /__ ___ __  ___ ____ ____ _(_)__            
  / _ \/ / _ `/ // / / _ `/ _ `/ _ `/ / _ \_          
 / .__/_/\_,_/\_, /  \_,_/\_, /\_,_/_/_//_( )         
/_/          /___/       /___/            |/          
            __            __                          
  ___ ____ / /_  ___ _   / /__  ___ ____     ___  ____
 / _ `/ -_) __/ / _ `/  / / _ \/ _ `/ _ \   / _ \/ __/
 \_, /\__/\__/  \_,_/  /_/\___/\_,_/_//_/   \___/_/   
/___/        __  __                                   
  ___ __ _  / /_/ /                                   
 (_-</  ' \/ __/ _ \_                                 
/___/_/_/_/\__/_//_(_)






""",f"""









        _        
  ___  (_)______ 
 / _ \/ / __/ -_)
/_//_/_/\__/\__/









you have: +{math.ceil(1.5*insert)}$










""",f"""









        _              __
  __ __(_)__  ___ ___ / /
 / // / / _ \/ -_) -_)_/ 
 \_, /_/ .__/\__/\__(_)  
/___/ /_/                









you have: +{math.ceil(2*insert)}$









""",f"""









       __             __                        ____
 ___  / /       ___  / /      __ _  __ __      /  _/
/ _ \/ _ \_    / _ \/ _ \    /  ' \/ // /     _/ /  
\___/_//_( )   \___/_//_/   /_/_/_/\_, ( )   /___/  
         |/__            ____     /___/|/           
 ___ _____/ /___ _____ _/ / /_ __  _    _____  ___  
/ _ `/ __/ __/ // / _ `/ / / // / | |/|/ / _ \/ _ \ 
\_,_/\__/\__/\_,_/\_,_/_/_/\_, /  |__,__/\___/_//_/ 
                          /___/





you have: +{math.ceil(3*insert)}$









""",f"""









 _      ____ _____ _________  __
| | /| / / // / _ /_  __/__ \/ /
| |/ |/ / _  / __ |/ /   /__/_/ 
|__/|__/_//_/_/ |_/_/   (_)(_)










you have: +{winprize}$









"""]
    return asci[x]
def startgambling():
    global money
    global asciilist
    global insert
    global luck
    global cashout
    global loan
    global loans
    global fired
    global loanpayment
    global strikes
    def reset():
        global loan
        global loans
        global loanpayment
        global fired
        global strikes
        global money
        loan = 0
        loans = 0
        loanpayment = 0
        fired = False
        strikes = 0
        money = 100
        return startgambling()
    def DaJob():
        global money
        global strikes
        global fired
        made = 0
        JobAmount = input("How many tasks shall boss trust you with?")
        JobInput = '0' + ''.join(filter(lambda x: x.isdigit(), JobAmount))
        for i in range(int(JobInput)):
            task = "".join(random.choices(["w", "a", "s", "d"], k=3))
            uwu = random.randint(1,500)
            if uwu == 1:
                task = "uwu"
            print("type: "+task)
            if input() == task:
                if task == "uwu":
                    money += 10
                    made += 10
                else:
                    money += 1
                    made += 1
            else:
                strikes += 1
                if strikes >= 10:
                    print("You useless piece of junk, can´t even handle your job. You are FIRED!")
                    time.sleep(1)
                    fired = True
                    return startgambling()
            if i == int(JobAmount)-1:
                print(f"made: {made}$")
                print(f"damages made: {strikes}")
                time.sleep(1)
                return startgambling()
        else:
            print("Insert number damit")
            DaJob()
    if money > 0:
        insert = 0
        xyz = input(asciilist(0))
        if xyz == "job":
            if fired == False:
                DaJob()
            else:
                print("You have been fired, no job for you ;)")
                time.sleep(1)
                return startgambling()
        if xyz == "reset":
            reset()
        if xyz == "damages":
            print(f"[{strikes}/10]")
            damagepayinsert = input("How much of damage you want to pay off? ")
            damagepay = '0' + ''.join(filter(lambda x: x.isdigit(), damagepayinsert))
            damagepay = int(damagepay)
            if damagepay <= 0:
                return startgambling()
            elif damagepay <= 10:
                if money >= damagepay * 10:
                    if strikes >= damagepay:
                        money -= damagepay * 10
                        strikes -= damagepay
                        print(f"Paid off {damagepay} damages")
                        time.sleep(1)
                        return startgambling()
                    else:
                        money -= strikes * 10
                        strikes -= strikes
                        print(f"Paid off {strikes} damages")
                        time.sleep(1)
                        return startgambling()
                print("You dont have enought money")
                time.sleep(1)
                return startgambling()
            elif damagepay > 10:
                if money >= 100:
                    if strikes == 10:
                        money -= 100
                        strikes -= 10
                        print("You paid off 10 damages")
                        time.sleep(1)
                        return startgambling()
                return startgambling()
        if xyz == "functions":
            print("job")
            print("loan")
            print("reset")
            print("damages")
            print("functions")
            time.sleep(5)
            return startgambling()
        if xyz == "loan":
            if loans <= 4:
                loanamount = input("How big of a loan you wish to get? ")
                if money <= 0:
                    if int(loanamount) > 20:
                        print("You don´t have enought money for this size of loan")
                        time.sleep(2)
                        return startgambling()
                if int(loanamount) / 10 > money:
                    print("You don´t have enought money for this size of loan")
                    time.sleep(2)
                    return startgambling()
                loan += math.ceil(int(loanamount) * 1.05)
                loanpayment = math.ceil(loan / 10)
                loans += 1
                money += int(loanamount)
                if money <= 0:
                    print(f"Still in depth of {money}")
                    time.sleep(2)
                    return startgambling()
                return startgambling()
            else:
                print("Way too many loans, get a job brokeass")
                time.sleep(2)
                return startgambling()
        insert = '0' + ''.join(filter(lambda x: x.isdigit(), xyz))
        insert = int(insert)
        if insert > money:
            print(asciilist(1))
            time.sleep(1)
            return startgambling()
        if insert == 0:
            return startgambling()
        print(asciilist(2))
        time.sleep(1)
        if luck+insert > 100:
            cashout += insert-(100-luck)
            luck = 100
        else:
            luck += insert
        randnum = random.randint(1, 1000)
        if int(500)>(randnum-luck/2) and int(500)<(randnum+luck/2):
            global winprize
            winprize = 20+math.ceil(luck/4+insert/3+cashout*(random.randint(5,15)/10))
            money += winprize
            asciislots(3,3,3)
            print(asciilist(8))
            luck = 0
            cashout = 0
            time.sleep(1)
            return startgambling()
        num1 = random.randint(1,3)*100
        num2 = random.randint(1,3)*10
        num3 = random.randint(1,3)
        num = num1+num2+num3
        win = "nil"
        asciislots(int((num1/100)-1),int((num2/10)-1),int(num3-1))
        if num == 111:
            win = insert * 1.5
            money += math.ceil(win)
            print(asciilist(5))
            time.sleep(1)
        elif num == 222:
            win =insert * 2
            money += math.ceil(win)
            print(asciilist(6))
            time.sleep(1)
        elif num == 333:
            win = insert * 3
            money += math.ceil(win)
            print(asciilist(7))
            time.sleep(1)
        else:
            money -= insert
            print(asciilist(3))
            time.sleep(1)
        print(money)
        if loan != 0:
            money -= loanpayment
            loan -= loanpayment
            if loan ==  0:
                loans = 0
    if money > 0:
        return startgambling()
    else:
        if loan != 0:
            money -= loan
            print(f"In depth of {money}") 
        print(asciilist(4))
        def thebrokeassfunction():
            global money
            global asciilist
            global insert
            global luck
            global cashout
            global loan
            global loans
            global fired
            global loanpayment
            inpp = 0
            inppp = 0
            while inpp != "reset" and inpp != "loan" and inpp != "job" and inpp != "functions":
                inpp = input()
            if inpp == "loan":
                if loans <= 4:
                    loanamount = input("How big of a loan you wish to get? (max 20) ")
                    if money <= 0:
                        if int(loanamount) > 20:
                            print("You don´t have enought money for this size of loan")
                            return thebrokeassfunction()
                    if int(loanamount) / 10 > money:
                        print("You don´t have enought money for this size of loan")
                        return thebrokeassfunction()
                    loan += math.ceil(int(loanamount) * 1.05)
                    loanpayment = math.ceil(loan / 10)
                    loans += 1
                    money += int(loanamount)
                    if money <= 0:
                        print(f"Still in depth of {money}")
                        time.sleep(2)
                        return thebrokeassfunction()
                    return startgambling()
                else:
                    print("Way too many loans, get a job brokeass")
                    return thebrokeassfunction()
            elif inpp == "job":
                if fired == False:
                    DaJob()
                else:
                    print("You have been fired, no job for you ;)")
                    return thebrokeassfunction()
            elif inpp == "functions":
                print("job")
                print("reset")
                print("damages")
                print("functions")
                return thebrokeassfunction()
            else:
                reset()
        thebrokeassfunction()
startgambling()
