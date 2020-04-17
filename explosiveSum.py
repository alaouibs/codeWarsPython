visited = {}
visited[1] = 1

import math
def exp_sum(number):
    if number < 0: return 0
    elif number == 0 or number == 1: return 1
    else:
        return int(sum([math.pow(-1,k - 1) * exp_sum(number - k*(3*k-1)/2) 
                  + math.pow(-1,k + 1) * exp_sum(number - k*(3*k+1)/2)  
                                       for k in range(1, number + 1)]))
print(exp_sum(10))