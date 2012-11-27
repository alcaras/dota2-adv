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
import math

pp = pprint.PrettyPrinter(indent = 4)

parser = argparse.ArgumentParser(description='balanced lane advisor for dota2')
parser.add_argument('heroes', metavar='heroes', type=str, nargs='+', help='your team')
parser.add_argument('-e', '--enemy', metavar='enemy', type=str, nargs='+', help='the other team', default='')
parser.add_argument('-c', '--consider', type=str, help='which list of heroes to consider (default = all heroes)', default='alpha')
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
            if u in scores:
                print str(round(scores[u],3)).rjust(9),
            else:
                print str("").rjust(9),
            print str(u).ljust(20), 
        print str(grid_lanes(u)).ljust(12*3+1),            
        print str(grid_positions(u)).ljust(6),            
        print str(grid_roles(u)).ljust(11),
        print str(round(weighted_position(u), 2)).rjust(5)

def can_consider_position(p, team):
    # basically checking if there is any hero that is exclusive to that 
    # position
    # or if there are two heroes of whom one must be that position
    # so we're looking at valid position configs and seeing if we can find one
    # that doesn't include that position
    role_set = build_roles(team)
    for role_config in role_set:
        if role_config[1][p-1] == []: # the role is open
            return True
    return False



def show_heroes_by_position(parsed_heroes, scores={}, enemy=False, team=[], limit=5):
    for p in [0, 1, 2, 3, 4, 5]:
        if p > 0:
            # should we consider this position at all, given our heroes?
            if not can_consider_position(p, team):
                continue
            print "Position", p
        else:
            print "Unknown position"
        i = 0
        for u in (parsed_heroes):
            if i >= limit:
                continue
            if p == 0:
                if u in positions:
                    continue
            else:
                if u not in positions:
                    continue
                if positions[u][p-1] == 0:
                    continue
                if recommended_position(u) != str(p):
                    continue
            if enemy:
                print str("enemy").rjust(9),
                print str(u).ljust(20), 
            else:
                if u in scores:
                    print str(round(scores[u],3)).rjust(9),
                else:
                    print str("").rjust(9),
                print str(u).ljust(20), 
            print str(grid_lanes(u)).ljust(12*3+1),            
            print str(grid_positions(u)).ljust(6),            
            print str(grid_roles(u)).ljust(11),
            print str(round(weighted_position(u), 2)).rjust(5)
            i += 1
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


consider_these_heroes = alpha

if args.consider == "alpha":
    consider_these_heroes = alpha
else:
    print "unknown args.consider", args.consider
    exit()

ra = get_values(args.heroes)
print args.consider, len(consider_these_heroes)

if args.enemy != "":
    print
    print_heroes(args.enemy, enemy=True)
    print 
else:
    print

print_heroes(args.heroes)

scores = {}

for hh in consider_these_heroes:
    if hh in parse_heroes(args.heroes):
        continue
    if hh in parse_heroes(args.enemy):
        continue

    foo = get_values(args.heroes + [hh])


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
    lane_role_jung = { 1 : "Safe Lane",
                  2 : "Solo Mid",
                  3 : "Solo Hard Lane",
                  4 : "Jungle",
                  5 : "Safe Lane (Babysit)",
                  }
    lane_role_normal = { 1 : "Safe Lane",
                  2 : "Solo Mid",
                  3 : "Hard Lane",
                  4 : "Hard Lane",
                  5 : "Safe Lane (Babysit)",
                  }

    lane_role =  lane_role_normal
    
    # if our #3 can solo hard lane
    # and our #4 can jungle
    if tl[2][0] in laning and tl[3][0] in laning:
        if laning[tl[2][0]][2] > 0 and laning[tl[3][0]][11] > 0:
            lane_role = lane_role_jung

    print str(score_role_config(tl)).ljust(10)
    for k, v in tl.iteritems():
        if len(v) > 0:
            print str(k+1).rjust(2), str(v).ljust(20),
            print lane_role[k+1]
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
    if laning_hero not in laning:
        return True
    zeroes = 0
    for i in range(0, 12):
        if laning[laning_hero][i] == 0:
            zeroes += 1
    if zeroes == 12:
        return True
    return False

def have_no_role_data(laning_hero):
    if laning_hero not in positions:
        return True
    zeroes = 0
    for i in range(0, 5):
        if positions[laning_hero][i] == 0:
            zeroes += 1
    if zeroes == 5:
        return True
    return False
            
def recu_roles(i, team, tl, roles_list, verbose=False):
    if i >= len(team):
        return [[score_role_config(tl), tl]]
    append_to_roles_list = []
    if team[i] in positions:
        for j, k in enumerate(positions[team[i]]):
            if k > 0 or have_no_role_data(team[i]):
                if tl[j] == []:
                    new_tl = deepcopy(tl)
                    new_tl[j] += [team[i]]
                    latest = recu_roles(i+1, team, new_tl, roles_list, verbose)
                    if latest:
                        append_to_roles_list = append_to_roles_list + latest
    else:
        for j, k in enumerate([0, 0, 0, 0, 0]):
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
        for j, k in enumerate(expanded_laning(team[i])):
            if j in disabled_lane_types:
                continue
            if have_no_laning_data(team[i]):
                if j == 11: # don't put heroes we don't have laning data for
                            # in the jungle
                    continue
            if k > 0 or have_no_laning_data(team[i]):
                new_tl = deepcopy(tl)
                new_tl[j] += [team[i]]
                latest = recu_lanes(i+1, team, new_tl, laning_list, verbose)
                if latest:
                    append_to_laning_list = append_to_laning_list + latest
    else:
        for j, k in enumerate([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            if j in disabled_lane_types:
                continue
            if j == 11: # not junglers
                continue
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


print 


if len(args.heroes) < 5:

    possible_heroes = []
    lane_conflicts = []
    role_conflicts = []
    nc_data = []

    us = parse_heroes(args.heroes)
    our_pos = 0
    for h in us:
        our_pos += weighted_position(h)
    print 15-our_pos

    for hh in consider_these_heroes:
        if hh in parse_heroes(args.heroes):
            continue
        if hh in parse_heroes(args.enemy):
            continue
   
        n=build_roles(args.heroes+[hh])

        if not len(n)>0:
            role_conflicts += [hh]
            continue

        if args.enemy:
            nc_data += [[nc_mod(hh, args.enemy), hh]]
        else:
            nc_data += [[pb_mod(hh), hh]]

    # now we have our list of possible heroes
    # all of whom could work based on lane or role
    # we need to sort it by counters

    print "perhaps"

    sorted_nc_data = sorted(nc_data, key=lambda l: l[0], reverse=True)
    
    sorted_hero_names = []
    scores_dictionary = {}

    for row in sorted_nc_data:
        sorted_hero_names += [row[1]]
        scores_dictionary[row[1]] = row[0]

    show_heroes_by_position(sorted_hero_names, scores=scores_dictionary, team=args.heroes)


else:
    print "analyzing your team"

    print "our roles:"
    v = build_roles(args.heroes, verbose=True)

    sorted_v = sorted(v, key=lambda l: l[0], reverse=True)

    # just show the top 3
    if len(sorted_v) > 0:
        for i, j in enumerate(sorted_v):
            pretty_roles(j[1])
            if i == 0:
                break
    else:
        print "No possible roles"

    print "our lanes:"
    n = build_lanes(args.heroes, verbose=True)

    sorted_n = sorted(n, key=lambda l: l[0], reverse=True)

    if len(sorted_n) > 0:
        for i, j in enumerate(sorted_n):
            pretty_lanes(j[1])
            if i == 0:
                break
    else:
        print "No possible lanes"

    





    


