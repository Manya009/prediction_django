from django.shortcuts import render
import pickle
import pandas as pd

car = pd.read_csv('./saved_models/Cleaned_car.csv')

model = pickle.load(open('./saved_models/LinearRegressionModel.pkl', 'rb'))


# Create your views here.
def home(request):
    return render(request, "cpp/index.html")


def car_price_predictor(request):
    if request.method == "POST":
        company = str(request.POST['company'])
        cmodel = str(request.POST['cmodel'])
        year = int(request.POST['year'])
        kms = int(request.POST['kms'])
        fuel = str(request.POST['fuel'])

        df = pd.DataFrame([[cmodel, company, year, kms, fuel]],
                          columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
        jojo = model.predict(df)

        return render(request, "cpp/car.html", {'reslut': int(jojo)})

    years = []
    for i in range(1960, 2026):
        years.append(i)
    years.reverse()

    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = years
    fuel_type = car['fuel_type'].unique()

    return render(request, "cpp/car.html",
                  {'companies': companies, 'cmodels': car_models, 'years': year, 'fuel_types': fuel_type})
