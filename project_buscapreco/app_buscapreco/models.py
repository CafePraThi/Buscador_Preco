from django.db import models


class Produto(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    site = models.TextField(max_length=300)
    quote_date = models.DateField()
    link_img = models.TextField(max_length=500, default='https://via.placeholder.com/150')


