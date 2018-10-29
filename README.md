# Fitmetrix Booking Tool ![Logo of the project](https://static.wixstatic.com/media/ebb8ab_f881ca6210334ed4b072e76742a47950~mv2.png/v1/fill/w_108,h_108,al_c,q_80,usm_0.66_1.00_0.01/ebb8ab_f881ca6210334ed4b072e76742a47950~mv2.webp)
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

What's all the bells and whistles this project can perform?
* What's the main functionality
* You can also do another thing
* If you get really randy, you can even do this

## Contributing

When you publish something open source, one of the greatest motivations is that
anyone can just jump in and start contributing to your project.

These paragraphs are meant to welcome those kind souls to feel that they are
needed. You should state something like:

"If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome."

If there's anything else the developer needs to know (e.g. the code style
guide), you should link it here. If there's a lot of things to take into
consideration, it is common to separate this section to its own file called
`CONTRIBUTING.md` (or similar). If so, you should say that it exists here.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/


## Licensing
"The code in this project is licensed under MIT license."
