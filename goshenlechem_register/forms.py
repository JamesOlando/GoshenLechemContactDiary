from django import forms
from .models import Diary


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary
        fields = ('firstname','secondname','dateofbirth','companyofoperation','position','country','contact','email')
        labels = {
            'firstname':'First Name',
            'secondname':'Second Name',
            'dateofbirth':'Date Of Birth',
            'companyofoperation':'Company Of Operation',
            'position':'Position',
            'country':'Country',
            'contact':'Contact',
            'email':'Email',
        }
    def __init__(self, *args, **kwargs):
        super(DiaryForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['country'].required = False