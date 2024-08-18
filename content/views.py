from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment

from .forms import CommentForm

# Create your views here.
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('details', slug=slug)
    else:
        form = CommentForm()

    form.fields['body'].label = ''

    return render(request, 'content/details.html', {'post': post, 'form': form})

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_slug = comment.post.slug
    comment.delete()
    
    return redirect('details', slug=post_slug)






