from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View

from accounts.account_links import *
from accounts.models import *
from accounts.utils import *
from .forms import UserForm


def recoveryRender(request):
	return HttpResponse("Enter email to recover !!!")


def homepageRender(request):
	return render(request, USER_DASHBOARD_PAGE)


def modalpageRender(request):
	return render(request, "index.html")


class LoginView(TemplateView):
	template_name = 'accounts/login_v4.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/')
		else:
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = {'loggedIn': False}
		if self.request.user.is_authenticated:
			print('Logged in: ' + str(self.request.user))
			ctx['loggedIn'] = True
		return ctx

	def post(self, request, *args, **kwargs):
		print(pretty_request(request))
		# print(request.get_host().split('.')[0])
		username = request.POST.get('username', False)
		password = request.POST.get('pass', False)
		# is_customer_domain = request.get_host().split('.')[0] == 'www'
		if username and password:
			user = authenticate(request, username=username, password=password)
			if user is not None and user.is_customer:
				login(request, user)
				print('Signing in: ' + str(request.user))
				return redirect('/')
			elif not user.is_customer:
				return HttpResponse('Not a Customer account')
			else:
				return HttpResponse('Error: User authentication error <a href="/login"">Try again</a>')
		else:
			return HttpResponse('Error: Username or password is empty <a href="/login">Try again</a>')


class ManagerLoginView(TemplateView):
	template_name = 'accounts/Manager_Login.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/homepage')
		else:
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = {'loggedIn': False}
		if self.request.user.is_authenticated:
			print('Logged in: ' + str(self.request.user))
			ctx['loggedIn'] = True
		return ctx

	def post(self, request, *args, **kwargs):
		print(pretty_request(request))
		username = request.POST.get('username', False)
		password = request.POST.get('pass', False)
		if username and password:
			user = authenticate(request, username=username, password=password)
			rest = Restaurant.objects.get(user=user)
			if user is not None and user.is_manager and rest.restaurant_key != '0':
				login(request, user)
				print('Signing in: ' + str(request.user))
				return redirect('/homepage')
			elif rest.restaurant_key == '0':
				return HttpResponse('Your account has not been approved yet')
			elif not user.is_manager:
				return HttpResponse('Not a Manager account')
			else:
				return HttpResponse('Error: User authentication error <a href="/login"">Try again</a>')
		else:
			return HttpResponse('Error: Username or password is empty <a href="/login">Try again</a>')


class AdminLoginView(TemplateView):
	template_name = 'accounts/Manager_Login.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/homepage')
		else:
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = {'loggedIn': False}
		if self.request.user.is_authenticated:
			print('Logged in: ' + str(self.request.user))
			ctx['loggedIn'] = True
		return ctx

	def post(self, request, *args, **kwargs):
		print(pretty_request(request))
		username = request.POST.get('username', False)
		password = request.POST.get('pass', False)
		if username and password:
			user = authenticate(request, username=username, password=password)
			if user is not None and user.is_superuser:
				login(request, user)
				print('Signing in: ' + str(request.user))
				return redirect('/homepage')
			elif not user.is_superuser:
				return HttpResponse('Not a Admin account')
			else:
				return HttpResponse('Error: User authentication error <a href="/login"">Try again</a>')
		else:
			return HttpResponse('Error: Username or password is empty <a href="/login">Try again</a>')


class RegisterView(TemplateView):
	template_name = 'accounts/colorlib-regform-7.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/')
		else:
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = super(RegisterView, self).get_context_data(**kwargs)
		ctx['user_form'] = UserForm(prefix='user')
		# ctx['profile_form'] = ProfileForm(prefix='profile')
		ctx = {'loggedIn': False}
		if self.request.user.is_authenticated:
			print('Logged in: ' + str(self.request.user))
			ctx['loggedIn'] = True
		return ctx

	def post(self, request, *args, **kwargs):
		print(request.POST)
		# print(pretty_request(request))

		# if password!=password_confirm
		# 	return

		user_form = UserForm(request.POST)
		# profile_form = ProfileForm(request.POST or None, request.FILES or None, prefix='profile')
		#
		# print(profile_form)

		if user_form.is_valid():
			user = user_form.save(commit=False)
			user.is_customer = True
			user.save()
			p = UserProfile.objects.create(user=user)
			p.save()
			print('Registering : ' + str(request.user))
			login(request, user)
			return redirect('/')
		# return HttpResponse("Signed Up!<br><a href='/'>Go to home</a>")
		else:
			return HttpResponse("Error : <a href='/signup'>Try again</a>!")


# class restaurant_t:
#
# 	def __init__(self, rest_name='', user_name='', email='', trade_license='', password=''):
# 		self.rest_name = rest_name
# 		self.user_name = user_name
# 		self.email = email
# 		self.trade_license = trade_license
# 		self.password = password
#
# 	def save(self):
#


class ManagerRegisterView(TemplateView):
	template_name = 'accounts/Manager_Registration_form.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/')
		else:
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = super(ManagerRegisterView, self).get_context_data(**kwargs)
		ctx['user_form'] = UserForm(prefix='user')
		# ctx['profile_form'] = ProfileForm(prefix='profile')
		ctx = {'loggedIn': False}
		if self.request.user.is_authenticated:
			print('Logged in: ' + str(self.request.user))
			ctx['loggedIn'] = True
		return ctx

	def post(self, request, *args, **kwargs):
		print(pretty_request(request))

		if request.POST.get('password') != request.POST.get('re_pass'):
			return

		user_form = UserForm(request.POST)
		user = None
		if user_form.is_valid():
			user = user_form.save(commit=False)
			user.is_manager = True
			user.save()
			login(request, user)
		# UserProfile.objects.create(user=user).save() # lagbe na i guess
		else:
			return HttpResponse("Invalid Form or pass")

		rest = Restaurant()
		# rest.user = User(username=request.POST['username'], password=request.POST['password'],
		#                  email=request.POST['email'])
		rest.restaurant_name = request.POST['rest_name']
		rest.trade_license = request.POST['trade_license']

		# rest.user.save()
		# rest.user = User.objects.get(username=request.POST['username'])
		rest.user = user
		rest.save()
		return redirect('/homepage')


class BranchRegisterView(TemplateView):
	template_name = 'accounts/Branch_Registration_Form.html'

	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/')
		else:
			return super().get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		ctx = super(BranchRegisterView, self).get_context_data(**kwargs)
		ctx['user_form'] = UserForm(prefix='user')
		# ctx['profile_form'] = ProfileForm(prefix='profile')
		ctx = {'loggedIn': False}
		if self.request.user.is_authenticated:
			print('Logged in: ' + str(self.request.user))
			ctx['loggedIn'] = True
		return ctx

	def post(self, request, *args, **kwargs):
		print(pretty_request(request))

		if request.POST.get('password') != request.POST.get('re_pass'):
			return

		user_form = UserForm(request.POST)
		user = None
		branch = RestaurantBranch()

		try:
			rest = Restaurant.objects.get(restaurant_key=request.POST['rest_key'])
			print(rest)
			if user_form.is_valid():
				user = user_form.save(commit=False)
				user.is_manager = True
				user.save()
				branch.user = user
				branch.restaurant_id = rest
				branch.save()
				login(request, user)
		# UserProfile.objects.create(user=user).save() # lagbe na i guess
			else:
				return HttpResponse("Invalid Form or pass")
		except Exception as e:
			return HttpResponse('Not Valid secret key')



		# rest.user = User(username=request.POST['username'], password=request.POST['password'],
		#                  email=request.POST['email'])
		print(branch)
		return redirect('/homepage')


# return HttpResponse("Signed Up!<br><a href='/'>Go to home</a>")


# <QueryDict: {'csrfmiddlewaretoken': ['wOK59fUnGw3uc4TTqlzeOoAI7xCzwnXZUYRrqdPOx6srYtgei56x0ne0JerJc2j5'],
# 'rest_name': ['Darbar'], 'username': ['notfound'], 'email': ['darbar@nowhere.com'], 'trade_license': ['420'],
# 'password': ['123456'], 're_pass': ['123456'], 'agree-term': ['on'], 'signup': ['Register']}>
# Registering : AnonymousUser

# user_form = UserForm(request.POST)
# rest_form = RestaurantForm(request.POST)
# profile_form = ProfileForm(request.POST or None, request.FILES or None, prefix='profile')
#
# print(profile_form)

# if user_form.is_valid():
# 	user = user_form.save(commit=False)
# 	user.save()
# 	p = UserProfile.objects.create(user=user)
# 	p.save()
# 	print('Registering : ' + str(request.user))
# 	return HttpResponse("Signed Up!<br><a href='/'>Go to home</a>")
# else:
# 	return HttpResponse("Error : <a href='/signup'>Try again</a>!")


def BranchRegister(request):
	user_form = UserForm(request.POST)
	# profile_form = ProfileForm(request.POST or None, request.FILES or None, prefix='profile')
	#
	# print(profile_form)

	if user_form.is_valid():
		user = user_form.save(commit=False)
		user.save()
		p = UserProfile.objects.create(user=user)
		p.save()
		print('Registering : ' + str(request.user))
		return HttpResponse("Signed Up!<br><a href='/'>Go to home</a>")
	else:
		return HttpResponse("Error : <a href='/signup'>Try again</a>!")


class LogoutView(View, LoginRequiredMixin):
	def get(self, request):
		print('Signing out: ' + str(request.user))
		logout(request)
		return redirect('/')


class ManagerLogoutView(View, LoginRequiredMixin):
	def get(self, request):
		print('Signing out: ' + str(request.user))
		logout(request)
		return redirect('/')
