from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=50,unique = True)
    profile_image = models.ImageField(upload_to = 'static/photos',blank=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 
    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField(blank=False)
    time = models.TimeField()
    date = models.DateField()
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    author = models.ForeignKey(User,on_delete=CASCADE,null=False,blank=False,related_name = 'questions')
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions' 

class Answer(models.Model):
    answer = models.TextField(blank=False)
    time = models.TimeField()
    date = models.DateField()
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    question = models.ForeignKey(Question,on_delete=CASCADE,null=True,related_name = 'answers')
    author = models.ForeignKey(User,on_delete=CASCADE,null=False,related_name='answers')


