from django.shortcuts import render

# Create your views here.

import html

# import reverse_lazy to redirect page to jobs template thanks.html
from django.urls import reverse_lazy

# import FromView to create form and TemplateView for template html
from django.views.generic import CreateView, FormView, TemplateView

# import send_email utility to send email via sendgrid API
from common.utils.email import send_email

# import Job and Application models from jobs\models.py
from .models import Applicant

# import class JobApplicationFrom in jobs\forms.py to display form fields
from .forms import JobApplicationForm

"""Replace JobAppView to inherit CreateView with model Applicant
   Also copy the templates\jobs\joke_writer.html to applicant_form.html 
   as CreateView infer with template name from the model name with postfix
   _form.html
# define template and form fields to use for display the form
class JobAppView(FormView):
    template_name = 'jobs/joke_writer.html'
"""
class JobAppView(CreateView):
    model = Applicant
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobs:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'receiver@example.com'
        
        # required by sendgrid since did not set default in send_email func
        from_email = 'sender@example.com'
        subject = 'Application for Joke Writer'
        content = f'''<p>Hey HR Manager!</p>
            <p>Job application received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        # need from_email argument since did not set default value
        # in send_email function parameter
        send_email(to, subject, content, from_email)
        return super().form_valid(form)

# html template for form submitted success
class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'
