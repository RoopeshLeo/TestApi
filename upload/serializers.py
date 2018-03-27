from rest_framework import serializers
from .models import File,College
class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model=File
        fields=('file','remark','timestamp')        
class CollegeSerializer(serializers.ModelSerializer):
    class Meta():
        model=College
        # fileds=('cname','clgcode','address','phone','principal')
        fields = '__all__'