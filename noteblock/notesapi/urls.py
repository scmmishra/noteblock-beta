from django.urls import include, re_path
from .views import notes_list, notes_detail

urlpatterns = [
	path("notes/", notes_list, name="notes_list"),
    path("notes/<int:pk>/", notes_detail, name="notes_detail")
]