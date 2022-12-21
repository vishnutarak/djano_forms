from django import forms
g={('MALE','male'),('FEMALE','female')}
c={('PYTHON','python'),('DJANGO','django'),('SQL','sql'),('WEBTECH','webtech')}
class name_form(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    #address=forms.CharField(max_length=1000,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.ChoiceField(choices=c)
    #course=forms.ChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)