from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.user  
    


class UserActivity(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    type = models.CharField(max_length=100)  
    duration = models.CharField(max_length=100)
    calories_burned = models.CharField(max_length=50)
    date = models.DateField()  
    prof_img = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, null=True) 

    def __str__(self):
        return self.type
    

  
