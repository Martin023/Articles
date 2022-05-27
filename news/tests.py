
from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt
# Create your tests here.
#This class inherits from the TestCase class. 
# We then create a setUp method that allows us to create an instance of the Editor class before every test.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')


    # Testing  instance
    # We create a test_instance test to confirm that the object is being instantiated correctly.


    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method

    ##NB all test methods must begin with test_ 
    def test_save_method(self):

        #or use self.editor.save_editor() to save the editor instance
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ArticleTestClass(TestCase):
    # we create a test class ArticleTestClass to test our Article model. 
    # We create the setUp method that allows us to define a new Editor and tag instance.

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        #Since the Editor and Article share a One to Many relationship we have to save the editor instance first
        #  then equate it to the editor field in the Article model.

        # Creating a new tag and saving it


        #The Article and tags share a Many to Many relationship.
        #  This means for us to create a join table we need the id property of both model instances.
        #  So first, we save both the tags and article instance to the database 
        # then we use the add function on the ManyToManyField to add a new tag.
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        # We also define a tearDown method that will allow us to delete all instances
        #  of our models from the database after each test
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()


    def test_get_news_today(self):

        ##create a new test inside the ArticleTestClass. 
        # We call the todays_news class method that is to get the news for that particular day.
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        #We create a new test to confirm getting news according to a given date.
        #  We define a test date string and convert it to a date object.
        #  We then call the days_news class method and pass in the date object.
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)


# RUNNING TESTS

## python3 manage.py test news<-- name of app  
