from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('analyze', views.analyze ,name='analyze'),
    path('info', views.info,name='info'),
    path('contract',views.contract,name='contract'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
