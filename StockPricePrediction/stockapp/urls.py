from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.mainPage, name='mainPage'),
    #url(r'^mainPage/$', views.mainPage, name='mainPage'),
    url(r'^StockPrediction/$',views.home,name='home'),
    url(r'^StockPrediction/controller$',views.stockPredict,name='stockPredict'),
    
]