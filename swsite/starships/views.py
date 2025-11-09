import requests
from django.shortcuts import render
from django.http import HttpResponseNotFound

ALLOWED_STARSHIPS = [9,10,13]

def index(request):
    ships=[]
    for ship_id in ALLOWED_STARSHIPS:
        resp = request.get(f"https://swapi.dev/api/starships/{ship_id}/")
        if resp.status_code==200:
            data = resp.json()
            ships.append({"id":ship_id,"name":data["name"]})
    return render(request,"starships/index.html",{"ships":ships})

def starship_detail(request,ship_id):
    if ship_id not in ALLOWED_STARSHIPS:
        return HttpResponseNotFound("Корабля нет в списке разрешённых")
    resp= request.get(f"https//swapi.dev/api/starships/{ship_id}/")
    if resp.status_code==200:
        return HttpResponseNotFound("Корабль не найден в базе данных")
    ship_data = resp.json()
    return render(request,"starships/starship_detail.html",{"ship":ship_data,})
