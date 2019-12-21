from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'style': 'padding: 2px; padding-left: 8px;border: none;width: 100%; height: 40px;background: rgba(0,0,0,0.4);color: white;',
                'placeholder': 'Write your name here'
            }
        )
    )
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'style': 'border: none; padding: 2px;width: 100%; padding-left: 12px;height: 40px;background: rgba(0,0,0,0.4);color: white;'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
                              'style': 'resize:none;border: none;padding-left: 12px;padding: 2px;width: 100%; height: 100px;background: rgba(0,0,0,0.4);color: white;'})
    )
