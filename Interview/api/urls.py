from django.urls import path
from .import views

urlpatterns = [
    path('shedule/',views.InterviewSheduleView.as_view(),name='shedule'),
    path('cancellApplication/',views.CancelApplicationView.as_view(),name='cancell application'),
    path('shedules/',views.getShedulesView.as_view(),name='shedules'),
    path('interviewCall/',views.InterviewView.as_view(),name="makeInterview"),
    path('status/',views.InterviewStatusView.as_view(),name="status"),

    path('test/',views.testView,name='test')
   
]
