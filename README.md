Innovacer-SDE(Platform)-Assignment

ABOUT:

A code has been created to keep track of all our favourite seasons and their latest episodes’ air time. It will send an email to the users account updating him about 
the details of the series names he entered as comma separated single string.

PREREQUISITES:

All the scipts that I have created were tested successfully on Linux based OS with Python 2.7.10 or Python 3 installed on the system.
Folling are the things you need to install to run the code:

Install pip for Python2
-->commands to install
	$ sudo apt update
	$ sudo apt install python-pip
	Verify installation by writing the pip version
	$ pip --version

Python 2.7 urllib2 library
-->It's a part of standard Python library

Python 2.7 BeautifulSoup library
-->commands to install
	$ apt-get install python-bs4
	$ easy_install beautifulsoup4
	If you don’t have easy_install  installed, you can download the Beautiful Soup 4 source tarball and install it with setup.py.
	$ python setup.py install
	
Python 2.7 smtplib library
-->commands to install
	$ pip install smtplib	
	
Python 2.7 sqlite3 library
-->It's a part of standard Python library

Python 2.7 googlesearch library
-->commands to install
	$ pip --version
	$ pip 8.0.2 (python 2.7)
	$ pip install -U googlesearch
	$ pip show googlesearch
To be able to send mails from python you need to follow the steps below
    1. While logged into your gmail at gmail.com, go to https://myaccount.google.com/security
    2. Scroll down to the part that says "Allow less secure apps"
    3. Turn ON "allow less secure apps".
	If you don't want to make your main gmail less secure, or if you don't already have gmail, then sign up for a new gmail solely for this purpose.



RUNNING THE CODE:

First you'll have to enter your emailid along with the password in the sendMail function.That will be our's senders ID.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
The code can be run by running the file Innovaccer.py on terminal
The input for the file will be the mail id of user and the series he wants to be updated about seperated by ",".
The code will send an email to the user updating him with latest dates and will store his input in a memory based database.
The code also considers the cases when the series entered is wrong or the dates of upcomming season are yet to be published.


FUNCTIONING:

1) Sending Email
 We need to import smtplib library
 
2) Create online database
 We need to import sqlite3 library.
 Using connect(databasedb) method, we will make connection to the database.db file else we can also use connect(:memory:) to mke database in RAM.
 Cursor helps in sending commands to the SQL. It is used to fetch records of the database. All commands are fetched using cursor only.
 Now we will use execute command to execute our query written inside it. For it call the cursor method and pass the query.
 Example: cur.execute("select * from List_of_series"), where cur is the cursor object i.e cur = con.cursor() 
 Finally, save the changes in the file by committing those changes and then lose the connection. 
 Example: con.commit() and con.close()











