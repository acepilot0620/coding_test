enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def sell(sellers,who,amount):
    who['profit'] += amount *0.9
    parent = sellers[who['parent']]
    parent['profit'] += amount*0.1
    seller_name = who
    sell_amount = amount
    while True:
        if sellers[seller_name]['parent'] != '-':
            # 민수 직속이 아닌경우
            sell(sellers,who,amount)
            seller_name = sellers[seller_name]['parent']
            sell_amount = 
        else:
            sellers[seller_name]['profit']             
            break

def solution(enroll, referral, seller, amount):
    answer = []
    sellers = {}
    for name, parent in zip(enroll,referral):
        sellers[name] = {"parent" : parent, 'profit' : 0}
    
    for who, amt in zip(seller,amount):
        
    return answer