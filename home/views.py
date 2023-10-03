from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from home.serializers import RegisterSerializer , LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from home.models import Person
from home.serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
#from rest_framework.authtoken.models import Token
#from rest_framework.authentication import TokenAuthentication


# Create your views here.



class person(APIView):

    authentication_classes = [JWTAuthentication]
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        print(request.user)
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self,request):
        data = request.data
        objs =  Person.objects.get(id = data['id'])        
        serializer = PersonSerializer(objs,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)       
        return Response(serializer.errors) 
    
    def patch(self,request):
        data = request.data
        objs =  Person.objects.get(id = data['id'])
        serializer = PersonSerializer(objs,data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors) 

@api_view(["GET" , "POST"])
def index(request):
    courses = {
        "Name" : "Python",
        "Description" : "SnakeScript"
    }
    return Response(courses)


class LoginApi(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            user = authenticate(username = serializer.data['username'] , password = serializer.data['password'])
            print(user)
            if user:            
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': status.HTTP_200_OK,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'message': 'Login successful',
                })
            else:
                return Response("invalid credentials")
        else:
            return Response("user credentials wrong")




class RegisterApi(APIView):
    
    def post(self,request):
        data = request.data
        print(data)
        serializer = RegisterSerializer(data = data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            #user = User.objects.get(username = serializer.data['username'])
            user = User.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user) 
            return Response({'status' : 200,
                            "payload" : serializer.data,
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                            'message' : "your data is saved"
                            })  
        else:
            print(serializer.errors)
            return Response(serializer.errors)    




# @api_view(["GET" , "POST" , "PUT" , "PATCH"])
# def person(request):
#     if request.method == "GET":
#         objs = Person.objects.all()
#         serializer = PersonSerializer(objs, many = True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         data = request.data
#         serializer = PersonSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)

#     elif request.method == "PUT":
#         data = request.data
#         objs =  Person.objects.get(id = data['id'])        
#         serializer = PersonSerializer(objs,data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)       
#         return Response(serializer.errors) 
    
#     elif request.method == "PATCH":
#         data = request.data
#         objs =  Person.objects.get(id = data['id'])
#         serializer = PersonSerializer(objs,data = data , partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors) 
    
#     else:
#         return Response('wrong method')
        

#     return Response()
    

        

