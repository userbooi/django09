from django.shortcuts import render

# Create your views here.
def blog(request):
    info = 'hi welcome to the blog'
    return render(request, 'blogs/blog.html', {'info':info})
