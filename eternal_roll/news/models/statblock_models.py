from django.db import models

class StatBlock(models.Model):
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelegency = models.IntegerField()
    wisdom  = models.IntegerField()
    charisma  = models.IntegerField()

    def __str__(self):
        return f"Str:{self.strength} Dex:{self.dexterity} Con:{self.constitution} Int:{self.intelegency} Wis:{self.wisdom} Ch:{self.charisma}"
