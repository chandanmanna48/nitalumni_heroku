from django import forms
from .models import Profile,Gallery

class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('regdno','profile_pic','passout_year','branch','profession','company','work_location','designation','work_country','contactno','street_name','street_number','city','state','district','country')

class Gallery_form(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title','description','images')