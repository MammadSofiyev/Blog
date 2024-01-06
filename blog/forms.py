from django import forms
from .models import Post,Comment,Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('image_field', 'title', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Addcomm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('name','body')
        widgets = {
         'name':forms.TextInput(attrs={'class':'form-control' }),
         'body':forms.Textarea(attrs={'class':'form-control' })
         
         
         }




class Contact(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ('username','email','message')
        widgets = {
         'username':forms.TextInput(attrs={'class':'form-control' }),
         'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
         'message':forms.Textarea(attrs={'class':'form-control' })

         
         }
