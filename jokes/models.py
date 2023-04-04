from django.db import models

# import reverse to use in get_absolute_url function
from django.urls import reverse

# import unique_slug from app common\utils\text.py to generate slug string
from common.utils.text import unique_slug

# Create Joke models here.
class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)

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