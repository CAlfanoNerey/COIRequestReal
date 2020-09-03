from django import forms
#from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator

from .models import Requester, Recipient, User

# from django.contrib.auth.forms import UserCreationForm
#
TITLE_STATES = [
    ('1','Alabama'), ('2','Alaska'), ('3','American Samoa'), ('4','Arizona'), ('5','Arkansas'), ('6','California'), ('7','Colorado'), ('8','Connecticut'), ('9','Delaware'),
    ('10','District of Columbia'), ('11','Florida'), ('12','Georgia'), ('13','Guam'), ('14','Hawaii'), ('15','Idaho'), ('16','Illinois'), ('17','Indiana'), ('18','Iowa'), ('19','Kansas'),
    ('20','Kentucky'), ('21','Louisiana'), ('22','Maine'), ('23','Maryland'), ('24','Massachusetts'), ('25','Michigan'), ('26','Minnesota'), ('27','Minor Outlying Islands'),
    ('28','Mississippi'), ('29','Missouri'), ('30','Montana'), ('31','Nebraska'), ('32','Nevada'), ('33','New Hampshire'), ('34','New Jersey'), ('35','New Mexico'), ('36','New York'),
    ('37','North Carolina'), ('38','North Dakota'), ('39','Northern Mariana Islands'), ('40','Ohio'), ('41','Oklahoma'), ('42','Oregon'), ('43','Pennsylvania'), ('44','Puerto Rico'),
    ('45','Rhode Island'), ('46','South Carolina'), ('47','South Dakota'), ('49','Tennessee'), ('50','Texas'), ('51','U.S. Virgin Islands'), ('52','Utah'), ('53','Vermont'), ('54','Virginia'),
    ('55','Washington'), ('56','West Virginia'), ('57','Wisconsin'), ('58','Wyoming'),

]

class RegisterUpdateForm(UserChangeForm):

    class Meta:
        model = User
        exclude= ['last_login', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'date_joined', 'groups','password']
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    #validators = [RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")]
    email = forms.EmailField(required = True)
    # error_messages = {
    #     'password_mismatch': "The two password fields didn't match.",
    # }
    # password1 = forms.CharField(label="Password",
    #                             widget=forms.PasswordInput)
    # password2 = forms.CharField(label="Password confirmation",
    #                             widget=forms.PasswordInput,
    #                             help_text="Enter the same password as above, for verification.")

    # name = forms.CharField(max_length=200)
    # address_line1 = forms.CharField(max_length=200)
    # address_line2 = forms.CharField(required=False, max_length=200)
    # # state = models.ForeignKey('States', null=True, blank=True)
    # city = forms.CharField(max_length=200)
    # state_or_territory = forms.ChoiceField(choices=TITLE_STATES)
    # # zipcode = models.PositiveIntegerField(blank =True, null=True, validators=[MaxValueValidator(99999)])
    # zipcode = forms.IntegerField(validators=[MaxValueValidator(99999)])
    # fax = forms.IntegerField(required=False)

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'date_joined', 'groups','password']
        fields = ('__all__')


            # 'name',
            # 'first_name',
            # 'last_name',
            # 'email',
            # 'address_line1',
            # 'address_line2',
            # 'city',
            # 'state_or_territory',
            # 'zipcode',
            # 'fax',
            #       )

class UpdatePasswordForm(UserCreationForm):


    class Meta:

        model= User
        exclude= [
            'name',
            'first_name',
            'last_name',
            'email',
            'address_line1',
            'address_line2',
            'city',
            'state_or_territory',
            'zipcode',
            'fax',
            'last_login', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'date_joined', 'groups',
            'password',
            'username'
        ]



class RequesterForm(forms.ModelForm):
    # addresLine1 = forms.CharField(label = 'Address Line 1', max_length=200,)
    # addresLine2 = forms.CharField(required=False)
    # city = forms.CharField(label = 'City', max_length=200,)
    # zip = forms.IntegerField(validators=[MaxValueValidator(99999)])
    # fax = forms.IntegerField(required=False)

    class Meta:
        model = Requester
        exclude = ['user']
        fields = ('__all__')

class RecipientForm(forms.ModelForm):

    class Meta:
        model = Recipient
        exclude = ['user']
        fields = ('__all__') #('user', 'name', 'address_line1', 'address_line2', 'city','state','email', 'zipcode', 'fax')


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
