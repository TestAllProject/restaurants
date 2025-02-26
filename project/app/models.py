from django.db import models

# Create your models here.

class About_section1(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class About_section2(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
class food_category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"
    
class menu(models.Model):
    image = models.ImageField(upload_to='media/')
    food_name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(food_category, on_delete=models.CASCADE, related_name='food')
    
    def __str__(self):
        return f'{self.food_name}'
    
# class book_table(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=254)
#     date = models.DateField(auto_now=False, auto_now_add=False)
#     time = models.TimeField(auto_now=False, auto_now_add=False)
#     number_of_people = models.IntegerField()

#     def __str__(self):
#         return f'{self.name}'