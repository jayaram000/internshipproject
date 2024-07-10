from django.shortcuts import render,redirect,get_object_or_404
from app1.models import Item,Category,Favo,BookingRequest
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest

# Create your views here.



def home(request):
    return render(request,'home.html')


def items(request):
    i = Item.objects.all()

    return render(request,'items.html',{'items':i,})


def category(request,n):
    c=Category.objects.get(name=n)
    item=Item.objects.filter(category=c)

    return render(request, 'itembycat.html', {'item': item,'c':c,})


@login_required
def upload(request):
    if (request.method == 'POST'):
        name=request.POST['name']
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES['image']
        phone=request.POST['phone']
        category=request.POST['category']
        u=request.user
        c=Category.objects.get(name=category)
        i=Item.objects.create(name=name,desc=desc,image=image,price=price,phone=phone,category=c,user=u)
        i.save()
        return redirect('app1:useruploads')
    return render(request, 'upload.html')


@login_required

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    favorites = None
    if request.user.is_authenticated:
        favorites = Favo.objects.filter(user=request.user, item=item)

    return render(request, 'itemdetail.html', {'p': item, 'f': favorites})

@login_required
def update(request,pk):
    try:
        item = Item.objects.get(id=pk)
    except Item.DoesNotExist:
        item = None

    if request.method == 'POST':
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        price = request.POST.get('price', '')
        new_image = request.FILES.get('image')
        phone = request.POST.get('phone', '')
        category_name = request.POST.get('category', '')

        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            category = None

        if item:
            item.name = name
            item.desc = desc
            item.price = price
            # item.image = image
            item.phone = phone
            item.category = category
            if new_image:
                item.image = new_image
            item.save()
            return redirect('app1:items')
    return render(request,'update.html',{'item':item})



@login_required
def user_uploads(request):

    u=request.user
    i=Item.objects.filter(user=u)
    return render(request,'useruploads.html',{'item':i})

@login_required
def post_delete(request,pk):
    u=request.user
    i=Item.objects.get(pk=pk,user=u)
    i.delete()
    return redirect('app1:useruploads')

# class PostDelete(DeleteView):       #here in deleteview we need to create a html file
#     model=Item
#     success_url = reverse_lazy('app1:useruploads')
#     template_name = "delete.html"

@login_required
def favourite(request, pk):
    item = get_object_or_404(Item, pk=pk)
    user = request.user
    existing_favorite = Favo.objects.filter(user=user, item=item).exists()

    if existing_favorite:
        Favo.objects.filter(user=user, item=item).delete()
    else:
        Favo.objects.create(user=user, item=item)

    return redirect('app1:itemdetail', pk=pk)

@login_required
def favor_view(request):

    f=Favo.objects.filter(user=request.user)
    return render(request, 'favo.html',{'f':f,})


def register(request):

    if (request.method=="POST"):

        un = request.POST['un']
        p = request.POST['pass']
        cpass = request.POST['cpass']
        fn = request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']

        userExists=User.objects.filter(username=un)
        emailExists=User.objects.filter(email=email)

        if cpass==p:
            if userExists:
                return render(request, 'register.html', {'failed': 'Username already exists!!'})
            else:
                if emailExists:
                    return render(request, 'register.html', {'failed': 'User with email already exists!!'})
                else:
                    u=User.objects.create_user(username=un, password=p,email=email,first_name=fn,last_name=ln)
                    u.save()
                    return render(request, 'register.html', {'success': 'User Created Successfully!!'})
        else:
            return render(request, 'register.html', {'failed': 'password not matching!!'})

    return render(request,'register.html')



def user_login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('app1:home')
        else:
            # msg="invalid credentials"
            return render(request, 'login.html', {'failed': "invalid credentials,Try again!!"})

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('app1:login')

@login_required
def request_form(request,pk):
    itemm = get_object_or_404(Item, pk=pk)

    if(request.method=='POST'):

        user=request.user
        item=itemm
        uploadedby=itemm.user.username
        # print(itemm.user.username)
        email=request.POST['email']
        date=request.POST['date']

        b=BookingRequest.objects.create(user=user,item=item,email=email,requested_date=date,uploadedBy=uploadedby)
        b.save()
        # messages.success(request, 'Form submitted successfully!')
        return  redirect('app1:itemdetail',pk=pk)



@login_required
def view_booking_requests(request):
    # Retrieve all booking requests
    u=request.user
    booking_requests = BookingRequest.objects.filter(uploadedBy=u)

    context = {
        'booking_requests': booking_requests,
    }
    return render(request, 'booking_requests.html', context)


@login_required
def reply_booking_request(request, pk):
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['accepted', 'not_available']:
            booking_request = get_object_or_404(BookingRequest, pk=pk)
            booking_request.booking_status = status
            booking_request.save()
            return redirect('app1:bookreq')
        else:
            pass
    else:
        return HttpResponseBadRequest("Method not allowed")

@login_required
def view_request(request):

    u=request.user
    viewrequest=BookingRequest.objects.filter(user=u)

    return render(request,'viewrequest.html',{'viewreq':viewrequest})
