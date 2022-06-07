from .models import *
from rest_framework.serializers import ModelSerializer

class LoaderCategoryProduct(ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = "__all__"

class LoaderProduct(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class LoaderSport(ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"

class LoaderComment(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LoaderUser(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LoaderHistoryReyting(ModelSerializer):
    class Meta:
        model = HistoryReyting
        fields = "__all__"

class LoaderTaskSport(ModelSerializer):
    sport = LoaderSport(read_only=True)
    class Meta:
        model = TaskSport
        fields = "__all__"

class LoaderTaskDieta(ModelSerializer):
    product = LoaderProduct(read_only=True)
    class Meta:
        model = TaskDieta
        fields = "__all__"

class LoaderAdvice(ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"


class LoaderNew(ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class LoaderHealthApp(ModelSerializer):
    class Meta:
        model = HealthApp
        fields = "__all__"


# class LoaderMotivationLetter(ModelSerializer):
#     class Meta:
#         model = MotivationLetter
#         fields = "__all__"


class LoaderExpertUser(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','image','expert_type','reyting','reyting_count','birthday','addres','phone','experience','information','gender')

class LoaderFastLost(ModelSerializer):
    class Meta:
        model = FastLost
        fields = "__all__"

class LoaderAboutUs(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

# class LoaderInfoAboutUs(ModelSerializer):
#     class Meta:
#         model = InfoAboutUs
#         fields = "__all__"

class LoaderHistoryTask(ModelSerializer):
    class Meta:
        model = HistoryTask
        fields = "__all__"


class LoaderQuestionAnswer(ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = "__all__"

class LoaderDayTask(ModelSerializer):
    ertalab_sport = LoaderTaskSport(many=True,read_only=True)
    ertalab_dieta = LoaderTaskDieta(many=True,read_only=True)
    abed_sport = LoaderTaskSport(many=True,read_only=True)
    abed_dieta = LoaderTaskDieta(many=True,read_only=True)
    kechki_sport = LoaderTaskSport(many=True,read_only=True)
    kechki_dieta = LoaderTaskDieta(many=True,read_only=True)
    class Meta:
        model = DayTask
        fields = "__all__"


class LoaderWeeklyProgram(ModelSerializer):
    dushanba = LoaderDayTask(read_only=True)
    seshanba = LoaderDayTask(read_only=True)
    chorshanba = LoaderDayTask(read_only=True)
    payshanba = LoaderDayTask(read_only=True)
    juma = LoaderDayTask(read_only=True)
    shanba = LoaderDayTask(read_only=True)
    yakshanba = LoaderDayTask(read_only=True)
    class Meta:
        model = WeeklyProgram
        fields = "__all__"

class LoaderTypeIll(ModelSerializer):
    class Meta:
        model = TypeIll
        fields = "__all__"


class LoaderFooter(ModelSerializer):
    class Meta:
      model = Footer
      fields = '__all__'
    
class LoaderSearchStatic(ModelSerializer):
    class Meta:
        model = SearchStatic
        fields = "__all__"


class LoaderCardFastLossType(ModelSerializer):
    class Meta:
        model = CardFastLossType
        fields = "__all__"
