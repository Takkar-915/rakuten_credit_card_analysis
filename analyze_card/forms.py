from django import forms

class CsvForm(forms.Form):
    uploaded_file = forms.FileField()


