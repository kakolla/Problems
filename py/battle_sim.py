"""
outcome = battle (team1, team2)

monster:
- name, # life points, attack strength


assumptions:
right now, monsters fight till the death
greedily replace monsters and fight
"""

# define classes

# define sim loop

from dataclasses import dataclass
from enum import Enum
class Types(Enum):
    fire = "fire"
    water = "water"

class Monster:
    name: str
    life: int
    attack: int
    type: Types # monster is this type 
    weakness: Types # monster has a weakness for this type

    def __init__(self, name, life, attack, type, weakness):
        self.name = name
        self.life = life
        self.attack = attack
        self.type = type
        self.weakness = weakness

    
    # def __lt__(self, other_monster: "Monster"):
    #     return self.attack > other_monster.attack

@dataclass
class Team:
    name: str
    roster: list[Monster] # needs to be a heap
    # _current_monster_index: int = 0

    def get_dmg(self, att: Monster, defend: Monster) -> int:
        dmg = att.attack
        import math
        if att.type == defend.weakness:
            dmg *= 2
        elif att.weakness == defend.type:
            dmg = math.floor(dmg / 2)
        return dmg

    def get_best_attacker(self, defender: Monster) -> Monster | None:
        import math # dont care about lazy load rn
        # get best attacker for the defender (considering its type)
        alive = [m for m in self.roster if m.life > 0 ]
        if not alive: return None

        max_attacker = max(alive, key= lambda x: self.get_dmg(x, defender))
        return max_attacker
    
    def remove_dead(self) -> None:
        self.roster = [m for m in self.roster if m.life > 0]



def battle(team1: Team, team2: Team) -> str:
    """ Return battle log"""
    # while both teams have alive monsters
    # fight, alternating between teams
    offsense: Team = team1
    defense: Team = team2

    log: list[str] = []
    offsense_monster = team1.roster[0]
    defense_monster = team2.get_best_attacker(offsense_monster)
    offsense_monster = team1.get_best_attacker(defense_monster)

    # while monsters alive on both teams
    while team1.roster and team2.roster:
        log.append(f"Team {offsense.name} turn")

        curr_attack = offsense_monster.attack

        # check type
        import math
        if offsense_monster.type == defense_monster.weakness:
            log.append(f"!{offsense_monster.name} had an advantage over {defense_monster.name}")
            curr_attack *= 2
        elif defense_monster.type == offsense_monster.weakness:
            log.append(f"!{defense_monster.name} had an advantage over {offsense_monster.name}")
            curr_attack = math.floor(curr_attack / 2)

        log.append(f"{offsense_monster.name} attacks {defense_monster.name} for {curr_attack} damage")

        defense_monster.life -= curr_attack

        if defense_monster.life <= 0:
            log.append(f"{defense_monster.name} is defeated")
            defense.remove_dead()
            if not defense.roster:
                break
            defense_monster = defense.get_best_attacker(offsense_monster) # get an optimizing monster back

        offsense, defense = defense, offsense # swap
        offsense_monster, defense_monster = defense_monster, offsense_monster
    
    if team1.roster:
        log.append(f"{team1.name} wins")
    else:
        log.append(f"{team2.name} wins")

    return "\n".join(log)

t1_monsters = [Monster(name="Dog", attack=2, life=3, weakness=Types.fire, type=Types.water), Monster(name="Wolf", life=4, attack=1, weakness=Types.fire, type=Types.water)]
# heapq.heapify(t1_monsters)
t1 = Team(name="Blue", roster=t1_monsters)

t2_monsters = [Monster(name="Cat", attack=3, life=3, weakness=Types.fire, type=Types.water), Monster(name="Tiger", life=4, attack=5, weakness= Types.fire,type=Types.water)]
# heapq.heapify(t2_monsters, )
t2 = Team(name="Red", roster=t2_monsters)

yr = battle(t1, t2)
print(yr)