from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
<<<<<<< HEAD
<<<<<<< HEAD
    users = User.objects.all()
    return render (request, 'blog/post_list.html', {'posts' : posts, 'users': users})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def author_perfil(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)

    return render(request, 'blog/author_perfil.html', {'author':author, 'posts': posts})
<<<<<<< HEAD

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
=======
    return render (request, 'blog/post_list.html', {'posts' : posts})
>>>>>>> parent of b750a96 (Update URLs)
=======
    return render (request, 'blog/post_list.html', {'posts' : posts})
>>>>>>> parent of b750a96 (Update URLs)
=======
>>>>>>> parent of 390d1b9 (Rascunhos Blog)
