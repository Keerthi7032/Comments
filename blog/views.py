from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
import json
import pandas as pd
import MySQLdb
from datetime import datetime

username = "root"
pwd = "root"
dbname = "comment_demo"
port = 3306
host = "107.180.71.58"

def get_connection():
    #connection establishment
    conn = MySQLdb.connect(host=host,  # your host 
                     user=username,       # username
                     passwd=pwd,     # password
                     db=dbname,
                     port = port)
    return conn

def run_query(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    f = cur.fetchall()
    return f[0][0]

# Create your views here.
context = {'Keerthi':["This graph is good",{'Alekhya':'No there is something wrong in it'}],'Goutham':['This graph has an anamoly',{}],'Manoj':['This',{}]}
 
def index(request):
    conn = get_connection()
    df = pd.read_sql('Select * from  comment',conn)
    dic = {}
    temp_df = df[df['parent_id']==str(1)]
    for i in temp_df['name']:
        print(temp_df['comment'])
        dic[i] = temp_df['comment']
    print(dic)
    return render(request, 'blog/index.html', {'context': context})
 
def insert(request):
    print(request.POST['id'])
    name=request.POST['name']
    content=request.POST['content']
    if(id==1):
        context[name]=[]
        context[name].append(content)
    else:
        ids = request.POST['id']
        dic_key = ids.split('_')
        print(context)
        if(len(dic_key)==3):
            context[dic_key[1]][1][name]='@'+dic_key[2]+' '+content
        else:
            context[dic_key[1]][1][name]='@'+dic_key[1]+' '+content
    print(context)
    return redirect('/blog/')