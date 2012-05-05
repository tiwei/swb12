from django import forms

class SubmitRequest(forms.Form): #Modify it as possible
    title = forms.CharField(max_length=100)
    message = forms.CharField()
    message = forms.CharField() #TODO link to a user
    company = forms.BooleanField(required=False)
    skills = forms.CharField()
    
    

