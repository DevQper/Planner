from django import forms
from django.contrib.admin import widgets
from .models import Task, Blogs, Reviews


class TaskForm(forms.ModelForm):
    date_end = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Task
        # fields = []
        exclude = ["active", "completeness"]
        widgets = {
            'goal': forms.Textarea(attrs={'class': 'my_goal_class'}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ["name_blog", "description"]


class BlogReview(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["text"]
