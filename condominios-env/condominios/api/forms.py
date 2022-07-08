from django import forms
from .models import Condominium, House

class condominium_form(forms.ModelForm):
   class Meta:
      model = Condominium
      fields = [
         'name',
         'code',
         ]
      labels = {
         'name':'Nombre',
         'code':'Codigo',
         }
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-input-text'}) ,
         'code': forms.TextInput(attrs={'class':'form-input-text'}) ,
      }
class house_form(forms.ModelForm):
   class Meta:
      model = House
      fields = [
         'headline',
         'fk_condominium',
         ]
      labels = {
         'headline':'Numero',
         'fk_condominium':'Condominio',
         }
      widgets = {
         'headline': forms.NumberInput(attrs={'class':'form-input-text'}) ,
         'fk_condominium': forms.Select(attrs={'class':'form-input-select'}),
      }