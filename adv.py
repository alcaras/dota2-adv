from heroes import heroes
from alpha import alpha

from roles import roles
from roles import known_roles

from aliases import aliases

from ranged_heroes import ranged_heroes

import argparse
import pprint
import string
import math

pp = pprint.PrettyPrinter(indent = 4)

parser = argparse.ArgumentParser(description='lane advisor for dota2')
parser.add_argument('heroes', metavar='heroes', type=str, nargs='+', help='your team')
parser.add_argument('-e', '--enemy', metavar='enemy', type=str, nargs='+', help='the other team', default='')
parser.add_argument('-c', '--consider', type=str, help='which list of heroes to consider (default = all heroes)', default='alpha')
args = parser.parse_args()
pp.pprint(args)


def parse_heroes(ah):
    us = []
    for i in range(0,5):
        if i < len(ah):
            h  = ah[i]
            hero = ""
            if h == "*" or h =="?":
                continue
            for z in heroes.itervalues():
                if h == z.lower():
                    hero = z
                elif h == z:
                    hero = z
            if h in aliases:
                hero = aliases[h]
            if hero == "":
                print "Unknown hero", h
                continue
            us += [hero]
    return us


def get_values(ah, verbose = False, enemy=False):
    us = parse_heroes(ah)

    usa = {}
    for k in known_roles:
        usa[k] = 0

    for u in us:
        if verbose:
            if enemy:
                print str("enemy").rjust(7),
            else:
                print str("").rjust(7),
            print str(u).ljust(20), 

            print roles[u]

        for r in roles[u]:
            if r in usa:
                usa[r] += 1
            else:
                usa[r] = 1

    return usa


consider_these_heroes = alpha

if args.consider == "alpha":
    consider_these_heroes = alpha
else:
    print "unknown args.consider", args.consider
    exit()

ra = get_values(args.heroes, verbose=False)
print args.consider, len(consider_these_heroes)

pp.pprint(ra) 

if args.enemy != "":
    print
    get_values(args.enemy, verbose=True, enemy=True)
    print 
else:
    print

get_values(args.heroes, verbose=True)
print


scores = {}

for hh in consider_these_heroes:
    if hh in parse_heroes(args.heroes):
        continue
    if hh in parse_heroes(args.enemy):
        continue

    foo = get_values(args.heroes + [hh])
    scores[hh] = 0.0

sorted_scores = sorted(scores.iteritems(), key=lambda (k,v): (v,k), reverse=True)

displayed = 10
for s in sorted_scores:
    if displayed == 0 or (s[1]<-500 and displayed < 4):
        break
    displayed -= 1
    print str(round(s[1],1)).rjust(7),
    print str(s[0]).ljust(20), 
    print roles[s[0]]

    
                       

    


