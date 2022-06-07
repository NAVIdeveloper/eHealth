from django.shortcuts import render
import random
import datetime
# Create your views here.
from .serializers import *
from .alghoritm import *
from rest_framework.generics import ListCreateAPIView
# Create your views here.
from django.db.models import Max,Min,Q as SearchQ
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action



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
        return Response(status=401)
    except:
        if type_client == '2':
            bio = request.POST['bio']
            age = request.POST['age']
            experience = request.POST['experience']
            birthday = request.POST['birthday']
            addres = request.POST['addres']
            experience = request.POST['experience']
            information = request.POST['information']

            pic = None
            if 'pic' in request.FILES:
                pic = request.FILES['pic']
            phone = request.POST['phone']

            user = User.objects.create(information=information,experience=experience,addres=addres,phone=phone,birthday=birthday,username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=int(type_client),bio=bio)
        else:
            type_g = request.POST['gender']
            age = request.POST['age']
            height = request.POST['height']
            weight = request.POST['weight']
            type_t = int(request.POST['type_loss'])
            going_to_loss = int(request.POST["going_to_loss"])
            can_not_dieta = []
            can_not_sports = []
            user = User.objects.create(
                gender=int(type_g),week_result=weight,age=age,
                weight=weight,height=height,task_type=type_t,
                username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=type_client,going_to_loss=going_to_loss)
            
            if type_t == 1 or type_t == 3:
                not_sports = eval(request.POST['can_not_sports'])
                for id in not_sports:
                    try:
                        id = int(id)
                        can_not_sports.append(Sport.objects.get(id=id))
                    except:
                        pass

            if type_t == 2 or type_t == 3:
                not_dieta = eval(request.POST['can_not_dieta'])
                for id in not_dieta:
                    try:
                        id = int(id)
                        can_not_dieta.append(Product.objects.get(id=id))
                    except:
                        pass
            user.task_sport_can_not.set(can_not_sports)
            user.task_dieta_can_not.set(can_not_dieta)
            try:   
                weekly_task = WeeklyProgram.objects.get(intended_weight=going_to_loss)
            except:
                if user.going_to_loss >= 10:
                    weekly_task = WeeklyProgram.objects.get(id=WeeklyProgram.objects.all().aggregate(Max('intended_weight'))['intended_weight__max']) 
                elif user.going_to_loss >= 5 and user.going_to_loss < 10:
                    weekly_task = WeeklyProgram.objects.filter(intended_weight__in=[1,2,3])[0]
                else:
                    weekly_task = WeeklyProgram.objects.get(id=WeeklyProgram.objects.all().aggregate(Min('intended_weight'))['intended_weight__min'])

            print(weekly_task)
            user.weekly_task = weekly_task
            user.save()

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

    def create(self,request):
        user = request.user
        text = request.POST['text']
        comment = Comment.objects.create(user=user,text=text)
        return Response(LoaderComment(comment).data)
    
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


class TypeIllViewSet(viewsets.ModelViewSet):
    queryset = TypeIll.objects.all()
    serializer_class = LoaderTypeIll
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

@api_view(['get'])
@permission_classes([AllowAny])
def Api_Expert(request):
    experts = User.objects.filter(user_type=2)
    data = LoaderExpertUser(experts,many=True).data
    
    return Response(data)


class FastLostView(viewsets.ModelViewSet):
    queryset = FastLost.objects.all()
    serializer_class = LoaderFastLost
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = LoaderQuestionAnswer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

@api_view(['post'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def View_Post_Reyting(request):
    user = request.user
    expert = request.POST['expert']
    expert=User.objects.get(username=expert)
    star = int(request.POST['star'])
    history = False
    try:
        history = HistoryReyting.objects.get(user=user,expert=expert)
        old_star = history.star
        history.star = star
        history.save()
        expert.reyting -= old_star
        expert.reyting += star
        expert.save()
        return Response(status=200)
    except:
        history = HistoryReyting.objects.create(user=user,expert=expert,star=star)
        expert.reyting += star
        expert.reyting_count += 1
        expert.save()
        return Response(status=201)


@api_view(['get'])
def Api_Search_Expert(request):
    search = request.GET['search']
    data = User.objects.filter(SearchQ(first_name__icontains=search) | SearchQ(last_name__icontains=search) | SearchQ(username__icontains=search),user_type=2)
    return Response(LoaderExpertUser(data,many=True).data)


@api_view(['get'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Api_Task_History(request):
    user = request.user
    data = HistoryReyting.objects.filter(user=user)
    return Response(LoaderHistoryTask(data).data)

@api_view(['get'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Api_Get_User_Task(request):
    user = request.user
    user.weekly_task
    today = str(datetime.today().date())
    week = date_week(today)
    DATA = {"week":week,"today":today}
    task = eval(f"user.weekly_task.{week.casefold()}")
    DATA['task'] = LoaderWeeklyProgram(user.weekly_task).data[week.casefold()]
    return Response(DATA)


class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = LoaderFooter
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class SearchStaticViewSet(viewsets.ModelViewSet):
    queryset = SearchStatic.objects.all()
    serializer_class = LoaderSearchStatic
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = LoaderAboutUs
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

class CardFastLossTypeViewSet(viewsets.ModelViewSet):   
    queryset = CardFastLossType.objects.all()
    serializer_class = LoaderCardFastLossType
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action == "list" or self.action == 'retrieve':
            return [AllowAny()]

        return [IsAdminUser()]

@api_view(['get'])
@permission_classes([AllowAny])
def Api_Get_Expert(request,pk:int):
    try:
        user = User.objects.get(id=pk)
        if user.user_type == 2:
            DATA = LoaderExpertUser(user).data
            return Response(DATA)
        else:
            return Response(status=204)
    except:
        return Response(status=204)


@api_view(['get'])
@permission_classes([AllowAny])
def counter(request):
    dietolog = User.objects.filter(expert_type = 1)
    sportsmen = User.objects.filter(expert_type = 2)
    foydalanuvchi = User.objects.filter(user_type = 1)
    erkaklar = User.objects.filter(user_type = 1 , gender=1)
    ayollar = User.objects.filter(user_type = 1 , gender=2)

    sum_dietolog = dietolog.count()
    sum_sportsmen = sportsmen.count()
    user_count = foydalanuvchi.count()
    erkaklar = erkaklar.count()
    ayollar = ayollar.count()
    context = {
        'dietolog' : sum_dietolog,
        'sportsmen' : sum_sportsmen,
        'bemorlar' : user_count,
        'erkaklar' : erkaklar,
        'ayollar' :ayollar


    }

    return Response(context)