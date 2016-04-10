#!/usr/bin/env python3

import os
import datetime
import xml.etree.ElementTree as ET

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

from resultater.models import Stevne, Start

stevner = ET.parse('stevner.xml').getroot()

for stevne in stevner:
    s = Stevne()

    navn        = stevne.attrib['navn']
    arrangør    = stevne.attrib['arrangør']
    år          = stevne.attrib['år']
    måned       = stevne.attrib['måned']
    dag         = stevne.attrib['dag']
    sted        = stevne.attrib['sted']
    stevneleder = stevne.attrib['stevneleder']
    premiering  = stevne.attrib['premiering']
    krets       = stevne.attrib['krets']
    distrikt    = stevne.attrib['distrikt']
    stype       = stevne.attrib['type']

    løype = stevne.find('løype')

    standplasser = int(løype.attrib['standplasser'])

    s.navn        = navn
    s.arrangør    = arrangør
    s.dato        = datetime.date(int(år), int(måned), int(dag))
    s.sted        = sted
    s.stevneleder = stevneleder
    s.premiering  = premiering
    s.krets       = krets
    s.distrikt    = distrikt
    s.stype       = stype

    s.standplasser = standplasser

    foo = [0]*10
    for i in range(standplasser):
        foo[i] = int(løype.find('standplass_{}'.format(i+1)).attrib['figurer'])

    s.figurer1  = foo[0]
    s.figurer2  = foo[1]
    s.figurer3  = foo[2]
    s.figurer4  = foo[3]
    s.figurer5  = foo[4]
    s.figurer6  = foo[5]
    s.figurer7  = foo[6]
    s.figurer8  = foo[7]
    s.figurer9  = foo[8]
    s.figurer10 = foo[9]

    s.save()

    for start in stevne.find('starter').findall('start'):
        strt = Start()

        strt.navn   = start.attrib['navn']
        strt.klubb  = start.attrib['klubb']
        strt.øvelse = start.attrib['øvelse']
        strt.klasse = start.attrib['klasse']

        foo = [(0,0)]*10
        for i in range(standplasser):
            poeng = int(start.find('standplass_{}'.format(i+1)).attrib['poeng'])
            soner = int(start.find('standplass_{}'.format(i+1)).attrib['soner'])
            foo[i] = (poeng,soner)

        strt.poeng1,  strt.soner1  = foo[0]
        strt.poeng2,  strt.soner2  = foo[1]
        strt.poeng3,  strt.soner3  = foo[2]
        strt.poeng4,  strt.soner4  = foo[3]
        strt.poeng5,  strt.soner5  = foo[4]
        strt.poeng6,  strt.soner6  = foo[5]
        strt.poeng7,  strt.soner7  = foo[6]
        strt.poeng8,  strt.soner8  = foo[7]
        strt.poeng9,  strt.soner9  = foo[8]
        strt.poeng10, strt.soner10 = foo[9]

        strt.save()
        s.starter.add(strt)

    #s.save()
