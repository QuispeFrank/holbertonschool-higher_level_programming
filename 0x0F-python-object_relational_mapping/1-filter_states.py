#!/usr/bin/python3
""" Filter states """
import MySQLdb
from sys import argv


def filter_states():
    """ script that lists all states with a name
        starting with N (upper N) from the database
        hbtn_0e_0_usa.
    """

    db_cnx = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db_cnx.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id')
    all_states = cur.fetchall()
    for states in all_states:
        print(states)

    cur.close()
    db_cnx.close()


if __name__ == '__main__':
    try:
        filter_states()
    except MySQLdb.Error as e:
        print(f'MySQL Error: {e.args[0]} {e.args[1]}')
