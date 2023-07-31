# Yvonne Aime
# COP2500
# Final Exam -  Review

import random

# Number 2 COP2500 Fall 2022
def nickname(name):
    n = name[0:-2]
    if(n[-1]=="k"): # -1 counting from right to left
        return n + "a"
    else: 
        return n + "ster"

# Number 3 COP2500 Fall 2022
results = {}
for i in range(14): # Due to the amount of games
    N = input("Name")
    points = int(input("Points?"))
    results[N] = points

# Number 1 COP2500 Spring 2022
def roller(N):
    r_list = [] 
    for i in range(N):
        die1 = random.int(1,8)
        die2 = random.int(1,8)
        total = die1 + die2
        r_list.append(total)
    return r_list

# Number 2 COP2500 Spring 2022
def score(nums):
    total = 0 
    for i in range(len(nums)):
        if(nums[i] > 0):
            total += nums[i]
    return total 

# Number 3 COP2500 Spring 2022
def merge_players(names, scores):
    ans = {}
    for i in range(len(names)):
        key = names[i]
        ans[key] = scores[i]
    return ans

# Number 4 COP2500 Spring 2022
def question_4(w1, w2, N):
    w1 = [0:N] # 0 - n 
    w2 = [N:]
    com = w1 + w2
    return com

# Number 5 COP2500 Spring 2022
def question_5(n_dict):
    ans = []
    for key in n_dict:
       ans.append(key[0])
    return ans 
