from django.db import models


class Task(models.Model):
    IMPORTANCE = (
        ("1", "very importance"),
        ("2", "importance"),
        ("3", "it would be better"),
        ("4", "not very important"),
        ("5", "trifle")
    )

    name = models.CharField(max_length=100)
    goal = models.TextField(max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    importance = models.CharField(choices=IMPORTANCE, default="1", max_length=100)
    active = models.BooleanField(default=True)
    completeness = models.BooleanField(default=False)
    my_completeness = models.BooleanField(default=False)


class Blogs(models.Model):
    name_user = models.CharField(max_length=50)
    name_blog = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    date_create = models.DateTimeField(auto_now_add=True)


class Reviews(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=2500)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True,
    )
    blog = models.ForeignKey(Blogs, verbose_name="блог", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.blog}"

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

