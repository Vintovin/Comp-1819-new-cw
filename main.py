from src.getTestData import *
from src.solution import solution
import time

d = get_data()
TestData = format_data(d)
matching = []

fastest_time = 0
fastest_index = 0

time_start = time.time()
#print(TestData[2].circle)
for  i, v in enumerate(TestData):
    #print(v.circle)
    start = time.time()
    results = solution(v)
    total_time = time.time()-start
    if fastest_time == 0:
        fastest_time = total_time
        fastest_index = i
    elif fastest_time > total_time:
        fastest_time = total_time
        fastest_index = i

    # print("-"*10)
    # print(f"Test Case {i} has {len(results)} intercepts")
    # for x, y in enumerate(results):
    #     print(f"intercept {x} | {y}")
    # print("-"*10)
    if len(results) != 0:
        matching.append(i)

t_time = time.time()-time_start

print(f"of {len(TestData)} cases there are {len(matching)} cases with solutions found")
print(f"the fastest completed case was case {fastest_index} at {fastest_time} seconds")
print(f"The whole program took {t_time} seconds to complete")

while True:
    m = input(f"do you want to check any test cases between 1 and {len(matching)-1}\nOr enter n to end\n")
    if m.lower() == "n":
        break

    n = int(m)-1
    result = solution(TestData[matching[n]])
    print(f"This was test case {matching[n]}")
    print(f"Test Case {matching[n]} has {len(result)} solutions")
    for i,v in enumerate(result):
        x,y = v
        print(f"{i+1} - x: {x} | y: {y}")
