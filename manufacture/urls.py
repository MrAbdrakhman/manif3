from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('salary_total', salary_total, name='salary_total'),
    path('raschet_eva', raschet_eva, name='raschet_eva'),
    path('raschet_pu', raschet_pu, name='raschet_pu'),
]