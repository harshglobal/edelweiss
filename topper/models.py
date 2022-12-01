from django.db import models

# Create your models here.
    


class InsertSymbols(models.Model):
    symbol = models.CharField(max_length=50,unique=True)
    exchange = models.CharField(max_length=50,default='NSE')
    upload = models.FileField(upload_to ='CSV/',blank=True,null=True)

    class Meta:
         ordering = ['symbol']
    def __str__(self):
        return self.symbol
