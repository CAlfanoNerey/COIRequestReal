import datetime
import glob
import os
from io import BytesIO

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.core.files import File
from datetime import datetime
import time
from django.db.backends.utils import logger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import ListView
from xhtml2pdf import pisa

from .forms import RequesterForm, RecipientForm, RegistrationForm, RegisterUpdateForm, UpdatePasswordForm, \
    RequesterDisplayForm

from django.views.generic.edit import CreateView, UpdateView, FormView
from .models import Recipient, Requester, User, Contact

from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import views as auth_views

# Create your views here.
from .utils1 import render_to_pdf


def indexView(request):
    return render(request, 'index.html')

class viewdoc(generic.DetailView):
    model = Recipient

    template_name = 'COIDoc2.html'


# class PickRequesterView(View):
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         requesterDisplay=


class getRequesterView(generic.DetailView):

    def get(self, request, *args, **kwargs):

        requesterdisplay = Requester.objects.all()

        return render(request, 'rChoose.html', {
            'requesterdisplay': requesterdisplay,
        })
        template_name = 'rChoose.html'
        return render(request, template_name, data)


@staff_member_required()
def editRequesterView(request, pk = None):
    if pk:
        requesterrec = Requester.objects.get(id=pk)
        form = RequesterForm(instance=requesterrec)
        if request.method == 'POST':
            form = RequesterForm(request.POST, instance=requesterrec)
            form.save()
            return redirect('accounts:rChoose')

    args = {'requester': requesterrec, 'form': form}

    return render(request, 'editrequester.html', args)



    # if request.method == "POST":
    #     context = {}
    #     form = RequesterDisplayForm(request.POST)
    #
    #     context['form'] = form
    #
    #     if form.is_valid():
    #         name = form.requester_id()
    #         return redirect('certholder', {'slug':name} )
    # else:
    #     form = RequesterDisplayForm()
    # return render(request, 'rChoose.html', {'form': form})


# @staff_member_required
class CertHolderView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        userdisplay = User.objects.all()
        recipientdisplay = Recipient.objects.all().filter(user_id = user)

        # data = {
        #     # 'user' : request.user.name,
        #     'user': userdisplay,
        #     'recipient': recipientdisplay
        # }


        return render(request, 'certholder.html', {
            'user': userdisplay,
            'recipient': recipientdisplay,
            'error_message': "You didn't select a choice.",
        })
        template_name = 'certholder.html'
        return render(request, template_name,data)

@staff_member_required()
def editRecipientView(request, pk=None):
    if pk:

        getrecipient = Recipient.objects.get(id=pk)
        #key = Recipient.objects.get(Requester_id=pk)
        form = RecipientForm(instance=getrecipient)
        if request.method == 'POST':
            form = RecipientForm(request.POST, instance=getrecipient)
            form.save()
            return redirect("accounts:certholder", pk = pk )

    args = {'recipient': getrecipient, 'form': form}

    return render(request, 'editrecipient.html', args)


# class CertHolderView(generic.DetailView):
#
#     def get(self, request, *args, **kwargs):
#
#         # user = request.user
#         # currUser = User.objects.get(id = user.pk)
#         # userdisplay = User.objects.all()
#         # recipientdisplay = Recipient.objects.all().filter(user_id = user)
#
#
#         requesterdisplay = Requester.objects.all()
#         recipientdisplay = Recipient.objects.all().filter(Requester.Requester_id )
#
#         #currRequester
#
#         return render(request, 'certholder.html', {
#             'currUser': currUser,
#             'user': userdisplay,
#             'recipient': recipientdisplay,
#             'error_message': "You didn't select a choice.",
#         })
#         template_name = 'certholder.html'
#         return render(request, template_name,data)

# class CertHolderView(ListView):
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         queryset = Recipient.objects.filter(user_id = user)
#         return render(request,queryset)


# class GeneratePdf(View):
#     def get(self, request, pk = None, requester_pk = None):
#         if pk:
#             cRequester = Requester.objects.get(id = requester_pk)
#             recipientdisplay = Recipient.objects.get(id=pk)
#
#             data = {'requester': cRequester, 'recipient': recipientdisplay}
#
#             pdf = render_to_pdf('COIDoc.html', data)
#             return HttpResponse(pdf, content_type='application/pdf')


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        user = request.user

        contact = Contact.objects.get(id=user.division_id)
        userdisplay = User.objects.get(id = user.id)
        recipientdisplay = Recipient.objects.get(id=self.kwargs['pk'])
        data = {
            # 'user' : request.user.name,
            'user': userdisplay,
            'recipient': recipientdisplay,
            'contact':contact
        }
        pdf = render_to_pdf('COIDoc.html', data)
        return HttpResponse(pdf, content_type='application/pdf')



# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('invoice.html')
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cooper",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('invoice.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")


@login_required()
def dashboardView(request):
    return render(request, 'accounts:dashboard.html')


def logoutview(request):
    return render(request, 'registration/logged_out.html')

# class SignUpView(CreateView):
#     form_class = RegistrationForm
#     success_url = reverse_lazy('accounts:login')
#     template_name = 'registration/register.html'

def SignUpView(request):
    if request.method == 'POST':
        context={}
        form =  RegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            newuser= form.save()

            return HttpResponseRedirect(reverse('emailview', args=(newuser.pk,)))


    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})



# class PasswordSubmit(FormView):
#     template_name = 'ppassword.hmtl'
#     form_class = 'PasswordForm'
#     success_url= 'accounts/emailview'

class EmailView(View):
    def get(self, request, *args, **kwargs):


        userpass= User.objects.get(id=self.kwargs['pk'])


        demail=EmailMessage(
            subject= 'login credentials',
            body = 'your username is'+' ' + str(userpass.username) + '\nyour password is '+str(userpass.ppassword),
            from_email= 'jhaverihussain@gmail.com',
            to=[userpass.email],
        )

        demail.send()
        return redirect('accounts:home')



# def registerView(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#
#             return redirect('login_url')
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'registration/register.html', {'form': form})


@staff_member_required
def requesterView(request):
    # context= {}
    # form = RequesterForm(request.POST)
    # context['form'] = form

    args = {'user': request.user}

    if request.method == "POST":

        context = {}
        form = RequesterForm(request.POST)
        form.instance.user = request.user
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    else:
        form = RequesterForm()
    return render(request, 'requester.html', {'form': form}, )


# def view_profile(request):
#     args = {'user': request.user}
#     return render(request, 'profile.html', args)

class ViewProfile(generic.DetailView):
    model = User
    template_name = 'profile.html'


def edit_profile(request):
    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile', pk=request.user.pk)

    else:
        form = RegisterUpdateForm(instance=request.user)
        args= {'form': form}
        return render(request, 'edit_profile.html', args)


@login_required()
def edit_password(request):
    if request.method == 'POST':
        form= UpdatePasswordForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile', pk=request.user.pk)
    else:
        form= UpdatePasswordForm()
        args={'form': form}
        return render(request, 'password.html', args)








#@staff_member_required
def recipientView(request):

        if request.method == "POST":

            context = {}
            form = RecipientForm(request.POST)
            form.instance.user = request.user
            context['form'] = form


            if form.is_valid():

                new_recipient = form.save()

                return HttpResponseRedirect(reverse('dropPDF', args=( new_recipient.pk, ) ))
        else:
            form = RecipientForm()
        return render(request, 'recipient.html', {'form': form}, )


class dropPDF(View):
    def get(self,request,*args,**kwargs):

        user = request.user

        contact = Contact.objects.get( id = user.division_id)
        userdisplay = User.objects.get(id=user.id)
        recipientdisplay = Recipient.objects.get(id=self.kwargs['pk'])
        data = {
            'user': userdisplay,
            'recipient': recipientdisplay,
            'contact' :contact
        }
        pdf = render_to_pdf('COIDoc.html', data)
        today= datetime.now()
        todays = today.strftime("%d-%b-%Y (%I:%M:%S)")

        filename = userdisplay.name+'_'+recipientdisplay.name + '_' + todays + ".pdf"
        recipientdisplay.pdf.save(filename, File(BytesIO(pdf.content)))
        recipientdisplay.dpdf.save(filename, File(BytesIO(pdf.content)))

        return redirect('accounts:demail')

def email(request):
    list_of_files = glob.glob(
        '/Users/husj/PycharmProjects/Finalrepo/COIRequestReal/mysite/pdf/pdf/*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    # print(latest_file)

    demail = EmailMessage(
        subject='email with attachment',
        body='your attachment',
        from_email='jhaverihussain@gmail.com',
        to=['jhaverihussain@gmail.com'],
    )
    demail.attach_file(latest_file)
    demail.send()
    return redirect('accounts:home')


def RequesterUpdate(request):
    model = User
    form_class = RegisterUpdateForm()
    template_name = "edit_requester.html"
    success_url = 'profile'

   # def getobject(self, *args, **kwargs):
   #      user_ = self.request.user
   #      return get_object_or_404(User, user=user_)






def loginview(request):
    if request.method == "POST":

        context = {}
        form = AuthenticationForm(None, request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:home')
    else:
        if request.user.is_authenticated:
            return redirect('accounts:home')
        else:
            ...

        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form}, )













# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             form=
#             return render(request, 'logged_in.html')
#         else:
#             return render(request, 'login.html',
#                 {'message': 'Bad username or password'}
#             )
#     else:
#         return render(request, 'login.html')
