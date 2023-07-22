from django.http import JsonResponse 
from  drinks.models import Drinks,Article, Categories
from .serializers import ArticleSerializer, DrinkSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
@api_view(['GET','POST'])
def drink_list (request, format=None):

    #getallthedrinks
    #serialize them 
    #return json
    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
       
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id, format=None):
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET'])
def article_detail(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return JsonResponse(serializer.data, safe=False)
    
@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
@api_view(['GET'])  
def articles_in_category(request, category_id):
    try:
        category = Categories.objects.get(pk=category_id)
    except Categories.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    articles = Article.objects.filter(category=category)
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)