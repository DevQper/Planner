from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Task, Blogs, Reviews
from .forms import TaskForm, BlogForm, BlogReview
from allauth.account.forms import LoginForm, SignupForm


def profile_count(tasks):
    tasks_count = tasks.count()
    my_completeness_tasks = tasks.filter(active=False, my_completeness=True, completeness=False).count()
    success_rate = my_completeness_tasks * 100 / 1
    success_rate1 = round(success_rate)
    return success_rate1


class TaskView(View):
    """Вывод задач"""
    def get(self, requests):
        tasks = Task.objects.all()
        task = tasks.filter(active=True, completeness=False)
        complete_task = Task.objects.filter(active=False, completeness=True).order_by()[:5]
        form = TaskForm()
        blogs = Blogs.objects.all()
        success_rate1 = profile_count(tasks)

        allauth_login = LoginForm(requests.POST or None)
        allauth_signup = SignupForm(requests.POST or None)

        return render(requests, "Task_list/base.html", {"Blogs_list": blogs, "Task_list": task, "complete_tasks": complete_task,
        "form": form, "success_rate1": success_rate1, "allauth_login": allauth_login, "allauth_signup": allauth_signup})


class BlogsView(View):
    def get(self, request):
        pass


class AddTask(View):
    def post(self, requests):
        form = TaskForm(requests.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class Delete(View):
    def post(self, requests, pk):
        task = Task.objects.get(id=pk)
        task.delete()

        return HttpResponse(status=200), redirect("/")


class MyCompleteness(View):
    def post(self, requests, pk):
        task = Task.objects.get(id=pk)
        task.my_completeness = True
        task.active = False
        task.save()

        return redirect("/")


class Completeness(View):
    def post(self, requests, pk):
        task = Task.objects.get(id=pk)
        task.completeness = True
        task.active = False
        task.save()

        return redirect("/")


class TaskHistory(View):
    def get(self, request):
        task = Task.objects.all()
        return render(request, "Task_list/history.html", {"Task_History": task})


class Profile(View):
    def get(self, request):
        tasks = Task.objects.all()
        success_rate1 = profile_count(tasks)
        return render(request, "Task_list/profile.html", {"success_rate1": success_rate1})


class BlogView(View):
    def get(self, request):
        return render(request, "Task_list/blog_create.html")

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name_user = request.user.username
            form.save()
        return redirect("/")


class AddReview(View):
    def post(self, request, pk):
        form = BlogReview(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.blog_id = pk
            form.save()
        return redirect("/")



