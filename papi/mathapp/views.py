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

