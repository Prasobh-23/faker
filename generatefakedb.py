from faker import Faker #To generate fake information
import mysql.connector  #To connect to the database
import time             
from tqdm import tqdm   #To show progressbar

fake = Faker()
list=[]

for i in tqdm(range(0,11000)):
    list.append([(fake.name()),fake.address(),fake.job()])

# The above for-loop is used to generate fake information. You can change the range 11000 to your need. 
# But always keep in mind the list in python has a limit in capacity.
# The loop will generate random fake info in each iteration and it will be appended to the list.
# You can also generate another type of information like ipv4 addresses, Currency, etc.
# Visit https://faker.readthedocs.io/en/master/ for more info about faker.

# The codes written below are used to establish a connection with the database and perform the query.
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "yourdbname"
    )
cur = conn.cursor()
sql = "INSERT INTO tablename (urdbcolunmname, urdbcolunmname, urdbcolunmname) VALUES(%s,%s,%s)"

try:
    cur.executemany(sql, list)
    conn.commit()
    print("Data has been uploaded successfuly")
    message = "Process finished successfuly. "
except:
    print("Error! Check db connection or try a lower range in the loop")
    message = "Process ended with an error!  "

finally:
    print(message + "Exiting....")
    cur.close()
    conn.close()
    time.sleep(3)
