from django.shortcuts import render

def memory_list(request):
    return render(request, 'memories/memory_list.html', {})