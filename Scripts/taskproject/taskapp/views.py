from django.shortcuts import render,get_object_or_404 , redirect
from django.contrib.auth.models import User
from .models import Item, CartItem
from django.http import JsonResponse


from django.contrib import auth

# Create your views here.
def enter(request):
    return render(request,'signup.html')

def add(request):
    username =request.GET['u1']
    email =request.GET['e1']
    password=request.GET['p1']
    user=User.objects.create_user(username=username,email=email,password=password)
    user.save()
    return render(request,'signup.html')




def index(request):
    return render(request,'index.html')



def login(request):
    return render(request,'login.html')
 

def loginuser(request):
    if request.method=='POST':
      username =request.POST['u1']
      password=request.POST['p1']
      user=auth.authenticate(username=username,password=password)
      if user is not None:
          auth.login(request,user)
          return redirect('/index')
      else:
          return redirect('/')

def cart(request):
     return render(request,'cart.html')

def shop(request):
    products = Item.objects.all()
    return render(request, 'shop.html', {'products': products})

def add_to_cart(request, product_id):
    product = Item.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/shop')


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def update_quantity(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')

        item = get_object_or_404(CartItem, id=item_id)
        item.quantity = quantity
        item.save()

        return JsonResponse({'message': 'Quantity updated successfully.'})

    return JsonResponse({'message': 'Invalid request.'}, status=400)

def remove_item(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        item_id = request.POST.get('item_id')

        item = get_object_or_404(CartItem, id=item_id)
        item.delete()

        cart = get_object_or_404(cart, user=request.user)
        total = cart.calculate_total()  # Replace with your calculation logic

        return JsonResponse({'message': 'Item removed successfully.', 'total': total})

    return JsonResponse({'message': 'Invalid request.'}, status=400)