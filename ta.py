
import urllib2																#Importing necessary libraries

from bs4 import BeautifulSoup

import smtplib
																		
import sqlite3	

from googlesearch import search 																				



#Function sendEmail will take input as the message to be send and the recipient's email and will send using the smtp library
def sendEmail(msg, email):
	s = smtplib.SMTP('smtp.gmail.com', 587)

	s.starttls()

	s.login("16ucs110@lnmiit.ac.in", "anju1031999")							#The sender needs to enter his email and password 

	s.sendmail("16ucs110@lnmiit.ac.in", "16ucs110@lnmiit.ac.in", msg)

	s.sendmail("16ucs110@lnmiit", email, msg)


	s.quit() 
				
#Function will create a database in the Random access memory of the local system.	
def createDatabase():														# creates a database in RAM 

	con = sqlite3.connect(":memory:") 										# create a connection using connect()

	cur = con.cursor() 														# All the commands will be executed using cursor object only

	cur.execute("create table List_of_series (Email_id, Name_of_series)") 




																			#user input for email address and list of series taken in form of comma separated single integer
email = raw_input("Email address: ")					

list_series = raw_input("TV Series: ")

																			#input taken in form of comma separated is tored in a list named as series_list
series_list = list_series.split(',')

																			#length of the series_list is the number of series the user has input 
length = len(series_list)

message = ""																# will contain the output message 
																			


months = ['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']


createDatabase()															#creting the database

for list_iterator in range(0, length):	
																			# This is the q-mark style: 

	cur.execute("insert into List_of_series values (?, ?)", (email, series_list[list_iterator])) 

																			# And this is the named style: 

	cur.execute("select * from List_of_series")	 
		



     to search 
    query = series_list[list_iterator] + " imdb"							# searching the IMDb movie page on Google
  
    for link_iterator in search(query, tld="co.in", num=1, stop=1, pause=2): 
        quote_page = link_iterator											# Link to the IMDb site of the series from where we'll scrap data further

    	
	result = quote_page.find('imdb')										# finding string IMDb in the fist url obtained in google search		
	

        if (result == -1): 													#if string imdb doesn't exist in the url it's clear the series name isn't
        																	#written correctly or such series doesn't exist

	     	message = message + "Tv series name: "+ series_list[list_iterator]+"/n" + "Status: "+" Series not found" + "\n\n"

        else:         	

			page = urllib2.urlopen(quote_page)						

			soup = BeautifulSoup(page, 'html.parser')

			name_box = soup.find('title')									

			series_detail = name_box.string									#in the imbd page of series we'll find its year of release and end(if ended)
																			#using scraping 							

																			

			if (series_detail[-9] != " "):									#in the time of series we'll check weather the series has ended or not(eg (2006 - 2012))

				message = message + "Tv series name: "+ series_list[list_iterator]+"\n" + "Status: " + "The show has finished streaming all its episodes." +"\n\n"

			else:

		

				k = soup.select('a[href^="/title/tt6077448/episodes?season="]')							#Finding tags by attribute value
				
				seasonNo = k[0].string

				p = soup.select('a[href^="/title/tt6077448/episodes?year="]')



				next_date = 'https://www.imdb.com' + k[0]['href']										

		

				page2 = urllib2.urlopen(next_date)														#we'll go to the web page of latest season

				trial = BeautifulSoup(page2, 'html.parser')


				dates_of_latest_season = trial.select(".airdate")										#dates of latest season is an array which contains the release dates of latest season on imdb(weather relesed or not)
				
				first_date =  dates_of_latest_season[0].string
				
				first_len = len(first_date)
				
				first_string = first_date.lstrip()		
				
				if (len(first_string)==0):																#we'll check if the first episode of series is released or not

																										# if it isn't released and year is also not mentined
				    message = message + "Tv series name: "+" "+series_list[list_iterator]+"\n" + "Status: " + "The year of release of  season :" + seasonNo + " is unkown" + "\n\n"
				
				elif(first_string[1] != " " and  first_string[2] != " "):								# in case the eries is yet to release only the year is mentioned on imdb
				
					message = message + "Tv series name: "+" "+series_list[list_iterator]+"\n" + "Status: " + "The next season begins in "+ first_string +"\n\n"
				
				else:																					#if dates of release of last episode is mentioned,  then scraping the and appending in mail
				
					it = -1;
					
					fristSS = dates_of_latest_season[it].string
					
					while(len(fristSS.lstrip())==0):													#finding the latest episode
					 
						it = it-1																	
						
						fristSS = dates_of_latest_season[it].string
						
					else:
					
						last_element = dates_of_latest_season[it].string

						lengthDate = len(last_element)    
		
						if (first_string[1] != " " and  first_string[2] != " "):					#checking if only year is mentioned													

							s = last_element.lstrip()												#remove spaces from the string

							message = message + "Tv series name: "+" "+series_list[list_iterator]+"\n" + "Status: " + "The next season begins in "+ s+"\n\n"

						else:

							s = last_element.lstrip()												#remove the leftmost spaces from the string

							monthNo = months.index(s[3:7])+1

							message = message + "Tv series name: "+" "+series_list[list_iterator]+"\n" + "Status: "+"The next episode airs on "+ str(s[8:12])+"-"+str(monthNo)+"-"+str(s[0:2])+"\n\n"
	con.commit()                                													#commiting respective changes in the database				

print message
con.close()
sendEmail(message, email)
print "The mail has been sent to :- "+email

#----------------------------------------------------------------------------------------------------------------------------

#SMS Code

# https://myaccount.google.com/u/1/lesssecureapps?pageId=none

# Turn Off the security and let it allow send the emails through third party apps.

# creates SMTP session

