from django import forms
from .models import it_is_fine

class there_you_go(forms.ModelForm):
    class Meta:
        model = it_is_fine
        fields = ['field1_e', 'field2_p']
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['field1_e'].initial = ''
        self.fields['field2_p'].initial = ''    