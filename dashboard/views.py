from django.shortcuts import render
from django.utils import timezone
from .models import SensorData
from datetime import timedelta

def index(request):
    latest_data = SensorData.objects.last()
    recent_data = SensorData.objects.all().order_by('-timestamp')[:100]  # Last 100 entries for chart
    context = {
        'latest_data': latest_data,
        'recent_data': recent_data
    }
    return render(request, 'dashboard/index.html', context)

def history(request):
    one_week_ago = timezone.now() - timedelta(days=7)
    weekly_data = SensorData.objects.filter(timestamp__gte=one_week_ago).order_by('-timestamp')
    context = {
        'weekly_data': weekly_data
    }
    return render(request, 'dashboard/history.html', context)
