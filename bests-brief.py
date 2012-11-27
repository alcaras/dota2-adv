
from copy import deepcopy
from heroes import heroes
from alpha import alpha



from aliases import aliases

from ranged_heroes import ranged_heroes

from roles import *
from positions import *
from laning import *
from pickbans import *

from winrate_76c_slark import winrate
from matchup_76c_slark import matchup

import argparse
import pprint
import string
import sys
import math

pp = pprint.PrettyPrinter(indent = 4)

parser = argparse.ArgumentParser(description='lane advisor for dota2')
parser.add_argument('-p', '--position', type=int,  help='filter by position', default='-1')
parser.add_argument('-l', '--lane', type=str, help='filter lane', default='')
parser.add_argument('-o', '--heroes', metavar=heroes, nargs='+', type=str, help='filter hero(es)', default='')
args = parser.parse_args()



def nc_mod(h, eh):
    them = parse_heroes(eh)
    s =  0
    for e in them:
        if h in matchup:
            if e in matchup[h]:
                s += matchup[h][e] - winrate[h]
        
    if s < 0:
        s -= 0
    return s

def pb_mod(h):
    if h in pickbans:
        return pickbans[h]
    return 0


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


def show_heroes(parsed_heroes, scores={}, enemy=False):
    for u in parsed_heroes:
        if enemy:
            print str("enemy").rjust(9),
            print str(u).ljust(20), 
        else:
            print str(u).ljust(20), 
        print



def print_heroes(ah, scores={}, enemy=False):
    hh = parse_heroes(ah)
    show_heroes(hh, scores, enemy)

   


def get_values(ah):
    us = parse_heroes(ah)

    usa = {}
    for k in known_roles:
        usa[k] = 0

    for u in us:
        for r in roles[u]:
            if r in usa:
                usa[r] += 1
            else:
                usa[r] = 1

    return usa



def analyze_team_positions(hh):
    team = parse_heroes(hh)
    pos = []
    for h in team:
        hp = priority_positions(h)
        for p in hp:
            if p[1] > 0:
                pos += [[p[1], h, p[0]]]

    pos_sorted = sorted(pos, key=lambda (e): e[0], reverse=True)

    slots = {1: "",
             2: "",
             3: "",
             4: "",
             5: ""}

    used_heroes = []

    for i in range(len(team)):
        for e in pos_sorted:
            if e[1] not in used_heroes:
                if slots[e[2]] == "":
                    slots[e[2]] = e[1]
                    used_heroes += [e[1]]
                    
    return slots
        
        
mid = heroes_for_lane(["Solo Mid"])

hmr = []

def get_lane_matchup_vs(enemy, lane):
    in_the_lane = heroes_for_lane([lane])
    hmr = []
    for h in mid:
        if h[1] in matchup:
            if enemy in matchup[h[1]]:
                hmr += [[h[1], (matchup[h[1]][enemy]-winrate[h[1]])*h[0]]]
    sorted_hmr = sorted(hmr, key = lambda(e): e[1], reverse=True)
    return sorted_hmr


def pretty_lanes(tl):
    print str("").rjust(10) + str(score_lane_config(tl)).ljust(10)
    for k, v in tl.iteritems():
        if len(v) > 0:
            print str(lanes_laning[k]).rjust(20), v
    print

def pretty_roles(tl):
    print str(score_role_config(tl)).ljust(10)
    for k, v in tl.iteritems():
        if len(v) > 0:
            print k+1, v, " "
    print

# build roles based on a team
def build_roles(team, verbose=False):
    if len(team)>5:
        return 0
    hh = parse_heroes(team)

    tl = {}
    for i in range(0, 5):
        tl[i] = []
    
    valid_laning_configs = recu_roles(0, hh, tl, roles_list=[], verbose=verbose)

    return valid_laning_configs

# build lanes based on a team
def build_lanes(team, verbose=False):
    if len(team)>5:
        return 0
    hh = parse_heroes(team)

    tl = {}
    for i in range(0, 12):
        tl[i] = []
    
    valid_laning_configs = recu_lanes(0, hh, tl, laning_list=[], verbose=verbose)

    return valid_laning_configs

# no dual mid, tri hard, tri safe, or roaming
disabled_lane_types = []

# no dual mid, tri hard, tri safe, or roaming
disabled_lane_types = [1, 4, 9, 10]


# given a config, give it a score
def score_lane_config(tl):
    score = 0
    for k, v in tl.iteritems():
        for h in v:
            if h in laning:
                score += laning[h][k]
            
    return score

def score_role_config(tl):
    score = 0
    for k, v in tl.iteritems():
        for h in v:
            if h in laning:
                score += positions[h][k]
            
    return score


def have_no_laning_data(laning_hero):
    zeroes = 0
    for i in range(0, 12):
        if laning_hero[i] == 0:
            zeroes += 1
    if zeroes == 12:
        return True
    return False

def have_no_role_data(laning_hero):
    zeroes = 0
    for i in range(0, 5):
        if laning_hero[i] == 0:
            zeroes += 1
    if zeroes == 5:
        return True
    return False
            
def recu_roles(i, team, tl, roles_list, verbose=False):
    if i >= len(team):
        return [[score_role_config(tl), tl]]
    append_to_roles_list = []
    if team[i] in laning:
        for j, k in enumerate(positions[team[i]]):
            if k > 0 or have_no_role_data(positions[team[i]]):
                if tl[j] == []:
                    new_tl = deepcopy(tl)
                    new_tl[j] += [team[i]]
                    latest = recu_roles(i+1, team, new_tl, roles_list, verbose)
                    if latest:
                        append_to_roles_list = append_to_roles_list + latest

    return append_to_roles_list


def recu_lanes(i, team, tl, laning_list, verbose=False):
    if i >= len(team):
        if valid_lanes(tl, team):
            return [[score_lane_config(tl), tl]]
        return None
    append_to_laning_list = []
    if team[i] in laning:
        for j, k in enumerate(laning[team[i]]):
            if j in disabled_lane_types:
                continue
            if k > 0: # or have_no_laning_data(laning[team[i]]):
                new_tl = deepcopy(tl)
                new_tl[j] += [team[i]]
                latest = recu_lanes(i+1, team, new_tl, laning_list, verbose)
                if latest:
                    append_to_laning_list = append_to_laning_list + latest

    return append_to_laning_list

def valid_lanes(tl, team):
    # can't have more than one in a solo lane
    if len(tl[0])> 1 or len(tl[2])>1 or len(tl[5])>1 or len(tl[6])>1 or len(tl[11])>1:
        return False
    # can't have more than two in a dual lane
    if len(tl[1]) >2 or len(tl[3]) >2 or len(tl[7]) >2 or len(tl[8]) >2:
        return False

    # mutex checks for each lane between solo duo tri
    if bool(len(tl[0])) and bool(len(tl[1])):
        return False
    if bool(len(tl[2])) and bool(len(tl[3])):
        return False
    if bool(len(tl[2])) and bool(len(tl[4])):
        return False
    if bool(len(tl[3])) and bool(len(tl[4])):
        return False
    if bool(len(tl[5])) and bool(len(tl[6])):
        return False
    if bool(len(tl[5])) and bool(len(tl[7])):
        return False
    if bool(len(tl[5])) and bool(len(tl[8])):
        return False
    if bool(len(tl[5])) and bool(len(tl[9])):
        return False
    if bool(len(tl[6])) and bool(len(tl[7])):
        return False
    if bool(len(tl[6])) and bool(len(tl[8])):
        return False
    if bool(len(tl[6])) and bool(len(tl[9])):
        return False
    if bool(len(tl[7])) and bool(len(tl[8])):
        return False
    if bool(len(tl[7])) and bool(len(tl[9])):
        return False
    if bool(len(tl[8])) and bool(len(tl[9])):
        return False

    if len(team)<4:
        return True

    # can't have just two in a tri lane
    if len(tl[4])==2 or len(tl[9])==2:
        return False

    if len(team)<5:
        return True

    # + J/R lanes
    if len(tl[6])==1 and (len(tl[10])==0 and len(tl[11])==0):
        return False
    if len(tl[8])==2 and (len(tl[10])==0 and len(tl[11])==0):
        return False

     # can't have just one in a dual lane
    if len(tl[1])==1 or len(tl[3])==1 or len(tl[7])==1 or len(tl[8])==1:
        return False

    # can't have just one in a tri lane
    if len(tl[4])==1 or len(tl[9])==1:
        return False
    if len(tl[4])>3 or len(tl[9])>3:
        return False


    # make sure each of the three main lanes is filled
    # Mid
    if not(bool(len(tl[0])) or bool(len(tl[1]))):
        return False

    # Hard
    if not(bool(len(tl[2])) or bool(len(tl[3])) or bool(len(tl[4]))):
        return False

    # safe
    if not(bool(len(tl[5])) or bool(len(tl[6])) or bool(len(tl[7])) or
           bool(len(tl[8])) or bool(len(tl[9]))):
        return False


                                                     


    return True




# for each lane
# show the bests, by role, 1-5


# lanes
# mid = solo mid
# ssafe = solo safe
# dsafe = dual safe
# shard = solo hard
# dhard = dual hard
# jungle = jungle
# ssafej = solo safe w/ jungler
# dsafej = dual safe w/ jungler

lane_args = {
    'mid' : 0,
    'shard' : 2,
    'dhard' : 3,
    'ssafe' : 5,
    'ssafej' : 6,
    'dsafe' : 7,
    'dsafej' : 8,
    'jungle' : 11,
}




filter_by_this_lane = -1
if args.lane != '':
    if args.lane in lane_args:
        filter_by_this_lane = lane_args[args.lane]
    else:
        print >> sys.stderr, "Unknown lane arg: ", args.lane
        print >> sys.stderr, "Use: mid, shard, dhard, ssafe, ssafej, dsafe, dsafej, or jungle"
        exit()

filter_by_this_position = -1
if args.position == -1:
    filter_by_this_position = - 1
elif args.position < 1 or args.position > 5:
    print >> sys.stderr, "Unknown position arg: ", args.position
    print >> sys.stderr, "Use: 1, 2, 3, 4, or 5"
    exit()
else:
    filter_by_this_position = args.position - 1

filter_by_heroes = ""
if args.heroes != "":
    hset = parse_heroes(args.heroes)
    filter_by_heroes = hset


hero_stack = []
hero_scores = {}

for hh in alpha:
    if filter_by_heroes != "":
        if hh not in filter_by_heroes:
            continue
    if hh not in laning:
        continue
    if hh not in positions:
        continue
    if filter_by_this_lane > -1:
        if laning[hh][filter_by_this_lane] == 0:
            continue
    if filter_by_this_position >- 1:
        if positions[hh][filter_by_this_position] == 0:
            continue
    hero_stack += [hh]
    if filter_by_this_lane != -1 and filter_by_this_position == -1:
        hero_scores[hh] = laning[hh][filter_by_this_lane] 
    if filter_by_this_lane == -1 and filter_by_this_position != -1:
        hero_scores[hh] = positions[hh][filter_by_this_position]
    if filter_by_this_lane == -1 and filter_by_this_position == -1:
        hero_scores[hh] = pickbans[hh] 
    if filter_by_this_lane != -1 and filter_by_this_position != -1:
        hero_scores[hh] = positions[hh][filter_by_this_position] * laning[hh][filter_by_this_lane] 
    

sorted_hero_stack = sorted(hero_stack, key=lambda h: hero_scores[h], reverse=True)

if filter_by_this_lane > -1:
    print "Filtering by lane:     ", lanes_laning[filter_by_this_lane]

if filter_by_this_position >- 1:
    print "Filtering by position: ", filter_by_this_position+1

print

show_heroes(sorted_hero_stack, hero_scores)
        

