#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@ File        : test_pysqlcipher3.py
@ Author      : yqbao
@ Version     : V1.0.0
@ Description : 
"""
from pysqlcipher3 import dbapi2 as sqlite

conn1 = sqlite.connect("test.db")
c1 = conn1.cursor()
c1.execute("PRAGMA key='123456'")
c1.execute("""create table stocks (date text, trans text, symbol text, qty real, price real)""")
c1.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
conn1.commit()
c1.close()

conn2 = sqlite.connect("test.db")
c2 = conn2.cursor()
c2.execute("PRAGMA key='123456'")
print(c2.execute("""select * from stocks""").fetchall())
c2.close()
