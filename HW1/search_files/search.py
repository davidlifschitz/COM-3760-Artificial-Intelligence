#search

import state
import frontier

def search(n):
    s=state.create(n)
    # print("this is the stack" + str(s))
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f[1],f[4],f[5]]
        ns=state.get_next(s)
        #print(ns)
        for i in ns:
            frontier.insert(f,i)
            print("inserted")
    # print("total number of inserts: " + str(f[4]))
    # print("total number of removes: " + str(f[5]))

    return 0
answer = []
pushes = []
pops = []

def run_search(n):
    for i in range(1,100):
        res = search(n)
        answer.append(res[1])
        pushes.append(res[2])
        pops.append(res[3])    
    print("for n of size: " + str(n) + ':\n')
    print(str(sum(answer)/len(answer)))
    print(str(sum(pushes)/len(pushes)))
    print(str(sum(pops)/len(pops)))

# run_search(2)
# run_search(3)
run_search(4)

#Outputs from functions:
#   from run_search(2):
#       Average depth: 1.63
#       Average number pushed: 6.08
#       Average number popped: 5.04
#
#   from run_search(3):
#       Average depth: 4.04
#       Average number pushed: 881.29
#       Average number popped: 505.41
#   from run_search(4):
#   doesn't terminate after 3 minutes