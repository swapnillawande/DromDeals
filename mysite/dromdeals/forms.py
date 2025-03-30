from django import forms
from dromdeals.models import PostProduct, ProductComments


class PostProductForm(forms.ModelForm):

    class Meta():
        model = PostProduct
        fields = ('user', 'title', 'text', 'photo')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }



class ProductCommentsForm(forms.ModelForm):

    class Meta():
        model = ProductComments
        fields = ('user', 'text')

        widgets = { 
            'user': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
