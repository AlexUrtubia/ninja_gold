from django.shortcuts import redirect, render
from random import randint
# Create your views here.
def inicio(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
    return render(request, 'index.html')

def process_money(request):
    if "farm" in request.POST:
        request.session['gold_amount'] += randint(10,20)
        
    if "cave" in request.POST:
        request.session['gold_amount'] += randint(5,10)
        
    if "house" in request.POST:
        request.session['gold_amount'] += randint(10,15)
        
    if "casino" in request.POST:
        request.session['gold_amount'] += randint(-50,50)
        
    return redirect('/')