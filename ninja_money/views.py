from django.shortcuts import redirect, render
from random import randint
from datetime import datetime

# Create your views here.
def inicio(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
        request.session['jugadas'] = []
    return render(request, 'index.html')

def process_money(request):
    time = datetime.now().strftime("a las %H:%M %p del %d-%m-%Y")
    if "farm" in request.POST:
        farm_prize = randint(10,20)
        request.session['gold_amount'] += farm_prize
        request.session['jugadas'].append([farm_prize, "Farm", time])
        
    if "cave" in request.POST:
        cave_prize = randint(5,10)
        request.session['gold_amount'] += cave_prize
        request.session['jugadas'].append([cave_prize, "Cave", time])
        
    if "house" in request.POST:
        house_prize = randint(10,15)
        request.session['gold_amount'] += house_prize
        request.session['jugadas'].append([house_prize, "House", time])
        
    if "casino" in request.POST:
        casino_prize = randint(-50,50)
        request.session['gold_amount'] += casino_prize
        request.session['jugadas'].append([casino_prize, "Casino", time])
        
    return redirect('/')