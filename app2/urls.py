from django.urls import path 
from app2.views import*
app_name = 'som'



urlpatterns = [ 
    path('sec/',sec,name='sec'),
]