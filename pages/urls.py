from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from .views import *

app_name = 'pages'

urlpatterns = [
    path('CalendarCount', views.CalendarCount, name= 'index' ),
    path('/count',views.count,name = 'count')
    #path('form', views.form),

]