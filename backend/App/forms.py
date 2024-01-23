from django import forms
from .models import AssetsIssuance, Staff

class AssignmentForm(forms.ModelForm):
    # asset = forms.CharField(widget=forms.ChoiceField(attrs={"class": "form-control"}))
    class Meta:
        model = AssetsIssuance
        fields = ['asset', 'asset_assignee']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].widget.attrs.update({'class': 'form-control'})
        self.fields['asset_assignee'].widget.attrs.update({'class': 'form-control-2'})

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         feild = ['username', 'fname', 'lname', 'email', 'position', ]