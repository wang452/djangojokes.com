# import forms to create class job application form 
from django import forms
from datetime import datetime

# add custom validator to validate future date from input 
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

# import model Applicant for the JobApplicationForm inner class Meta
from .models import Applicant

# ensure value entered for required fields
def validate_checked(value):
    if not value:
        raise ValidationError("Required.")


class JobApplicationForm(forms.ModelForm):

    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI')
    )

    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text = 'Check all days that you can work.',
        widget = forms.CheckboxSelectMultiple(
            attrs = {'checked':True}
        )
    )

    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true.',
        validators=[validate_checked]
    )

    class Meta:
        model = Applicant
        fields = (
            'first_name', 'last_name', 'email', 'website', 'employment_type',
            'start_date', 'available_days', 'desired_hourly_wage',
            'cover_letter', 'confirmation', 'job')
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'website': forms.TextInput(
                attrs = {'placeholder':'https://www.example.com'}
            ),
            'start_date': forms.SelectDateWidget(
                attrs = {
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = range(datetime.now().year, datetime.now().year+2)
            ),
            'desired_hourly_wage': forms.NumberInput(
                attrs = {'min':'10.00', 'max':'100.00', 'step':'.25'}
            ),
            'cover_letter': forms.Textarea(attrs={'cols': '100', 'rows': '5'})
        }
        error_messages = {
            'start_date': {
                'past_date': 'Please enter a future date.'
            }
        }


# replace JobApplicationForm to inherit forms.ModelForm to use model Applicant

# move validate_future_date to the jobs\models.py where new Job and
# Applicant models created
"""
def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )
"""

# replace JobApplicationFrom to inherit forms.ModelForm with model Applicant
# All fields in this form are redefined in the Applicant model in models.py
# use the inner class Meta in redefined JobApplicationForm above to modify
# widgets attributes of the field in the form for HTML form control display 
"""
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
        ('contract', 'Contract work')
    )
    employment_type = forms.ChoiceField(choices=emp_types)
    YEARS = range(datetime.now().year, datetime.now().year+2)

    
    # start_date = forms.DateField(
    #   help_text='The earliest date you can start working.',
    #    widget=forms.SelectDateWidget(
    #        years=YEARS,
    #        attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}
    #    ),
    #    validators=[validate_future_date],
    #    error_messages={'past_date': 'Please enter a future date.'}
    #)
    

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
    
    # change to TypedMultipleChoiceField to convert string to int 
    # with coerce option to send to server
    # available_date = forms.MultipleChoiceField(
    available_days = forms.TypedMultipleChoiceField(
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
        label='I certify that the information I have provided is true.',
        # add validator to ensure confirmation is checked
        validators=[validate_checked]
    )
"""
