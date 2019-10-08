from django import forms


class CreateWordForm(forms.Form):
    word_text = forms.CharField('Word Text', max_length=100)
    desc_text = forms.Textarea(attrs={'style': 'width: 100%'})

