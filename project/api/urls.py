 
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from   .views import *

urlpatterns = [
path('snippets/', SnippetList.as_view()),
path('snippets/<int:pk>/', SnippetDetail.as_view())
]