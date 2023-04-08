# import forms to create class job application form 
from django import forms
from datetime import datetime

# add custom validator to validate future date from input 
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus':True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    
    # replace website from forms.URLField to forms.CharField to add
    # built-in validators URLValidator
    # website = forms.URLField(
    website = forms.CharField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'size': 50,
                'placeholder': 'https://www.example.com',
            }
        ),
        validators=[URLValidator(schemes=['http', 'https'])]
    )
    emp_types = (
        (None, '---Please Choose---'),
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract-work', 'Contract work')
    )
    employment_type = forms.ChoiceField(choices=emp_types)
    YEARS = range(datetime.now().year, datetime.now().year+2)

    """
    start_date = forms.DateField(
        help_text='The earliest date you can start working.',
        widget=forms.SelectDateWidget(
            years=YEARS,
            attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}
        ),
        validators=[validate_future_date],
        error_messages={'past_date': 'Please enter a future date.'}
    )
    """

    start_date = forms.DateField(
        help_text='The earliest date you can start working.',
        widget=forms.SelectDateWidget(
            years=YEARS,
            attrs={'style': 'width: 31%; display: inline-block;'}
            # attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}
        ),
        validators=[validate_future_date],
        error_messages={'past_date': 'Please enter a future date.'}
    )

    date_avail = (
        ('1', 'MON'),
        ('2', 'TUE'),
        ('3', 'WED'),
        ('4', 'THu'),
        ('5', 'FRI')
    )
    
    # change to TypedMutlipleChoiceField to convert string to int 
    # with coerce option to send to server
    # available_date = forms.MultipleChoiceField(
    available_date = forms.TypedMultipleChoiceField(
        choices=date_avail,
        coerce=int,
        help_text='Select all days that you can work.',
         widget=forms.CheckboxSelectMultiple(
            attrs={
                'checked': True
            }
         )
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'min': '10.00',
                'max': '100.00',
                'step': '.25'
            }
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )
