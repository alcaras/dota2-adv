
known_roles = ["Nuker",
               "Pusher",
               "Lane Support",
               "Support",
               "Disabler",
               "Initiator",
               "Carry",
               "Jungler",
               "Durable",
               "Escape",]

hard_carries = [
    "Anti-Mage",
    "Drow Ranger",
    "Faceless Void",
    "Lifestealer",
    "Morphling",
    "Naga Siren",
    "Outworld Destroyer",
    "Phantom Assassin",
    "Sniper",
    "Spectre",
    ]

roles = {
    'Alchemist': ['Carry', 'Disabler', 'Durable'],
    'Ancient Apparition': ['Disabler', 'Support'],
    'Anti-Mage': ['Carry', 'Escape'],
    'Axe': ['Disabler', 'Durable', 'Initiator', 'Jungler'],
    'Bane': ['Disabler', 'Nuker', 'Support'],
    'Batrider': ['Disabler', 'Escape', 'Initiator', 'Nuker'],
    'Beastmaster': ['Disabler', 'Durable', 'Initiator'],
    'Bloodseeker': ['Carry', 'Jungler'],
    'Bounty Hunter': ['Carry', 'Escape', 'Nuker'],
    'Brewmaster': ['Carry', 'Durable', 'Initiator', 'Pusher'],
    'Broodmother': ['Carry', 'Escape', 'Pusher'],
    'Chaos Knight': ['Carry', 'Disabler', 'Durable', 'Pusher'],
    'Centaur Warrunner': ['Disabler', 'Durable', 'Initiator'],
    'Chen': ['Jungler', 'Pusher', 'Support'],
    'Clinkz': ['Carry', 'Escape'],
    'Clockwerk': ['Durable', 'Initiator'],
    'Crystal Maiden': ['Disabler', 'Lane Support', 'Nuker', 'Support'],
    'Dark Seer': ['Escape', 'Initiator', 'Nuker'],
    'Dazzle': ['Lane Support', 'Support'],
    'Death Prophet': ['Durable', 'Nuker', 'Pusher'],
    'Disruptor': ['Disabler', 'Initiator', 'Nuker', 'Support'],
    'Doom Bringer': ['Carry', 'Durable', 'Nuker'],
    'Dragon Knight': ['Carry', 'Disabler', 'Durable', 'Pusher'],
    'Drow Ranger': ['Carry'],
    'Earthshaker': ['Disabler', 'Initiator', 'Lane Support', 'Support'],
    'Enchantress': ['Durable', 'Jungler', 'Pusher', 'Support'],
    'Enigma': ['Disabler', 'Initiator', 'Jungler', 'Pusher'],
    'Faceless Void': ['Carry', 'Disabler', 'Escape', 'Initiator'],
    'Gyrocopter': ['Disabler', 'Initiator', 'Nuker'],
    'Huskar': ['Carry', 'Durable', 'Initiator'],
    'Invoker': ['Carry', 'Escape', 'Initiator', 'Nuker'],
    'Jakiro': ['Disabler', 'Lane Support', 'Nuker', 'Pusher'],
    'Juggernaut': ['Carry', 'Pusher'],
    'Keeper of the Light': ['Pusher'],
    'Kunkka': ['Carry', 'Disabler', 'Durable', 'Initiator'],
    'Leshrac': ['Disabler', 'Nuker', 'Pusher', 'Support'],
    'Lich': ['Lane Support', 'Nuker', 'Support'],
    'Lifestealer': ['Carry', 'Durable', 'Escape', 'Jungler'],
    'Lina': ['Disabler', 'Nuker', 'Support'],
    'Lion': ['Disabler', 'Lane Support', 'Nuker', 'Support'],
    'Lone Druid': ['Carry', 'Durable', 'Jungler', 'Pusher'],
    'Luna': ['Carry', 'Nuker'],
    'Lycanthrope': ['Carry', 'Durable', 'Jungler', 'Pusher'],
    'Magnus': ['Carry'],
    'Meepo': ['Carry', 'Disabler', 'Initiator'],
    'Mirana': ['Carry', 'Disabler', 'Escape', 'Nuker'],
    'Morphling': ['Carry', 'Escape', 'Initiator', 'Nuker'],
    'Naga Siren': ['Carry', 'Disabler', 'Escape', 'Pusher'],
    "Nature's Prophet": ['Carry', 'Escape', 'Jungler', 'Pusher'],
    'Necrolyte': ['Carry', 'Durable', 'Support'],
    'Night Stalker': ['Durable', 'Initiator'],
    'Nyx Assassin': ['Disabler', 'Nuker'],
    'Ogre Magi': ['Disabler', 'Durable', 'Nuker'],
    'Omniknight': ['Durable', 'Lane Support', 'Support'],
    'Outworld Destroyer': ['Carry'],
    'Phantom Assassin': ['Carry', 'Escape'],
    'Phantom Lancer': ['Carry', 'Escape', 'Pusher'],
    'Puck': ['Disabler', 'Escape', 'Initiator', 'Nuker'],
    'Pudge': ['Disabler', 'Durable'],
    'Pugna': ['Nuker', 'Pusher', 'Support'],
    'Queen of Pain': ['Carry', 'Escape', 'Nuker'],
    'Razor': ['Carry', 'Durable', 'Nuker'],
    'Riki': ['Carry', 'Escape'],
    'Rubick': ['Disabler', 'Pusher'],
    'Sand King': ['Disabler', 'Initiator', 'Nuker'],
    'Shadow Demon': ['Disabler', 'Nuker', 'Support'],
    'Shadow Fiend': ['Carry', 'Nuker'],
    'Shadow Shaman': ['Disabler', 'Nuker', 'Pusher', 'Support'],
    'Silencer': ['Carry', 'Initiator', 'Support'],
    'Skeleton King': ['Carry', 'Disabler', 'Durable'],
    'Slardar': ['Carry', 'Disabler', 'Durable', 'Initiator'],
    'Slark' : ['Escape'],
    'Sniper': ['Carry'],
    'Spectre': ['Carry', 'Durable'],
    'Spirit Breaker': ['Carry', 'Disabler', 'Durable', 'Initiator'],
    'Storm Spirit': ['Carry', 'Disabler', 'Escape', 'Initiator'],
    'Sven': ['Carry', 'Disabler', 'Initiator', 'Support'],
    'Templar Assassin': ['Carry', 'Escape'],
    'Tidehunter': ['Disabler', 'Durable', 'Initiator', 'Support'],
    'Tinker': ['Nuker', 'Pusher'],
    'Tiny': ['Disabler', 'Durable', 'Initiator', 'Nuker'],
    'Treant Protector': [   'Disabler',
                            'Durable',
                            'Initiator',
                            'Lane Support'],
    'Undying': ['Disabler', 'Durable', 'Initiator', 'Pusher'],
    'Ursa': ['Carry', 'Durable', 'Jungler'],
    'Vengeful Spirit': ['Disabler', 'Initiator', 'Lane Support', 'Support'],
    'Venomancer': ['Initiator', 'Nuker', 'Pusher', 'Support'],
    'Viper': ['Carry', 'Durable'],
    'Visage': ['Support'],
    'Warlock': ['Disabler', 'Initiator', 'Lane Support', 'Support'],
    'Weaver': ['Carry', 'Escape'],
    'Windrunner': ['Disabler', 'Escape', 'Nuker', 'Support'],
    'Wisp': ['Support'],
    'Witch Doctor': ['Disabler', 'Support'],
    'Zeus': ['Nuker', 'Support']
    }

#for h in hard_carries:
#    roles[h] += ['Hard Carry']
# known_roles += ['Hard Carry']