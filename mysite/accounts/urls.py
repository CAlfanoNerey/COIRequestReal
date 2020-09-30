from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView
from .views import SignUpView


urlpatterns = [
    path('', views.indexView, name='home'),

    path('dashboard/', views.dashboardView, name="dashboard"),
    path('register/', views.SignUpView, name='register_url'),
    path('contact/',views.ContactView.as_view(), name= 'contact'),
    path('login/', views.loginview, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/requester/', views.requesterView, name='requester_url'),
    path('requester/', views.requesterView, name='requester_url'),
    path('<int:pk>/profile/', views.ViewProfile.as_view(), name='view_profile'),
    path('requesterupdate/', views.edit_profile, name='requester_update'),
    path('recipient/', views.recipientView, name='recipient'),
    path('<int:pk>/password/', views.edit_password, name='password'),
    #path('<int:pk>/viewdoc/', views.viewdoc, name='viewdoc')
    path('rChoose/', staff_member_required(views.getRequesterView.as_view()), name='rChoose'),
    path('<int:pk>/editrequester/', views.editRequesterView, name='editrequester'),
    path('<int:pk>/editrecipient/', views.editRecipientView, name='editrecipient'),
    path('<int:pk>/certholder/', login_required(views.CertHolderView.as_view()), name='certholder'),
    path('<int:pk>/droppdf/', views.dropPDF.as_view(), name='dropPDF'),
    path('<int:pk>/admindroppdf/', views.admindropPDF, name='admindroppdf'),
    path('email/', views.email, name='demail'),
    path('<int:pk>/viewdoc/', views.GeneratePdf.as_view(), name='viewdoc'),
    path('<int:pk>/adminviewdoc/', views.adminGeneratePdf, name='viewdoc'),
    path('<int:pk>/emailview/', views.EmailView.as_view(), name='emailview'),
    path('<int:pk>/admincertholder/', views.AdminCertHolderView.as_view(), name='admincertholder'),
    path('<int:pk>/adminzrecipient/', views.AdminzRecipientView, name='adminzrecipient'),
    path('<int:pk>/delete/', views.RecipientDeleteView, name='recipientdelete')
    # path('passwordsubmit/',views.PasswordSubmit.as_view(), name= 'passwordsubmit')
    # path(
    #     'login/',
    #     LoginView.as_view(
    #         template_name="login.html",
    #         authentication_form=UserLoginForm
    #         ),
    #     name='login'
    # ),
]
