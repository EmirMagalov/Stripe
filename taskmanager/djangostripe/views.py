import json

from django.db.models import F, Window
from django.db.models import Subquery, OuterRef
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import stripe

def home(request):
    subquery=Item.objects.filter(sex=OuterRef('sex')).order_by('-id').values('id')[:2]
    cloth = Item.objects.filter(id__in=Subquery(subquery))
    return render(request,"djangostripe/home.html",{"cloth":cloth})

def clothslug(request,slug):
    cloth=Item.objects.get(slug=slug)
    return render(request, "djangostripe/slug.html", {"cloth": cloth})

def session(request):
    if request.method == "POST":
        add = {
            "name": request.POST.get("name"),
            "img": request.POST.get("img"),
            "size": request.POST.get("size"),
            "price": request.POST.get("price"),
            "count": request.POST.get("count")
        }
        if request.method == "POST":

            if not request.session.get('basket'):

                request.session["basket"] = list()

            else:
                request.session["basket"] = list(request.session["basket"])
                for i in request.session["basket"]:
                    if i["name"]==request.POST.get("name"):
                        i["size"]=request.POST.get("size")
                        request.session.modified = True
            item = next((i for i in request.session["basket"] if i["name"] == request.POST.get("name")), False)

            if not item:
                request.session["basket"].append(add)
                request.session.modified = True


        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def sessiondel(request):
  if request.method == "POST":
        for i in request.session["basket"]:
            if i["name"] == request.POST.get("name"):
                i.clear()

        while {} in request.session['basket']:
            request.session["basket"].remove({})


        request.session.modified = True

        return redirect(request.META.get('HTTP_REFERER'))

  else:
        return redirect(request.META.get('HTTP_REFERER'))

def basket(request):
    return render(request,"djangostripe/basket.html")

def mens(request):
    cloth=Item.objects.filter(sex__name="Mens")
    return render(request, "djangostripe/mens.html",{"cloth":cloth})

def womens(request):
    cloth=Item.objects.filter(sex__name="Womens")
    return render(request, "djangostripe/womens.html",{"cloth":cloth})



stripe.api_key = "sk_test_51OI8b2FVjktvFpLSjuosUdOR0ajC3BfB5hWSGO89JFjZ8ySURKvqnDOC2q0AnT92kNYowa712NAefgqwtUlaSVHS00L36bVIhT"


def chek(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        # data=json.load(request.body)
        data = json.loads(request.body.decode('utf-8'))
        try:
            charge = stripe.PaymentIntent.create(
                amount= int(float(data["amount"]) * 100),
                currency='usd',
                description='Оплата заказа',
                payment_method=token,
            )

            # Обработайте успешный платеж
            del request.session["basket"]
            return redirect(request.META.get('HTTP_REFERER'))

        except stripe.error.CardError as e:
            # Обработка ошибки при обработке карты
            return render(request, 'error.html', {'error': str(e)})

    return redirect(request.META.get('HTTP_REFERER'))