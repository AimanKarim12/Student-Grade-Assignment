#STUDENT GRADE ASSIGNMENT'

#LIST OF GRADES
import random 
grades = []
for n in range(34):
    grades.append(random.randint(1, 100))

#VARIABLES
sumofgrades = sum(grades)
lenofgrades = len(grades)
avg = sumofgrades/lenofgrades

#LOOP 
loop = True
while loop: 

    #PRINT MAIN MENU
    print("MAIN MENU")
    print("1. Display All Grades")
    print("2. Display Honors")
    print("3. Stats")
    print("4. Randomize Grades")
    print("5. Exit")

    #Menu Selection From User
    select = input ("Enter Selection (1-5): ")

    #Selection Results 

    #First Selection 
    if select == "1":
        print("ALL GRADES: ")
        print(*grades, sep = "% \n")

    #Second Selection 
    elif select == "2":
         for n in grades:
            if n >= 80:
                print(str(n) + "%")
            
    #Third Selection    
    elif select == "3":
        print("STATS: ")
        print("LOWEST GRADE: ", min(grades),"%")
        print("AVERAGE GRADE: ",avg, "%")
        print("HIGHEST GRADE :", max(grades),"%")

    #Fourth Selection
    elif select == "4":
        print ("RANDOMIZE GRADES")
        grades = []
        for n in range(35):
         grades.append(random.randint(1, 100))
        print(*grades, sep = "% \n")
        print ("NEW GRADES HAVE BEEN COMFIRMED")

    #Fifth Selection
    elif select == "5":
        print ("EXIT")
        loop = False