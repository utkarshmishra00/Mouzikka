from cx_Oracle import *
from traceback import *
conn = None
try:
    conn = connect("mouzikka/music@127.0.0.1/xe")
    print("connected successfully to the database")
    print("Database Version:",conn.version)
    print("DB user:",conn.username)
except DatabaseError:
    print("DB error:",format_exc())