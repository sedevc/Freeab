#!/usr/bin/env python

import sqlite3

conn=sqlite3.connect('data.db')

curs=conn.cursor()

print "\nEntire database contents:\n"
for row in curs.execute("SELECT * FROM temps"):
    print row

print "\nDatabase entries for the garage:\n"
for row in curs.execute("SELECT * FROM temps WHERE zone='garage'"):
    print row

conn.close()
