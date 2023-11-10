from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# for post method:
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#      print(request.data)
#      return Response({'msg':'This is a post request'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
       return Response({'msg': 'This is a get request'})
    
    if request.method == "POST":
     print(request.data) 
     return Response({'msg':'This is a post request'})

# @api_view(['PUT'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# @api_view(['PATCH'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# @api_view(['DELETE'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})