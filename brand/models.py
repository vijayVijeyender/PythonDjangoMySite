from django.db import models

# Create your models here.
class Brand (models.Model):
    brandName=models.CharField(max_length=200, null=True)
    brandNameTn=models.CharField(max_length=200, null=True)
    brandDescription=models.CharField(max_length=200, null=True)
    brandDescriptionTn=models.CharField(max_length=200, null=True)


    class Meta:
        db_table = 'Brand'