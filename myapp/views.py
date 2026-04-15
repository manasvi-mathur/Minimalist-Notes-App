from django.shortcuts import render
from django.http import JsonResponse
from .models import Note
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

def api_notes(request):
    notes = list(Note.objects.all().values('id', 'content', 'created_at').order_by('-created_at'))
    return JsonResponse(notes, safe=False)

@csrf_exempt
def add_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')
        if content:
            note = Note.objects.create(content=content)
            return JsonResponse({'id': note.id, 'content': note.content})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def delete_note(request, note_id):
    if request.method == 'DELETE':
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return JsonResponse({'success': True})
        except Note.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def update_note(request, note_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content', '')
            if content:
                note = Note.objects.get(id=note_id)
                note.content = content
                note.save()
                return JsonResponse({'id': note.id, 'content': note.content})
        except Note.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)
