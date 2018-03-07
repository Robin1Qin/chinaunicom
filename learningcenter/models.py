from django.db import models


class Catagory(models.Model):
    name = models.CharField(verbose_name='名称', max_length=30)

    class Meta:
        verbose_name = '分类'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    author = models.CharField(verbose_name='作者', max_length=16)
    content = models.TextField(verbose_name='博客正文')
    created = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    Catagory = models.ForeignKey(Catagory, verbose_name='分类', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Article, verbose_name='博客', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='称呼', max_length=16)
    content = models.CharField(verbose_name='内容', max_length=240)
    created = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
