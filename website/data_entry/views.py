from django.shortcuts import render
from django.http import HttpResponse
import csv
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
import xlrd
from xlwt import Workbook


def index(request) :
    wb = Workbook()
    b = xlrd.open_workbook('/Users/m02ghan/PycharmProjects/website/dt.csv')
    s = b.sheet_by_index(0)

    a = s.col_values(1, 0, s.nrows)
    b = s.col_values(2, 0, s.nrows)
    query = request.GET.get('search')

    for i in range(0,len(b)) :
        if(b[i] == query) :
            message = "trans for {} ".format(query) + "can be : " + a[i]

    #message = "trans for {} ".format(query) + "can be : "

    #template = index.html
    context = {
         message,
    }

    return render(request,context)



def detail(request,data_id):
    return HttpResponse("<h2>details for data id : " + str(data_id) + "</h2>")


def home(request):
    #query = request.GET.get('search')
    message = "Hello I am learning"
    #template = "<h2>"
    context = {
        'message' : message,
    }
    return render(request,context)
