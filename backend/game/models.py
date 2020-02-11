import base64
from django.db import models
from django.utils import timezone


class Game(models.Model):
    GAME_STATUS = (
        ('1', 'Game-Over'),
        ('0', 'Game-Cancelled'),
        ('2', 'In-Progress'),
    )
    room_name = models.CharField(max_length=30)
    game_status = models.CharField(max_length=1, choices=GAME_STATUS)
    first_winner = models.IntegerField()
    second_winner = models.IntegerField()
    third_winner = models.IntegerField()
    fourth_winner = models.IntegerField()
    fifth_winner = models.IntegerField()
    sixth_winner = models.IntegerField()
    date_created = models.DateTimeField()


class User(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    monster_name = models.CharField(max_length=30)
    # the user can be an email or guest thus username, guest must be unique
    username = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    online = models.BooleanField(null=False, blank=False, default=False)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Dice(models.Model):
    DICE_VALUE = (
        ('1', 'ONE'),
        ('2', 'TWO'),
        ('3', 'THREE'),
        ('4', 'ATTACK'),
        ('5', 'HEAL'),
        ('6', 'ENERGY'),
    )
    DICE_SELECTED = (
        ('1', 'SELECT'),
        ('0', 'DISCARD'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_number = models.IntegerField()
    dice1 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice1_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice2 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice2_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice3 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice3_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice4 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice4_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice5 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice5_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice6 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice6_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice7 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice7_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice8 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice8_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    date_created = models.DateTimeField()


class Play(models.Model):
    MONSTER_POSITION = (
        ('1', 'TOKYO'),
        ('0', 'OUTSIDE'),
    )
    CARD_TYPE = (
        ('1', 'KEEP'),
        ('0', 'DISCARD'),
    )
    CARD = (
        ('00', 'No Card'),
        ('01', 'Acid Attack'),
        ('02', 'Alien Metabolism'),
        ('03', 'Alpha Monster'),
        ('04', 'Apartment Building'),
        ('05', 'Armor Plating'),
        ('06', 'Background Dweller'),
        ('07', 'Burrowing'),
        ('08', 'Camouflage'),
        ('09', 'Commuter Train'),
        ('10', 'Complete Destruction'),
        ('11', 'Corner Store'),
        ('12', 'Dedicated News Team'),
        ('13', 'Drop from High Altitude'),
        ('14', 'Eater of the Dead'),
        ('15', 'Energize'),
        ('16', 'Energy Hoarder'),
        ('17', 'Evacuation Orders (x2)'),
        ('18', 'Even Bigger'),
        ('19', 'Extra Head(x2)'),
        ('20', 'Fire Blast'),
        ('21', 'Fire Breathing'),
        ('22', 'Freeze Time'),
        ('23', 'Frenzy'),
        ('24', 'Friend of Children'),
        ('25', 'Gas Refinery'),
        ('26', 'Giant Brain'),
        ('27', 'Gourmet'),
        ('28', 'Heal'),
        ('29', 'Healing Ray'),
        ('30', 'Herbivore'),
        ('31', 'Herd Culler'),
        ('32', 'High Altitude Bombing'),
        ('33', 'It Has a Child'),
        ('34', 'Jet Fighters'),
        ('35', 'Jets'),
        ('36', 'Made in a Lab'),
        ('37', 'Metamorph'),
        ('38', 'Mimic'),
        ('39', 'Monster Batteries'),
        ('40', 'National Guard'),
        ('41', 'Nova Breath'),
        ('42', 'Nuclear Power Plant'),
        ('43', 'Omnivore'),
        ('44', 'Opportunist'),
        ('45', 'Parasitic Tentacles'),
        ('46', 'Plot Twist'),
        ('47', 'Poison Quills'),
        ('48', 'Poison Spit'),
        ('49', 'Psychic Probe'),
        ('50', 'Rapid Healing'),
        ('51', 'Regeneration'),
        ('52', 'Rooting for the Underdog'),
        ('53', 'Shrink Ray'),
        ('54', 'Skyscraper'),
        ('55', 'Smoke Cloud'),
        ('56', 'Solar Powered'),
        ('57', 'Spiked Tail'),
        ('58', 'Stretchy'),
        ('59', 'Tanks'),
        ('60', 'Telepath'),
        ('61', 'Urbavore'),
        ('62', 'Vast Storm'),
        ('63', 'We are Only Making It Stronger'),
        ('64', 'Wings'),
        ('65', 'Amusement Park'),
        ('66', 'Army'),
        ('67', 'Cannibalistic'),
        ('68', 'Intimidating Roar'),
        ('69', 'Monster Sidekick'),
        ('70', 'Reflective Hide'),
        ('71', 'Sleep Walker'),
        ('72', 'Super Jump'),
        ('73', 'Throw a Tanker'),
        ('74', 'Thunder Stomp'),
        ('75', 'Unstable DNA'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card1_swept = models.CharField(max_length=2, choices=CARD)
    card1_swept_type = models.CharField(max_length=1, choices=CARD_TYPE)
    card2_swept = models.CharField(max_length=2, choices=CARD)
    card2_swept_type = models.CharField(max_length=1, choices=CARD_TYPE)
    card3_swept = models.CharField(max_length=2, choices=CARD)
    card3_swept_type = models.CharField(max_length=1, choices=CARD_TYPE)
    card_purchased = models.CharField(max_length=2, choices=CARD)
    card_purchased_type = models.CharField(max_length=1, choices=CARD_TYPE)
    card_used = models.CharField(max_length=2, choices=CARD)
    card_used_type = models.CharField(max_length=1, choices=CARD_TYPE)
    location = models.CharField(max_length=1, choices=MONSTER_POSITION)
    victory_points = models.IntegerField()
    energy_cube = models.IntegerField()
    life_points = models.IntegerField()
    date_created = models.DateTimeField()
