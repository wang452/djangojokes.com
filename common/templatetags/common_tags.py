import random

# import template module to create custom tag
from django import template

# import Joke from the djangojokes database model jokes defined in models.py
from jokes.models import Joke

# Create an instance of template.library() to register the custom tag
register = template.Library()

# Register this custom tag as inclusion_tag type named random_joke
# This custom tag provides data context for the associated html template
# which is located in the templates\common folder 
@register.inclusion_tag('common/joke.html')
def random_joke():
    count = Joke.objects.count()
    if count > 0: # In case we haven't added any jokes yet
        i = random.randint(0, count-1) # get random between 9 to count-1
        joke = Joke.objects.all()[i]
        return {'joke': joke}
    else:
        return {
            'joke': {
                'question': 'You know what is funny?',
                'answer': 'There are no jokes in the database.'
            }
        }
