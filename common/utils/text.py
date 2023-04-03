import random
import string

# import slugify to create slug string
from django.utils.text import slugify

def unique_slug(s, model, num_chars=50):
    """
    Return slug of num_chars length unique to model

    `s` is the string to turn into a slug
    `model` is the model we need to use to check for uniqueness
    """
    slug = slugify(s) # create new slug

    # slice slug to max length of num_chars and strip hyphen at the end of line
    slug = slug[:num_chars].strip('-') 
    while True:
        # get record of new slug in the model passed-in
        dup = model.objects.filter(slug=slug)

        # return new slug if not existed in model
        if not dup:
            return slug

        # if existed in model, generate new slug with random string
        # of 10 alphabet letter plus the hyphen between them
        slug = slug[:39] + '-' + random_string(10)
        
# return random string of 10 characters in lowercase
def random_string(num_chars=10):
    letters = string.ascii_lowercase # get all alphabet in lowercase a-z
    # return a string with 10 random alphaget
    return ''.join(random.choice(letters) for i in range(num_chars))
