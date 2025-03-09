import random
import csv

###FUNCTIONS#####
# Load quiz data from CSV using csv.reader###
def load_ques():
    global Sciques,Techques,Gkques,Spques,Mathsques,nSci,nTech,nGk,nSp,nMaths,ntotal,allmix,ques,dict_category    
    #variables
    Sciques=[]
    Techques=[]
    Gkques=[]
    Spques=[]
    Mathsques=[]
    nSci=0
    nTech=0
    nGk=0
    nSp=0
    nMaths=0
    ntotal=0
    dict_category={1:['Sci',nSci,Sciques],2:['Tech',nTech,Techques],3:['Gk',nGk,Gkques],4:['Sports',nSp,Spques],5:['Maths',nMaths,Mathsques]}

    
    with open("quiz_data.csv","r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
                category=row.pop(0)
                for i in range(1,6):
                    if category==dict_category[i][0]:
                        dict_category[i][2].append(row)
                        dict_category[i][1]+=1

    
    for i in dict_category:
        ntotal+=dict_category[i][1]
    allmix=Sciques+Gkques+Techques+Mathsques+Spques
    ques={1:Sciques,2:Techques,3:Gkques,4:Spques,5:Mathsques,6:allmix}

###########################
    
def score_result(score,n):
    try:
        per=(score/(n*10))*100
    except:
        per=0
    
    if per>=80 and per<=100:
        print('EXCELLENT performance ☺')
    elif per>=70:
         print('Bravo!!')
    elif per>=50:
         print('GREAT job!')
    elif per>=33:
         print('Well done!!')
    else:
         print('Better luck next time :)')
        
#DISPLAY MENU############

def display_menu():
    print('''

    ******************************
               QUIZ
    ******************************       
    1. Start
    2. add questions
    3. Exit

    ''')
##############################################

def starting_quiz():
    print('''

    ******************************
               QUIZ
    ******************************
    1. Science
    2. Technology
    3. GK
    4. Sports
    5. Maths
    6. All of the above
    7. Back

    ''')
#####################################################

def quiz(choice,n):
    score=0
    QList=ques[choice]
    random.shuffle(QList)
    for i in range(n):
        print('Question ',i+1)
        print(QList[i][0])
        print('1.',QList[i][1])
        print('2.',QList[i][2])
        print('3.',QList[i][3])
        print('4.',QList[i][4])
        
        ans=input('Enter your option:')
        if ans==QList[i][5]:
            print('Correct answer\n')
            score+=10
        else:
            print('Incorrect answer')
            print('Correct ans is:',QList[i][int(QList[i][5])],'\n')
        
    print('****************************')
    print ('Your score=',score,'Out of',n*10)
    score_result(score,n)
    print('****************************\n')
    input('press a key...')
    
###############
def add_ques():
    while True:
        file=open("quiz_data.csv",'a',newline='')
        ob=csv.writer(file)
        print('''
    1. Science
    2. Technology
    3. GK
    4. Sports
    5. Maths
    ''')
        ch=int(input('select category: '))
        c=dict_category[ch][0]
        q=input('enter ques:')
        Q1=input('enter option(1):')
        Q2=input('enter option(2):')
        Q3=input('enter option(3):')
        Q4=input('enter option(4):')
        a=input('enter correct option(1/2/3/4):')
        ob.writerow([c,q,Q1,Q2,Q3,Q4,a])
        file.close()

        ch=int(input('to enter more ques press 1: '))
        if ch!=1:
            break

#Main program

while True:
    try:
        load_ques()
        display_menu()
        ch = int(input("what you would like to do: "))
        if ch==1:
            while True:
                starting_quiz()
                choice = int(input("Select a category: "))
                if choice<6:
                    for i in range(1,6):
                        if choice==i:
                            print("Enter the number of questions for",dict_category[i][0],"category:( max-",dict_category[i][1],") ")
                            n=int(input())
                            quiz(choice,n)
            
                elif choice == 6:
                    print("Enter the number of questions:( max-",ntotal,") ")
                    n=int(input())
                    quiz(choice,n)
                elif choice == 7:
                    break
                else:
                    print('!!wrong choice entered...PLEASE! select from above given options only!!')
        elif ch==2:
            add_ques()
            print('question(s) added')
    
        elif ch==3:
            a=input('do you really want to exit(yes/no):')
            if a=='yes':
                print('''
    ********************************
               Thank You
    ********************************
''')
                break
            else:
                continue
        else:
            print('!!wrong choice entered...PLEASE! select from above given options only!!')
    except:
            print('!!!due to some ERROR quiz is restarted!!!')
