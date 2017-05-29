from django import forms


class ContactForm(forms.Form):
    flavor = forms.CharField(max_length=100)
    name = forms.CharField(max_length=50)
    phone = forms.IntegerField(max_value=11)
    # adress = forms.CharField(max_length=120)
    data = forms.DateTimeField()
