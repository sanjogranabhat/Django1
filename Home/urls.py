from django.urls import path

from .import views

urlpatterns =[
    path('',views.index),
    path('add_employee/',views.add_employee),
    path('update/<int:id>/',views.update_employee, name='update')
    
]