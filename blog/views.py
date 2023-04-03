from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .models import Post, User, Tags, Category, Comments
from .forms import PostForm, UserForm, LoginForm, CommentForm
# from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# @login_required(login_url='login')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment = Comments.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                parent = request.POST.get('comments.id')
                parent = Comments.objects.filter(id=parent).last()
            except:
                parent = None
            comment = form.save(commit=False)
            comment.post = post
            comment.parent = parent
            comment.save()
        return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comment': comment})
    # post = get_object_or_404(Post, slug=slug)
    # return render(request, 'blog/post_detail.html', {'post': post})

def category(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    category = posts.category
    posts = Post.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request,'blog/category.html', context)


# @login_required(login_url='login')
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post_detail.html', {'post': post})


@login_required(login_url='login')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # post.tag.set(form.cleaned_data.get('tag'))
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required(login_url='login')
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.tag.set(form.cleaned_data.get('tag'))
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    posts = Post.objects.filter(
        published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_detail', slug=slug)


def publish(self):
    self.published_date = timezone.now()
    self.save()


def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post_list')


def signup_request(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # post.published_date = timezone.now()
            # return redirect('post_detail', slug=post.slug)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})


# authentication/views.py
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print("BBBBBBBBBBBBBB")
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            print(user, 'AAAAAAAAAAAAAAA')
            # print('username')
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect("/")
            else:
                message = 'Login failed!'
    return render(
        request, 'blog/login.html', context={'form': form, 'message': message})


def LogoutPage(request):
    logout(request)
    return redirect('login')


def edit_profile(request):
    print('outside post')
    # form = UserForm(instance=request.user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        print('inside method')
        # print(form)
        if form.is_valid():
            print('inside form')
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})


# def edit_profile(request):
#     return render(request, 'blog/edit_profile.html')


# def post_signin(request):
#     form = forms.LoginForm()
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponse("hii")
#     return render(request, 'blog/post_signin.html', context={'form': form})


# def login_page(request):
# 	# form = LoginForm()

# 	if request.method == "POST":
# 		print(request,"AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
# 		form = LoginForm(request.POST)
# 		# print(form)
# 		if form.is_valid():
# 			print(form, 'this is print')
# 			username = form.cleaned_data.get('username')
# 			print(username, 'BBBBBBBBBBBBBB')
# 			password = form.cleaned_data.get('password')
# 			print(password, 'BBBBBBBBBBBBBB')
# 			user = authenticate(username=username, password=password)
# 			print(password, username, 'thi si sjggggggggggggggggggggg')
# 			if user:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				# return redirect("/")
# 				return HttpResponse("You are now logged in")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 			form = LoginForm()
# 	return render(request=request, template_name="blog/login.html", context={"form":form})


# def post_signup(request):
#     return render(request, 'blog/post_signup.html')

# def post_signin(request):
#     form = LoginForm()
#     return render(request, 'blog/post_signin.html', {'form': form})
    # return render(request, 'blog/post_signin.html', {'form': form})


# def post_signin(request):
#         if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse ("Username or Password is incorrect!!!")

#     return render (request,'login.html')
