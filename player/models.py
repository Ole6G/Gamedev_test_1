from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_login = models.DateTimeField(auto_now_add=True)
    daily_entries = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def add_boost(self, boost_type):
        boost = Boost(player=self, boost_type=boost_type)
        boost.save()
        return boost

    def __str__(self):
        return f"{self.username} - Points: {self.points}, Daily Entries: {self.daily_entries}"


class Boost(models.Model):
    BOOST_TYPES = (
        ('speed', 'Speed Boost'),
        ('strength', 'Strength Boost'),
        ('spell amplification', 'Spell Amplification Boost'),
        ('spell resistence', 'Spell Resistence Boost'),
        ('precision', 'Precision Boost'),
        ('positive effect duration', 'Positive Effect Duration Boost'),
        ('attack speed', 'Attack Speed Boost'),
        ('cast time', 'Cast Time Boost'),
    )

    player = models.ForeignKey(Player, related_name='boosts', on_delete=models.CASCADE)
    boost_type = models.CharField(max_length=30, choices=BOOST_TYPES)
    acquired_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.boost_type} for {self.player.username} acquired at {self.acquired_at}"
