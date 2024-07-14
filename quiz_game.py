print("welcome to my computer quiz!")

playing =input("do you want to play?")
score=0
if playing != "yes":
    quit()

print("okay! let's play :)")

answer = input("what does gpu stand for ?")
if answer == "graphics processing unit":
        print('correct!')
        score += 1
else:
    print("incorrect!")


answer = input("what does ram stand for ?")
if answer == "randam access memory":
        print('correct!')
        score += 1

else:
    print("incorrect!")


answer = input("what does cpu stand for ?")
if answer == "central processing unit":
        print('correct!')
        score += 1

else:
    print("incorrect!")


answer = input("what does rom  stand for ?")
if answer == "read only memory":
        print('correct!')
        score += 1 
else:
    print("incorrect!")


answer = input("Who is known as the Father of the Nation in India?")
if answer == "Mahatma Gandhi":
        print('correct!')
        score += 1
else:
    print("incorrect!")

answer = input("Which planet is known as the Red Planet?")
if answer == "Mars":
         print("correct")
         score += 1
else:
    print("incorrect'") 

answer = input(" What is the chemical symbol for water?")
if answer == "H2o":
        print("correct")
        score += 1
else:
    print("incorrect")

print("you got" + str (score) + "question correct")    
print("you got" + str ((score/7)*100) + "%.") 


 