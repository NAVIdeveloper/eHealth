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
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication


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
            video = request.POST['video']
            user = User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=int(type_client),bio=bio,video=video)
        else:
            type_g = request.POST['type_g']
            register_date = datetime.datetime.now()
            age = request.POST['age']
            height = request.POST['height']
            weight = request.POST['weight']
            type_t = int(request.POST['type_t'])
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

@api_view(['get'])
@permission_classes([AllowAny])
def View_Product(request):
    print("sms")
    DATA = LoaderProduct(Product.objects.all(),many=True).data
    return Response(DATA)

@api_view(['get','post'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def View_Category(request):
    if request.method == 'GET':   
        DATA = {}
        DATA = LoaderCategoryProduct(CategoryProduct.objects.all(),many=True).data
        return Response(DATA)
    elif request.method == 'POST':  
        id = int(request.POST['id'])
        products = Product.objects.filter(category__id=id)

@api_view(['get'])
@permission_classes([AllowAny])
def View_Sport(request):
    DATA = LoaderSport(Sport.objects.all(),many=True).data
    return Response(DATA)

class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = LoaderComment
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        comment = Comment.objects.create(user=request.user,text=request.POST['text'])
        data = LoaderComment(comment)
        return Response(data.data)

@api_view(['get'])
@permission_classes([AllowAny])
def View_News(request):
    DATA = LoaderNew(New.objects.all(),many=True).data
    return Response(DATA)

@api_view(['get'])
@permission_classes([AllowAny])
def View_News_Detail(request,pk):
    DATA = LoaderNew(New.objects.get(id=pk)).data
    return Response(DATA)

@api_view(['get'])
@permission_classes([AllowAny])
def View_Advice(request):
    DATA = LoaderAdvice(Advice.objects.all().order_by('-id'),many=True).data
    return Response(DATA)

@api_view(['get'])
@permission_classes([AllowAny])
def View_Advice_Random(request):
    DATA = LoaderAdvice(random.choice( Advice.objects.all().order_by('-id') )).data
    return Response(DATA)

@api_view(['get'])
@permission_classes([AllowAny])
def View_Health_App(request):
    DATA = LoaderHealthApp(HealthApp.objects.last()).data
    return Response(DATA)

