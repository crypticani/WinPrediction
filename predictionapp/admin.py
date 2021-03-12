from django.contrib import admin
from .models import *


admin.site.site_header = "UTSAV Admin Panel"
admin.site.site_title = "UTSAV Admin Panel"

class TeamRegistrationA(admin.ModelAdmin):
    list_display = ['reg_id', 'year', 'category', 'get_event_name', 'get_team_name', 'get_captain_name']

    def get_team_name(self, obj):
        return obj.team_name.team_name
    get_team_name.admin_order_field  = 'reg_id'  #Allows column order sorting
    #get_team_name.short_description = 'Team Name'  #Renames column head

    def get_event_name(self, obj):
        return obj.team_name.event_name
    get_event_name.admin_order_field  = 'reg_id'  #Allows column order sorting
    #get_event_name.short_description = 'Event Name'  #Renames column head

    def get_captain_name(self, obj):
        return obj.team_name.captain
    get_event_name.admin_order_field  = 'reg_id'  #Allows column order sorting
    #get_event_name.short_description = 'Captain'  #Renames column head
 
    list_filter = ['year', 'category', 'team_name__event_name']
    search_fields = ['team_name__team_name', 'team_name__captain']


class PermanentTeamA(admin.ModelAdmin):
    list_display = ['id', 'category', 'event_name', 'team_name', 'captain']
    list_filter = ['category', 'event_name']
    search_fields = ['team_name', 'captain', 'vice_captain']


class TeamPlayersA(admin.ModelAdmin):
    list_display = ['get_team_name', 'get_category', 'get_event_name', 'player_name', 'id_number', 'is_active']

    def get_team_name(self, obj):
        return obj.team_id.team_name
    get_team_name.admin_order_field  = 'team_id'  #Allows column order sorting
    #get_team_name.short_description = 'Team Name'  #Renames column head

    def get_event_name(self, obj):
        return obj.team_id.event_name
    get_event_name.admin_order_field  = 'team_id'  #Allows column order sorting
    #get_event_name.short_description = 'Event Name'  #Renames column head

    def get_category(self, obj):
        return obj.team_id.category
    get_event_name.admin_order_field  = 'team_id'  #Allows column order sorting
    #get_event_name.short_description = 'Category'  #Renames column head

    list_filter = ['team_id__category', 'team_id__event_name', 'team_id__team_name', 'is_active']
    search_fields = ['player_name', 'id_number']


class TeamRecordA(admin.ModelAdmin):
    list_display = ['event_id', 'event_name', 'date', 'category', 'get_team1', 'get_team2', 'get_winner']

    def get_team1(self, obj):
        return obj.team1
    get_team1.admin_order_field  = 'record_id'  #Allows column order sorting
    #get_team1.short_description = 'Team 1'  #Renames column head

    def get_team2(self, obj):
        return obj.team2
    get_team2.admin_order_field  = 'record_id'  #Allows column order sorting
    #get_team2.short_description = 'Team 2'  #Renames column head

    def get_winner(self, obj):
        return obj.winner
    get_winner.admin_order_field  = 'record_id'  #Allows column order sorting
    #get_winner.short_description = 'Winner'  #Renames column head


class TeamEventsA(admin.ModelAdmin):
    list_display = ['tevent_id', 'events']

admin.site.register(TeamEvents, TeamEventsA)
admin.site.register(PermanentTeam, PermanentTeamA)
admin.site.register(TeamPlayers, TeamPlayersA)
admin.site.register(TeamRegistrationmodel, TeamRegistrationA)
admin.site.register(TeamRecordModel, TeamRecordA)
admin.site.register(Categories)