from django import forms
from .models import Order, Customer, Product
from django.contrib.auth.models import User





class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_by", "shipping_address", "mobile", "email", "payment_method"]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    

       
    class Meta:
        model = Customer 
        fields = ["username", "password", "email", "full_name", "address"]
        
    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname). exists():
            raise forms.ValidationError(
            "Customer with this username allready exists!")
        return uname   



class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProductForm(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))

    class Meta:
        model = Product
        fields = ["title", "slug", "category", "image", "marked_price", "selling_price", "description", "warranty", "return_policy"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the product title here..."}),
            "slug": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the product slug here..."}),
            "category": forms.Select(attrs={"class":"form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "marked_price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "marked price of the product..."}),
            "selling_price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "selling price of the product..."}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descriptions hire...", "rows": 5 }),
            "warranty": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the product warrenty here..."}),
            "return_policy": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the product return police  here..."}),

        }



class PasswordForgotForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Enter email used in customer account..."})) 


    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass 
        else:
            raise forms.ValidationError(
             "Customer with this account dost not exists...")
        return e            