from rest_framework import serializers
from .models import *


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):

    recipe = serializers.PrimaryKeyRelatedField(many=False, queryset=Recipe.objects.all())
    ingredient = IngredientSerializer(many=False)

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'recipe', 'quantity', 'units', 'cost_in_pounds')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('name', 'recipe_ingredients', 'serves', 'kcal', 'protein', 'carbohydrate',
                  'fat', 'saturated_fat', 'fibre', 'sugar', 'salt')


class MealSerializer(serializers.HyperlinkedModelSerializer):

    recipe_id = serializers.PrimaryKeyRelatedField(source='recipe', queryset=Recipe.objects.all(), write_only=True)
    recipe = RecipeSerializer(many=False, read_only=True)

    class Meta:
        model = Meal
        fields = ('recipe', 'recipe_id', 'timestamp', 'purchased_ingredients', 'user')
        read_only_fields = ('timestamp', 'recipe')

