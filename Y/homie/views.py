from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Lander.html')

def page1(request):
    posts = BlogPost.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})


from django.shortcuts import redirect, get_object_or_404
from .models import BlogPost

def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogPost.objects.create(title=title, content=content)
        return redirect('page1')
    return render(request, 'create_post.html')

def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    return redirect('page1')
