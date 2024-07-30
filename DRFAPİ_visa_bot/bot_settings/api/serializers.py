from rest_framework import serializers
from bot_settings.models import Bot_Setting



#model serializer (dinamik serializer oluşturma yöntemi)
class Bot_Setting_Serializer(serializers.ModelSerializer):
    class Meta:        
        model=Bot_Setting
        fields='__all__'
        
        
#standart serializer (manuel serializer oluşturma yöntemi)

"""
class Bot_Setting_Serializer_Standart(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    isRunning=serializers.BooleanField()
    CheckFrequency=serializers.IntegerField()
    CheckToDate=serializers.IntegerField()
 
    def create(self, validated_data):
        print(validated_data)
        return Bot_Setting.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.isRunning =validated_data.get('isRunning',instance.isRunning)
        instance.CheckFrequency =validated_data.get('CheckFrequency',instance.CheckFrequency)
        instance.CheckToDate = validated_data.get('CheckToDate',instance.CheckToDate)
        print(instance)
        instance.save()
        return instance 
"""