from django import forms
from datetime import date
from django.core.validators import RegexValidator

from semi_rest_app.models import Show

class UserForm(forms.Form):
    title = forms.CharField(
        min_length=1, max_length=255,required=True, validators=[
            RegexValidator(
                regex=r'^[A-Za-z\s]+$',
                message="Title can only contain characters and spaces."
            )
        ] ,error_messages={
            "required":"Title must not be empty."
        },
        
    )
    network = forms.CharField(
        min_length=1, max_length=255,required=True, validators=[RegexValidator(
            regex=r'^[a-zA-z/s]+$',
            message= 'Network can only contain characters and spaces'
        )]
        ,error_messages={
            "required":"Network must not be empty."
        }
    )
    release_date = forms.DateField(
        required=True,
        widget= forms.DateInput(attrs={"type":"date"}),
        error_messages={"required":"Date cannot be empty"}

    )
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows":4}), error_messages={"required":"Description cannot be empty"})
    
    url = forms.URLField(required=True, error_messages={"required":"Image URL cannot be empty."})

    def clean_release_date(self):
        release_date = self.cleaned_data.get("release_date")
        if release_date and release_date > date.today():
            raise forms.ValidationError("The release date cannot be in the future")
        return release_date
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        release_date = cleaned_data.get('release_date')
        if Show.objects.filter(title__iexact = title, release_date = release_date).exists():
            raise forms.ValidationError("Duplicate Listing!!")
