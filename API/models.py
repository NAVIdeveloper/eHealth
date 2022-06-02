from datetime import datetime
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
    register_date = models.DateField(null=True,blank=True)
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
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='news/')
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

class TitleAdvice(models.Model):
    uz_title = models.CharField(max_length=255)
    en_title = models.CharField(max_length=255)
    ru_title = models.CharField(max_length=255)
    def __str__(self):
        return self.uz_title

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

class MotivationLetter(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    img = models.ImageField(upload_to='motivation_letter/')
    def __str__(self):
        return self.text_uz


class FastLost(models.Model):
    image = models.ImageField(upload_to='fastlost/')
    name_uz = models.CharField(max_length=40, blank=True, null=True)
    name_ru = models.CharField(max_length=40, blank=True, null=True)
    name_en = models.CharField(max_length=40, blank=True, null=True)


    def __str__(self):
        return self.name_uz



class DailyMotivation(models.Model):
    text_uz = models.CharField(max_length=300, null=True, blank=True)
    text_ru = models.CharField(max_length=300, null=True, blank=True)
    text_en = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.text_uz

class WeeklyMusic(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    music = models.FileField(upload_to='music/')

    def __str__(self) -> str:
        return self.name


class TaskSport(models.Model):
    activity = models.ForeignKey(Sport, on_delete=models.CASCADE)
    duration = models.IntegerField()
    total_calories =models.IntegerField()
    def __str__(self): 
        return self.activity.name
    

class TaskDieta(models.Model):
    product = models.ManyToManyField(Product)
    grams = models.IntegerField()
    total_calories =models.IntegerField()
    def __str__(self): 
        return self.product.name

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
        return self.name

class WeeklyProgram(models.Model):
    title = models.CharField(max_length=255)
    dushanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day1")
    seshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day2")
    chorshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day3")
    payshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day4")
    juma = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day5")
    shanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day6")
    yakshanba = models.ForeignKey(DayTask,on_delete=models.CASCADE,related_name="day7")

    def __str__(self):
        return self.title

