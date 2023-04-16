from django.urls import path
from . import views

urlpatterns=[
    path('',views.IndexPageView.as_view(),name='homepage'),
    path('contact-us/',views.ContactPageView.as_view(),name='contact'),
]