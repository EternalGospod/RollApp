from django.db import models	

class SpellComponent(models.Model):
	spell = models.ForeignKey('Spell', on_delete=models.PROTECT, related_name='spell_components')
	component = models.ForeignKey('Component', on_delete=models.PROTECT, related_name='components')
	class Meta:        
		constraints = [
            models.UniqueConstraint(
                fields=[
                    'spell',
					'component'
                ],
                name='unique 3',
            )
        ]
	