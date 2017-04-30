# Data Science in the Cloud

This project was conceived by a Northeastern University Data Science Professor and developed by four Boston University students for the class EC528 Cloud Computing. Typically when one works on a data science project, the data is given and the researcher is tasked with building the best models to address the problem. The final outcome can be evaluated through an evaluation critereon, but the methods, tools, packages, and libraries can be varied. This is especially challenging for Professors who must grade their students on their methods. To address this problem, this project utilizes Docker to allow the sharing of the environments used to build these data science models.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python 2.7, Django 1.10.5, Docker

```
apt-get install python2.7
apt-get install python-pip
pip install django==1.10.5
```
To install Docker we refer you to their documentation:
[Get Docker](https://docs.docker.com/engine/installation/)


### Installing

A step by step series of examples that tell you have to get a development env running

Pull the repository to your local machine

```
git pull https://github.com/BU-CS-CE-528-2017/Data-Science-in-the-Cloud
```

To run the website, navigate to the webApp folder and run manage.py

```
cd ~/your/path/Data-Science-in-the-Cloud/webApp
python manage.py runserver 8000
```

This will run the website on the localhost, which you can navigate to by going to this url in your web browser

```
http://localhost:8000/
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com//) - The web framework used
* [Bootstrap](http://getbootstrap.com/) - The front-end framework used
* [Docker](https://www.docker.com/) - Primary technology used

## Contributing

Please read [CONTRIBUTING.md](https://github.com/BU-CS-CE-528-2017/Data-Science-in-the-Cloud/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Yanjiang Dong** - [dongyj1](https://github.com/dongyj1)
* **Christine Duong** - [ChristineDuong](https://github.com/ChristineDuong)
* **Wei Jiang** - [jiangwei221](https://github.com/jiangwei221)
* **Caroline Jones** - [CarolineGlucksman](https://github.com/CarolineGlucksman)

See also the list of [contributors](https://github.com/BU-CS-CE-528-2017/Data-Science-in-the-Cloud/contributors) who participated in this project.

## License


## Acknowledgments

* A big thank you to our mentor Srikanth Krishnamurthy - [sriboston](https://github.com/sriboston)
* Another equally big thank you to our instructors:
	* Orran Krieger - [okrieg](https://github.com/okrieg) 
	* Ata Turk - [ataturk](https://github.com/ataturk)
	* Peter Desnoyers
	* Michael Daitzman
* Thank you to our classmates who provided us with feedback and kept us on our toes
* Thank you to [PurpleBooth](https://github.com/PurpleBooth) for this README template
