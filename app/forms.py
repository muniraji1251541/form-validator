from django import forms
from django.core import validators

def validate_for_z(value):
    if value[0]=='z':
        raise forms.ValidationError('Name cannot start with z')

def validation_for_len(value):
    if len(value)<3:
        raise forms.ValidationError('Length is low')

def validation_for_age(value):
    if value<20:
        raise forms.ValidationError('Age should be more then 20')


class Form_validator(forms.Form):
    name=forms.CharField(max_length=20,validators=[validate_for_z,validators.MinLengthValidator(3)])
    age=forms.IntegerField(validators=[validation_for_age])
    email=forms.EmailField()
    reemail=forms.EmailField()
    number=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=10,widget=forms.HiddenInput,required=False)

    def clean(self):
        em=self.cleaned_data['email']
        rem=self.cleaned_data['reemail']
        if em!=rem:
            raise forms.ValidationError('Email not matched')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('Bot is catched')