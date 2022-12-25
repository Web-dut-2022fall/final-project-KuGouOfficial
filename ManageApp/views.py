from django.db import OperationalError, DatabaseError
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import models
from .models import DB


# Create your views here.


def index(req, opt=None):
    items = {}
    context = {'items': items}
    for each in DB.objects.all():
        items[each.key] = each.value
    context[opt] = 'true'
    return render(req, 'index.html', context=context)


def create(req):
    context = {}
    if req.method == 'POST':
        key = req.POST.get('key').strip()
        value = req.POST.get('value').strip()
        context['key'] = key
        context['value'] = value
        print(key, value)
        try:
            if key == '' or value == '':
                raise BlankError
            try:
                DB.objects.get(key=key)
                context['error'] = '数据已存在'
            except models.DB.DoesNotExist:
                try:
                    DB(key=key, value=value).save()
                    context['hint'] = '插入成功'
                except OperationalError:
                    context['error'] = '数据库已锁定'
        except BlankError:
            context['error'] = '不能留空'
    return render(req, 'create.html', context=context)


def delete(req):
    if req.method == 'POST':
        key = req.POST.get('key').strip()
        DB.objects.get(key=key).delete()
    return index(req, 'delete')


def modify(req):
    items = {}
    context = {'items': items}
    for each in DB.objects.all():
        items[each.key] = each.value
    if req.method == 'POST':
        key = req.POST.get('key').strip()
        val = req.POST.get('value').strip()
        try:
            item = DB.objects.get(key=req.POST.get('pre-key'))
            item.delete()
            DB(key=key, value=val).save()
        except models.DB.DoesNotExist:
            DB(key=key, value=val).save()
            key = req.POST.get('pre-key')
            print(key)
            DB.objects.get(key=key).delete()
        except OperationalError:
            context['error'] = '数据库已锁定'
        context['items'][key] = val
        return HttpResponseRedirect("/modify")

    return render(req, 'modify.html', context=context)


def search(req):
    return index(req)


class BlankError(DatabaseError):
    pass
