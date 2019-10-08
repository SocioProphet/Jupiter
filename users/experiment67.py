__author__ = "Quynh Nguyen and Bhaskar Krishnamachari"
__copyright__ = "Copyright (c) 2019, Autonomous Networks Research Group. All rights reserved."
__license__ = "GPL"
__version__ = "2.1"

"""
    Experiment 67: collect overhead latency and power overhead (CPU & memory)
"""

import sys
import os
import _thread
import shutil
from flask import Flask, request
import paho.mqtt.client as mqtt
import time
sys.path.append("../")
import jupiter_config

app = Flask(__name__)
    
def k8s_get_nodes(node_info_file):
    """read the node info from the file input
  
    Args:
        node_info_file (str): path of ``node.txt``
  
    Returns:
        dict: node information 
    """

    nodes = {}
    node_file = open(node_info_file, "r")
    for i,line in enumerate(node_file):
        node_line = line.strip().split(" ")
        nodes[node_line[0]] = node_line[1]   
    return nodes

def retrieve_tasks(dag_info_file):
    config_file = open(dag_info_file,'r')
    dag_size = int(config_file.readline())

    tasks={}
    tasksid={}
    for i, line in enumerate(config_file, 1):
        dag_line = line.strip().split(" ")
        tasks[dag_line[0]]=i 
        tasksid[i]=dag_line[0]
        if i == dag_size:
            break
    
    return tasks,tasksid

class collector():
    def __init__(self,ID,subs,server,port,timeout,looptimeout,node_log):
        self.id = ID
        self.subs = subs
        self.server = server
        self.port = port
        self.timeout = timeout
        self.looptimeout = looptimeout
        self.client = mqtt.Client()
        self.username = 'anrgusc'
        self.password = 'anrgusc'
        self.client.username_pw_set(self.username,self.password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.server, self.port, self.timeout)
        self.node_log = node_log
        self.client.loop_forever()
        
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self,client, userdata, flags, rc):
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        subres = client.subscribe(self.subs,qos=1)
        print("Connected with result code "+str(rc))
        

    def on_message(self,client, userdata, msg):
        message = msg.payload.decode()
        print('--------------')
        print(message)
        print('--------------')
        with open(self.node_log,'a') as f:
            f.write(message)





if __name__ == '__main__':
    

    jupiter_config.set_globals()

    global SERVER_IP, DAG_PATH, folder
    SERVER_IP = "127.0.0.1"
    NODE_PATH = jupiter_config.HERE + 'nodes.txt'
    nodes = k8s_get_nodes(NODE_PATH)
    folder = 'poweroverhead'
    
    print(nodes)
    N = len(nodes)
    DAG_PATH = jupiter_config.APP_PATH + 'configuration.txt'
    tasks,tasksid = retrieve_tasks(DAG_PATH)
    print(tasks)
    M = len(tasks)

    try:
        os.mkdir(folder)
    except:
        print('Folder already existed')

    task_folder = folder+'/M%d'%(M)
    try:
        os.mkdir(task_folder)
    except:
        print('Folder already existed')

    
        
    for node in nodes:
        node_log = '%s/M%d/%s_N%d_M%d.log'%(folder,M,node,N,M)
        cur_sub = 'poweroverhead_%s'%(node)
        print(cur_sub)
        _thread.start_new_thread(collector,(node,cur_sub,SERVER_IP,1883,300,1,node_log))

    app.run(host='0.0.0.0',port=5055)