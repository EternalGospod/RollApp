from django.db import models	


class SpellKlass(models.Model):
	spell = models.ForeignKey('Spell', on_delete=models.PROTECT, related_name='spell_klass')
	klass = models.ForeignKey('Klass', on_delete=models.PROTECT, related_name='klass')
	class Meta:        
		constraints = [
            models.UniqueConstraint(
                fields=[
                    'klass',
					'spell'
                ],
                name='unique 4',
            )
        ]