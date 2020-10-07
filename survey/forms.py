from django import forms
from survey.models import Profil, Otvet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField, ModelForm
from survey.models import *


class ExtendedUserCreationForm(UserCreationForm):

    
    email = forms.EmailField(required=True)
   
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2'  )

    def save(self, commit=True):
        user = super().save(commit==False)
        user.email = self.cleaned_data['email']
       

        if commit:
            user.save()
        return user

class UserProfil(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('age', 'specialite', 'language')
   


   
class OtvetForm(forms.ModelForm):
    #stimul1 = Stimul_slov.objects.all()
    #def __init__(self, *args, **kwargs):
        # self._errors = None
        #super(OtvetForm, self).__init__(*args, **kwargs)
        
        
        #forms.ModelForm.__init__(*args, **kwargs)
        #self.fields = []
        #self.fields.append({'stimul':"123",#field.stimul,
                   # 'answer': "12333"})#field.answer})

        # for field in Otvet.objects.all():
        #     self.fields.append({'stimul':field.stimul,
        #                         'answer':field.answer})
     class Meta:
         model = Otvet
         fields = ('answer', 'stimul' )
         widgets = {"stimul": forms.HiddenInput()}
         #fields = ('stimuls', )
      
       
#class AnsForm(forms.ModelForm):
#    stm = Stimul_slov.objects.all()
#    class Meta:
#        model = Answer
#        fields = ('__all__')