from django.db import models

class Question(models.Model):
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
    team = models.CharField(choices=TEAM_CHOICES,max_length=20, default="MI")

    def __str__(self):
	    return self.team