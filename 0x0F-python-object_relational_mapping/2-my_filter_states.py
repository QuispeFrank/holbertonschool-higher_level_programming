#!/usr/bin/python3
""" Filter states by user input """
import MySQLdb
from sys import argv


def filter_states():
    """ functions that takes in an argument and displays all
        values in the states table of hbtn_0e_0_usa where name
        matches the argument.
    """

    db_cnx = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = db_cnx.cursor()
    NAME = argv[4]
    cur.execute(
        'SELECT * FROM states WHERE name LIKE BINARY "{}" \
                ORDER BY id'.format(NAME))
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
