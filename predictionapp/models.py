from django.db import models
import datetime


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10, default="Male")


    class Meta:
        verbose_name_plural = "Category"


    def __str__(self):
        return self.category


class TeamEvents(models.Model):
    tevent_id = models.AutoField(primary_key=True)
    events = models.CharField(blank=True, max_length=20)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Team Events"

    def __str__(self):
        return str('{} {}'.format(self.events, self.category))


class PermanentTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.ForeignKey(TeamEvents, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=30)
    captain = models.CharField(max_length=30)
    vice_captain = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Permanent Teams"

    def __str__(self):
        return str('{} {}'.format(self.team_name, self.event_name))
    

class TeamPlayers(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(PermanentTeam, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=6, default=000000)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Team Players"
    
    def __str__(self):
        return self.player_name
    


class TeamRegistrationmodel(models.Model):
    reg_id = models.AutoField(primary_key=True)
    year = models.IntegerField(default=datetime.date.today().year)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    team_name = models.ForeignKey(PermanentTeam, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Team Registration"

    def __str__(self):
        return str(self.team_name)


class TeamEventList(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.ForeignKey(TeamEvents, on_delete=models.CASCADE)
    team1 = models.ForeignKey(TeamRegistrationmodel, related_name='team11', on_delete=models.CASCADE, limit_choices_to={'year': datetime.date.today().year})
    team2 = models.ForeignKey(TeamRegistrationmodel, related_name='team12', on_delete=models.CASCADE, limit_choices_to={'year': datetime.date.today().year})
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Team Event List"

    def __str__(self):
        return str('{} vs {}, {}'.format(self.team1, self.team2, self.datetime.date()))


class TeamRecordModel(models.Model):
    record_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(TeamEventList, on_delete=models.CASCADE)
    score_team1 = models.CharField(blank=True, max_length=30)
    score_team2 = models.CharField(blank=True, max_length=30)
    winner = models.ForeignKey(TeamRegistrationmodel, related_name='team3', on_delete=models.CASCADE, limit_choices_to={'year': datetime.date.today().year})

    class Meta:
        verbose_name_plural = "Team Records"

    def __str__(self):
        return str(self.winner)