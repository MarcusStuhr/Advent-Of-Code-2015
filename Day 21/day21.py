from itertools import combinations
from math import ceil

HERO_INITIAL_HP = 100
HERO_INITIAL_DAMAGE = 0
HERO_INITIAL_ARMOR = 0

BOSS_INITIAL_HP = 104
BOSS_INITIAL_DAMAGE = 8
BOSS_INITIAL_ARMOR = 1

WEAPONS = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
ARMOR = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
RINGS = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

def get_costs():
    min_cost = float('inf')
    max_cost = 0
    
    for num_weapons in xrange(1,1+1):
        for num_armor in xrange(0,1+1):    
            for num_rings in xrange(0,len(RINGS)+1):
                for weapon in combinations(WEAPONS,num_weapons):
                    for armor in combinations(ARMOR,num_armor):
                        for rings in combinations(RINGS,num_rings):
                            hero_cost = 0
                            hero_hp = HERO_INITIAL_HP
                            hero_damage = HERO_INITIAL_DAMAGE
                            hero_armor = HERO_INITIAL_ARMOR
                            boss_hp = BOSS_INITIAL_HP
                            boss_damage = BOSS_INITIAL_DAMAGE
                            boss_armor = BOSS_INITIAL_ARMOR
                            
                            for c,d,a in weapon:
                                hero_cost += c
                                hero_damage += d
                                hero_armor += a
                            for c,d,a in armor:
                                hero_cost += c
                                hero_damage += d
                                hero_armor += a
                            for c,d,a in rings:
                                hero_cost += c
                                hero_damage += d
                                hero_armor += a
                                
                            damage_to_boss = max(1, hero_damage - boss_armor)
                            damage_to_hero = max(1, boss_damage - hero_armor)
    
                            if ceil(float(hero_hp) / damage_to_hero) >= ceil(float(boss_hp) / damage_to_boss):
                                min_cost = min(min_cost, hero_cost)
                            else:
                                max_cost = max(max_cost, hero_cost)
                                
    return min_cost, max_cost


def main():
    print "Answer to part 1: {}".format(get_costs()[0])
    print "Answer to part 2: {}".format(get_costs()[1])


if __name__ == "__main__":
    main()
