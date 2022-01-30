from os import stat


f = open("1.txt", "r")
num = int(f.readline())
# n, l (testcases)

def file_to_lst(file):
    lst = []
    for i in file:
        lst.append(i)
    print(lst)
    return lst

def lst_to_testcases(lst):
    index = 0
    final = []
    while index != len(lst):
        n = int(lst[index][0])
        l = int(lst[index][2])
        tests = []
        for i in range(n):
            index +=1
            strr = lst[index][:-1]
            tests.append(strr)
        final.append(((n, l), tests))
        index +=1
    return final

lst = file_to_lst(f)
final = lst_to_testcases(lst)

# ((n, l), tests)

def states(tests):
    # [1100, 1010]
    states_lst = []
    dictt = {}
    for i in range(len(tests[0])):
        dictt[i] = ''
    for i in range(len(tests)):
        for j in range(len(tests[i])):
            dictt[j]+=tests[i][j]
    for i in dictt.keys():
        states_lst.append(dictt[i])
    return states_lst

def filter_similar_states(states_lst):
    new_lst = []
    cols = []
    count_lst = []
    count = -1
    for i in states_lst:
        if i not in cols:
            new_lst.append(i)
            cols.append(i)
            count +=1
            count_lst.append(count+1)
        else:
            ind = cols.index(i)
            count_lst.append(ind+1)
    # print(cols)

    return len(new_lst), count_lst


def output(f, st, temp):
    strr = ''
    for i in temp:
       strr += str(i) + ' '
    f.write(str(st)+"\n")
    f.write(strr+"\n")
    return f
f = open("f1.txt", 'x')
f = open("f1.txt", 'w')
save = []
for i in final:
    save.append(states(i[1]))
count = 0
final_states = []
for i in save:
    st, temp = filter_similar_states(i)
    print(st, " " ,temp)
    f = output(f, st, temp)

f.close()

