from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Notes
# Create your views here.
def notes_list(request):
    MAX_OBJECTS = 20
    notes = Notes.objects.all()[:MAX_OBJECTS]
    data = {"results": list(notes.values("id", "title", "content", "created_by__username", "pub_date"))}
    return JsonResponse(data)

def notes_detail(request, pk):
    notes = get_object_or_404(Notes, pk=pk)
    data = {"results": {
        "id": notes.id,
        "title": notes.title,
        "content": notes.content,
        "created_by": notes.created_by.username,
        "pub_date": notes.pub_date
    }}
    return JsonResponse(data)