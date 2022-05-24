from django.shortcuts import render
import random
import datetime
# Create your views here.
from .serializers import *
from rest_framework.generics import ListCreateAPIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action


def check_algoritm(obj):
    if obj.height % 2 != 0:
        obj.height = obj.height -1
    normals = Normal.objects.filter(age_start__lte=obj.age,age_end__gte=obj.age,height=obj.height)
    norma = normals[0]
    if obj.gender == 1:
        if norma.male_weight < obj.height:
            return norma.male_weight
        else:
            return False
    else:
        if norma.female_weight < obj.height:
            return norma.female_weight
        else:
            return False

def a_day_kaloriya(kg:int):
    return int(kg*15)



def algoritm_loss(days:int,kg:int):
    one_kg_kk = 3500
    have_to_loss_a_day = int(int(kg*one_kg_kk) / days)
    
    return have_to_loss_a_day   


@api_view(['post'])
@permission_classes([AllowAny])
def View_Register(request):
    type_client = request.POST['type']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    # if len(User.objects.filter(username=username)) == 0:
    try:
        user = User.objects.get(username=username)
        return Response(status=400)
    except:
        if type_client == '2':
            bio = request.POST['bio']
            age = request.POST['age']
            experience = request.POST['experience']
            
            pic = None
            if 'pic' in request.FILES:
                pic = request.FILES['pic']
            phone = request

            user = User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=int(type_client),bio=bio,video=video)
        else:
            type_g = request.POST['type_g']
            register_date = datetime.datetime.now()
            age = request.POST['age']
            height = request.POST['height']
            weight = request.POST['weight']
            type_t = int(request.POST['type_loss'])
            going_to_loss = int(request.POST["going_to_loss"])
            can_not_dieta = []
            can_not_sports = []
            user = User.objects.create(
                gender=int(type_g),register_date=register_date,week_result=weight,age=age,
                weight=weight,height=height,task_type=type_t,
                username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=type_client,going_to_loss=going_to_loss)
            
            if type_t == 1 or type_t == 3:
                not_sports = request.POST['can_not_sports']
                for id in not_sports:
                    id = int(id)
                    user.task_sport_can_not.add(Sport.objects.get(id=id))
                
            if type_t == 2 or type_t == 3:
                not_dieta = request.POST['can_not_dieta']
                for id in not_dieta:
                    id = int(id)
                    user.task_dieta_can_not.add(Product.objects.get(id=id))
            # user.task_sport_can_not = can_not_sports
            # user.task_dieta_can_not = can_not_dieta
            # user.save()
        token_key = Token.objects.create(user=user)
        DATA = {
                "username":username,
                "key":str(token_key),
                "type_client":type_client,
            }
        return Response(DATA)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = LoaderProduct
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = LoaderSport
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]
        print(self.action)
        return [IsAdminUser()]

class AdviceViewSet(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = LoaderAdvice
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = LoaderComment
    htpp_method_names = ['get','delete']
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = LoaderNew
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class HealthAppViewSet(viewsets.ModelViewSet):
    queryset = HealthApp.objects.all()
    serializer_class = LoaderHealthApp
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]


class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    serializer_class = LoaderCategoryProduct
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]
    
    def retrieve(self, request, pk=None):
        products = Product.objects.filter(category__id=pk)
        serializer = LoaderProduct(products,many=True)
        return Response(serializer.data)

class MotivationLetterViewSet(viewsets.ModelViewSet):
    queryset = MotivationLetter.objects.all()
    serializer_class = LoaderMotivationLetter
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

@api_view(['get'])
@permission_classes([AllowAny])
def Api_Expert(request):
    experts = User.objects.filter(user_type=2)

    return Response(LoaderExpertUser(experts,many=True).data)

