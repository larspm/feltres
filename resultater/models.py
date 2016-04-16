from django.db import models
from django.core.urlresolvers import reverse

ØVELSER = (
    ('F',  'Finfelt'),
    ('G',  'Grovfelt'),
    ('M',  'Militærfelt'),
    ('R',  'Revolverfelt'),
    ('SP', 'Spesialpistol'),
    ('SR', 'Spesialrevolver'),
    ('M1', 'Magnum 1'),
    ('M2', 'Magnum 2')
)

KLASSER = (
    ('A',   'A'),
    ('B',   'B'),
    ('C',   'C'),
    ('D',   'D'),
    ('K1',  'K1'),
    ('K2',  'K2'),
    ('J',   'J'),
    ('Jm',  'Jm'),
    ('Jk',  'Jk'),
    ('U',   'U'),
    ('U16', 'U16'),
    ('U14', 'U14'),
    ('U12', 'U12'),
    ('ÅR',  'Åpen rekrutt'),
    ('V50', 'V50'),
    ('V55', 'V55'),
    ('V60', 'V60'),
    ('V65', 'V65'),
    ('V70', 'V70'),
    ('SH1', 'SH1')
)

class Start(models.Model):
    navn = models.CharField(max_length=60)
    klubb = models.CharField(max_length=60)
    øvelse = models.CharField(max_length=15, choices=ØVELSER)
    klasse = models.CharField(max_length=11, choices=KLASSER)

    poeng1 = models.PositiveIntegerField(default=0)
    soner1 = models.PositiveIntegerField(default=0)
    poeng2 = models.PositiveIntegerField(default=0)
    soner2 = models.PositiveIntegerField(default=0)
    poeng3 = models.PositiveIntegerField(default=0)
    soner3 = models.PositiveIntegerField(default=0)
    poeng4 = models.PositiveIntegerField(default=0)
    soner4 = models.PositiveIntegerField(default=0)
    poeng5 = models.PositiveIntegerField(default=0)
    soner5 = models.PositiveIntegerField(default=0)
    poeng6 = models.PositiveIntegerField(default=0)
    soner6 = models.PositiveIntegerField(default=0)
    poeng7 = models.PositiveIntegerField(default=0)
    soner7 = models.PositiveIntegerField(default=0)
    poeng8 = models.PositiveIntegerField(default=0)
    soner8 = models.PositiveIntegerField(default=0)
    poeng9 = models.PositiveIntegerField(default=0)
    soner9 = models.PositiveIntegerField(default=0)
    poeng10 = models.PositiveIntegerField(default=0)
    soner10 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.navn+self.klubb+self.øvelse+self.klasse

class Stevne(models.Model):

    # Generell info
    navn        = models.CharField(unique=True, max_length=30)
    arrangør    = models.CharField(max_length=30)
    dato        = models.DateField()
    sted        = models.CharField(max_length=30)
    stevneleder = models.CharField(max_length=30)
    premiering  = models.CharField(max_length=30)
    krets       = models.CharField(max_length=30)
    distrikt    = models.CharField(max_length=30)
    stype       = models.CharField(max_length=30)

    # Løype
    standplasser = models.PositiveIntegerField()
    figurer1  = models.PositiveIntegerField()
    figurer2  = models.PositiveIntegerField()
    figurer3  = models.PositiveIntegerField()
    figurer4  = models.PositiveIntegerField()
    figurer5  = models.PositiveIntegerField()
    figurer6  = models.PositiveIntegerField()
    figurer7  = models.PositiveIntegerField()
    figurer8  = models.PositiveIntegerField()
    figurer9  = models.PositiveIntegerField()
    figurer10 = models.PositiveIntegerField()

    # Starter
    starter = models.ManyToManyField(Start)

    def get_html_url(self):
        return reverse('stevne-html', kwargs={'stevnenr':self.navn})

    def get_xlsx_url(self):
        return reverse('stevne-xlsx', kwargs={'stevnenr':self.navn})
