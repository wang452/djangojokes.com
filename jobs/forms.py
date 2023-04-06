# import forms to create class job application form 
from django import forms
from datetime import datetime

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus':True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'size': 50,
                'placeholder': 'https://www.example.com',
            }
        )
    )
    emp_types = (
        (None, '---Please Choose---'),
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract-work', 'Contract work')
    )
    employment_type = forms.ChoiceField(choices=emp_types)
    YEARS = range(datetime.now().year, datetime.now().year+2)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.',
        widget=forms.SelectDateWidget(
                years=YEARS,
        )
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
