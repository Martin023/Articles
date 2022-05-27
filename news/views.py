from django.shortcuts import render,redirect
import datetime as dt
from .models import Article


# Create your views here.
from django.http import HttpResponse,Http404

def welcome(request):
    return render(request,'welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})


# View Function to present news from past days

def past_days_news(request, past_date):
    ##For our past_days_news view function we first import the redirect function from
    #  the django.shortcuts. We use this function so that we can redirect a User to the news_today view 
    # function if the date they had entered was the same as today's date. We then render the template 
    # file with the date context variable.


    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
    
        return redirect(news_today)
    news = Article.days_news(date)
    return render(request, 'all-news/welcome.html', {"date": date,"news":news})


#We create a new class method search_by_title which takes in a search_term  as a second argument.
#This method will allow us to filter the all the Articles in our database and return ones matching to our search query.

# We filter the model data using the __icontains query filter.
#  This filter will check if any word in the titlefield of our articles matches the search_term.


def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


        
#reate the view function and pass in the integer article_id from the URL.
#  We then query the database for a single object using the get function.
#  and pass in the article_id.
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})



# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def past_days_news(request,past_date):
#         # Converts data from the string Url
    
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()

#     day = convert_dates(date)
#     html = f'''
#         <html>
#             <body>
#                 <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)