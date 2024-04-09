from django.db import models	

class Spell(models.Model):
	name = models.CharField(max_length=256)
	time_cast = models.IntegerField()
	distance = models.IntegerField()
	components = models.ManyToManyField('Component',  through='SpellComponent') #матеериальный компонгент пока в описании
	duration = models.IntegerField()
	klass = models.ManyToManyField('Klass', through='SpellKlass')
	arh_type = models.ForeignKey('ArchType',on_delete=models.PROTECT, null=True,blank=True)
	#source да похй
	level = models.IntegerField()
	school = models.ForeignKey('School',on_delete=models.PROTECT, null=True,blank=True)
	discription = models.TextField(null=True)


	def __str__(self):
		return self.name
	
class School(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
	
    
class ArchType(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name
