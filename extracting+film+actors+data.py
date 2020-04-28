
# coding: utf-8

# In[ ]:


import requests
import MySQLdb
from bs4 import BeautifulSoup


# In[ ]:


HOST = "localhost"
USERNAME = "alekhya"
PASSWORD = ""
DATABASE = "ACTORS_DATA"


# In[ ]:


#getting url to extract data from and parsing it


# In[ ]:


url_to_scrape ='https://www.imdb.com/list/ls004440136/'

plain_html_text = requests.get(url_to_scrape)

soup = BeautifulSoup(plain_html_text.content, "html.parser")


# In[ ]:


print(soup.prettify())


# In[ ]:


#extracting data


# In[ ]:


actor_name= seven_day.find_all(class_="lister-item-index unbold text-primary")

actor_image = seven_day.find_all("src",class_="lister-item-image")

actor_personality = seven_day.find_all(class_="text-muted text-small")


# In[ ]:


a1= actor_name[0]
a2 =actor_image[0]
a3 = actor_personality[1]


# In[ ]:


print(a1.prettify())
print(a2.prettify())
print(a3.prettify())


# In[ ]:


#creating database and using the database


# In[ ]:


CREATE DATABASE ACTORS_DATA;


# In[ ]:


USE ACTORS_DATA;


# In[ ]:


#creating table to insert values into it.


# In[ ]:


CREATE TABLE `classes` (
 `actor_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `actor_image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `actor_personality` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 PRIMARY KEY (`actor_name`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


# In[ ]:


#connecting to database and creating a cursor to it


# In[ ]:


db = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)


# In[ ]:


cursor = db.cursor()


# In[ ]:


#inserting values into database


# In[ ]:


sql = "INSERT INTO classes(actor_name,actor_image,actor_personality) VALUES ('{}', '{}', '{}')";


# In[ ]:


#executing the sql statement in try block, of inserting values into database and committing it to database to insert values.


# In[ ]:


try:

 cursor.execute(sql)

 db.commit()


# In[ ]:


#if there is any exception the execution rolls back to the prevoius state


# In[ ]:


except:

 db.rollback()


# In[ ]:


#closing the database


# In[ ]:


db.close()

