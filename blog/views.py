from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import CommentForm, AddPostForm, EditPostForm


class PostList(generic.ListView):
    """
    View for list of blog post entries.
    Home page.
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    View for a particular post.
    Render comment form and like functionality
    for logged in users.
    """

    def get(self, request, pk, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Commented!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class AddPost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    View with form for adding posts.
    Redirects to added post.
    """

    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_message = 'Your new post has been added!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.liked = False
        form.instance.status = 1
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    View with form for editing posts.
    Redirects to edited post.
    """

    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'
    success_message = 'Your post has been updated!'


class DeletePost(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    """
    View with button to confirm deleting posts.
    """

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = 'Post deleted!'


class PostLike(View):
    """
    View with method for liking posts.
    Checks if user has liked or not
    and displays the correct like icon
    in the templates.
    """

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Reloads page when liking or unliking
        return HttpResponseRedirect(reverse('post_detail', args=[pk]))


def error_404(request, exception):
    """
    Handler for error 404
    """
    return render(request, 'error_404.html', status=404)

def error_500(request):
    """
    Handler for error 500
    """
    return render(request, 'error_500.html', status=500)
