enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def sell(sellers,who,amount):
    who['profit'] += int(amount *0.9)
    parent = sellers[who['parent']]
    profit = amount*0.1
    if parent != '-':
        sell(sellers,parent,profit)

def solution(enroll, referral, seller, amount):
    answer = []
    sellers = {}
    for name, parent in zip(enroll,referral):
        sellers[name] = {"parent" : parent, 'profit' : 0}
    
    for who, amt in zip(seller,amount):
        who = sellers[who]
        sell(sellers,who,amt)
    
    for value in sellers.values:
        answer.append(value['profit'])    
    return answer

print(solution(enroll,referral,seller,amount))
