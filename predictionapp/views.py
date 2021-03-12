from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages


def Display(request):
    email = request.user.email
    allTeams = PermanentTeam.objects.filter(email=email)
    choice = 0
    players = TeamPlayers.objects.filter(team_id__id=choice)
    context = {
        'allTeams' : allTeams,
        'data' : players,
    }
    if request.method == "POST":
        if 'choiceButton' in request.POST:
            choice = request.POST.get('choice')
            request.session['choice'] = choice
            players = TeamPlayers.objects.filter(team_id__id=choice)
            context = {
                'allTeams' : allTeams,
                'data' : players,
                'mychoice': choice,
            }
            return render(request, 'display.html', context)
        if 'active' in request.POST:
            pl_id = request.POST.get('active')
            choice = request.session['choice']
            obj = get_object_or_404(TeamPlayers ,player_id=pl_id)
            if obj.is_active == True:
                TeamPlayers.objects.filter(player_id=pl_id).update(is_active=False)
                messages.info(request, "Removed!")
            elif obj.is_active == False:
                TeamPlayers.objects.filter(player_id=pl_id).update(is_active=True)
                messages.info(request, "Added!")
            players = TeamPlayers.objects.filter(team_id__id=choice)
            context = {
                'data' : players,
                'allTeams' : allTeams,
                'mychoice': choice,
            }
            return render(request, 'display.html', context)
    return render(request, 'display.html', context)