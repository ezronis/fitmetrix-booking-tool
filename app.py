import requests
import browsercookie
import FitMetrixAPI as fmAPI
import utils
import data
from bs4 import BeautifulSoup

# grabbing cookies from chrome browser
cj = browsercookie.chrome()
s = requests.Session()

# setting cookies for this session
#s.cookies = cj

# logging in and printing title of html response
l = fmAPI.login(s, data.username, data.password)
print(utils.get_html_title(l.content))

# iterating through class names in classes array
for keys, values in data.practice.items():
    # getting schedule
    day = utils.get_vip_date(2018, 10, 31, keys)
    sched = fmAPI.get_schedule(s, day, day)
    '''
    # creating record of schedule for requested date range
    Html_file = open("html/sched_test" + (day) + ".html","w")
    Html_file.write(str(sched.content))
    Html_file.close()
    '''
    # validating "title" of schedule, <span id="wmrhDateCurr">October 31, 2018</span>
    soup = BeautifulSoup(sched.content, 'html.parser')
    print(soup.find(id="wmrhDateCurr").next_element)

    # getting appointment ids for classes in sched.html
    apptids = utils.get_apptids(str(sched.content))
    print(str(apptids))
    for c in values:
            print('class: '+ c)
            class_index = []
            class_index = utils.get_class_index(str(sched.content), c)
            print(class_index)
            for i in class_index:
                    print('index of current class:' + str(i))
                    apptid = apptids[i]
                    print('apptid:' + str(apptid))
                    booking = fmAPI.book_spot1(s, apptid, data.spot)
                    print(utils.get_html_title(booking.content))