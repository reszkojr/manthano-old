from django import forms

from .models import Classroom

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Div, Submit
from crispy_tailwind.tailwind import CSSContainer

class ClassroomCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        individual_inputs = {"text": "text"}
        self.helper.css_container = CSSContainer(individual_inputs)
        self.helper.layout = Layout(
            HTML('<label for="name" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Class\' name:</label>'),
            Field("name", placeholder="Best class in the world!", css_class="text-input w-full mb-4"),
            HTML('<label for="code" class="text-left block mb-1 text-sm font-medium text-gray-900 dark:text-white">Class\' code:</label>'),
            Field("code", placeholder="dabestclass", css_class="text-input w-full mb-4"),
            Div(
                HTML('<button type="submit" class="text-white font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center bg-blue-600 hover:bg-blue-700 outline-none border-none focus:outline-neonblue-600 mx-auto">Create</button>'),
            ),
        )
        self.helper.form_show_labels = False
        self.helper.form_method = 'POST'
    class Meta:
        model = Classroom
        fields = ['name', 'code']