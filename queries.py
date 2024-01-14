import shortuuid as shortuuid
import ujson

from pydb import sql_fetchall, sql_fetchone, sql_exec, get_connection



def insert_apart(event_action: str, payload: dict):
    sql = """
        insert into events (
            correlation_id, event_action, ids, payload)
        values (%s, %s, %s, %s);
    """
    correlation_id = shortuuid.uuid()
    json_dump = ujson.dumps(payload, indent=2)
    sql_exec(sql, param=(correlation_id, event_action, json_dump), commit=True)


# def insert_apart(payload: dict):
#     sql = """
#         insert into events (
#             correlation_id, event_action, payload) 
#         values (%s, %s, %s);
#     """"
#     correlation_id = shortuuid.uuid()
#     json_dump = ujson.dumps(payload, indent=2)
#     sql_exec(sql, param=(correlation_id, event_action, json_dump), commit=True)
