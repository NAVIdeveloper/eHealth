from datetime import datetime
from itertools import product
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
# Create your models here.

class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)

    category = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE)
    kaloriya = models.FloatField()

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)
    
    video = models.URLField(null=True,blank=True)
    kaloriya = models.FloatField()
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    image = models.ImageField(upload_to='profile/',null=True,blank=True)
    going_to_loss = models.IntegerField(default=0,null=True,blank=True)
    user_type = models.IntegerField(choices=(
        (1, "client"),
        (2, "expert")
    ), default=1)
    birthday = models.DateField(null=True,blank=True)
    expert_type = models.IntegerField(choices=(
        (1, "dietolog"),
        (2, "sportsmen")
    ),null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    network = models.URLField(null=True,blank=True)
    reyting = models.FloatField(default=0,null=True,blank=True)
    reyting_count = models.IntegerField(default=0,null=True,blank=True)
    type_g = [
        (1, "Erkak"),
        (2,"Ayol")]
    gender = models.IntegerField(choices=type_g,null=True,blank=True)
    week_result = models.IntegerField(default=0,null=True,blank=True)
    avarage = models.IntegerField(default=0,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    height = models.IntegerField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    task_sport_can_not = models.ManyToManyField(Sport,blank=True)
    task_dieta_can_not = models.ManyToManyField(Product,blank=True, related_name="NoDieta")
    type_t = [
        (1,"Dieta"),
        (2,"Sport"),
        (3,"All")] 
    task_type = models.IntegerField(choices=type_t,null=True,blank=True)

    weekly_task = models.ForeignKey('WeeklyProgram',on_delete=models.CASCADE,null=True,blank=True)

    addres = models.CharField(max_length=255,null=True,blank=True)
    experience = models.IntegerField(default=1)
    information = models.IntegerField(default=1,choices=((1,1),(2,2),(3,3)))
    phone = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return self.user.username

class HistoryReyting(models.Model):
    expert = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="from_user")
    star = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} : {str(self.star)} -> {self.expert.username}"

class New(models.Model):
    img = models.ImageField(upload_to='news/',max_length=999999)

    title = models.CharField(max_length=255)
    text = models.TextField(null=True,blank=True)

    en_title = models.CharField(max_length=255)
    en_text = models.TextField(null=True,blank=True)

    ru_title = models.CharField(max_length=255)
    ru_text = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title

class Advice(models.Model):
    uz_text = models.CharField(max_length=255)
    en_text = models.CharField(max_length=255)
    ru_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.uz_text

class Normal(models.Model):
    age_start = models.IntegerField()
    age_end = models.IntegerField()
    height = models.IntegerField(unique=True)
    male_weight = models.FloatField()    
    female_weight = models.FloatField()    
    def __str__(self):
        return str(self.height)

class HealthApp(models.Model):
    logo = models.ImageField(upload_to="healthapp/")
    
    title_uz  = models.CharField(max_length=255)
    title_en  = models.CharField(max_length=255)
    title_ru  = models.CharField(max_length=255)
    
    text_uz = models.TextField()
    text_en = models.TextField()
    text_ru = models.TextField()
    
    text2_uz = models.CharField(max_length=255)   
    text2_en = models.CharField(max_length=255)
    text2_ru = models.CharField(max_length=255)
    
    img = models.ImageField(upload_to="healthapp/")

    def __str__(self):
        return self.title_uz

# class MotivationLetter(models.Model):
#     text_uz = models.TextField()
#     text_ru = models.TextField()
#     text_en = models.TextField()
#     img = models.ImageField(upload_to='motivation_letter/')
#     def __str__(self):
#         return self.text_uz

class TypeIll(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    text1_uz = models.TextField()
    text1_ru = models.TextField()
    text1_en = models.TextField()
    
    text2_uz = models.TextField()
    text2_ru = models.TextField()
    text2_en = models.TextField()
    
    text3_uz = models.TextField()
    text3_ru = models.TextField()
    text3_en = models.TextField()
    
    text4_uz = models.TextField()
    text4_ru = models.TextField()
    text4_en = models.TextField()
    
    text5_uz = models.TextField()
    text5_ru = models.TextField()
    text5_en = models.TextField()


    img = models.ImageField(upload_to='ill/')
    def __str__(self):
        return self.title_uz



class FastLost(models.Model):
    image = models.ImageField(upload_to='fastlost/')
    name_uz = models.CharField(max_length=40, blank=True, null=True)
    name_ru = models.CharField(max_length=40, blank=True, null=True)
    name_en = models.CharField(max_length=40, blank=True, null=True)


    def __str__(self):
        return self.name_uz


class TaskSport(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    duration = models.IntegerField()
    total_calories =models.IntegerField()
    def __str__(self): 
        return f"{self.sport.name} {self.duration}min {self.total_calories}kk"
    

class TaskDieta(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    grams = models.IntegerField()
    total_calories =models.IntegerField()
    def __str__(self): 
        return f"{self.product.name} {self.grams}g {self.total_calories}kk"

# test models here

class DayTask(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    ertalab_sport = models.ManyToManyField(TaskSport,blank=True,related_name="sport_time1")
    ertalab_dieta = models.ManyToManyField(TaskDieta,blank=True,related_name="dieta_time1")
    abed_sport = models.ManyToManyField(TaskSport,blank=True,related_name="sport_time2")
    abed_dieta = models.ManyToManyField(TaskDieta,blank=True,related_name="dieta_time2")
    kechki_sport = models.ManyToManyField(TaskSport,blank=True,related_name="sport_time3")
    kechki_dieta = models.ManyToManyField(TaskDieta,blank=True,related_name="dieta_time3")
    weight_limit = models.IntegerField(default=1)
    def __str__(self):
        return self.name + " " + str(self.weight_limit)

class WeeklyProgram(models.Model):
    title = models.CharField(max_length=255)
    dushanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day1")
    seshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day2")
    chorshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day3")
    payshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day4")
    juma = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day5")
    shanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day6")
    yakshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day7")
    intended_weight = models.PositiveIntegerField(default=1)
    last_update = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title_uz = models.CharField(max_length = 40, null = True, blank=True)
    title_ru = models.CharField(max_length = 40, null = True, blank=True)
    title_en = models.CharField(max_length = 40, null = True, blank=True)

    img = models.ImageField(upload_to="info/")
    uz_text = models.TextField()
    en_text = models.TextField()
    ru_text = models.TextField()

    
    def __str__(self): 
        return str(self.title_uz)

# class InfoAboutUs(models.Model):
#     uz_title = models.CharField(max_length=555)
#     en_title = models.CharField(max_length=555)
#     ru_title = models.CharField(max_length=555) 
    

#     def __str__(self):
#         return self.uz_title

class Footer(models.Model):
    address = models.CharField(max_length=55, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.URLField()
    instagram = models.URLField()
    telegram = models.URLField()
    application = models.URLField()
    work_time = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.phone
    
class HistoryTask(models.Model):
    task = models.ForeignKey(DayTask,on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField(default=0)
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)
    night = models.BooleanField(default=False)
    
    def __str__(self):
        return self.date


class SearchStatic(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    
    text_uz = models.TextField()
    text_en = models.TextField()
    text_ru = models.TextField()

    img = models.ImageField(upload_to="static/search/")

    def __str__(self):
        return self.title_uz

class CardFastLossType(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    
    img1 = models.ImageField(upload_to='card/fastloss/')
    title_uz1 = models.CharField(max_length=255)
    title_ru1 = models.CharField(max_length=255)
    title_en1 = models.CharField(max_length=255)
    
    text_uz1 = models.TextField()
    text_ru1 = models.TextField()
    text_en1 = models.TextField()

    img2 = models.ImageField(upload_to='card/fastloss/')
    title_uz2 = models.CharField(max_length=255)
    title_ru2 = models.CharField(max_length=255)
    title_en2 = models.CharField(max_length=255)
    
    text_uz2 = models.TextField()
    text_ru2 = models.TextField()
    text_en2 = models.TextField()
    
    def __str__(self) -> str:
        return self.title_uz

class QuestionAnswer(models.Model):
    question_uz = models.TextField()
    answer_uz = models.TextField()
    question_ru = models.TextField()
    answer_ru = models.TextField()
    question_en = models.TextField()
    answer_en = models.TextField()

    def __str__(self) -> str:
        return self.question_uz
