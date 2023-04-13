from django import forms

from .models import Classroom

class ClassroomCreationForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name']