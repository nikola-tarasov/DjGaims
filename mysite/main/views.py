from django.shortcuts import redirect, render
from django.views import View
from .models import Gaim,Likes
from  .form import CommentsForms



# Create your views here.



class Gaims(View):
    def get(self, request):
        posts = Gaim.objects.all()
        return render(request, 'main/index.html', {'post': posts})
    

class DitailPost(View):
    def get(self, request, pk):
        post = Gaim.objects.get(id = pk)
        return render(request, 'main/ditailPost.html', {"post":post})
    
class addComments(View):
    def post(self, request, pk):
        form = CommentsForms(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk 
            form.save() 
            return redirect(f"/{pk}")

def get_ip_client(request):
    x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward:
        ip = x_forward.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_ip_client(request)
        try:
            Likes.objects.get(ip = ip_client, pos_id = pk)
            return redirect(f"/{pk}")
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect (f"/{pk}")

class DelLike(View):
    def get(self, request, pk):

        ip_client = get_ip_client(request)

        try:
            like =  Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect (f'/{pk}')
        except:
            return redirect (f'/{pk}')









      
        
