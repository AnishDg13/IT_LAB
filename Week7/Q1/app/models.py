from django.db import models
from django import forms




class LIVES(models.Model):
    person_name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    def __str__(self):
        return self.person_name
    

class WORKS(models.Model):
    person_name = models.ForeignKey(LIVES, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)    
    salary = models.FloatField()
    class Meta:
        ordering = ['person_name']

class WorksForm(forms.ModelForm):
    class Meta:
        model = WORKS
        fields='__all__'
class LivesForm(forms.ModelForm):
    class Meta:
        model=LIVES
        exclude = ('company_name',)