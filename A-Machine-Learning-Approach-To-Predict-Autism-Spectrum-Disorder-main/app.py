#!C:\Program Files\Python311\python.exe
from flask import *
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd
import openpyxl
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle


#create a Flask class object 
app = Flask(__name__,template_folder='template/') 

#decorator to access the service
@app.route("/index", methods=['GET', 'POST'])
def index():#asdclassify

    if request.method=="POST":
        #extract form inputs
        cname = request.form.get("cname")
        age = request.form.get("age")
        sex = request.form.get("sex")
        bwj = request.form.get("bwj")
        fads = request.form.get("fads")
        testingperson = request.form.get("testingperson")
        sreason = request.form.get("sreason")
        aq1=request.form.get("aq1")
        aq2=request.form.get("aq2")
        aq3=request.form.get("aq3")
        aq4=request.form.get("aq4")
        aq5=request.form.get("aq5")
        aq6=request.form.get("aq6")
        aq7=request.form.get("aq7")
        aq8=request.form.get("aq8")
        aq9=request.form.get("aq9")
        aq10=request.form.get("aq10")

        #listing all the inputs
        lis=[aq1,aq2,aq3,aq4,aq5,aq6,aq7,aq8,aq9,aq10,age,sex,bwj,fads]

        #cleaning the data and preparing for predict function
        lis = list(map(lambda x: x.replace('yes', '1'), lis))
        lis = list(map(lambda x: x.replace('no', '0'), lis))
        lis = list(map(lambda x: x.replace('M', '1'), lis))
        lis = list(map(lambda x: x.replace('F', '0'), lis))

        #converting the elements of the list to int
        lis = [int(i) for i in lis]
        #print(lis)

        #passing the data to model and getting the result
        loaded_model = pickle.load(open("rf_model.pickle","rb"))
        test_result=loaded_model.predict([lis])
        #print(type(test_result))

        #converting the nparray data to python list
        test_result=list(test_result)
        print(type(test_result))
        print(test_result)
        print(test_result[0])

        #comparing the result for final output display
        if test_result[0]==1:
            return render_template("result.html",cname=cname,age=age, sex=sex, bwj=bwj, fads=fads, testingperson=testingperson, sreason=sreason, aq1=aq1, aq2=aq2, aq3=aq3, aq4=aq4, aq5=aq5, aq6=aq6, aq7=aq7, aq8=aq8, aq9=aq9, aq10=aq10,result="Symptoms of Person shows ASD positive")
            print("Symptoms of Person shows ASD positive")
        elif test_result[0]==0:
            return render_template("result.html",cname=cname,age=age, sex=sex, bwj=bwj, fads=fads, testingperson=testingperson, sreason=sreason, aq1=aq1, aq2=aq2, aq3=aq3, aq4=aq4, aq5=aq5, aq6=aq6, aq7=aq7, aq8=aq8, aq9=aq9, aq10=aq10,result="Symptoms of Person shows ASD negative")
            print("Symptoms of Person shows ASD negative")

    return render_template("index.html")

if(__name__)== '__main__':
    app.run(debug=True)
