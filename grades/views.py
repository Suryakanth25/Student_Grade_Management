from django.shortcuts import render
from .forms import MarksForm
from .models import models

# Create your views here.

def calculate(request):
    total = average = grade = None
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            print("Form Valid")
            mark1 = form.cleaned_data['sub1']
            mark2 = form.cleaned_data['sub2']
            mark3 = form.cleaned_data['sub3']

            total = mark1+mark2+mark3
            average = total/3

            if average>=90:
                grade = "A"
            elif average>=80:
                grade = "B"
            elif average>=70:
                grade = "C"
            elif average>=60:
                grade = "D"
            elif average<50:
                grade = "Fail"
    else:
        print("Form Invalid:", form.errors)
        form = MarksForm()

    return render(request, 'grades/index.html', {'form':form, 
                                                 'total':total,
                                                 'average':average,
                                                 'grade':grade})