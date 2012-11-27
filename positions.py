# hero name = [# of times picked * winrate in position 1, 2, 3, 4, 5]
# data from http://dota-academy.com/herolist/from/20120826/to/20121115/regions/ALL/


 


positions = {
    "Alchemist" : [3,0,0,0,0],
    "Ancient Apparition" : [0,0,0,2,7.92],
    "Anti-Mage" : [35.19,0,0,0,0],
    "Axe" : [0,0,0,0,0],
    "Bane" : [0,0,0,2,1],
    "Batrider" : [0,13,18.9,9,1],
    "Beastmaster" : [0,1,22,4.97,0],
    "Bounty Hunter" : [1.98,9,46.4,4.97,0],
    "Brewmaster" : [2,19.98,12,0,0],
    "Broodmother" : [3.04,4.94,7,0,0],
    "Chaos Knight" : [35,18.91,3.01,0,0],
    "Chen" : [0,0,0,54.72,2.97],
    "Clinkz" : [4,3,0,0,0],
    "Clockwerk" : [0,0,0,1,0],
    "Crystal Maiden" : [0,0,0,0,24.18],
    "Dark Seer" : [0,1.98,44.84,7.98,0],
    "Dazzle" : [0,1,0,2.01,1],
    "Death Prophet" : [0,0,0,0,0],
    "Disruptor" : [0,0.99,0,3,14.04],
    "Doom Bringer" : [2.01,0,3,1,0],
    "Dragon Knight" : [7.98,5,0,0,0],
    "Drow Ranger" : [1,0,0,0,0],
    "Earthshaker" : [0,0,0,3.04,5.04],
    "Enchantress" : [0,0,0.99,28.91,4],
    "Enigma" : [0,1,21.15,33,0.99],
    "Faceless Void" : [7.98,0,0,0,0],
    "Geomancer" : [0,0,0,0,0],
    "Gyrocopter" : [0,0,0,0,0],
    "Huskar" : [0,0,0,0,0],
    "Invoker" : [2,59.22,3.96,0,1],
    "Jakiro" : [0,0,0,14.04,43.89],
    "Juggernaut" : [11,1,1,0,0],
    "Keeper of the Light" : [0,0,6.03,12.1,12.1],
    "Kunkka" : [2,0,0,0,0],
    "Leshrac" : [4.98,4.94,7.04,35.1,39.2],
    "Lich" : [0,0,0,1,5.04],
    "Lifestealer" : [14,0,0,0,0],
    "Lina" : [0,0,0,8,6.97],
    "Lion" : [0,0,0,1,1],
    "Lone Druid" : [35.1,2.01,2,0,0],
    "Luna" : [7.03,0,0,0,0],
    "Lycanthrope" : [11,4,0,1,0],
    "Magnataur" : [0,1,0,1,0],
    "Mirana" : [2,3,2,2.01,0],
    "Morphling" : [57.66,1,0,0,0],
    "Naga Siren" : [22.79,4.98,0,1,0],
    "Nature's Prophet" : [4,15,29.7,8,0],
    "Necrolyte" : [1,0,0,0,0],
    "Night Stalker" : [0,12.88,6.05,0,0],
    "No Hero" : [0,0,0,0,0],
    "Nyx Assassin" : [0,3,1,0.99,0],
    "Ogre Magi" : [0,0,0,0,0],
    "Omniknight" : [0,0,3,0,0],
    "Outworld Destroyer" : [0,0,0,0,0],
    "Phantom Assassin" : [3,0,0,0,0],
    "Phantom Lancer" : [2.97,0,0,0,0],
    "Puck" : [0,7.02,6,0,0],
    "Pudge" : [0,7.02,3,0,0],
    "Pugna" : [0,0.99,0,0,0],
    "Queen of Pain" : [3,41.8,7,0,1],
    "Razor" : [0,1,0,0,0],
    "Riki" : [2,1,0,0,0],
    "Rubick" : [0,18.13,10.08,34.22,31.92],
    "Sand King" : [0,3,8.99,15.12,2.01],
    "Shadow Demon" : [0,0,0,1,21.09],
    "Shadow Fiend" : [15.95,1,0,0,0],
    "Shadow Shaman" : [0,1.98,1,10.03,31.9],
    "Silencer" : [0,0,0,0,0],
    "Slardar" : [4,1,1,0,0],
    "Sniper" : [2.01,0,0,0,0],
    "Spiritbreaker" : [0,0,0,0,0],
    "Storm Spirit" : [1.98,15.08,3,0,0],
    "Sven" : [11.02,1,1,2.01,0],
    "Tauren Chieftain" : [0,0,0,0,0],
    "Templar Assassin" : [8,44.1,1,0,0],
    "Tidehunter" : [0,3,39,35.1,10],
    "Tinker" : [3.04,10.85,2,0,0],
    "Tiny" : [24.05,2,0.99,0,0],
    "Treant Protector" : [0,0,0,0,0],
    "Undying" : [3,4,6,4,1],
    "Ursa" : [1,0,0,0,0],
    "Vengeful Spirit" : [0,0,0,1,9.89],
    "Venomancer" : [0,0,0,4.95,57.6],
    "Viper" : [1,0,0,0,0],
    "Visage" : [0,0,0,1,0],
    "Warlock" : [0,0,0,0,0],
    "Weaver" : [2,0,1,0,0],
    "Windrunner" : [0,11,34.31,7.04,0],
    "Wisp" : [0,0,0,4.02,26.84],
    "Witch Doctor" : [0,0,0,0,1],
    "Zeus" : [0,0,0,0,0],
}

def priority_positions(hero):
    if hero not in positions:
        return [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)] # we have no data
    hp = { 1 : positions[hero][0],
           2 : positions[hero][1],
           3 : positions[hero][2],
           4 : positions[hero][3],
           5 : positions[hero][4],}
    sorted_hp = sorted(hp.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    return sorted_hp
           

def heroes_for_position(position):
    possible_heroes = []
    for k, v in positions.iteritems():
        if v[position-1] > 0:
            possible_heroes += [[v[position-1], k]]
    sorted_possible_heroes = sorted(possible_heroes,
                                    key=lambda e: e[0],
                                    reverse=True)
    return sorted_possible_heroes
            
        
def recommended_position(hero):
    if hero not in positions:
        return "?"
    if priority_positions(hero)[0][1] == 0:
        return "?"
    return str(priority_positions(hero)[0][0])

        
def possible_positions(hero):
    if hero not in positions:
        return "?????"
    if priority_positions(hero)[0][1] == 0:
        return "?????"
    pp = priority_positions(hero)
    position_string = ""
    for p in pp:
        if p[1] > 0:
            position_string += str(p[0])
    return position_string

def grid_positions(hero):
    if hero not in positions:
        return "?????"
    if priority_positions(hero)[0][1] == 0:
        return "?????"
    pp = sorted(priority_positions(hero), key=lambda e:e[0], reverse=False)
    position_string = ""
    for p in pp:
        if p[1] > 0:
            position_string += str(p[0])
        else:
            position_string += " "
    return position_string

def weighted_position(hero):
    if hero not in positions:
        return 0 # we don't have position information
    if priority_positions(hero)[0][1] == 0:
        return 0
    weight_sum = 0
    weight_top = 0
    for k, v in enumerate(positions[hero]):
        weight_top += float((k+1) * v)
        weight_sum += float(v)
    weight_avg = weight_top/weight_sum
    return weight_avg

