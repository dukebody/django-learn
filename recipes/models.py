from django.db import models

# Create your models here.


class Recipe(models.Model):
    # id field is automatically added
    # fields are required by default
    author = models.ForeignKey('auth.User')  # link to other model
    name = models.CharField(max_length=256)
    time = models.PositiveIntegerField(
        help_text='# minutes it takes to prepare the recipe'
    )
    serves = models.PositiveIntegerField(
        help_text='# people this recipe serves'
    )
    ingredients = models.TextField()
    procedure = models.TextField()

    def __str__(self):  # self is the recipe instance
        # text representation of a recipe
        return self.name
