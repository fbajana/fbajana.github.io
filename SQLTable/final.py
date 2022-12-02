import mysql.connector as mc
from mysql.connector import errorcode

def show_connection():
    try:
        conn = mc.connect(host='localhost',user='root',password='Thepass0fTheworld@',db='')
        print("Connected")
    except mc.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Connection closed")
        conn.close()

conn = mc.connect(host='localhost',user='root',password='Thepass0fTheworld@',db='')
c = conn.cursor()


def read_data():
    c.execute('SHOW DATABASES')
    writers = c.fetchall()  # data is read in the form of list
    for writer in writers:  # print individual item in the list
        print(writer)

def drop_menagrie():
    c.execute('DROP menagerie')

def make_menagerie():
    c.execute('CREATE DATABASE menagerie')
    c.execute('USE menagerie')
    c.execute('CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), \
        species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)')
    c.execute("INSERT INTO pet (name,owner,species,sex,birth,death) VALUES \
    ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL),\
    ('Fang','Benny', 'dog', 'm','1990-08-27',NULL),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29'),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL),\
    ('Whistler','Gwen', 'bird', NULL ,'1997-12-09',NULL),\
    ('Slim','Benny', 'snake', 'm','1996-04-29',NULL),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL)")
    c.execute('SELECT * FROM pet')
    items = c.fetchall()
    for item in items:
        print(item)

def femaleDogs():
    c.execute('USE menagerie')
    c.execute('SELECT * FROM pet WHERE sex = "f" AND species = "dog"')
    items = c.fetchall()
    for item in items:
        print(item)

def namesAndBirth():
    c.execute('USE menagerie')
    c.execute('SELECT name, birth FROM pet')
    items = c.fetchall()
    for item in items:
        print(item)

def petPerOwner():
    c.execute('USE menagerie')
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    items = c.fetchall()
    for item in items:
        print(item)

def finalTable():
    c.execute('USE menagerie')
    c.execute('SELECT name, birth, MONTH(birth) FROM pet')
    items = c.fetchall()
    for item in items:
        print(item)

def commit_close():

    conn.commit()
    c.close()
    conn.close()

def main():
    #show_connection()
    #read_data()
    #drop_menagrie()
    #make_menagerie()
    #femaleDogs()
    #namesAndBirth()
    #petPerOwner()
    finalTable()

    commit_close()



if __name__ == '__main__':
    main()
