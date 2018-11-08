from pymongo import MongoClient
from pprint import pprint
import sys
client = MongoClient()
db = client.ds2
col = db.grades

def pagination():
    result = col.find({'sid':{'$gte':10,'$lte':19}},{'_id':0}).limit(10)
    for i in result:
        print(i)

def letter():
    
    for i in range(100):
        result_q = col.find({'sid':i, 'grades.type': 'quiz'}, {'_id':0,'grades.$':1})
        for j in result_q:
            a = j.values()
            for p in a:
                b = p[0]
                c = b['score']
                quiz_s = c*0.2

        result_h = col.find({'sid':i, 'grades.type': 'homework'}, {'_id':0,'grades.$':1})
        for k in result_h:
            a = k.values()
            for p in a:
                b = p[0]
                c = b['score']
                homework_s = c*0.3

        result_e = col.find({'sid':i, 'grades.type': 'exam'}, {'_id':0,'grades.$':1})
        for l in result_e:
            a = l.values()
            for p in a:
                b = p[0]
                c = b['score']
                exam_s = c*0.5

        total = quiz_s + homework_s + exam_s
        
        if total >= 90:
            grade = 'A'
        elif total >= 80:
            grade = 'B'
        elif total >= 70:
            grade = 'C'
        elif total >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        col.update({'sid':i},{'$set':{'total':total, 'letter':grade}})
    
    
    presult = col.find({},{'_id':0,'sid':1,'total':1,'letter':1}).limit(10).sort([('total',-1)])
    pprint(list(presult))

    
def perfect():
   
    for i in range(100):
        chk = 0
        result_q = col.find({'sid':i, 'grades.type': 'quiz'}, {'_id':0,'grades.$':1})
        for j in result_q:
            a = j.values()
            for p in a:
                b = p[0]
                quiz_r = b['score']
                quiz_s = quiz_r*0.2
                if quiz_r == 100:
                    chk = 1

        result_h = col.find({'sid':i, 'grades.type': 'homework'}, {'_id':0,'grades.$':1})
        for k in result_h:
            a = k.values()
            for p in a:
                b = p[0]
                homework_r = b['score']
                homework_s = homework_r*0.3
                if homework_r == 100:
                    chk = 1

        result_e = col.find({'sid':i, 'grades.type': 'exam'}, {'_id':0,'grades.$':1})
        for l in result_e:
            a = l.values()
            for p in a:
                b = p[0]
                exam_r = b['score']
                exam_s = exam_r*0.5
                if exam_r == 100:
                    chk = 1
        
        result = list(col.find({'sid':i},{'_id':0,'note':1}))
        if result != [{}]:
            chk = 1
            
        if chk == 1:
            total = quiz_s + homework_s + exam_s + 10
            if total > 100:
                total = 100
        else:
            total = quiz_s + homework_s + exam_s
            
        pmax = 0
        pmin = 100
        if quiz_r > pmax:
            pmax = quiz_r
        if homework_r > pmax:
            pmax = homework_r
        if exam_r > pmax:
            pmax = exam_r
        
        if quiz_r < pmin:
            pmin = quiz_r
        if homework_r < pmin:
            pmin = homework_r
        if exam_r < pmin:
            pmin = exam_r

        perc = ((total-pmin) / (pmax - pmin)) * 100
        
        if perc >= 80:
            grade = 'A'
        elif perc >= 50:
            grade = 'B'
        elif perc >= 20:
            grade = 'C'
        elif perc >= 10:
            grade = 'D'
        else:
            grade = 'F'
        
        col.update({'sid':i},{'$set':{'letter':grade}})

    presult = col.find({},{'_id':0,'sid':1,'letter':1}).limit(11)
    pprint(list(presult))

if __name__ == "__main__":
    client = MongoClient()
    db = client.ds2
    col = db.grades

    raw_input = sys.argv[1]
    #TODO
    if raw_input == 1:
        pagination()
    elif raw_input == 2:
        letter()
    elif raw_input == 3:
        perfect()
    else:
        print("Check your number!!")
    client.close()
