from .models import forms
from .models import Contactform

class Contact_f(forms.ModelForm):
    class Meta:
        model = Contactform
        fiedls = "__all__"



