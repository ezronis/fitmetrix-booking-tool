import requests
import data

def login(session):
    querystring = {"locationID": data.locationID}
    payload = "USERNAME=%s&PASSWORD=%s&LocationID=%s&REMEMBERME=true" % (data.username, data.password, data.locationID)
    headers = {'content-type': "application/x-www-form-urlencoded", 'Connection' :'keep-alive'}
    response = session.post(data.login_url, data=payload, headers=headers, params=querystring)
    print('logged in!')
    return response

def get_schedule(session, start, end):
    querystring = {"datestart":start,"dateend":end,"facguid":"d0b9fcb4-5aaa-e811-a974-9602e5420515","instructors":"","classes":"","classtypes":"","useExternalURL":"0","locationID":"5044","isenrollment":"0","includenonreservable":"0"}
    headers = {'content-type': "application/x-www-form-urlencoded", 'Connection' :'keep-alive'}
    response = session.get(data.schedule_url, headers=headers, params=querystring)
    print('got schedule')
    return response

def book_spot1(session, apptid, spot):
    querystring = {"locationID":"5044","actType":"","apptid":apptid,"spot":spot,"From":"SchedulePayment","makePreferred":"","interval":"1","userType":"1","guestEmail":"","guestName":""}
    headers = {'content-type': "application/x-www-form-urlencoded", 'Connection' :'keep-alive'}
    response = session.get(data.booking_url1, headers=headers, params=querystring)
    return response

def book_spot2(session, apptid):
    querystring = {"GUID":"d0b9fcb4-5aaa-e811-a974-9602e5420515","apptid":apptid,"spot":"77161","interval":"1","waitlist":"False","ClientServiceID":"163099","From":"SchedulePayment","cameFromContract":"False","userType":"1","bookToSchedulingSystem":"True"}
    headers = {'content-type': "application/x-www-form-urlencoded", 'Connection' :'keep-alive'}
    url = 'https://www.fitmetrix.io/WebPortal/saveProfileAppt?GUID=d0b9fcb4-5aaa-e811-a974-9602e5420515&apptid=12237766&spot=77161&interval=1&waitlist=False&ClientServiceID=163099&From=SchedulePayment&cameFromContract=False&userType=1&bookToSchedulingSystem=True'
    response = session.get(data.booking_url2, headers=headers, params=querystring)
    return response