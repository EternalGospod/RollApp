
from django.db import models

class Skill(models.Model):
	name = models.CharField(max_length=32)
	
	def __str__(self):
		return self.name
	
class CharSkill(models.Model):
	char = models.ForeignKey('CharList', on_delete=models.PROTECT, null=True, related_name='skills' )
	skill = models.ForeignKey('Skill', on_delete=models.PROTECT, null=True, related_name='chars')
	class Meta:        
		constraints = [
            models.UniqueConstraint(
                fields=[
                    'char',
					'skill'
                ],
                name='unique 2',
            )
        ]
