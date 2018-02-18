from django.shortcuts import render
from django.utils import timezone
from .models import Memory

def memory_list(request):
    memories = Memory.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'memories/memory_list.html', {'memories': memories})
