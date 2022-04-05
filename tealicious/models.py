from django.db import models


# Create your models here.

class categories(models.Model):
     name = models.CharField(default='', max_length=50, unique=True)

     def __str__(self):
        return self.name

class AddItem(models.Model):
    title=models.CharField(default='',max_length=200)
    category=models.ForeignKey(categories, null=True, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50, default='', blank=True)
    Price=models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def get_all_item_by_category_id(category_name):
        if category_name:
            return AddItem.objects.filter(category__name=category_name)
        else:
            return AddItem.objects.all()

    def __str__(self):
        return self.title


class Event(models.Model):
    Fullname=models.CharField(default='',max_length=100)
    email = models.EmailField(max_length=100, default='')
    number = models.IntegerField(default='')
    venue=models.TextField()
    Date=models.DateField()

    def __str__(self):
        return self.Fullname

class Franchise(models.Model):
    Fullname=models.CharField(default='',max_length=100)
    email = models.EmailField(max_length=100, default='')
    number = models.IntegerField(default='')
    Location=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Fullname



