from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('analyze', views.analyze ,name='analyze'),
    path('info', views.info,name='info'),
    path('contract',views.contract,name='contract'),
]
