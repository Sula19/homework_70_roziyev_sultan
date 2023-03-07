from django import forms
from django.forms import widgets
from webapp.models import Tasks
from webapp.validators import CustomSummaryValidator, CustomDescriptionValidator


class TasksForm(forms.ModelForm):
    summary = forms.CharField(validators=(CustomSummaryValidator(),))
    description = forms.CharField(widget=widgets.Textarea(), validators=(CustomDescriptionValidator(),))

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Кратоке описание',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип',
        }
