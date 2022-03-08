from django.db import models

# Create your models here.
class Berita(models.Model):
    judul_berita = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    isi = models.TextField()
    penulis = models.CharField(max_length=200)
    tanggal_upload = models.CharField(max_length=200)
      
    def __str__(self):
        return self.judul_berita