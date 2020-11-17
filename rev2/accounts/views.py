from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method =="POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request,'회원가입 환영합니다')
            signed_user.send_welcome_email()   # FIXME : 비동기 혹은 Celery로 처리하는 것을 추천 ㄴ
            next_url=request.GET.get('next','/')
            return redirect(next_url)
    else :
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form':form,
    })