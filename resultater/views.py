import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from io import StringIO

from django.shortcuts import render
from django.http import HttpResponse

from .models import Stevne, ØVELSER, KLASSER

# Create your views here.

klassefarger = {
    'A'           :'#0070C0',
    'B'           :'#00B050',
    'C'           :'#974807',
    'D'           :'#000000',
    'K1'          :'#808080',
    'K2'          :'#808080',
    'J'           :'#808080',
    'Jm'          :'#808080',
    'Jk'          :'#808080',
    'U'           :'#808080',
    'U16'         :'#808080',
    'U14'         :'#808080',
    'U12'         :'#808080',
    'Åpen rekrutt':'#808080',
    'V50'         :'#808080',
    'V55'         :'#808080',
    'V60'         :'#808080',
    'V65'         :'#808080',
    'V70'         :'#808080',
    'SH1'         :'#808080'
}

def index(request):
    context = {'stevner':Stevne.objects.all()}
    return render(request, 'resultater/index.html', context)

def stevne(request, stevnenr):
    try:
        s = Stevne.objects.get(navn=stevnenr)
    except:
        return HttpResponse("Stevnet {} finnes ikke".format(stevnenr))

    figurer = (s.figurer1,s.figurer2,s.figurer3,s.figurer4,s.figurer5,s.figurer6,s.figurer7,s.figurer8,s.figurer9,s.figurer10)[:s.standplasser]

    maxsum_fgmr = sum(6 + min(f,6) for f in figurer)
    maxsum_spes = sum(5 + min(f,5) for f in figurer)

    context = {
        'navn':s.navn,
        'stevnetype':s.stype,
        'arrangør':s.arrangør,
        'dato':str(s.dato),
        'sted':s.sted,
        'stevneleder':s.stevneleder,
        'premiering':s.premiering,
        'figurer':figurer,
        'maxsum_fgmr':maxsum_fgmr,
        'maxsum_spes':maxsum_spes
    }


    resultatmap={}
    for start in s.starter.all():
        ss = {}

        ss['navn']       = start.navn
        ss['klubb']      = start.klubb
        ss['poeng']      =     (start.poeng1,start.poeng2,start.poeng3,start.poeng4,start.poeng5,start.poeng6,start.poeng7,start.poeng8,start.poeng9,start.poeng10)[:s.standplasser]
        ss['soner']      = sum((start.soner1,start.soner2,start.soner3,start.soner4,start.soner5,start.soner6,start.soner7,start.soner8,start.soner9,start.soner10)[:s.standplasser])
        ss['poengsum']   = sum(ss['poeng'])
        ss['rekkefølge'] = ss['poengsum'] * 60 + ss['soner']

        if start.øvelse not in resultatmap:
            resultatmap[start.øvelse] = {
                'rekkefølge' : [ø[1] for ø in ØVELSER].index(start.øvelse),
                'klasser'    : {}
            }

        if start.klasse not in resultatmap[start.øvelse]['klasser']:
            resultatmap[start.øvelse]['klasser'][start.klasse] = {
                'rekkefølge' : [k[1] for k in KLASSER].index(start.klasse),
                'skyttere'   : []
            }

        resultatmap[start.øvelse]['klasser'][start.klasse]['skyttere'].append(ss)

    # konverter dicts til lister av dicts for å kunne bruke dictsort
    # generer plot for hver øvelse
    resultatliste = []
    for øvelse,øvelsedata in resultatmap.items():
        øvelsedata['øvelse'] = øvelse
        øvelsedata['klasser'] = [dict(kd,klasse=kn) for kn,kd in øvelsedata['klasser'].items()]

        øvelsedata['klasser'].sort(key=lambda x: x['rekkefølge'])

        poengliste  = [[s['poengsum'] for s in k['skyttere']]for k in øvelsedata['klasser']]
        klasseliste = [k['klasse'] for k in øvelsedata['klasser']]
        fargeliste  = [klassefarger[k] for k in klasseliste]
        plt.clf()
        plt.figure(figsize=(6,4))
        plt.hist(poengliste, bins=maxsum_fgmr+1, range=(0,maxsum_fgmr), color=fargeliste, stacked=True)
        plt.legend(klasseliste, framealpha=0.5, loc='upper left')
        svg = StringIO()
        plt.savefig(svg, format='svg')
        øvelsedata['plot'] = svg.getvalue()

        resultatliste.append(øvelsedata)
    context['resultater'] = resultatliste


    return render(request, 'resultater/stevne.html', context)
