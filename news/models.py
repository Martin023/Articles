from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    
    def save_editor(self):
        self.save()

class Tags(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=30)
    editor = models.ForeignKey(Editor,on_delete=models.DO_NOTHING )
    tags = models.ManyToManyField(Tags)
    published_date = models.DateTimeField(auto_now_add=True)
    post = models.CharField(max_length=200)
    article_image = models.ImageField(upload_to = 'articles/')

    @classmethod
    #Django provides a query filter date that allows us to convert out datetimefield to a date.
    #  Query filters allow us to customize our queries to fit our needs.
    #  They are defined using two underscores before the field.
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(published_date__date = today)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


    @classmethod

    ##We create a class method days_news. 
    # This method takes a date object as an argument.
    #  It then filters the model data according to the given date and returns it.
    def days_news(cls,date):
        news = cls.objects.filter(published_date__date = date)
        return news
   

    def __str__(self):
        return self.title

 
