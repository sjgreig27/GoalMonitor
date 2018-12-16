from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=280, blank=True, null=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=2, max_digits=6)
    units = models.CharField(max_length=10, null=True, blank=True)
    cost_in_pounds = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.ingredient.name + '(' + self.quantity + ' ' + self.units + ')'


class Recipe(models.Model):
    name = models.CharField(max_length=280, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, symmetrical=False, through=RecipeIngredient)
    serves = models.IntegerField()
    kcal = models.DecimalField(decimal_places=2, max_digits=6)
    protein = models.DecimalField(decimal_places=2, max_digits=6)
    carbohydrate = models.DecimalField(decimal_places=2, max_digits=6)
    fat = models.DecimalField(decimal_places=2, max_digits=6)
    saturated_fat = models.DecimalField(decimal_places=2, max_digits=6)
    fibre = models.DecimalField(decimal_places=2, max_digits=6)
    sugar = models.DecimalField(decimal_places=2, max_digits=6)
    salt = models.DecimalField(decimal_places=2, max_digits=6)


    @property
    def recipe_ingredients(self):
        return RecipeIngredient.objects.filter(recipe=self)

    def __str__(self):
        return self.name


class Meal(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    purchased_ingredients = models.BooleanField()

    def __str__(self):
        return self.recipe.name

