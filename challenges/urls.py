from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage,name="Home"),
    path("<int:month>", views.show_month_challenge_by_number),
    path("<str:month>", views.show_month_challenge , name="month-challange" ),
    
    
]



