import sys
from datetime import datetime

import requests
from lxml import html

import data
import utils
import FitMetrixAPI as fmAPI

# creating new session
session = requests.Session()

# login to mcdancefitness.com
login_response = fmAPI.login(session)
print("printing cookie values from login")
print(session.cookies.get_dict())

# now to get the schedule
for key, values in data.practice.iteritems():
    day = utils.get_vip_date(2018, 10, 28, key)
    schedule_response = fmAPI.get_schedule(session, day, day)
    # writing schedule to html file
    #print(schedule_response.content)
    Html_file= open("sched_test_1028.html","w")
    Html_file.write(schedule_response.content)
    Html_file.close()
    print('created html file with schedule')
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
            
def main():
    """Main entry point for the script."""
    pass

if __name__ == '__main__':
    sys.exit(main())