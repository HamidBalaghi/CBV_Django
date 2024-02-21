from django import forms


# from .models import Person


class PersonAdminForm(forms.ModelForm):
    def clean(self):
        name = self.cleaned_data.get('name')
        if name == 'None':
            raise forms.ValidationError({'name': 'Name cannot be None'})


class SearchForm(forms.Form):
    search = forms.CharField()
