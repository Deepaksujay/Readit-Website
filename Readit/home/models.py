from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import related

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to = 'profile_pics',blank=True)
    verified = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 
    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 
    def __str__(self):
        return self.category
class Question(models.Model):
    question = models.TextField(blank=True)
    time = models.TimeField()
    date = models.DateField()
    likes = models.ManyToManyField(User,blank=True,related_name='q_likes')
    category = models.ForeignKey(Category,default = None,on_delete=RESTRICT,blank=False,related_name='questions')
    author = models.ForeignKey(User,on_delete=CASCADE,null=False,blank=False,related_name = 'questions')
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions' 
    def __str__(self):
        return self.author.name+'-'+str(self.time)+'-('+str(self.date)+')'

class Answer(models.Model):
    answer = models.TextField(blank=False)
    time = models.TimeField()
    date = models.DateField()
    likes = models.ManyToManyField(User,blank = True,related_name='a_likes')
    dislikes = models.ManyToManyField(User,blank = True,related_name='a_dislikes')
    question = models.ForeignKey(Question,on_delete=CASCADE,null=True,related_name = 'answers')
    author = models.ForeignKey(User,on_delete=CASCADE,null=False,related_name='answers')
    def __str__(self):
        return self.author.name+'-'+str(self.time)+'-('+str(self.date)+')'


