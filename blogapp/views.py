from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpform, Blogform
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Blogmodels
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView

# Create your views here.


@csrf_protect
class Registeruser(View):
    def get(self, request):
   
        fm = SignUpform()
        return render(request, "base/signup.html", {"form": fm})

    def post(self, request):
        fm = SignUpform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("login")
        return render(request, "base/signup.html", {"form": fm})


class Loginpage(View):
    def get(self, request):
        fm = AuthenticationForm()
        if request.user.is_authenticated:
            return redirect("userblog")
        else:
            return render(request, "base/login.html", {"form": fm})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("userblog")
        else:
            messages.info(request, "Email or password is incorrect")
        return render(request, "base/login.html", {"form": form})


class Logoutuser(View):
    def post(self, request):
        logout(request)
        return redirect("home")




class Userblog(LoginRequiredMixin, View):
    def get(self, request):
        form = Blogform(request.POST)
  
        user = Blogmodels.objects.filter(user=request.user.id)

        return render(request, "base/userblog.html", {"form": form, "user": user})
    
    

    def post(self, request):
        form = Blogform(request.POST, request.FILES)
        user = Blogmodels.objects.filter(user=request.user.id)

        if form.is_valid():
            new_blog = form.save(commit=False)

            existing_title = Blogmodels.objects.filter(
                blog_title=new_blog.blog_title, user=request.user.id
            )

            if existing_title.exists():
                messages.error(
                    request, "Title already exists choose another title for your blog"
                )
            else:
                new_blog.user = request.user
                new_blog.save()
                messages.success(request, "Blog has been added.")
            return redirect("userblog")
        else:
            messages.error(request, "Form is not valid.")

            return render(request, "base/userblog.html", {"form": form, "user": user})


class Editblog(LoginRequiredMixin,View):
    def get(self, request, id):
        blog = get_object_or_404(Blogmodels, id=id)
        form = Blogform( instance=blog)
        user_id = blog.user_id
       
        context = {"blog": [blog],
                   "form":form }
        get_object_or_404(Blogmodels, id=id, user_id=request.user.id)
        return render(request, "base/edit.html", context)
        

    def post(self, request ,id):
        
        
        blog = get_object_or_404(Blogmodels, id=id)
        print(blog)
        form = Blogform(request.POST, instance=blog)
        user = request.user.id

        if request.user == blog.user:
            if form.is_valid():
                form.save()
            
            return redirect("/userblog")

        else:
            messages.error(request, "You are not authorized to edit this task.")
            return redirect("/userblog")
            

        


class Homepage(View):
    def get(self, request):
        
        obj = Blogmodels.objects.all()
        
        paginator = Paginator(obj,2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
        "obj":obj,
        "page_obj": page_obj
        
        }
        return render(request, "base/home.html", context)
    

class Blogdetail(View):
    def get(self,request, slug):
        obj = get_object_or_404(Blogmodels, slug=slug)
        context = {"obj": obj}
        return render(request, "base/blogdetail.html", context)

class Blogdelete(LoginRequiredMixin,View):
    def get(self, request, id):
        obj = get_object_or_404(Blogmodels, id =id)
        context = {"obj": obj}
        
        user =request.user.id
        
        if request.user == obj.user:
            obj.delete()
            messages.success(request,("Blog has been deleted"))
            
            return redirect('userblog')
        else:
            messages.error(request, "You are not authorized to delete this task.")
            return redirect("/home")
    


class Createblog(LoginRequiredMixin, View):
    def get(self, request):
        form = Blogform(request.POST)
  
        user = Blogmodels.objects.filter(user=request.user.id)

        return render(request, "base/create.html", {"form": form, "user": user})
    
    

    def post(self, request):
        form = Blogform(request.POST, request.FILES)
        user = Blogmodels.objects.filter(user=request.user.id)

        if form.is_valid():
            new_blog = form.save(commit=False)

            existing_title = Blogmodels.objects.filter(
                blog_title=new_blog.blog_title, user=request.user.id
            )

            if existing_title.exists():
                messages.error(
                    request, "Title already exists choose another title for your blog"
                )
            else:
                new_blog.user = request.user
                new_blog.save()
                messages.success(request, "Blog has been added.")
            return redirect("userblog")
        else:
            messages.error(request, "Form is not valid.")

            return render(request, "base/userblog.html", {"form": form, "user": user})

