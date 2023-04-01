# forms.py
from django import forms
from .models import *

class admin_bikesForm(forms.ModelForm):

	class Meta:
		model = bikes
		fields = ['disable']
		
class bikesForm(forms.ModelForm):

	class Meta:
		model = bikes
		fields = ['name','model','new','city','price','discription','img','username','disable']
		

class carsForm(forms.ModelForm):

	class Meta:
		model = cars
		fields = ['name','model','new','city','price','discription','img','username','disable']
		
class mobilesForm(forms.ModelForm):

	class Meta:
		model = mobiles
		fields = ['name','model','new','city','price','discription','img','username','disable']

class laptopsForm(forms.ModelForm):

	class Meta:
		model = laptops
		fields = ['name','model','new','city','price','discription','img','username','disable']


		

class admin_carsForm(forms.ModelForm):

	class Meta:
		model = cars
		fields = ['disable']
		
class admin_mobilesForm(forms.ModelForm):

	class Meta:
		model = mobiles
		fields = ['disable']

class admin_laptopsForm(forms.ModelForm):

	class Meta:
		model = laptops
		fields = ['disable']


class User_infoForm(forms.ModelForm):

	class Meta:
		model = User_info
		fields = ['User_name','user_contact','user_address','user_email']

class Buyer_infoForm(forms.ModelForm):

	class Meta:
		model = Buyer_info
		fields = ['Buyer_name','seller_name','product_id','Product_name','varification']


class RatingForm(forms.ModelForm):

	class Meta:
		model = Rating
		fields = ['buyer_id','Buyer_name','Product_catagory','product_id','rate','comment']


class contactForm(forms.ModelForm):

	class Meta:
		model = contact
		fields = ['name','email','subject','Details',]
