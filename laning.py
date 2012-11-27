# hero name = [# of times picked * winrate in solo mid, dual mid, dual hard, tri hard, solo safe, solo safe + jungle/roam, dual safe, dual safe + jungle/roam, tri safe, roam, jungle
# data from http://dota-academy.com/herolist/from/20120826/to/20121115/regions/ALL/

# for ease of referencing the array
laning_lanes = {
    "Solo Mid" : 0,  
    "Dual Mid" : 1,  
    "Solo Hard" : 2,
    "Dual Hard" : 3,
    "Tri Hard" : 4,
    "Solo Safe" : 5,
    "Solo Safe+J/R" : 6,
    "Dual Safe" : 7,
    "Dual Safe+J/R" : 8,
    "Tri Safe" : 9,
    "Roam" : 10,
    "Jungle" : 11,
}

lanes_micro = {
    0 : " m",
    1 : "M ",
    2 : " h",
    3 : "H ",
    4 : "Hh",
    5 : " s",
    6 : "js",
    7 : "S ",
    8 : "Sj",
    9 : "Ss",
    10 :" r",
    11 :" j",
    }

lanes_laning = {}
for k, v in laning_lanes.iteritems():
    lanes_laning[v] = k

laning = {
    "Alchemist" : [0,0,1,0,0,1,0,0,0,1,0,0],
    "Ancient Apparition" : [0,0.98,0,0,3.01,0,0,1,2,2.01,0,0],
    "Anti-Mage" : [0,1.98,2.01,1,2,1,1,0.99,4.05,13.02,0,0],
    "Axe" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Bane" : [0,0,0,0,0,0,0,0,0,1,1,0],
    "Batrider" : [13,0,7.05,0,0.99,4,2,0,2.01,1,0,11.04],
    "Beastmaster" : [1,0,18.04,0,0,1,0,0,0,0,0,1],
    "Bounty Hunter" : [1,0,48.98,1,0,3,3.01,0,0.99,0,0,1],
    "Brewmaster" : [8.96,1,3,0,1,1,0,3,5.04,6.03,0,0],
    "Broodmother" : [0,0,9.9,1,0,0,0.99,0,0,0,0,0],
    "Chaos Knight" : [0,10,1,3.96,6.97,0,0,3,19.98,7,0,0],
    "Chen" : [0,0,0,0,1,0,0,0,0,0,0,46],
    "Clinkz" : [2,0,0,0,0,1.98,2.01,1,0,0,0,0],
    "Clockwerk" : [0,0,1,0,0,0,0,0,0,0,0,0],
    "Crystal Maiden" : [0,6.05,0,0,0.99,0,0,1,4,8.01,0,0],
    "Dark Seer" : [2,0,29.89,3,0,2,3,0,0,0,1,3.04],
    "Dazzle" : [1,1,0,0,1,0,0,0,0,0,0,0],
    "Death Prophet" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Disruptor" : [0.99,1,0,2,2.03,0,0,1,3.04,6.08,1,0],
    "Doom Bringer" : [0,0,0,0,0,0,0,0,2,0,0,4],
    "Dragon Knight" : [6.05,1,0,0,0,0,0,0,4,1,0,0],
    "Drow Ranger" : [0,0,0,0,0,0,0,0,1,0,0,0],
    "Earthshaker" : [0,0,0,0.99,0,0,0,0,1,4.97,0,0],
    "Enchantress" : [0,0,0,0,0.99,0,0,0,0,1,1,27.03],
    "Enigma" : [0,1,7.92,0,0,0,1,0,0,0,0,40.04],
    "Faceless Void" : [0,0.99,0,0,0,0,0,1,6,0,0,0],
    "Geomancer" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Gyrocopter" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Huskar" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Invoker" : [39.95,0,0,0,0,4,3,1,1,0,0,0],
    "Jakiro" : [0,6.03,0,1.98,9.03,0,0,5,24.84,9.1,1,0],
    "Juggernaut" : [3,1,0,1,0,0,0,1,5,0.99,1,0],
    "Keeper of the Light" : [0,3,5.04,4,3.96,0,0,0.99,1,5.95,0,2],
    "Kunkka" : [0,0,0,1,0,0,0,0,0,1,0,0],
    "Leshrac" : [2,4,0,2.03,14.04,1,1,4,30.24,17.15,0.99,1],
    "Lich" : [0,1.02,2.01,0.99,0,0,0,0,1,0,0,0],
    "Lifestealer" : [0,0,0,0,2.01,0,0,1,9,1,0,1],
    "Lina" : [1,3.99,0,0,3.96,0,0,1,3,1,0,0],
    "Lion" : [0,0,0,0,0,0,0,0,0,2.01,0,0],
    "Lone Druid" : [2,0,7.92,0,0.99,0.99,1,1,4.95,5.04,0,1],
    "Luna" : [0,0,0,0.99,0,0,1,1,2.03,1,0,0],
    "Lycanthrope" : [0,0,1,0,0,0.99,0,0,2.01,0,0,10.01],
    "Magnataur" : [0.99,0,0,0,0,0,0,0,0,0,0,1],
    "Mirana" : [3,0,1,0,1,0,1,0,0,1,0,0],
    "Morphling" : [18.04,7.05,0,1,1,2,0.99,3,8.04,5.04,0,0],
    "Naga Siren" : [2,3,1,3,4.03,0,1,3.04,3.99,7.04,0,0],
    "Nature's Prophet" : [4,0,20.06,0,0,4,0.99,0,0,2,0,15.08],
    "Necrolyte" : [0,0,0,0,0,1,0,0,0,0,0,0],
    "Night Stalker" : [7,2.01,0,0,2,0,0,2,1,3,0,0],
    "No Hero" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Nyx Assassin" : [1,3,0,0,0,0,0,0,0,1,0,0],
    "Ogre Magi" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Omniknight" : [0,0,3,0,0,0,0,0,0,0,0,0],
    "Outworld Destroyer" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Phantom Assassin" : [0,0,0,1,0,0,1,0,0,0,0,0],
    "Phantom Lancer" : [0,0,0,0,1,0,0,0,0.99,0.99,0,0],
    "Puck" : [6,0,2.01,0,0,0,0,0,0,0,0,0],
    "Pudge" : [3,1,0,1,0,0,1,0,2,2,0,0],
    "Pugna" : [0.99,0,0,0,0,0,0,0,0,0,0,0],
    "Queen of Pain" : [39.36,3,2,0,1,0.99,1,1,0.99,0,0,0],
    "Razor" : [0,0,0,0,1,0,0,0,0,0,0,0],
    "Riki" : [0,0,0,0,1,0,0,0,1,0.99,0,0],
    "Rubick" : [15.98,5.98,4.98,4,9.01,0,2,5.04,9.9,21.9,0,0],
    "Sand King" : [2.01,0,1.02,0,1.02,1.02,1,0,6,4.96,0,0],
    "Shadow Demon" : [0,0,0,2,4.95,0,0,0,3.01,2,2.01,0],
    "Shadow Fiend" : [4.94,1,0,0,0,0,0,2.01,8,1,0,0],
    "Shadow Shaman" : [1.98,1,0,1,1,0,0,3,15.93,11.97,0,0],
    "Silencer" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Slardar" : [0,0,0,1,2,0,0,0,1,2,0,0],
    "Sniper" : [0,0,0,0,0,1,0,0,0,1,0,0],
    "Spiritbreaker" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Storm Spirit" : [10.05,0,0,0,0,1,1,0,2,1,0,0],
    "Sven" : [0,0,0,1,2,0,1,1,4.97,3.99,1,0],
    "Tauren Chieftain" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Templar Assassin" : [39,3.96,1,0,0,0,0,1,0,0,0,0],
    "Tidehunter" : [4,1,22,0.99,4.95,7,4,2.03,9,17,2,2.01],
    "Tinker" : [7.98,0,0,0,0,0,0,0,0.99,3,0,0],
    "Tiny" : [1,0,0,4.02,1,0,0,2,12.07,1.98,0,0],
    "Treant Protector" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Undying" : [0,0,0,7.02,7,0,0,2.01,0.99,2,0,0],
    "Ursa" : [1,0,0,0,0,0,0,0,0,0,0,0],
    "Vengeful Spirit" : [0,0,0,1,2,0,1,1,2,2,0,0],
    "Venomancer" : [0,7.98,0,10.08,9.02,0,0,1,14.04,10.92,0.99,0],
    "Viper" : [0,0,0,0,0,0,0,0,1,0,0,0],
    "Visage" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Warlock" : [0,0,0,0,0,0,0,0,0,0,0,0],
    "Weaver" : [0,0,2,0,1,0,0,0,0,0,0,0],
    "Windrunner" : [13,1,18.87,3.04,3,1,2,1,1,0,0,0],
    "Wisp" : [0,0,0,4,0,0,0,6,10.07,6.96,0,0],
    "Witch Doctor" : [0,0,0,0,0,0,0,0,1,0,0,0],
    "Zeus" : [0,0,0,0,0,0,0,0,0,0,0,0],
    }
    
    
def priority_laning(hero):
    if hero not in laning:
        return [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)] # no data
    hl = {}
    for i in range(0, 12):
        hl[i] = laning[hero][i]
    sorted_hl = sorted(hl.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    return sorted_hl
           

def heroes_for_lane(lane_string):
    lane = laning_lanes[lane_string[0]]
    possible_heroes = []
    for k, v in laning.iteritems():
        if v[lane] > 0:
            possible_heroes += [[v[lane], k]]
    sorted_possible_heroes = sorted(possible_heroes,
                                    key=lambda e: e[0],
                                    reverse=True)
    return sorted_possible_heroes            
        
def recommended_lane(hero):
    if hero not in laning:
        return "?"
    if priority_laning(hero)[0][1] == 0:
        return "?"
    return str(lanes_laning[priority_laning(hero)[0][0]])

def possible_lanes(hero):
    if hero not in laning:
        return "?"
    if priority_laning(hero)[0][1] == 0:
        return "?"
    pp = priority_laning(hero)
    lane_string = ""
    for p in pp:
        if p[1] > 0:
            lane_string += str(lanes_micro[p[0]]) + " "
    return lane_string

def grid_lanes(hero):
    if hero not in laning:
        return "?"
    if priority_laning(hero)[0][1] == 0:
        return "?"
    pp = sorted(priority_laning(hero), key=lambda e:e[0], reverse=False)
    lane_string = ""
    for p in pp:
        if p[1] > 0:
            lane_string += str(lanes_micro[p[0]]) + " "
        else:
            lane_string += "  " + " "
    return lane_string

def expanded_laning(hero):
    # safe, mid, hard, jungle
    expanded_lane = [0,0,0,0,0,0,0,0,0,0,0,0]
    mid = [0, 1, 10]
    safe = [5, 6, 7, 8, 9, 10]
    jungle = [11]
    hard = [2, 3, 10]
    lanes = [mid, safe, jungle, hard]
    for l in lanes:
        interim = 0
        for i in l:
            interim += laning[hero][i]
        for i in l:
            expanded_lane[i] = interim
    return expanded_lane    
    
laning_lanes = {
    "Solo Mid" : 0,  
    "Dual Mid" : 1,  
    "Solo Hard" : 2,
    "Dual Hard" : 3,
    "Tri Hard" : 4,
    "Solo Safe" : 5,
    "Solo Safe+J/R" : 6,
    "Dual Safe" : 7,
    "Dual Safe+J/R" : 8,
    "Tri Safe" : 9,
    "Roam" : 10,
    "Jungle" : 11,
}
