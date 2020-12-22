from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class paket(models.Model):
    paket_ucrt = models.CharField(max_length=5,verbose_name="Paket Ücreti")
    paket_title = models.CharField(max_length=25,verbose_name="Paket Başlığı")
    paket_1 = models.CharField(max_length=25,verbose_name="Paket Özelliği 1",blank=True)
    paket_2 = models.CharField(max_length=25,verbose_name="Paket Özelliği 2",blank=True)
    paket_3 = models.CharField(max_length=25,verbose_name="Paket Özelliği 3",blank=True)
    paket_4 = models.CharField(max_length=25,verbose_name="Paket Özelliği 4",blank=True)
    paket_5 = models.CharField(max_length=25,verbose_name="Paket Özelliği 5",blank=True)
    paket_6 = models.CharField(max_length=25,verbose_name="Paket Özelliği 6",blank=True)
    paket_7 = models.CharField(max_length=25,verbose_name="Paket Özelliği 7",blank=True)
    paket_8 = models.CharField(max_length=25,verbose_name="Paket Özelliği 8",blank=True)
    paket_9 = models.CharField(max_length=25,verbose_name="Paket Özelliği 9",blank=True)
    def __str__(self):
        return self.paket_title
class musteri(models.Model):
    satis = models.CharField(max_length=5,verbose_name="Tpplam Satış")
    puan = models.CharField(max_length=5,verbose_name="Puan")
    musteri = models.CharField(max_length=5,verbose_name="Müşteri")
    ürün = models.CharField(max_length=5,verbose_name="Ürün")
class sss(models.Model):
    sss_title = models.CharField(max_length=50,verbose_name="Başlık")
    sss_content = models.CharField(max_length=500,verbose_name="İçeriği")