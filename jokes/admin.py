from django.contrib import admin

# Register your models here.

# Import the Joke model from jokes app
# add Category model to be manage by Django Admin tool
from .models import Category, Joke, Tag

# Register Joke model to be managed and create JokeAdmin
@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke

    # Specify the fields display for jokes lising
    list_display = ['question', 'created', 'updated']

    # Return empty tuple if create a new joke 
    # Return value of created and updated fields for update an existing joke
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object - add slug field as read-only
            return ('slug', 'created', 'updated')

        return ()

# Register Category model to be managed and create CategoryAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

# Register Tag model to be managed in Django Admin tool
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['tag', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()
