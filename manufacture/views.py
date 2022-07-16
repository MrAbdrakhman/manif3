from django.shortcuts import render

from .models import Employee, Working_out, Occupation, SalaryTotal


def index(request):
    return render(request, 'manufacture/index.html')

def salary_total(request):
    employers = Employee.objects.all()
    workers = Occupation.objects.all()
    payroll = SalaryTotal.objects.all()
    context = {
        'employers': employers,
        'workers': workers,
        'payroll': payroll,
    }
    return render(request, 'manufacture/salary_total.html', context)

def raschet_eva(request):
    return render(request, 'manufacture/raschet_eva.html')

def raschet_pu(request):
    return render(request, 'manufacture/raschet_pu.html')

