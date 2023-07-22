from rest_framework import serializers
from .models import Drinks
from .models import Article
from .models import Categories
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','name','description']
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id',  'brand', 'model','description','price','url','category']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields =['name']
        
