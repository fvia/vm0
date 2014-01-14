from django.db import models

# Create your models here.

class Items ( models.Model):
	#item_id autoumeric
    item_date = models.DateTimeField()
    person_ref = models.CharField(max_length=50) #pot estar duplicat la mateixa persona pot tenir molts items
    person_name = models.CharField(max_length=50)
    #offense_tags 0-n
    height = models.IntegerField(default=0) # alcada
    weight = models.IntegerField(default=0) # pes
    #picture un fitxer jpg 
    
