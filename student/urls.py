from django.urls import path
from student.views import registration,postfeedback,viewtimetable,leaveapplication,homepage,getreg,login,getlogin,logout
urlpatterns = [
    path('registration/',registration,name="registration"),
    path('feedbacks/',postfeedback,name="feedback"),
    path('timetable/',viewtimetable,name="timetable"),
    path('leave/',leaveapplication,name="leave"),
    path("home/",homepage,name="home"),
    path("getreg",getreg,name="getreg"),
    path("login",login,name='login'),
    path("getlog",getlogin,name="getlogin"),
    path("logout",logout,name="logout"),
]
