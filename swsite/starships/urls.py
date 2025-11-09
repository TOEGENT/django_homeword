from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('starship/<int:ship_id>/', views.starship_detail,name="starship_detail")
]

