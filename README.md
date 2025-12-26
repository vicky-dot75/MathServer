# Ex.04 Design a Website for Server Side Processing
## Date:10-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:

<html>
<head>
    <title>mileage</title>
    <style>
        body {
            background-color: #5ad5fa;
            
            font-family: Georgia, serif;

            font-size: 30px
}
        
        .box {
            width: 700px;
            margin: auto;
            margin-top: 120px;
            padding: 100px;
            background-color: #cbff3d;
            color: rgb(0, 0, 0);
            border: 4px dashed rgb(255, 0, 0);
            text-align: center;
            font-size: 18px
            
            
        }
        input {
            padding: 5px;
            margin: 8px;
            font-size: 20px
        }
        .btn {
            padding: 6px 15px;
            cursor: pointer;
            font-size: 15px
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>fuel consumption rate Calculator</h1>
        <h2> VIGNESH-S (25014344)<h2>
        

        <form method="POST">
            {% csrf_token %}
            Distance (km):
            <input type="text" name="distance" value="{{ km }}"><br>

            Fuel Used (liters):
            <input type="text" name="fuel" value="{{ lt }}"><br>

            <button class="btn" type="submit">Calculate</button><br><br>

            Mileage:
            <input type="text" value="{{ mileage }}" readonly> km/l
            
        </form>
    </div>
</body>
</html>

views.py

from django.urls import path
from . import views

urlpatterns = [
    path('mileage/', views.mileage, name='mileage'),
]

from django.shortcuts import render

def mileage(request):
    mileage = 0
    km = 0
    lt = 0

    if request.method == "POST":
        km = float(request.POST.get('distance', 0))
        lt = float(request.POST.get('fuel', 0))
        if lt > 0:
            mileage = km / lt

    return render(request, 'mathapp/mileage.html', {
        'km': km,
        'lt': lt,
        'mileage': round(mileage, 2)
    })

from django.contrib import admin
from django.urls import path, include

url,py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mathapp.urls')),  # only include app, nothing else
]

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (21).png>)


## OUTPUT - WEBPAGE:

![alt text](<Screenshot (19).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
