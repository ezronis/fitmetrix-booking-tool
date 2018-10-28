import requests
import data
import utils
import FitMetrixAPI as fmAPI

session = requests.Session()
usr = "", 
pw = ""
locationID = "5044"
login_url = "https://www.fitmetrix.io/memberportal/login/d0b9fcb4-5aaa-e811-a974-9602e5420515"

querystring = {"locationID": locationID}
payload = "USERNAME=%s&PASSWORD=%s&LocationID=%s&REMEMBERME=true" % (usr, pw, locationID)
headers = {'content-type': "application/x-www-form-urlencoded"}
login_response = session.post(login_url, data=payload, headers=headers, params=querystring, timeout=5)

print('printing header values from login')
for key, value in login_response.headers.iteritems():
    print key, ":", value

print("printing cookie values from login")
print(session.cookies.get_dict())
session.cookies.clear()

day = utils.get_vip_date(2018, 11, 3, 0)
schedule_response = fmAPI.get_schedule(session, day, day)
Html_file= open("sched_test_113.html","w")
Html_file.write(schedule_response.content)
Html_file.close()
apptids = utils.get_apptids(schedule_response.content)
for class_name in values:
    index = []
    index = utils.get_class_index("sched_test_1028.html", class_name)
    print('got index, len is ' + str(len(index)))
    print(index)
    for i in index:
        print('index of current class:' + str(i))
        apptid = apptids[i]
        print('apptid:' + str(apptid))
        r = fmAPI.book_spot1(session, apptid, data.spot)
        print(utils.get_html_title(r.content))
        f = fmAPI.book_spot2(session, apptid)
        print(utils.get_html_title(f.content))
