from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('sport', SportViewSet)
router.register('comment', CommentViewSet)
router.register('advice', AdviceViewSet)
router.register('new', NewViewSet)
router.register('homeheader', HealthAppViewSet)
router.register('category', CategoryProductViewSet)
router.register('motivation_letter', MotivationLetterViewSet)
router.register('fastlost', FastLostView)