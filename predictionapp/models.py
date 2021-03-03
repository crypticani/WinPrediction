from django.db import models
import datetime


class TeamEvents(models.Model):
    tevent_id = models.AutoField(primary_key=True)
    events = models.CharField(blank=True, max_length=20)

    class Meta:
        verbose_name_plural = "Team Events"

    def __str__(self):
        return self.events


class PermanentTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    c = (('Male', 'Male'), ('Female', 'Female'))
    category = models.CharField(blank=True, max_length=10, choices=c)
    event_name = models.ForeignKey(TeamEvents, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=30)
    captain = models.CharField(max_length=30)
    vice_captain = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Permanent Teams"

    def __str__(self):
        return str('{} {} {}'.format(self.category, self.event_name, self.team_name))
    

class TeamPlayers(models.Model):
    team_id = models.ForeignKey(PermanentTeam, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=6, default=000000)

    class Meta:
        verbose_name_plural = "Team Players"
    
    def __str__(self):
        return self.player_name
    


class TeamRegistrationmodel(models.Model):
    reg_id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=datetime.date.today().year)
    c = (('Male', 'Male'), ('Female', 'Female'))
    category = models.CharField(blank=True, max_length=10, choices=c)
    team_name = models.ForeignKey(PermanentTeam, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Team Registration"

    def __str__(self):
        return str(self.team_name)


class TeamRecordModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    event_name = models.ForeignKey(TeamEvents, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    categories = (('Male', 'Male'), ('Female', 'Female'))
    category = models.CharField(blank=True, max_length=10, choices=categories)
    team1 = models.ForeignKey(TeamRegistrationmodel, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(TeamRegistrationmodel, related_name='team2', on_delete=models.CASCADE)
    score_team1 = models.CharField(blank=True, max_length=30)
    score_team2 = models.CharField(blank=True, max_length=30)
    winner = models.ForeignKey(TeamRegistrationmodel, related_name='team3', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Team Records"

    def __str__(self):
        return str(self.winner)
