#main program
import difficult
import easy
import csv
file = open("easy.csv",'r')
file1=open("difficult.csv",'r')

try:
    while True:
        print("""
1.EASY GAME
2.DIFFICULT GAME
3.VIEW PLAYERS AND SCORES
4.STOP
""")
        c=int(input("Enter your choice (1/2/3/4) :: "))
        if c==1:
            easy.easy()
        elif c==2:
            difficult.difficult()
        elif c==3:
            while True:
                try:
                    le=int(input("Enter 1 for easy and 2 for difficult :: "))
                    if le==1:
                        read=csv.reader(file)
                        for one in read:
                            print(one)
                        break
                    elif le ==2:
                        read=csv.reader(file1)
                        for one in read:
                            print(one)
                        break
                    else:
                        print("out of range")
                except ValueError:
                    print("something went wrong")
        elif c==4:
            break
        else:
            print("out of range")
except ValueError:
    print("try again")
                
            
            
