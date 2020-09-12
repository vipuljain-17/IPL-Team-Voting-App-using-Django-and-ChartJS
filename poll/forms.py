from django import forms
from .models import Question

class PollForm(forms.Form):
    TEAM_CHOICES = (
        ("MI","Mumbai Indians"),
        ("CSK","Chennai Super Kings"),
        ("RCB","Royal Challengers Banglore"),
        ("RR","Rajasthan Royals"),
        ("DC","Delhi Capitals"),
        ("SRH","Sunrisers Hyderabad"),
        ("KXIP","Kings XI Punjab"),
        ("KKR","Kolkata Knight Riders")
    )
    team = forms.ChoiceField(choices=TEAM_CHOICES, widget=forms.RadioSelect)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        widgets =  {'team': forms.RadioSelect}
