from django.db import models
	

class CharList(models.Model):

	owner = models.ForeignKey(
		'User',
		on_delete=models.CASCADE,
		)
	
	char_name = models.CharField(
		 max_length = 128,
		 blank=False
		 )

	level = models.IntegerField(
		blank=True,
		null =True
		)
	
	stat_block = models.ForeignKey(
		'StatBlock',
		on_delete=models.PROTECT,
		null=True,
		blank=True
		)
	
	max_hp = models.IntegerField(
		blank=True,
		null=True
		)

	cur_hp = models.IntegerField(
		blank=True,
		null=True
		)
	
	spell = models.ManyToManyField(
		'Spell',
		through='CharSpell'
		) 
	
	#class_ability

	mastery_bonus = models.IntegerField(
		blank=True,
		null=True
		)
	
	rasa = models.ForeignKey(
		'Rasa',
		on_delete=models.PROTECT,
		null=True
		)
	
	klass = models.ForeignKey(
		'Klass',
		on_delete=models.PROTECT,
		null=True
		)
	
	skill = models.ManyToManyField(
		'Skill',
		through='CharSkill'
		)
	
	# invetnory
    # TODO разобраться что можно удалять что нет ))))))

	def __str__(self):
		return self.char_name

	def save(self, *args, **kwargs):
		self.mastery_bonus = self.level // 5 + 2
		super(CharList, self).save(*args, **kwargs)


class Rasa(models.Model):
	name = models.CharField(max_length=32)
	
	def __str__(self):
		return self.name
