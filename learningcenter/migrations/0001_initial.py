# Generated by Django 2.0.1 on 2018-01-30 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('author', models.CharField(max_length=16, verbose_name='作者')),
                ('content', models.TextField(verbose_name='博客正文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
            ],
            options={
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='称呼')),
                ('content', models.CharField(max_length=240, verbose_name='内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningcenter.Article', verbose_name='博客')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='Catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningcenter.Catagory', verbose_name='分类'),
        ),
    ]