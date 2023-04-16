
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname', 'mobile', 'emp_code', 'position')

        # updating labels
        labels = {
            'fullname': 'Full name',
            'emp_code': 'EMP. Code',
        }

    # this shows "select" in "position"
    def __init__(self, *args, **kargs):
        super(EmployeeForm, self).__init__(*args, **kargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False    #filling emp_code column isn't neccessary

