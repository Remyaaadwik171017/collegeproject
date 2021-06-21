from django.urls import path
from calculations.views import get_addition_page, calculate, get_substraction_page, get_mul_page, get_division_page, \
    calculate_mul, calculate_div, calculate_sub

urlpatterns = [
    path("add", get_addition_page, name="getadd"),
    path("calculate", calculate, name="add"),
    path("sub", get_substraction_page, name="getsub"),
    path("calculate_sub", calculate_sub, name="sub"),
    path("div", get_division_page, name="getdiv"),
    path("calculate_div", calculate_div, name="div"),
    path("mul", get_mul_page, name="getmul"),
    path("calculate_mul", calculate_mul, name="mul"),
]
