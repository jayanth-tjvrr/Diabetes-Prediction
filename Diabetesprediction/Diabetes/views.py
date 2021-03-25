from django.shortcuts import render
from django.conf import settings
import os
import pickle
from scipy import integrate
import numpy as np
import pandas as pd
import math
# Create your views here.

def Diabetesprediction(request):
    d=True
    ans=NotImplemented 
    if request.method == "POST":
        a=[]
        print(type(a))
        print(request.POST)
        print(len(request.POST))
        for key,value in request.POST.items():
            print(type(value))
            a.append(value)
        del a[0]
        del a[7]
        for i in range(len(a)):
            a[i]=float(a[i])
        print(a)
        Xnew = [{'Plasma glucose concentration a 2 hours in an oral glucose tolerance test':a[0],'Diastolic blood pressure (mm Hg)':a[1],'Triceps skin fold thickness (mm)':a[2],'2-Hour serum insulin (mu U/ml)':a[3],'Body mass index (weight in kg/(height in m)^2)':a[4],'Diabetes pedigree function':a[5],'Age (years)':a[6]}]
        #data=[[a[0],a[1],a[2],a[3],a[4],a[5],a[6]]]
        #Xnew=pd.DataFrame(data,columns=['Plasma glucose concentration a 2 hours in an oral glucose tolerance test','Diastolic blood pressure (mm Hg)','Triceps skin fold thickness (mm)','2-Hour serum insulin (mu U/ml)','Body mass index (weight in kg/(height in m)^2)','Diabetes pedigree function','Age (years)'])
        Xnew=pd.DataFrame(Xnew)
        data=['Plasma glucose concentration a 2 hours in an oral glucose tolerance test','Diastolic blood pressure (mm Hg)','Triceps skin fold thickness (mm)','2-Hour serum insulin (mu U/ml)','Body mass index (weight in kg/(height in m)^2)','Diabetes pedigree function','Age (years)']
        pi = pickle.load(open('log_model.pkl','rb'))
        for c in data:
            Xnew[c]=np.log(Xnew[c])
        b=pi.predict(Xnew)
        print(Xnew)
        f={1:'YES',0:'NO'}
        val=int(b)
        ans=f[val]
        d=False
    return render(request,'index.html',{'d':d,'ans':ans})