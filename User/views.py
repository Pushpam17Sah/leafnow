from django.shortcuts import render

# Create your views here.
from User.forms import UserForm


def user_list(request):
    return render(request, 'User/user_list.html', {})


def index(request):
    return render(request, 'User/index.html', {})


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return render(request, 'User/user_edit.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'User/user_edit.html', {'form': form})

