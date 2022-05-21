from datetime import datetime
from distutils.command.upload import upload
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
    kaloriya = models.IntegerField()

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    ru_name = models.CharField(max_length=255)
    
    video = models.URLField(null=True,blank=True)
    kaloriya = models.IntegerField()
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    image = models.ImageField(upload_to='profile/',null=True,blank=True)
    going_to_loss = models.IntegerField(default=0,null=True,blank=True)
    user_type = models.IntegerField(choices=(
        (1, "client"),
        (2, "expert")
    ), default=1)
    bio = models.TextField(null=True,blank=True)
    video = models.URLField(null=True,blank=True)
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
    task_sport_can_not = models.ManyToManyField(Sport)
    task_dieta_can_not = models.ManyToManyField(Sport, related_name="NoDieta")
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
        return self.name

class HistoryReyting(models.Model):
    expert = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="from_user")
    star = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} : {str(self.star)} -> {self.expert.username}"

class TaskSport(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    activity = models.ForeignKey(Sport, on_delete=models.CASCADE)
    duration = models.IntegerField()


class TaskDieta(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    morning = models.ManyToManyField(Product, related_name='morning_time')
    lunch = models.ManyToManyField(Product, related_name='lunch_time')
    night = models.ManyToManyField(Product)
    limit = models.DateField()

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
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    en_title = models.CharField(max_length=255)
    en_text = models.CharField(max_length=255)
    
    ru_title = models.CharField(max_length=255)
    ru_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text

class Normal(models.Model):
    age_start = models.IntegerField()
    age_end = models.IntegerField()
    height = models.IntegerField(unique=True)
    male_weight = models.FloatField()    
    male_weight = models.FloatField()    
    def __str__(self):
        return str(self.height)

class HealthApp(models.Model):
    logo = models.ImageField(upload_to="healthapp/")
    
    title_uz  = models.CharField(max_length=255)
    text_uz = models.TextField()
    text2_uz = models.CharField(max_length=255)
    
    title_en  = models.CharField(max_length=255)
    text_en = models.TextField()
    text2_en = models.CharField(max_length=255)
    
    title_ru  = models.CharField(max_length=255)
    text_ru = models.TextField()
    text2_ru = models.CharField(max_length=255)
    
    img = models.ImageField(upload_to="healthapp/")

    def __str__(self):
        return self.title_uz