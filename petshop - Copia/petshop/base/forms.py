from django import forms
from base.models import contatom,reservam

class contatoform(forms.ModelForm):
    class Meta:
        model = contatom
        fields = ['nome','email','mensagem']


class reservaform(forms.ModelForm):
    class Meta:
        model = reservam
        fields = ['nome_do_pet','telefone','dia_da_reserva','observaçao']
   