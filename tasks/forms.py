from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'category']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('category', css_class='form-group col-md-6 mb-3'),
                Column('due_date', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Submit('submit', 'Add Task', css_class='btn btn-primary')
        )
        
        # Customize field labels and attributes
        self.fields['title'].label = 'Task Title'
        self.fields['category'].label = 'Category'
        self.fields['due_date'].label = 'Due Date & Time'
        
        # Add Bootstrap classes
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        self.fields['due_date'].widget.attrs.update({'class': 'form-control'})
