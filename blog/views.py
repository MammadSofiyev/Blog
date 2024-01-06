from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post,Comment,About
from .forms import Addcomm,Contact,PostForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls  import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class Homeview(ListView):
    model = Post
    template_name = "blog/home.html"



class Article_page(DetailView):
    model = Post
    template_name = "blog/article.html"
    def get_context_data(self, *args, **kwargs):
          context = super(Article_page, self).get_context_data(*args, **kwargs)
       
          # Remove the line trying to fetch 'pk' from self.kwargs
          # stuff = get_object_or_404(Post, id=self.kwargs['pk'])
          
          # Use aggregate to get total likes for all posts
          stuff = get_object_or_404(Post, id=self.kwargs['pk'])
          total_likes = stuff.total_likes()
          context['total_likes'] = total_likes
          return context
       

class Add_post(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/addpost.html"

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign logged-in user as the author
        return super().form_valid(form)

class UpdateViewform(UpdateView):
     model = Post
     template_name = 'blog/update.html'
     fields = ['title','author','body']
def Log_in(request):
   if request.method == 'POST':
       username = request.POST.get('username')
       pass2 = request.POST.get('pass')
       user = authenticate(request,username=username,password=pass2)
       if user is not None:
         login(request,user)
         return redirect('home')
       else:
         return HttpResponse("Username or password is incorrect")
         
   return render(request,"blog/login.html")
def Sign_up(request):
     if request.method == 'POST':
          uname = request.POST.get('username')
          email = request.POST.get('email')
          pass2 = request.POST.get('pass')
          pass3 = request.POST.get('pass2')
          if pass2!=pass3:
            return HttpResponse("Your passwords do not match!")
          else:
            myuser = User.objects.create_user(uname,email,pass2)
            myuser.save()
            return redirect("login")
          
       
     return render (request,'blog/signup.html')
def Logout(request):
  logout(request)
  return redirect('login')

class  Contact(CreateView):
  model = Contact
  form_class = Contact
  template_name = 'blog/contact.html'
  success_message = 'Everything is fine'
  success_url = reverse_lazy('contact')

class  Addcommentview(CreateView):
   model = Comment
   form_class = Addcomm
   template_name = 'blog/addcomment.html'
   def form_valid(self,form):
     form.instance.post_id =self.kwargs['pk']
     return super().form_valid(form)
   success_url = reverse_lazy('home')

def ab(request):
  about = About.objects.first()
  context = {'body': about.body}
  return render(request,'blog/aboutus.html',context)
   
def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)  # Use the post ID from the URL directly
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))
   

@login_required 
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('some_success_url')  
    else:
        form = PostForm()
    return render(request, 'addpost.html', {'form': form})
