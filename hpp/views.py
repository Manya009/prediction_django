from django.shortcuts import render
import pickle
import numpy as np
from pickle import load

model = pickle.load(open('./saved_models/model.pkl', 'rb'))


# Create your views here.

def house_price_predictor(request):
    if request.method == "POST":
        year = request.POST['year']
        bed = request.POST['bed']
        bath = request.POST['bath']
        jojo = model.predict([[year, bed, bath]])
        return render(request, "hpp/house.html", {'reslut': int(jojo)})
    return render(request, "hpp/house.html")
