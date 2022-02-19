from django import forms



class search_from(forms.Form) :
    symbol= forms.CharField()
    year= forms.CharField()
    month= forms.CharField()
    day  = forms.CharField()



days_s= [(10,10),(50,50),(100,100),(500,500)]
class search_day(forms.Form) :
    symbol= forms.CharField()
    days  = forms.ChoiceField(choices=days_s)
