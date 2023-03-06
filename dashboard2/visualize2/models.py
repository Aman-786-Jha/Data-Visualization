from django.db import models


# Create your models here.
class DataData(models.Model):
    id = models.TextField(primary_key=True)
    end_year= models.TextField(default=0,blank=False,null=False)
    intensity = models.TextField(default=0,blank=False,null=False)
    sector = models.TextField(blank=True,null=True)
    topic = models.TextField(blank=True,null=True)
    url = models.TextField(blank=True,null=True)
    region = models.TextField(default='region',blank=False,null=False)
    start_year = models.TextField(default=0,blank=False,null=False)
    impact = models.TextField(default=0,blank=False,null=False)
    insight = models.TextField(blank=True,null=True)
    added = models.TextField(blank=True,null=True)
    published = models.TextField(blank=True,null=True)
    country = models.TextField(default='starnge country',blank=False,null=False)
    relevance = models.TextField(default=0,blank=False,null=False)
    pestle = models.TextField(default='pestle',blank=False,null=False)
    source = models.TextField(blank=True,null=True)
    title = models.TextField(blank=True,null=True)
    likelihood = models.TextField(default=0,blank=False,null=False)
    
