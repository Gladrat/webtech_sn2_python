from django import forms


JOBS = [
    ("rh", "Ressources humaines"),
    ("mkg", "Marketing"),
    ("dg", "Direction générale"),
]


# from .models import User

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=12, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect())
    cgu_accept = forms.BooleanField(initial=False)
    
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        # user = User.objects.get(pseudo=pseudo)
        # if user:
        #     raise forms.ValidationError("Ce pseudo existe déjà !")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de $")
        return pseudo