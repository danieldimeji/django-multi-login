from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login
from .forms import SignUpForm, SignInForm


class SignUpView(View):

    template_name = 'sign-up.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            print('Sign up successfull')
            return redirect('sign-up')
        else:
            print(form.errors)
            print('Sign up error')
            return render(request, self.template_name, {'form':self.form_class})


class SignInView(View):

    template_name = 'sign-in.html'
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = form.login()
            if user is not None:
                login(request, user)
                return redirect('sign-in')
            else:
                return render(request, self.template_name, {'form':self.form_class})
        else:
            print(form.errors)
            return render(request, self.template_name, {'form':self.form_class})
