from django import forms
# from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, RegexValidator

from .models import Requester, Recipient, User, Contact

# from django.contrib.auth.forms import UserCreationForm
#
TITLE_STATES = [
    ('1', 'Alabama'), ('2', 'Alaska'), ('3', 'American Samoa'), ('4', 'Arizona'), ('5', 'Arkansas'),
    ('6', 'California'), ('7', 'Colorado'), ('8', 'Connecticut'), ('9', 'Delaware'),
    ('10', 'District of Columbia'), ('11', 'Florida'), ('12', 'Georgia'), ('13', 'Guam'), ('14', 'Hawaii'),
    ('15', 'Idaho'), ('16', 'Illinois'), ('17', 'Indiana'), ('18', 'Iowa'), ('19', 'Kansas'),
    ('20', 'Kentucky'), ('21', 'Louisiana'), ('22', 'Maine'), ('23', 'Maryland'), ('24', 'Massachusetts'),
    ('25', 'Michigan'), ('26', 'Minnesota'), ('27', 'Minor Outlying Islands'),
    ('28', 'Mississippi'), ('29', 'Missouri'), ('30', 'Montana'), ('31', 'Nebraska'), ('32', 'Nevada'),
    ('33', 'New Hampshire'), ('34', 'New Jersey'), ('35', 'New Mexico'), ('36', 'New York'),
    ('37', 'North Carolina'), ('38', 'North Dakota'), ('39', 'Northern Mariana Islands'), ('40', 'Ohio'),
    ('41', 'Oklahoma'), ('42', 'Oregon'), ('43', 'Pennsylvania'), ('44', 'Puerto Rico'),
    ('45', 'Rhode Island'), ('46', 'South Carolina'), ('47', 'South Dakota'), ('49', 'Tennessee'), ('50', 'Texas'),
    ('51', 'U.S. Virgin Islands'), ('52', 'Utah'), ('53', 'Vermont'), ('54', 'Virginia'),
    ('55', 'Washington'), ('56', 'West Virginia'), ('57', 'Wisconsin'), ('58', 'Wyoming'),

]


class RegisterUpdateForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'date_joined', 'groups',
                   'password']
        fields = '__all__'



class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    # validators = [RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")]
    email = forms.EmailField(required=True)

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
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'date_joined', 'groups',
                   'password', 'first_name', 'last_name']
        fields = ('__all__')

    class PasswordForm(forms.ModelForm):
        class Meta:
            model = User
            exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'user_permissions', 'date_joined',
                       'groups', 'password', 'username', 'divison', 'address_line1', 'address_line2', 'city',
                       'state_or_territory'
                       'zipcode', 'fax',

                       ]

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
        model = User
        exclude = [
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
            'username',
            'division',

        ]


class RequesterForm(forms.ModelForm):
    # addresLine1 = forms.CharField(label = 'Address Line 1', max_length=200,)
    # addresLine2 = forms.CharField(required=False)
    # city = forms.CharField(label = 'City', max_length=200,)
    # zip = forms.IntegerField(validators=[MaxValueValidator(99999)])
    # fax = forms.IntegerField(required=False)

    class Meta:
        model = Requester
        fields = ('__all__')


class DatePicker(forms.DateInput):
    input_type = 'date'


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        exclude = ['user', 'pdf', 'dpdf','description']
        labels = {
            'projectname': 'Project Name',
            'wcity': 'City',
            'wstate': 'State',
            'wzipcode': 'Zipcode',
            'description': 'Description',
            'projectsdate': 'Project Start Date',
            'projectedate': 'Project End Date',
            'rtype': 'Request Type If Needed',
            'employeenum': 'Estimated Number of Employees for Project',
            'cost': 'Estimated Payroll for Project',
            'datefield': 'Date',
            'notes': 'Notes'

        }
        fields = (
            '__all__')  # ('user', 'name', 'address_line1', 'address_line2', 'city','state','email', 'zipcode', 'fax')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 76}),
            'datefield': DatePicker(),
            'projectedate': DatePicker(),
            'projectsdate': DatePicker()
        }
        help_texts = {'projectname': 'Optional If Standard',
                      'wcity': 'Optional If Standard',
                      'wstate': 'Optional If Standard',
                      'wzipcode': 'Optional If Standard',
                      'description': 'Optional If Standard',
                      'projectsdate': 'Optional If Standard',
                      'projectedate': 'Optional If Standard',
                      'employeenum': 'Optional If Standard',
                      'cost': 'Optional If Standard',
                      'notes': 'Any Additional Information Regarding the Request',
                      'address': 'Optional If Standard'

                      }



class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        labels = {
            'yourbusinessname':'Business Name',
            'yourname': 'Name',
            'address' : 'Address Line 1',
            'address2' : 'Address Line 2',
            'city' : 'City',
            'state' :'State',
            'zipcode' : 'Zip Code',
            'phonenumber' : 'Phone Number',
            'email' : 'Email'
        }
        fields=('__all__')


class ContactUpdateForm(UserChangeForm):
    class Meta:
        model = Contact

        labels = {
            'yourbusinessname': 'Business Name',
            'yourname': 'Name',
            'address': 'Address Line 1',
            'address2': 'Address Line 2',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zip Code',
            'phonenumber': 'Phone Number',
            'email': 'Email'
        }
        fields = ('__all__')


class RequesterDisplayForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Requester
        fields = ('name',)

    def get_name(self):
        return self.name


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
