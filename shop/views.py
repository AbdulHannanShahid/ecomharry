from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
from django.contrib import messages
import json
import datetime
# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}

    print(params)
    return render(request, 'index.html', params)
    
   # products = Product.objects.all()
   # n = len(products)
   # nSlides = n//4 + ceil((n/4)-(n//4))
   # params = {'noofslides':nSlides, 'range':range(1,nSlides), 'product':products}
   # return render(request, 'index.html', params)
def search(request):
    query= request.POST.get('search')
    allProds = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(product_category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 : #or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)
def searchMatch(query, item):
    if query in item.product_name or query in item.product_category:
        return True
    else:
        return False

def contactus(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone,desc=desc)
        contact.save()
        thank = True
        return render(request, 'contactus.html', {'thank':thank})
        #messages.success(request,"Thank you for contacting us. Your Query will be resolved soon.")
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')
def productview(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,'productview.html', {'product':product[0]})

def checkout(request):
     if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','')+''+request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        
        order = Orders(items_json=items_json ,name=name, email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
     return render(request, 'checkout.html')
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse(orderId)
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')

