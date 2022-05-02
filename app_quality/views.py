from django.shortcuts import render
from ..app_file_storage.models import Messages

# Create your views here.

def quality_admin_view(request):
    return render(request, 'app_quality/quality_admin.html')
