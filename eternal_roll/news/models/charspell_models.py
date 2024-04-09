from django.db import models	
	
class CharSpell(models.Model):
	char = models.ForeignKey('CharList', on_delete=models.PROTECT, related_name='chars')
	spell = models.ForeignKey('Spell', on_delete=models.PROTECT, related_name='spells' )
	class Meta:        
		constraints = [
            models.UniqueConstraint(
                fields=[
                    'char',
					'spell'
                ],
                name='unique 1',
            )
        ]
	