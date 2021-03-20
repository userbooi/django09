from django.shortcuts import render

# Create your views here.
def home(request):
    jobs = 'jobs1 summery'
    return render(request, 'jobs/index.html', {'jobs':jobs})
