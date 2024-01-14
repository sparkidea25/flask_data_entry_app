# General mysql connector file
import logging

import pymysql.cursors
import os
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

dbhost = os.getenv("DB_HOST", 'localhost')
dbport = int(os.getenv("DB_PORT", '3306'))
dbname = os.getenv("DB_DATABASE", 'apart')
dbuser = os.getenv("DB_USERNAME", 'root')
dbpass = os.getenv("DB_PASSWORD", 'PAKEvURFd((Gl1Vw')

logging.info(f"Using DB host: {dbhost}:{str(dbport)} db: {dbname}"
                    f" User: {dbuser}")


def get_connection(autocommit=True):
    return pymysql.connect(
        host=dbhost,
        port=dbport,
        db=dbname,
        user=dbuser,
        passwd=dbpass,
        autocommit=autocommit,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,  # Dict is simpler than tuple
        connect_timeout=15
    )


def sql_exec(sql, param=None, cursor=None, fetch_one=False, fetch_all=False, commit=False, event=False):
    if cursor is not None:
        cur = cursor
    else:
        conn = get_connection()
        cur = conn.cursor()
    rows = []

    if not param:
        ret = cur.execute(sql)
    else:
        ret = cur.execute(sql, param)

    if commit and not cursor:
        conn.commit()

    if fetch_one:
        rows = cur.fetchone()

    if fetch_all:
        rows = cur.fetchall()

    if not fetch_one and not fetch_all:
        rows = ret

    if not cur:
        cur.close()
        conn.close()
    return rows


def sql_fetchall(sql, param=None, cursor=None):
    """
        Used to execute MySQL statements with autocommit. We try to execute SQL via this function.
    """
    conn = None
    if not cursor:
        conn = get_connection(autocommit=True)
        cursor = conn.cursor()

    if param is None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, param)
    rows = cursor.fetchall()

    if conn:
        cursor.close()
        conn.close()
    return rows


def sql_fetchone(sql, param=None, cursor=None):
    """
        Used to execute MySQL statements with autocommit. We try to execute SQL via this function.
    """
    conn = None
    if not cursor:
        conn = get_connection(autocommit=True)
        cursor = conn.cursor()

    if param is None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, param)
    row = cursor.fetchone()

    if conn:
        cursor.close()
        conn.close()
    return row
