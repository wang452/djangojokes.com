from django.db import models

# import reverse to use in get_absolute_url function
from django.urls import reverse

# import unique_slug from app common\utils\text.py to generate slug string
from common.utils.text import unique_slug

# new - associate user to joke to get AUTH_USER_MODEL 
from django.conf import settings

# Create Joke models here.
class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    
    # new - associate user to joke with one-to-many relationship
    # one user many have more than one jokes
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    # column category defined many-to-one relationship with Category model
    # where many jokes for one category
    # use string 'Category' instead of Category because Joke model is defined
    # before the Category model.
    # other option is moved the Class Category definition above Joke model
    # to avoid the error 'NameError: name 'Category' is not defined
    # add null=True to run makemigrations and migrate to database because
    # category field is not existed in existing row joke in Joke table
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    # add field tags to Joke model that has many-to-many relationship 
    # with the Tag model where one joke can assigned with many tags and one tag
    # assigned to one joke
    # add blank=True to make tags field as optional instead of required by default
    tags = models.ManyToManyField('Tag', blank=True)

    # add new slug field to Joke model that is unique and not editable
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # return absolute url to the JokeDetailView template
    def get_absolute_url(self):
        # change arg pass in from primary key id to slug string
        return reverse('jokes:detail', args=[self.slug])
        # return reverse('jokes:detail', args=[str(self.pk)])

    # override the save() method to set the value of slug field
    def save(self, *args, **kwargs):
        if not self.slug:  # for all new records, slug does not have value
            value = str(self)  # get the value of object from question field

            # generate new slug string from passed-in value and model itself
            self.slug = unique_slug(value, type(self)) 

        # call the super.save() method to save the data
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question


# Create Category model here
class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category

    # override default plural form of model name is just the name of model
    # followed by an "s". Use inner class Meta with verbose_name_plural to
    # override the default
    # add ordering by category instead of default random order to display
    # the category as option in select html form control
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category']

# Create Category model here
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:tag', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag
    

    # override the default random order to display the tags in select option
    class Meta:
        ordering = ['tag']

