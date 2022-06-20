from django.shortcuts import render
from rest_framework import generics
import random
import datetime
from datetime import datetime,timedelta
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
from django.contrib.auth import authenticate


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
        return Response(1)
    except:
        if type_client == '2' or type_client == '3':
            bio = request.POST['bio']
            age = request.POST['age']
            experience = request.POST['experience']
            birthday = request.POST['birthday']
            addres = request.POST['addres']
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
                not_sports = eval(f"""[{request.POST['can_not_sports']}]""")
                print(type(not_sports))
                print("Sport")
                print(not_sports)
                for id in not_sports:
                    try:
                        id = int(id)
                        can_not_sports.append(Sport.objects.get(id=id))
                    except:
                        pass

            if type_t == 2 or type_t == 3:
                not_dieta = eval(f"""[{request.POST['can_not_dieta']}]""")
                print(not_dieta)
                print(type(not_dieta))
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


def Check_Weekly_Program(id):
    program = WeeklyProgram.objects.get(id=id)
    old_date = program.last_update
    today = datetime.today()
    print(today)
    print(old_date)
    days = today.date() - old_date.date()
    if days.days < 7:
        pass
    else:
        gived = [
            program.yakshanba,
            program.dushanba,
            program.seshanba,
            program.chorshanba,
            program.payshanba,
            program.juma,
            program.shanba
        ]
        not_gived = DayTask.objects.filter(weight_limit=program.intended_weight)
        not_gived = list(not_gived)
        for g in gived:
            not_gived.remove(g)

        program.dushanba = random.choice(not_gived)
        not_gived.remove(program.dushanba)
        
        program.seshanba = random.choice(not_gived)
        not_gived.remove(program.seshanba)
        
        program.chorshanba = random.choice(not_gived)
        not_gived.remove(program.chorshanba)
        
        program.payshanba = random.choice(not_gived)
        not_gived.remove(program.payshanba)
        
        program.juma = random.choice(not_gived)
        not_gived.remove(program.juma)
        
        program.shanba = random.choice(not_gived)
        not_gived.remove(program.shanba)
        
        program.yakshanba = random.choice(not_gived)
        not_gived.remove(program.yakshanba)
        program.last_update = today
        program.save()

        

@api_view(['get'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Api_Get_User_Task(request):
    user = request.user
    user.weekly_task
    Check_Weekly_Program(user.weekly_task.id)
    today = str(datetime.today().date())
    week = date_week(today)
    DATA = {"week":week,"today":today}
    task = eval(f"user.weekly_task.{week.casefold()}")
    DATA['task'] = LoaderWeeklyProgram(user.weekly_task).data[week.casefold()]
    return Response(DATA)


@api_view(['get'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Api_All_History_User_Task(request):
    DATA = {}
    last_date = None
    for i in HistoryTask.objects.filter(user=request.user):
        if last_date != None:
            day = last_date - i.date
            if day.days != 1:
                for r in range(day.days-1):
                    c = last_date - timedelta(days=1)
                    DATA[str(c)] = False
                    last_date = c
                
        if i.morning_sport == True and i.morning_diet == True and i.afternoon_sport == True and i.afternoon_diet == True and i.night_sport == True and i.night_diet == True:
            DATA[str(i.date)] = True
        else:
            DATA[str(i.date)] = False
        last_date = i.date
    return Response(DATA)


@api_view(['get'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Api_History_User_Task(request):
    user = request.user
    today = str(datetime.today().date())
    week = date_week(today)
    DATA = {"week":week,"today":today}
    task = eval(f"user.weekly_task.{week.casefold()}")
    try:
        history = HistoryTask.objects.get(user=user,date=today,task=task)
    except:
        history = HistoryTask.objects.create(user=user,date=today,task=task)
    
    return Response(LoaderHistoryTask(history).data)

@api_view(['post'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def Api_Done_User_Task(request):
    user = request.user
    today = str(datetime.today().date())
    week = date_week(today)
    DATA = {"week":week,"today":today}
    task = eval(f"user.weekly_task.{week.casefold()}")
    try:
        history = HistoryTask.objects.get(user=user,date=today,task=task)
    except:
        history = HistoryTask.objects.create(user=user,date=today,task=task)
    morning = request.POST['morning']
    afternoon = request.POST['afternoon']
    night = request.POST['night']
    steps = request.POST['steps']
    loosed_weight = 0
    if str(morning) == '1' and history.morning_sport != True:
        history.morning_sport = True
        lossed = 0
        for i in task.morning_sport.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight += lossed
    elif str(morning) == '2' and history.morning_diet != True:
        history.morning_diet = True
        lossed = 0
        for i in task.morning_diet.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight += lossed
    elif str(morning) == '-1' and history.morning_sport != False:
        history.morning_sport = False
        lossed = 0
        for i in task.morning_sport.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight -= lossed
    elif str(morning) == '-2' and history.morning_diet != False:
        history.morning_diet = False
        lossed = 0
        for i in task.morning_diet.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight -= lossed

    if str(afternoon) == '1' and history.afternoon_sport != True:
        history.afternoon_sport = True
        lossed = 0
        for i in task.afternoon_sport.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight += lossed
    elif str(afternoon) == '2' and history.afternoon_diet != True:
        history.afternoon_diet = True
        lossed = 0
        for i in task.afternoon_diet.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight += lossed
    elif str(afternoon) == '-1' and history.afternoon_sport != False:
        history.afternoon_sport = False
        lossed = 0
        for i in task.afternoon_sport.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight -= lossed
    elif str(afternoon) == '-2' and history.afternoon_diet != False:
        history.afternoon_diet = False
        lossed = 0
        for i in task.afternoon_diet.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight -= lossed
        
    if str(night) == '1' and history.night_sport != True:
        history.night_sport = True
        lossed = 0
        for i in task.night_sport.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight += lossed
    elif str(night) == '2' and history.night_diet != True:
        history.night_diet = True
        lossed = 0
        for i in task.night_diet.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight += lossed
    elif str(night) == '-1' and history.night_sport != False:
        history.night_sport = False
        lossed = 0
        for i in task.night_sport.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight -= lossed
    elif str(night) == '-2' and history.night_diet != False:
        history.night_diet = False
        lossed = 0
        for i in task.night_diet.all():
            lossed += 1/3500 * i.total_calories
        loosed_weight -= lossed
    
    history.steps = int(steps)
    history.save()
    loosed_weight += 1/3500 * history.steps * 0.04
    user.weight = user.weight - loosed_weight
    user.save()
    DATA = LoaderHistoryTask(history).data
    DATA['lost'] = loosed_weight
    
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
def Api_Counter(request):
    dietolog = User.objects.filter(user_type = 3)
    sportsmen = User.objects.filter(user_type = 2)
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


<<<<<<< HEAD
from rest_framework import generics

class ListDietolog(generics.ListAPIView):
    queryset = User.objects.filter(expert_type = 1)  
=======
@api_view(['post'])
@permission_classes([AllowAny])
def loginpage(request):
    username = request.POST['username']
    password=request.POST['password']

    try:
        user = User.objects.get(username = username)
        if str(user.password) == str(password):
            token = Token.objects.get(user=user)
            return Response(token.key)
        else:
            return Response(404)            
    except Exception as e:
        print(e)
        return Response(404)

@api_view(['post'])
@permission_classes([AllowAny])
def is_email_user(request):
    email = request.POST['email']
    name = request.POST['username']
    nameusers = User.objects.filter(username=name)
    users = User.objects.filter(email=email)
    if nameusers.count() == 0 and users.count() == 0:
        return Response(401)
    else:
        return Response(200)



class ListDietolog(generics.ListAPIView):
    queryset = User.objects.filter(user_type = 3)  
    serializer_class = LoaderExpertUser
    permission_classes = [AllowAny]

class ListSportsmen(generics.ListAPIView):
    queryset = User.objects.filter(user_type = 2)  
>>>>>>> 55166b053ec8721aeccbf438a95b17d212f4acfb
    serializer_class = LoaderExpertUser
    permission_classes = [AllowAny]