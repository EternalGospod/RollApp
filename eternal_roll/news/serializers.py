import io
from rest_framework import serializers
from django.db import transaction
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    class Meta:
        model = News
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    class Meta:
        model = Category
        fields = "__all__"



#ЧАРНИК
class CharSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharSkill  #ссылается на промеждуточную табилцу 
        fields = ('id',)

class CharListSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    # serializers.PrimaryKeyRelatedField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    # char_name =  
    level =  serializers.IntegerField()
    # stat_block =  
    # max_hp =  
    # cur_hp =  
    # spell =  
    # #class_ability
    mastery_bonus =  serializers.IntegerField(read_only=True)
    # rasa =
    # klass =  
    # skill =  CharSkillSerializer(source='skills', many=True)
    skill = serializers.ListSerializer(child=serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all()))
    # # invetnory
    # разобраться что можно удалять что нет ))))))
    def update(self, instance, validated_data):
        if validated_data.get('skill'):
            with transaction.atomic(): # with контекстный менеджер ( открывает и сам закрывает соединение) 
                # atomic - атомарность ( все или ничего) 
                data = validated_data.pop('skill') # pop удаляет из словаря
                CharSkill.objects.filter(char=instance).delete() 
                CharSkill.objects.bulk_create( # в булк_креэай мы передаем список сырых обьек.
                    [  #фишка булкриэйта то что идет 1 запрос вместо многих
                        CharSkill(char=instance, skill=i) for i in data #список сырыйх обьектов
                    ]
                ) 
        return super().update(instance, validated_data) 
    class Meta:
        model = CharList 
        fields = "__all__"
    

class RasaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    class Meta:
        model = Rasa
        fields = "__all__"


class StatBlockSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    strength = serializers.IntegerField(max_value=30, min_value=0)
    dexterity = serializers.IntegerField(max_value=30, min_value=0)
    constitution = serializers.IntegerField(max_value=30, min_value=0)
    intelegency = serializers.IntegerField(max_value=30, min_value=0)
    wisdom  = serializers.IntegerField(max_value=30, min_value=0)
    charisma  = serializers.IntegerField(max_value=30, min_value=0)

    # def save(self, *args, **kwargs):
    #     # original_owner = CharList.owner
    #     if self.pk:
    #         original_owner = CharList.objects.get(pk=self.pk).owner
    #         if self.owner != original_owner:  
    #             raise ValueError("Это не твой стат блок!")
    #     super(CharList, self).save(*args, **kwargs)

    
    class Meta:
        model = StatBlock
        fields = "__all__"




    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return News.objects.create(**validated_data)  # ** так понял распокованный словарь validated_date

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance


'''
class UsersSerializer(serializers.ModelSerializer):
    # login = serializers.CharField(max_length=64)
    # role_id = serializers.IntegerField()       #PrimaryKeyRelatedField(queryset=UsersRoles.objects.all()) # че за говно 
    # email = serializers.CharField(max_length=128)
    # password = serializers.CharField(max_length=128)
    # logged_in = serializers.BooleanField(default=True)
    # user_token = serializers.CharField(max_length=256, read_only=True)
    # time_registration = serializers.DateTimeField(read_only=True)
    # time_played = serializers.DateTimeField(read_only=True) 
    # description = serializers.CharField(max_length=1024, read_only=True)
    # user_photo = serializers.ImageField(read_only=True) 
    class Meta:
        model = Users
        # fields = "__all__"
        exclude = ("user_token", "description",)

'''