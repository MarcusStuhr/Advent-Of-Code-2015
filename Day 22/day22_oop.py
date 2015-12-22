from copy import deepcopy

HERO_INITIAL_HP = 50
HERO_INITIAL_ARMOR = 0
HERO_INITIAL_MANA = 500
BOSS_INITIAL_HP = 71
BOSS_INITIAL_DAMAGE = 10

INITIAL_SPELLS = {("Magic Missile",53,4,0,0,0,0,0),
                  ("Drain",73,2,0,2,0,0,0),
                  ("Shield",113,0,0,0,7,0,6),
                  ("Poison",173,0,3,0,0,0,6),
                  ("Recharge",229,0,0,0,0,101,5)}

class Spell(object):

    def __init__(self, name, cost, cast_damage, effect_damage, heal, armor_boost, mana_boost, duration):
        self.name = name
        self.cost = cost
        self.cast_damage = cast_damage
        self.effect_damage = effect_damage
        self.heal = heal
        self.armor_boost = armor_boost
        self.mana_boost = mana_boost
        self.duration = duration

class GameState(object):
    memo_cache = {}
    best_min = float('inf')

    def __init__(self, hero_hp, boss_hp, boss_damage, hero_armor, hero_mana, mana_spent, timers, spells, hard_mode):
        self.hero_hp = hero_hp
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.hero_armor = hero_armor
        self.hero_mana = hero_mana
        self.mana_spent = mana_spent
        self.timers = timers
        self.spells = {spell.name : spell for spell in spells}
        self.hard_mode = hard_mode
        self.active_player = "hero"

    def get_args(self):
        return (self.hero_hp, self.boss_hp, self.hero_mana, self.mana_spent, tuple(self.timers), self.hard_mode)

    def apply_effects(self):
        if self.timers["Shield"] > 0:
            self.hero_armor = self.spells["Shield"].armor_boost
        else:
            self.hero_armor = 0
        if self.timers["Poison"] > 0:
            self.boss_hp -= self.spells["Poison"].effect_damage
        if self.timers["Recharge"] > 0:
            self.hero_mana += self.spells["Recharge"].mana_boost
        for status in self.timers:
            self.timers[status] = max(0, self.timers[status]-1)

    def play(self):
        memo_key = self.get_args()

        if memo_key in GameState.memo_cache:
            return GameState.memo_cache[memo_key]

        if self.hard_mode and self.active_player == "hero":
            self.hero_hp -=1

        self.apply_effects()

        if self.boss_hp <= 0:
            GameState.best_min = min(GameState.best_min, self.mana_spent)
            return self.mana_spent

        if self.hero_mana == 0 or self.hero_hp <= 0 or self.mana_spent >= GameState.best_min:
            return float('inf')

        if self.active_player == "hero": #hero's turn
            min_mana_spent = float('inf')

            for spell in self.spells:

                if self.hero_mana >= self.spells[spell].cost:
                    if spell in self.timers and self.timers[spell]>0:
                        continue
                    new_state = deepcopy(self)
                    if spell in new_state.timers:
                        new_state.timers[spell] = self.spells[spell].duration
                    new_state.hero_hp += new_state.spells[spell].heal
                    new_state.boss_hp -= new_state.spells[spell].cast_damage
                    new_state.hero_mana -= new_state.spells[spell].cost
                    new_state.mana_spent += new_state.spells[spell].cost
                    new_state.active_player = "boss"
                    min_mana_spent = min(min_mana_spent, new_state.play())

            self.memo_cache[memo_key] = min_mana_spent
            return min_mana_spent

        else: #boss' turn
            self.hero_hp -= max(1, self.boss_damage - self.hero_armor)
            self.active_player = "hero"
            return self.play()

def main():
    hero_hp = HERO_INITIAL_HP
    hero_armor = HERO_INITIAL_ARMOR
    hero_mana = HERO_INITIAL_MANA
    mana_spent = 0
    boss_hp = BOSS_INITIAL_HP
    boss_damage = BOSS_INITIAL_DAMAGE
    timers = {"Shield":0, "Poison":0, "Recharge":0}
    spells = tuple(Spell(*args) for args in INITIAL_SPELLS)

    game_state_easy = GameState(hero_hp, boss_hp, boss_damage, hero_armor, hero_mana, mana_spent, timers, spells, False)
    game_state_hard = GameState(hero_hp, boss_hp, boss_damage, hero_armor, hero_mana, mana_spent, timers, spells, True)

    print "Answer to part 1: {}".format(game_state_easy.play())
    GameState.memo_cache.clear()
    GameState.best_min = float('inf')
    print "Answer to part 2: {}".format(game_state_hard.play())

if __name__ == "__main__":
    main()
