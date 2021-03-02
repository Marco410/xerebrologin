from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from . import views, urls, pds,tabla,tablaparch
from .views import HomePage

urlpatterns = [

    #Path del core
    path('',HomePage.as_view(), name="home"),
    path('file_upload', views.fileUpload, name='file_upload'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
    path('save-config', views.InsertConfig, name='save-config'),
    path('tabla', tabla.makeTabla, name='tabla'),
    path('cor', tablaparch.makeCohCorr, name='cor'),
    path('pds', pds.makePds, name='pds'),
    path('get-config/<int:id>/<int:idA>', views.ConfigInicial, name='get-config')
    #path('plotSignal', views.plotSignal, name='plotSignal'),
    #path('get_data', views.get_data, name='get_data'),

]