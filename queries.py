import shortuuid as shortuuid
import ujson

# from pydb import sql_fetchall, sql_fetchone, sql_exec, get_connection
from pydb import sql_exec, sql_fetchall, sql_fetchone, get_connection



def insert_apart(apart_link: str = ''):
    sql = """
        insert into events (
            apart_link)
        values (%s);
    """
    # correlation_id = shortuuid.uuid()
    print('see it is corr')
    # print(type(correlation_id))
    # json_dump = ujson.dumps(payload, indent=2)
    sql_exec(sql, param=(apart_link), commit=True)
    
def get_all_apart():
    sql = """
        SELECT * FROM events
    """
    rows = sql_fetchall(sql)
    return rows


# def insert_apart(payload: dict):
#     sql = """
#         insert into events (
#             correlation_id, event_action, payload)
#         values (%s, %s, %s);
#     """"
#     correlation_id = shortuuid.uuid()
#     json_dump = ujson.dumps(payload, indent=2)
#     sql_exec(sql, param=(correlation_id, event_action, json_dump), commit=True)
