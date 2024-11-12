from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "shop_app/home.html", {"products": products})


def detail(request, id):
    details = Product.objects.get(id=id)
    return render(request, "shop_app/detail.html", {"details": details})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zipcode = request.POST.get("zipcode", "")
        total = request.POST.get("total", "")

        order = Order(
            items=items,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            total=total,
        )
        order.save()

    return render(
        request,
        "shop_app/checkout.html",
    )


def delete_item(request, id):
    product_objects = Product.objects.get(id=id)
    if request.method == "POST":
        product_objects.delete()
        return redirect("checkout")
    return render(request, "shop/delete.html", {"product_objects": product_objects})


def seller(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, "shop_app/seller.html", {"products": products})


def create_product(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            new_product.seller = request.user
            new_product.save()
            return redirect("home")

    product_form = ProductForm()
    return render(
        request, "shop_app/create_product.html", {"product_form": product_form}
    )


def product_edit(request, id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect("invalid")

    product_form = ProductForm(
        request.POST or None, request.FILES or None, instance=product
    )
    if request.method == "POST":
        if product_form.is_valid():
            product_form.save()
            return redirect("home")
    return render(
        request,
        "shop_app/edit.html",
        {"product_form": product_form, "product": product},
    )


def product_delete(request, id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect("invalid")
    if request.method == "POST":
        product.delete()
        return redirect("home")
    return render(request, "shop_app/delete.html", {"product": product})


@login_required
def dashboard(request):
    products = Product.objects.filter(seller=request.user)
    print(products)
    return render(request, "shop_app/dashboard.html", {"products": products})


def sales(request):
    orders = OrderDetail.objects.filter(product__seller=request.user)
    total_sales = orders.aggregate(Sum("amount"))
    print(total_sales)

    # 365 day sales sum
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = OrderDetail.objects.filter(
        product__seller=request.user, created_on__gt=last_year
    )
    yearly_sales = data.aggregate(Sum("amount"))

    # 30 day sales sum
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = OrderDetail.objects.filter(
        product__seller=request.user, created_on__gt=last_month
    )
    monthly_sales = data.aggregate(Sum("amount"))

    # 7 day sales sum
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = OrderDetail.objects.filter(
        product__seller=request.user, created_on__gt=last_week
    )
    weekly_sales = data.aggregate(Sum("amount"))

    # Everday sum for the past 30 days
    daily_sales_sums = (
        OrderDetail.objects.filter(product__seller=request.user)
        .values("created_on__date")
        .order_by("created_on__date")
        .annotate(sum=Sum("amount"))
    )

    product_sales_sums = (
        OrderDetail.objects.filter(product__seller=request.user)
        .values("product__name")
        .order_by("product__name")
        .annotate(sum=Sum("amount"))
    )
    print(product_sales_sums)

    return render(
        request,
        "shop_app/sales.html",
        {
            "total_sales": total_sales,
            "yearly_sales": yearly_sales,
            "monthly_sales": monthly_sales,
            "weekly_sales": weekly_sales,
            "daily_sales_sums": daily_sales_sums,
            "product_sales_sums": product_sales_sums,
        },
    )
