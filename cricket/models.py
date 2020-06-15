from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import signals
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
import uuid


class CricketTimeStamp(models.Model):
	"""
	Single TimeStamp Class for whole project
	"""
	date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
	date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)

	class Meta:
		abstract = True

class Team(CricketTimeStamp):
	"""Table to store Team information
	"""
	id = models.UUIDField(primary_key=True,default = uuid.uuid4)
	team_name = models.CharField(null=False,blank=False,max_length=100)
	logo = models.ImageField(_('Team Logo'),upload_to='cricket_images/', blank=False,
							null=False, max_length=4096)
	club_state = models.CharField(null=False,blank=False,max_length=100)

	def get_absolute_url(self):
		return reverse('cricket:team-details', kwargs={'pk': self.pk})

	def __str__(self):
		return self.team_name	
	class Meta:
		app_label = 'cricket'
		ordering = ['team_name']
		verbose_name = _('Team')

class Player(CricketTimeStamp):
	""""
	Table to store Player Information
	"""
	id = models.UUIDField(primary_key=True,default = uuid.uuid4)
	first_name = models.CharField(null=False,blank=False,max_length=100)
	last_name = models.CharField(null=True,blank=True,max_length=100)
	picture = models.ImageField(_('Player Image'),blank=True,upload_to='cricket_images/',
							  null=True, max_length=4096)
	jersey_number = models.PositiveIntegerField(unique=True,blank=False,null=False)
	origin_country = models.CharField(null=False,blank=False,max_length=100)
	team = models.ForeignKey(Team, db_index=True, blank=True, null=True, related_name="players_team",
								verbose_name=_('Team'),on_delete=models.PROTECT)

	def __str__(self):
		return self.first_name

	@property
	def full_name(self):
		"Returns the players's full name."
		return '%s %s' % (self.first_name, self.last_name)

	class Meta:
		app_label = 'cricket'
		ordering = ['first_name']
		verbose_name = _('Player')

class PlayerMatchData(CricketTimeStamp):
	"""
	Table to store Player Run data in Match
	"""
	player = models.ForeignKey(Player, db_index=True, blank=False, null=False, related_name="player",
								verbose_name=_('TeamPlayers'),on_delete=models.PROTECT)
	no_of_matches = models.PositiveIntegerField(blank=True,null=True)
	highest_score = models.PositiveIntegerField(_("Highest Score"),blank=True,null=True)
	total_runs = models.PositiveIntegerField(_("Total Runs"),blank=True,null=True)
	total_wickets = models.PositiveIntegerField(_("Total Wickets"),blank=True,null=True)
	total_centuries = models.PositiveIntegerField(_("Total Centuries"),blank=True,null=True)
	total_fifties = models.PositiveIntegerField(_("Total Fifties"),blank=True,null=True)

	class Meta:
		app_label = 'cricket'
		ordering = ['no_of_matches']
		verbose_name = _('PlayerMatchData')

class MatchData(CricketTimeStamp):
	"""
	Table to store Match data of teams
	"""
	home_team = models.ForeignKey(Team, db_index=True, blank=False, null=False, related_name="home_team",on_delete=models.PROTECT)
	away_team = models.ForeignKey(Team, db_index=True, blank=False, null=False, related_name="away_team",on_delete=models.PROTECT)
	winner_team = models.ForeignKey(Team, db_index=True, blank=True, null=True, related_name="winners",on_delete=models.PROTECT)

	def save(self, *args, **kwargs):
		if self.winner_team is not None and (self.winner_team == self.home_team or self.winner_team == self.away_team):
			super().save(*args, **kwargs)
		elif self.winner_team is None:
			super().save(*args, **kwargs)
		else:
			raise ValidationError(u'Please enter a valid team')

	class Meta:
		app_label = 'cricket'
		verbose_name = _('MatchData')

class MatchPoints(CricketTimeStamp):
	"""
	Table to store Match Points of Teams
	"""
	team = models.OneToOneField(Team, max_length=50, related_name='point_team',on_delete=models.PROTECT)
	points = models.PositiveIntegerField(default=0)

	class Meta:
		app_label = 'cricket'
		ordering = ['-points']
		verbose_name = _('MatchPoints')
