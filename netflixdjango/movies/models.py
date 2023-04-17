from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kategori(models.Model):
    name=models.CharField(max_length=100, verbose_name='Kategori Adı')
    def __str__(self):
        return self.name
class Tur(models.Model):
    name=models.TextField(max_length=50)

    def __str__(self):
        return self.name

class Movies(models.Model):
    filmismi=models.CharField(max_length=200, verbose_name='Film Adı')

    # tur=models.CharField(max_length=100, verbose_name='Film Türü')
    
    tur=models.ManyToManyField("tur", null=True,)
    acıklama=models.TextField(max_length=600,verbose_name='Film Açıklaması')
    resim=models.FileField(upload_to='afiş',blank=True, null=True, verbose_name="Afiş")
    Kategori=models.ForeignKey(Kategori,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.filmismi
    
class Izlenenler(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    izlenen=models.ManyToManyField("Movies",null=True)

    def __str__(self):
       return self.user.username