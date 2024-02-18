from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.contrib import messages
from .models import *
from .forms import *

from django.forms import modelformset_factory, inlineformset_factory

#=-=-=-=-=-=-=-=-=-=-=-=-=-> P A G E   V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def dashboard(request):
    invoices = Invoice.objects.all()
    clients = Client.objects.all()
    customers = clients.count()
    paid = invoices.filter(status='Paid').count()
    past_due = invoices.filter(status='Past_Due').count()
    pending = invoices.filter(status='Pending').count()

    context = {
        'invoices': invoices,
        'clients': clients,
        'customers': customers,
        'paid': paid,
        'past_due': past_due,
        'pending': pending,
    }
    return render(request,'app/dashboard.html', context)



#=-=-=-=-=-=-=-=-=-=-=-=-=-> C L I E N T    V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request,'app/all_clients.html', context)


def client(request, pk):
    clients = Client.objects.get(id=pk)
    inv = Invoice.objects.filter(client_id=pk)
    count = inv.count()
    context = {
        'clients': clients,
        'inv': inv,
        'count': count,
    }
    return render(request,'app/clients.html', context)

#=-=-=-=-=-=-=-=-=-=-=-=-=-> I N V O I C E    V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


def displayInvoice(request, pk):
    inv = Invoice.objects.get(id=pk)
    prod = Product.objects.get()



def createInvoice(request):
    if request.method == "POST":
        form = CreateInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices')
    else:
        form = CreateInvoiceForm()
    return render(request, 'components/createInvoice.html', { 'form': form })


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'app/invoice.html'
    context_object_name = 'invoice'


def updateInvoice(request, pk):
    inv = Invoice.objects.get(id=pk)
    form = CreateInvoiceForm(instance=inv)
    if request.method == 'POST':
        form = CreateInvoiceForm(request.POST, instance=inv)
        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice updated successfully')
            return redirect('dashboard')
    else:
        form = CreateInvoiceForm(instance=inv)
        messages.warning(request, 'Error: Invoice Not Created')
        return render(request, 'components/createInvoice.html', {'form': form })



def deleteInvoice(request, pk):
    inv = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        inv.delete()
        messages.success(request, 'Invoice deleted successfully')
        return redirect('dashboard')
    context = { 
        'inv': inv,
    }

    return render(request, 'components/deleteInvoice.html', context)




class InvoicesListView(ListView):
    model = Invoice
    template_name = 'app/invoices.html'
    context_object_name = 'invoices'
    ordering = ('-date')




#=-=-=-=-=-=-=-=-=-=-=-=-=-> P R O D U C T    V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    
class ProductListView(ListView):
    model = Product
    template_name = 'app/products.html'
    context_object_name = 'products'



def products(request):
    inv = Invoice.objects.all()
    product = Product.objects.all()
    
    context = {
        'inv': inv,
        'product': product,
    }
    return render(request, 'app/products.html', context)



def createProduct(request):
    form = AddProductForm(request.POST)

    if form.is_valid():
        form.save
        return redirect('dashboard')
    else:
        form = AddProductForm()
    return render(request, 'components/addProduct.html', { 'form': form })



#=-=-=-=-=-=-=-=-=-=-=-=-=-> P A G E   V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("my-login")
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)



def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("my-login")



#=-=-=-=-=-=-=-=-=-=-=-=-=-> P A G E   V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#=-=-=-=-=-=-=-=-=-=-=-=-=-> P A G E   V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#



