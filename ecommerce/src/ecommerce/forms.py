from django import forms

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","type":"text","placeholder":"User Name","name":"fullname"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form_control","type":"email","placeholder":"User E-Mail","name":"email"}))
	content = forms.CharField(widget=forms.Textarea(attrs={"class":"form_control","name":"content","cols":"30","rows":"10","placeholder":"Your Content"}))

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'gmail.com' in email:
			raise forms.ValidationError('Email Must Be From Gmail.com.')
		return email


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form_control","placeholder":"User Name","name":"username"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Password","name":"password"}))
