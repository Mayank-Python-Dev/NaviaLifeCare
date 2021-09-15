from django.shortcuts import render, redirect

from django.http import HttpResponse

import spacy

import pandas as pd

from django.contrib import messages

from .models import *

# Create your views here.
# getfile = ""
getMedicalData = ""

def search(request):
    if request.method == "POST":
        try:
            gettext = request.POST['getText']
            spacyLoaded = spacy.load("en_core_med7_lg")
            getOutput = spacyLoaded(gettext)
            createDictionary = {}
            for ent in getOutput.ents:
                createDictionary[ent.label_] = ent.text

            globals()['getMedicalData'] = MedicalData.objects.filter(sku_name__icontains = createDictionary['DRUG'])

            messages.success(request,f'Successfully found!')
            return redirect('search')
        except:
            messages.warning(request,f'Not Found!')
            return redirect('search')   
            
    context = {'getMedicalData':getMedicalData}
    return render(request, 'navialifeapp/search.html', context)


def upload_csv(request):

    if request.method == "POST":
        getfile = request.FILES['getFile']
        df = pd.read_csv(getfile)
        df = df.replace(to_replace="-", value=0.0)
        transpose_df = df.transpose()
        final_df = transpose_df.to_dict()

        medical_data = [MedicalData(
            sku_id=value['sku_id'],
            product_id=value['product_id'],
            sku_name=value['sku_name'],
            price=value['price'],
            manufacturer_name=value['manufacturer_name'],
            salt_name=value['salt_name'],
            drug_form=value['drug_form'],
            Pack_size=value['Pack_size'],
            strength=value['strength'],
            product_banned_flag=value['product_banned_flag'],
            unit=value['unit'],
            price_per_unit=value['price_per_unit'],
        ) for key, value in final_df.items()]

        MedicalData.objects.bulk_create(medical_data)
        messages.success(request, f'Successfully Uploaded!')

        return redirect('upload')


    return render(request,'navialifeapp/upload_csv.html')