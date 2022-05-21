from django.urls import path
from .views import  *

urlpatterns = [
    path("register/",View_Register),
    
    path("category-product/",View_Category),
    path("sport/",View_Sport),
    path("product/",View_Product),

    path("comment/",CommentView.as_view()),
    
    path("news/",View_News),
    path("news/<int:pk>/",View_News_Detail),

    path("advice/",View_Advice),
    path("advice/random/",View_Advice_Random),    

    path("healthyUp/",View_Health_App)    
]