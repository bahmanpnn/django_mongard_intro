from django import forms

class TodoCreateForm(forms.Form):
    title=forms.CharField(label='title',max_length=100)
    body=forms.CharField(label="body")
    created_date=forms.DateTimeField(required=False)