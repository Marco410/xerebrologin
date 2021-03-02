from django.db import models
from django.contrib.auth.models import User
import os,errno
import socket

# Create your models here.
class Senal(models.Model):
    signal = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name= "senal"

    def __str__(self):
        return self.signal

def custom_upload_to(instance,filename):
    nombre_equipo = socket.gethostname()
    ip = socket.gethostbyname(nombre_equipo)
    return '/'.join(['archivos', str(ip), filename])

class Config_User(models.Model):
    name = models.TextField(null=False,blank=False)
    ncanales = models.IntegerField(null=True,blank = False) 
    canales = models.TextField(null=False,blank=False)
    active = models.TextField(null=False, blank=False, default=1)
    ip = models.TextField(null=False, blank=False)
    file_name = models.FileField(upload_to=custom_upload_to,null= True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['created_at']

class TablesUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name_tabla = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['created_at']