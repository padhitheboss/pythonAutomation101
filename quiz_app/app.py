import csv
header = ['Name','ID','Score']

ques = open('questions.txt','r')
ans = open('answers.txt','r')
#for line in ques:
#    print (line)
#    ans = input('Enter Answer:')
questions = ques.read().split('\n')
answers = ans.read().split('\n')
qna = dict(zip(questions,answers))
ans.close()
ques.close()
score = 0
name = input("Enter Your Name: ")
id = input("Enter Your ID: ")
for qa in qna:
    print(qa)
    inp = input('Answer: ')
    if inp == qna[qa]:
        score+=1
print(f"Your score is {score} out of {len(qna)}")

with open('result.csv','a',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow([name,id,score])