from django import forms

class PatientData(forms.Form):
    pregnancies = forms.IntegerField(label='Ciąże')
    glucose = forms.IntegerField(label='Glukoza')
    blood_preasure = forms.IntegerField(label='Ciśnienie krwi')
    skin_thickness = forms.IntegerField(label='Grubość skóry')
    insulin = forms.IntegerField(label='Insulina')
    bmi = forms.FloatField(label='BMI')
    diabetes_pedigree_function = forms.FloatField(label='Funkcja rodowodu cukrzycy')
    age = forms.IntegerField(label='Wiek')
