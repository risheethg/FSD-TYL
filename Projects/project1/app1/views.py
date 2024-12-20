from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def app_data(request):
    return render(request,"template1.html")

def template_data(request):
    return render(request,"template6.html")

def api_data(request):
    data = [
    {
        "Name": "Somu",
        "Payment": {
            "Total": 600
        },
        "Transaction": {
            "price": 400
        }
    },
    {
        "Name": "John",
        "Payment": {
            "Total": 500
        },
        "Transaction": {
            "price": 350
        }
    },
    {
        "Name": "Alice",
        "Payment": {
            "Total": 700
        },
        "Transaction": {
            "price": 250
        }
    },
    {
        "Name": "Somu",
        "Payment": {
            "Total": 300
        },
        "Transaction": {
            "price": 450
        }
    }
    ]
    return render(request,'template2.html',{"data":data})

def response_page(request):
    return render(request,"template5.html")

def login_page(request):
    return render(request,"login_template.html")

from .models import collection

def handle_mongo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        collection.insert_one({'name':name})
    response = collection.find({})
    print(response)
    return render(request,"mongo_form.html",{'dbdata':response})