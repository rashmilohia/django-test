from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('employee_home')
    else:
        return render(request, 'rashmi_django_test/welcome.html')
