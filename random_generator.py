import random
import time

operator = ["*","-","+"]
min_operand = 3
max_operand = 15
Total_problem = 10
def generator_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator1 = random.choice(operator)
    expr = str(left)+  " " + operator1 + " " + str(right)
    answer= eval(expr)
    return expr,answer

wrong = 0
input("press enter to start!")
print("-----------------------")
 
start_time = time.time()
for i in range(Total_problem):
    expr,answer =   generator_problem()
    while True:
        guess=input("problem #" + str(i + 1) + ":" + expr + " = " )
        if guess == str(answer):
                break
        else:
              wrong += 1
end_time = time.time()
total_time = round(end_time - start_time,2)

print("----------------")
print("nice work! you finished in", total_time, "second" + ("s" if total_time != 1 else "") + "!")






































    