from django.db import models


class Recipe(models.Model):
    # Define the tuple for the choices of recipe_type. The first element in each tuple is the
    #   actual value to be set on the model, and the second element is the human-readable name.
    BREAKFAST = 'BR'
    LUNCH = 'LU'
    DINNER = 'DI'
    DESSERT = 'DE'
    RECIPE_TYPE_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DESSERT, 'Dessert'),
    )

    # Define the fields of the Model for a recipe
    name = models.CharField(max_length=80)
    description = models.TextField()
    rating = models. PositiveIntegerField(default=1)
    recipe_type = models.CharField(max_length=2, choices=RECIPE_TYPE_CHOICES, default=DINNER)
    recipe_steps = models.TextField(default='Add recipe steps!')
    ingredients = models.TextField(default='Add ingredients!')
    image = models.ImageField(upload_to='images/', default = 'images/default_image.jpg')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
