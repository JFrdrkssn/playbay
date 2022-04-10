from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, AddPostForm, EditPostForm


class PostList(generic.ListView):
    """
    
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    
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

        # Automatically passes in email and username
        # to comment form when logged in
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.user = request.user
            # Save the comment to the correct post
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
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


class AddPost(LoginRequiredMixin, generic.CreateView):
    """
    
    """

    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.liked = False
        form.instance.status = 1
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, generic.UpdateView):
    """
    
    """

    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    """
    
    """

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class PostLike(View):
    """
    
    """

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Reloads page when liking or unliking
        return HttpResponseRedirect(reverse('post_detail', args=[pk]))
