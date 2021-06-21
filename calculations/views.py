from django.shortcuts import render

# Create your views here.
def get_addition_page(request):
    return render(request,"addition.html")
def calculate(request):
    num1=request.POST.get("num1")
    num2 =request.POST.get("num2")
    res=int(num1)+int(num2)
    print(res)
    return render(request,"addition.html")
def get_substraction_page(request):
    return render(request,"substraction.html")
def calculate_sub(request):
    num1=request.POST.get("num1")
    num2 =request.POST.get("num2")
    res=int(num1)-int(num2)
    print(res)
    return render(request,"substraction.html")
def get_division_page(request):
    return render(request,"division.html")
def calculate_div(request):
    num1=request.POST.get("num1")
    num2 =request.POST.get("num2")
    res=int(num1)/int(num2)
    print(res)
    return render(request,"division.html")
def get_mul_page(request):
    return render(request,"multiplication.html")
def calculate_mul(request):
    num1=request.POST.get("num1")
    num2 =request.POST.get("num2")
    res=int(num1)*int(num2)
    print(res)
    return render(request,"multiplication.html")
