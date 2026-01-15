import time
import random
import csv

name= input("Input ur name : ")
print("Loading...")
time.sleep(0.5)

def init():
    with open('./resource/word_list.csv','rt',encoding='UTF-8') as f:
        crs=csv.DictReader(f)
        dap=random.choice(list(crs))        
        return dap
     
dap=init()        

word=''
turn=10

def exemWord(word):
    rst=''
    for i in dap['Name']:
        if i in word:
            rst+=i
        else:
            rst+='_'
    return rst

# (exemWord('asdf'))

# 턴이 유효하면
# 입력받고
# 
while turn > 0:
    print(turn,'Remaind')
    word+=input("Guess words: ") 
    # print(word)
    if exemWord(word) == dap['Name']:        
        print('-'*100)
        print('congraturation')
        print('Answer is',dap['Name'])
        print('-'*100)
        break
    else:
        print('>'*10,exemWord(word))
        turn -= 1

