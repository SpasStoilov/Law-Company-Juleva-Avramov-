from django import forms
from website.models import Employees
from website.models import Clients


class ConsultationsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'
        labels = {
            'client_first_name': 'Име',
            'client_last_name': 'Фамилия',
            'lawyer_name': 'Лист с адвокати',
            'text': 'Текст',
            'email_client': 'Е-маил',
            'image': 'Качете файл (не е задължително)',
            'number': 'Телефон за връзка (не е задължително)'
        }

        widgets = {
            'client_first_name': forms.TextInput(attrs={'class': 'form-control', 'label': 'Име'}),
            'client_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lawyer_name': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'email_client': forms.EmailInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'})
        }

