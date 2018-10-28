import datetime
import re
from bs4 import BeautifulSoup


# gets todays date and a week from today
def get_thiswk_dates():
    today = datetime.datetime.today()
    nextWk = today + datetime.timedelta(days=6)
    wkstart = today.strftime('%m/%d/%Y')
    wkend = nextWk.strftime('%m/%d/%Y')
    print('today: ' + wkstart + '\n next week: ' + wkend)
    return wkstart, wkend

def get_todays_date():
    today = datetime.datetime.today()
    today = today.strftime('%m/%d/%Y')
    return today

def get_dates(year, month, day, delta):
    today = datetime.date(year, month, day)
    nextWk = today + datetime.timedelta(days=6)
    wkstart = today.strftime('%m/%d/%Y')
    wkend = nextWk.strftime('%m/%d/%Y')
    print('today: ' + wkstart + '\n next week: ' + wkend)
    return wkstart, wkend

def get_date(year, month, day):
    day = datetime.date(year, month, day)
    day = day.strftime('%m/%d/%Y')
    print('day: ' + day)
    return day

def get_vip_date(year, month, day, delta):
    today = datetime.date(year, month, day)
    today_delta = today + datetime.timedelta(days=delta)
    vip = today_delta.strftime('%m/%d/%Y')
    print('vip date: ' + vip)
    return vip

def get_apptids(data):
    regex = r"classId_(\d+)"
    # test_str = "id=\\\"classId_11877209"
    matches = re.finditer(regex, data, re.MULTILINE)
    apptids = []
    for matchNum, match in enumerate(matches):
        '''
        matchNum = matchNum + 1
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum,
            start = match.start(), end = match.end(), match = match.group()))
        '''
        for groupNum in range(0, len(match.groups())):
            
            groupNum = groupNum + 1
            '''
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum,
                start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
            '''
            apptids.append(match.group(groupNum))
    return apptids

def get_class_index(html, class_name):
    # if html is a file, the split will return an array of ['filename', ''] (size is 2)
    if len(html.split('.html')) > 1:
        with open(html) as file:
            data = file.read()
    # else, html is the content of a request
    else:
        data = html
    # creating soup reading schedule
    soup = BeautifulSoup(data, 'html.parser')

    # identifying all classes in soup
    class_name_tags = soup.find_all("span", class_="sw-classname")

    # getting all classes from schedule
    class_names = []
    for c in class_name_tags:
        print(c)
        class_names.append(str(c.contents[0]))

    # getting all positions that class Code Red exits in class_names array
    x = [i for i, n in enumerate(class_names) if n == class_name]
    return x

def get_html_title(data):
    # creating soup reading schedule
    soup = BeautifulSoup(data, 'html.parser')
    return soup.title.string
