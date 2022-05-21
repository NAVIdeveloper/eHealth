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
    class Meta:
        model = TaskSport
        fields = "__all__"

class LoaderTaskDieta(ModelSerializer):
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