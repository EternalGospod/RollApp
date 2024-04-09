
from django.db import models

class Skill(models.Model):
	name = models.CharField(max_length=32)
	
class CharSkill(models.Model):
	char = models.ForeignKey('CharList', on_delete=models.PROTECT, null=True )
	skill = models.ForeignKey('Skill', on_delete=models.PROTECT, null=True)
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
