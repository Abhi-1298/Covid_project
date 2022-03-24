from django.shortcuts import render
import json
import requests
# Create your views here.


def covid(request):
    response=requests.get("https://api.covid19api.com/total/country/india")
    res=response.json()
    return render(request,"covid.html",{"data":res})


def graph(request,days=365,charttype='bar'):
    
    response=requests.get("https://api.covid19api.com/total/country/india")
    data=response.json() 

    data_days=data[-days:] 

    chart_x_dates=[]       
    chart_y_Confirmed=[]
    chart_y_Deaths=[]
    chart_y_Recovered=[]
    chart_y_active=[]

    for data in data_days:
        chart_x_dates.append(data["Date"])
        chart_y_Confirmed.append(data['Confirmed'])
        chart_y_Deaths.append(data['Deaths'])
        chart_y_Recovered.append(data['Recovered'])
        chart_y_active.append(data['Active'])
    
    covid_data={
        "dates":chart_x_dates,
        "confirmed":chart_y_Confirmed,
        "deaths":chart_y_Deaths,
        "recovered":chart_y_Recovered,
        "active": chart_y_active
    }
    return render(request,"graph.html",{'covid_Data':json.dumps(covid_data),"chart_type":charttype})



