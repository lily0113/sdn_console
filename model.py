import web
import sqlite3
import requests
import json

conn = sqlite3.connect('todo.db')
print "Opened database successfully";
"""
conn.execute('''CREATE TABLE tododo (
    id INTEGER PRIMARY KEY,
    title TEXT);''')

print "Table created successfully";
"""
conn.close()


db = web.database(dbn='sqlite', db='todo.db')

url = "http://10.10.88.150:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:536996704256480/table/0"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='}
alljson = json.loads(requests.get(url, headers=headers).text)
#node_info = alljson['node'][0]

def get_switch():

    id = node_info['id']
    dscrption = node_info['flow-node-inventory:description']
    hardware = node_info['flow-node-inventory:hardware']
    ports = node_info['node-connector'][1]['flow-node-inventory:port-number']
    return ports

def get_host():
    return "host------------------info"

def get_link():
    return "link------------------info"

def get_flows():

    flows = alljson
    return flows

def get_todos():
    return db.select('tododo', order='id')

def new_todo(text):
    db.insert('tododo', title=text)

def del_todo(id):
    db.delete('tododo', where="id=$id", vars=locals())