from django import forms

class NameForm(forms.Form):
    childName = forms.CharField(label='Childs name', max_length=100)
    childAddress = forms.CharField(label='Child\'s Address', max_length=100)
    childPhone = forms.NumField(label='Child\'s Phone Number', max_length=10)
    childParent = forms.CharField(label='Parent\'s Name', max_length=10)
    
