from django import forms
from .models import Category,Location


class EditForm(forms.Form):
    TIME_CHOICE = (
        (None,"----------"),
        ("part-time","Part-time"),
        ("full-time",("Full-time"))
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.all()
    )

    time = forms.ChoiceField(choices = TIME_CHOICE)
