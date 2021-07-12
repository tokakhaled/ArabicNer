
from flask import Flask, request
import jsonpickle
import json
import mysql.connector
from flask_cors import CORS

    
conn = mysql.connector.connect(
                host="db4free.net",
                user="fatimaelsaadny",
                database="al_sahaba_db",
                password="123456789")
    
#==========================================================================
def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(
                host="db4free.net",
                user="fatimaelsaadny",
                database="al_sahaba_db",
                password="123456789")
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

#====================================================================
# Create flask app
app = Flask(__name__)
CORS(app)


#======================================================================
# ExractSefat for Web
@app.route('/extractSefat', methods=["GET"])
def extractSefat():
    
# 1  get id :
    id = request.args.get('personId')
    print(id)
    
# 2 check txt entity :   
    cursor = conn.cursor(buffered=True)
    sahaba = cursor.execute('SELECT sefatId FROM `personsefat` where person_Id =%s', [id])
    sahaba =cursor.fetchall()
    print("sahaba",sahaba)
       
    newsahaba=list()
    for item in sahaba:
        newsahaba.append(item[0])
    print("newsahaba",newsahaba)
    
    storedSefat=list()
    for id in newsahaba:
        cursor.execute('SELECT sefatName  FROM `sefattable`where sefatId =%s',[id])
        sefa=cursor.fetchone()
        storedSefat.append(sefa[0])
    print("storedSefat",storedSefat)
        
    
    #1 retrive from database
    json_string = jsonpickle.encode(storedSefat,unpicklable=False)
    response = app.response_class(
    response=json_string,
    status=200,
    mimetype='application/json')
    print("response",response)
   
    return response


#=================================================================================
# Exract All Sefat for Android


@app.route('/extractAllSefat', methods=["GET"])
def extractAllSefat():
    cursor = conn.cursor(buffered=True)
    class person:
        def __init__(self,name,sefat):
            self.name=name
            self.sefat=sefat
    
# 1  get id :
    ids = [2,21,22,23,24,25,26,27,28,29]
    print(ids)
    objlist=list()
    
    for id in ids:
        print(id)
    
# 2 select sahabyname and sefaid based on id :  
        name =cursor.execute('SELECT personName FROM `personalities` where personId =%s', [id])
        name =cursor.fetchone()
        print("name",name)
        
        sahaba = cursor.execute('SELECT sefatId FROM `personsefat` where person_Id =%s', [id])
        sahaba =cursor.fetchall()
        print("sahaba",sahaba)
        
#create list of sefaid        
        newsahaba=list()
        for item in sahaba:
            newsahaba.append(item[0])
        print("newsahaba",newsahaba)
        
#create list of stored sefa   
        storedSefat=list()
        for id in newsahaba:
            cursor.execute('SELECT sefatName  FROM `sefattable`where sefatId =%s',[id])
            sefa=cursor.fetchone()
            storedSefat.append(sefa[0])
        print("storedSefat",storedSefat)
        
        p=person(name[0], storedSefat)
        objlist.append(p)
        
        
    json_string = jsonpickle.encode(objlist,unpicklable=False)
    response = app.response_class(
    response=json_string,
    status=200,
    mimetype='application/json')
    print("response",response)
 
    return response
#=================================================================================
# Exract Places for Web
@app.route('/extractPlaces', methods=["GET"])
def extractPlaces():
    
# 1  get id :
    id = request.args.get('personId')
    print(id)
    
# 2 check txt entity :   
    cursor = conn.cursor(buffered=True)
    sahaba = cursor.execute('SELECT placeId FROM `visitedplaces` where personId =%s', [id])
    sahaba =cursor.fetchall()
    print("sahaba",sahaba)
       
    newsahaba=list()
    for item in sahaba:
        newsahaba.append(item[0])
    print("newsahaba",newsahaba)
    
    storedPlaces=list()
    for id in newsahaba:
        cursor.execute('SELECT visitedPlaces  FROM `placetble`where placeId =%s',[id])
        place=cursor.fetchone()
        storedPlaces.append(place[0])
    print("storedSefat",storedPlaces)
        
    
    #1 retrive from database
    json_string = jsonpickle.encode(storedPlaces,unpicklable=False)
    response = app.response_class(
    response=json_string,
    status=200,
    mimetype='application/json')
    print("response",response)
   
    return response

#=================================================================================
# Exract All Places for Android


@app.route('/extractAllPlaces', methods=["GET"])
def extractAllPlaces():
    cursor = conn.cursor(buffered=True)
    class person:
        def __init__(self,name,Places):
            self.name=name
            self.Places=Places
    
# 1  get id :
    ids = [2,21,22,23,24,25,26,27,28,29]
    print(ids)
    objlist=list()
    
    for id in ids:
        print(id)
    
# 2 select sahabyname and sefaid based on id :  
        name =cursor.execute('SELECT personName FROM `personalities` where personId =%s', [id])
        name =cursor.fetchone()
        print("name",name)
        
        sahaba = cursor.execute('SELECT placeId FROM `visitedplaces` where personId =%s', [id])
        sahaba =cursor.fetchall()
        print("sahaba",sahaba)
        
#create list of placeid        
        newsahaba=list()
        for item in sahaba:
            newsahaba.append(item[0])
        print("newsahaba",newsahaba)
        
#create list of stored place  
        storedPlaces=list()
        for id in newsahaba:
            cursor.execute('SELECT visitedPlaces  FROM `placetble`where placeId =%s',[id])
            place=cursor.fetchone()
            storedPlaces.append(place[0])
        print("storedPlaces",storedPlaces)
        
        p=person(name[0], storedPlaces)
        objlist.append(p)
        
        
    json_string = jsonpickle.encode(objlist,unpicklable=False)
    response = app.response_class(
    response=json_string,
    status=200,
    mimetype='application/json')
    print("response",response)
 
    return response

# #============================================================
# import os

# @app.route('/getSpeech', methods=["GET"])
# def getSpeech():
#     cursor = conn.cursor(buffered=True)
    
# # 1  get id :
#     id = request.args.get('personId')
#     print(id)
#     aud=cursor.execute('SELECT Audio FROM personalities WHERE personId=%s', [id])
#     aud =cursor.fetchone()
#     print(aud[0].decode("utf-8"))
#    # os.system(aud[0].decode("utf-8"))
    
#     json_string = jsonpickle.encode(os.system(aud[0].decode("utf-8")),unpicklable=False)
#     response = app.response_class(
#     response=json_string,
#     status=200,
#     mimetype='application/json')
#     print("response",response)
    
#     return response
    


#===========================================================================
if __name__ == '__main__':
    connect()
    # app.run(host='127.0.0.1', port=5000)
    app.run(threaded=True, port=5000)
    
    
    
    
    
    
    
    
    
    