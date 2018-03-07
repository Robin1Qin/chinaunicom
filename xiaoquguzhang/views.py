from django.shortcuts import render, HttpResponse
from django.views import View

from .models import XiaoQuGuZhang, Raduis
from .forms import XiaoQuGuZhangForm
import os, re, time


def add(request):
    bars = '0.0.0.0'
    account = '0000'
    yujing = 'false'
    if request.method == 'POST':
        form = XiaoQuGuZhangForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            bars = request.POST['bars'].strip()
            account = request.POST['account'].strip()
    else:
        form = XiaoQuGuZhangForm()

    XiaoQuGuZhang_list = XiaoQuGuZhang.objects.order_by('-pub_date')[:10]
    XiaoQuGuZhang_bars_list = XiaoQuGuZhang.objects.all().values('bars').order_by('-pub_date')[1:10]
    XiaoQuGuZhang_account_list = XiaoQuGuZhang.objects.all().values('account').order_by('-pub_date')[1:10]
    print(XiaoQuGuZhang_account_list)
    if ({'account': account} not in XiaoQuGuZhang_account_list) and ({'bars': bars} in XiaoQuGuZhang_bars_list):
        yujing = 'true'
    return render(request, 'xiaoquguzhang_add.html',
                  {'XiaoQuGuZhang_list': XiaoQuGuZhang_list, 'XiaoQuGuZhang_form': form,
                   'yujing': yujing})


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


def radius(request):
    path = 'd:\\logs\\access.log'
    f = open(path, 'rb')
    ip_pattern = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b")
    account_pattern1 = re.compile( r"\s\w*-\[")
    account_pattern2 = re.compile(r":\w*-\[")
    for line in f:
        try:
            str = line.decode("utf-8")
            if 'Accounting-Request' in str:
                problem = str.split(', ')[-1]
                account = account_pattern1.findall(str)[0][1:-2]
            elif 'Access-Request' in str:
                problem = str.split('], ')[-1]
                account = account_pattern2.findall(str)[0][1:-2]
            ip_list = ip_pattern.findall(str)
            pub_date = str[0:26].replace("/", "-")
            if len(ip_list) != 0:
                Raduis.objects.create(pub_date=pub_date, bars_ip=ip_list[0], problem=problem, account=account)

        except:
            continue
    return HttpResponse(path)
