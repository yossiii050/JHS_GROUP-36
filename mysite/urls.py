"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls.views import home_page_view,home_template,home
from users.views import loginPage,logoutUser,ReportEmployer,ReportCandidate,approveEmp,changestatus,registered_users
from mysite.mysite.views import maintenance
from payments.views import paymentpage

urlpatterns = [
    path('jobs/',include('jobs.urls'),name="jobs"),
    path('register/',include('users.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('payments/',paymentpage),
    path('tech/',include('tech.urls')),
    path('', home,name="home page"),
    path('login/',loginPage,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('maintenance/', maintenance),
    path('users/', include('users.urls')),
    path('ReportEmployer/',ReportEmployer,name="ReportEmployer"),
    path('ReportCandidate/',ReportCandidate,name="ReportCandidate"),
    path('appr/',approveEmp),
    path('Reports/',approveEmp),
    path('registered-users/', registered_users, name='registered_users'),

    

]
