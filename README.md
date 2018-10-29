# Fitmetrix Booking Tool
> Book a spot for any fitness class!
Don't you love beating out your gym frenemie on the best spot in class? This script will allow you to programattically book any spot for any class if your gym uses the Fitmetrix API. 

## Installing / Getting started

A quick introduction of the minimal setup you need to get this up & running.

```shell
vim creds.py
# add username and password objects with strings assigned
# update data.py dictionary "classes" with desired classnames by day
python3 app.py
```
Make sure to update the creds.py file with your username and password, as well as the classes dictionary with the desired classes by day.

### Initial Configuration
```
pip3 install -r requirements.txt
``

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/ezronis/fitmetrix-booking-tool.git
cd fitmetrix-booking-tool/
pip3 install -r requirements.txt
```

And state what happens step-by-step.

## Features

* Book any class given a date and spot number
* Book multiple classes in a given time frame
* Schedule bookings to reoccur

## Contributing

f you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Links

- Repository: https://github.com/ezronis/fitmetrix-booking-tool
- Issue tracker: 
  - In case of sensitive bugs like security vulnerabilities, please contact
    shyezroni@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!

## Licensing
The code in this project is licensed under MIT license.
