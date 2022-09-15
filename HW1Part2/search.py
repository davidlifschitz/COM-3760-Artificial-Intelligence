#search

import state
import frontier

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f[1],f[2]]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0
# a = search(4)
# print(a)
# print(len(a[0][1]))
# print()

answer = []
pushes = []
pops = []

def run_search(n):
    for i in range(1,100):
        res = search(n)
        print(res)
        answer.append(len(res[0][1]))
        pushes.append(res[1])
        pops.append(res[2])    
    print("for n of size: " + str(n) + ':\n')
    print(str(sum(answer)/len(answer)))
    print(str(sum(pushes)/len(pushes)))
    print(str(sum(pops)/len(pops)))

# run_search(2)
# run_search(3)
run_search(4)


#RESULTS

#FOR SIMPLE HEURISTIC



#FOR MANHATTAN HEURISTIC:
#for n of size: 4:
# Average length of moves: 15.87
# Average number of inserts; 6745.1
# Average number of removes: 3428.3


