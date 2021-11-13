from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import CommentForm




# Create your views here.




def home(request):
    return render(request, 'geodrapp/home.html', {'title': 'home'})

def about(request):
    return render(request, 'geodrapp/about.html', {'title': 'about'})

def blog(request):
    context = {
        'title':'blog',
        'posts': Post.objects.all(),
    }
    return render(request, 'geodrapp/blog.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False

    else:
        post.likes.add(request.user.id)
        liked = True

    return HttpResponseRedirect(reverse('geodrapp-post_detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'geodrapp/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('geodrapp-blog')




class PostListView(ListView):
    model = Post
    template_name = 'geodrapp/blog.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'geodrapp/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    ordering = ['-date_added']

    def get_context_data(self, *args , **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image_1', 'content_1', 'image_2', 'content_2', 'image_3', 'content_3', 'image_4', 'content_4',
              'image_5', 'content_5', 'image_6', 'content_6', 'image_7']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image_1', 'content_1', 'image_2', 'content_2', 'image_3', 'content_3', 'image_4', 'content_4',
              'image_5', 'content_5', 'image_6', 'content_6', 'image_7']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def project(request):
    return render(request, 'geodrapp/project.html', {'title': 'project'})

def service(request):
    return render(request, 'geodrapp/service.html', {'title': 'service'})

def storymap(request):
    return render(request, 'geodrapp/storymap.html', {'title': 'storymap'})

def logo(request):
    return render(request, 'geodrapp/logo.html', {'title': 'logo'})

def event(request):
    return render(request, 'geodrapp/event.html', {'title': 'event'})

def announcement(request):
    return render(request, 'geodrapp/announcement.html', {'title': 'announcement'})

def calendar(request):
    return render(request, 'geodrapp/calendar.html', {'title': 'calendar'})

def gis(request):
    return render(request, 'geodrapp/gis.html', {'title': 'Training of GIS'})

def overview(request):
    return render(request, 'geodrapp/overview.html', {'title': 'Overview'})

def data(request):
    return render(request, 'geodrapp/data.html', {'title': 'data'})

def structure(request):
    return render(request, 'geodrapp/structure.html', {'title': 'structure'})

def management(request):
    return render(request, 'geodrapp/management.html', {'title': 'management'})

def board(request):
    return render(request, 'geodrapp/board.html', {'title': 'board'})

def clients(request):
    return render(request, 'geodrapp/clients.html', {'title': 'clients'})

def partners(request):
    return render(request, 'geodrapp/partners.html', {'title': 'partners'})

def training(request):
    return render(request, 'geodrapp/training.html', {'title': 'training'})

def research(request):
    return render(request, 'geodrapp/research.html', {'title': 'research'})

def consultancy(request):
    return render(request, 'geodrapp/consultancy.html', {'title': 'consultancy'})