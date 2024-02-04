from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    title=forms.CharField(label='title',max_length=100)
    body=forms.CharField(label="body")
    created_date=forms.DateTimeField(required=False)

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=('title','body')