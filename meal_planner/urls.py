from django.conf.urls import url, include
from rest_framework import routers
from .views import IngredientViewSet, MealViewSet, RecipeViewSet, RecipeIngredientViewSet

router = routers.DefaultRouter()
router.register(r'ingredient', IngredientViewSet)
router.register(r'meal', MealViewSet)
router.register(r'recipe', RecipeViewSet)
router.register(r'recipe-ingredient', RecipeIngredientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]