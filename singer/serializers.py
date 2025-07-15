from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class SingerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingerImage
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    created_at = serializers.CharField(read_only = True)
    updated_at = serializers.CharField(read_only = True)
    
    
    #이미지
    images = SingerImageSerializer(many=True, read_only = True)
    
    #==============================================================
    #노래
    songs = serializers.SerializerMethodField(read_only =True)
    
    def get_songs(self, instance):
        serializers = SongSerializer(instance.songs, many = True)
        return serializers.data
    
    #==============================================================
    #태그
    tags = serializers.SerializerMethodField()
    
    def get_tags(self, instance):
        tag = instance.tags.all()
        return [t.name for t in tag]
    
    class Meta:
        model = Singer
        fields = '__all__'
        #fields = '__all__'
        #fields = ('id', 'name', 'content', 'debut')
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']