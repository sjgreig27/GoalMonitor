"""goal_monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitor-app/', include('monitor_app.urls')),
    path('smoking/', include('quit_smoking.urls')),
    path('meals/', include('meal_planner.urls')),
    path('health-monitor/', include('health_monitor.urls')),
    path('workout/', include('workout_planner.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
