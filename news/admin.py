
from django.contrib import admin
from .models import Editor,Article,Tags

# Register your models here.
# Adding our models to admin page

class ArticleAdmin(admin.ModelAdmin): ##We then specify the filter_horizontal property that
    # allows ordering of many
    # to many fields and pass in the tags article field.
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tags)