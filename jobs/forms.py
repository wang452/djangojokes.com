# import forms to create class job application form 
from django import forms

class JobApplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(initial='https://', required=False)
    emp_types = (
        (None, '---Please Choose---'),
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract-work', 'Contract work')
    )
    employment_type = forms.ChoiceField(choices=emp_types)
    start_date = forms.DateField(
        help_text='The earliest date you can start working.'
    )
    date_avail = (
        ('mon', 'MON'),
        ('tue', 'TUE'),
        ('wed', 'WED'),
        ('thu', 'THu'),
        ('fri', 'FRI')
    )
    available_date = forms.MultipleChoiceField(
        choices=date_avail,
        help_text='Select all days that you can work.'
    )
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )
