#!/usr/bin/env python

import sqlite3

conn=sqlite3.connect('data.db')

curs=conn.cursor()

#print "\nEntire database contents:\n"
#for row in curs.execute("SELECT * FROM temps"):
#    print row

#print "\nDatabase entries for the garage:\n"
#for row in curs.execute("SELECT * FROM temps WHERE zone='garage'"):
#    print row


def add_temp_reading (zonestr, temp):
    # I used triple quotes so that I could break this string into
    # two lines for formatting purposes
    curs.execute("""INSERT INTO temps values(date('now'),
        time('now'), (?), (?))""", (zonestr,temp))

    # commit the changes
    conn.commit()

add_temp_reading("garage", 23)


conn.close()
