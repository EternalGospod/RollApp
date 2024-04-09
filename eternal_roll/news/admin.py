from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)   #такой спосбо для случаев когда что то переопределяешь
class UserAdmin(admin.ModelAdmin):  # другое наследование потмоу чт оменеджер другой (наверное)
    ...
@admin.register(Category)
class Category(admin.ModelAdmin):
    ...
@admin.register(News)
class News(admin.ModelAdmin):
    ...
@admin.register(Rasa)
class Rasa(admin.ModelAdmin):
    ...
@admin.register(Klass)
class Klass(admin.ModelAdmin):
    ...
@admin.register(CharList)
class CharList(admin.ModelAdmin):
    ...
@admin.register(StatBlock)
class StatBlock(admin.ModelAdmin):
    ...