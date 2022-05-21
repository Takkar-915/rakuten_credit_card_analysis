from distutils.command.upload import upload
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from analyze_card.forms import CsvForm
import csv,io
import pandas as pd

from analyze_card.function import convert_csv, process_csv

# Create your views here.

def index(request):
    if request.method == 'POST':
        upload = CsvForm(request.POST,request.FILES)
        if upload.is_valid():
            data = pd.read_csv(io.StringIO(request.FILES['uploaded_file'].read().decode('UTF-8')), delimiter=',')
            df = process_csv(data)

            response = convert_csv(df)

            return response

        else:
            upload = CsvForm()
            return render(request,'index.html',{'form':upload})
            
