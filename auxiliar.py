from math import sqrt
from random import randint
from time import sleep

# ATTRIBUTES
# name(name): character's name
# STRENGTH(strg)
# melee attack(mlAtk): attack made in close-quarter [range:0]
# block(blk): defense against melee attacks
# life(life): character's health. when its reach 0, is defeated
# AGILITY(agi)
# dodge(ddg): defense against ranged attacks
# ranged attack(rgAtk): attack made far away [range:1]
# speed(spd): how acts first in each round
# POWER(pwr)
# armor(arm): damage reduced by each attack
# damage(dmg): damage deal by each attack
# critical(crit): chance to double damage


class Fighter:
    def __init__(self, name, strg, agi, pwr, pos):
        self.name = name
        self.strg = strg
        self.agi = agi
        self.pwr = pwr
        self.life = (strg * 20) + 100
        self.ddg = int(agi * 2.5)
        self.blk = int(strg * 2.5)
        self.mlAtk = strg * 2
        self.rgAtk = agi * 2
        self.spd = agi * 2
        self.arm = int(pwr // 2)
        self.dmg = pwr * 3
        self.crit = int(pwr // 1.5)
        self.act = 0
        self.pos = pos
        self.atkroll = randint(1, 100)

    # chance to double damage
    def critical(self):
        chance = sqrt(sqrt(self.crit)) * 3.2
        if chance >= 50:
            chance = 50
        if self.atkroll >= 100 - chance:
            self.dmg *= 2
            return True
        return False

    # return attributes to basics
    def reroll(self):
        self.atkroll = randint(1, 100)
        self.mlAtk = self.strg * 2
        if self.name == 'Ban':
            self.mlAtk = self.strg * 4
        elif self.name == 'Meliodas':
            self.mlAtk = self.strg * 2.4
        elif self.name == 'Diane':
            self.mlAtk = self.strg * 3
        self.rgAtk = self.agi * 2
        if self.name == 'Escanor':
            self.rgAtk = self.strg * 1.5
        elif self.name == 'Merlin':
            self.rgAtk = self.pwr * 2
        self.dmg = randint(self.pwr * 3, self.pwr * 5)
        if self.name == 'Diane':
            self.dmg = randint(int(self.strg * 4.5), int(self.strg * 7.5))
        elif self.name == 'Meliodas':
            self.dmg = randint(self.pwr * 3.9, self.pwr * 6.5)
        self.spd = (self.agi * 2) + randint(1, 100)

    # chance to hit an attack
    def hitchance(self, defense, melee=True):
            atk = self.mlAtk
            if melee == False:
                atk = self.rgAtk
            hit = atk / defense
            if defense <= atk:
                res = 100 - (100 / hit * 2 ** (-hit))
                if res > 95:
                    res = 95
            else:
                hit = -(defense / atk)
                res = 100 / 2 ** (-hit)
                if res < 5:
                    res = 5
            return int(res)


def Action(p1: Fighter, p2: Fighter):
    # verify if player choose the Strong Strike
    if p1.act == 0:
        p1.mlAtk = int(p1.mlAtk - 0.2 * p1.mlAtk)
        p1.dmg = int(p1.dmg + 0.5 * p1.dmg)
        print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
        if p1.atkroll > 100 - p1.hitchance(p2.blk):
            if p1.critical():
                print('CRITICAL HIT!')
                print(f'{p1.name} hit a Strong Strike and dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            else:
                print(f'{p1.name} hit a Strong Strike and dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            sleep(1)
            print(f'{p2.name} current life is {p2.life}!')
            sleep(1)
        else:
            print(f'{p1.name} tried to hit {p2.name} that blocked!!')
            sleep(1)
    # verify if player choose the Fast Strike
    elif p1.act == 1:
        p1.mlAtk = int(p1.mlAtk + 0.5 * p1.mlAtk)
        p1.dmg = int(p1.dmg + 0.2 * p1.dmg)
        print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
        if p1.atkroll > 100 - p1.hitchance(p2.blk):
            if p1.critical():
                print('CRITICAL HIT!')
                print(f'{p1.name} hit a Fast Strike and dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            else:
                print(f'{p1.name} hit a Fast Strike and dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            sleep(1)
            print(f'{p2.name} current life is {p2.life}!')
            sleep(1)
        else:
            print(f'{p1.name} tried to hit {p2.name} that blocked!')
            sleep(1)
    # verify if player choose Shove
    elif p1.act == 2:
        p1.dmg = int(p1.dmg + 0.25 * p1.dmg)
        print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
        if p1.atkroll > 100 - p1.hitchance(p2.blk):
            player1.pos = 1
            print(f'Fighters are far apart.')
            if p1.critical():
                print('CRITICAL HIT!')
                print(f'{p1.name} hit a Shove that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))} '
                      f'and pushed {p2.name} away!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            else:
                print(f'{p1.name} hit a Shove that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))} '
                      f'and pushed {p2.name} away!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            sleep(1)
            print(f'{p2.name} current life is {p2.life}!')
            sleep(1)
        else:
            print(f'{p1.name} tried to push {p2.name} that blocked!!')
            sleep(1)
    # verify if player choose the Power Shot
    elif p1.act == 3:
        p1.rgAtk = int(p1.rgAtk - 0.2 * p1.rgAtk)
        p1.dmg = int(p1.dmg + 0.5 * p1.dmg)
        print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
        if p1.atkroll > 100 - p1.hitchance(p2.ddg, False):
            if p1.critical():
                print('CRITICAL HIT!')
                print(f'{p1.name} hit a Power Shot that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            else:
                print(f'{p1.name} hit a Power Shot that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            sleep(1)
            print(f'{p2.name} current life is {p2.life}!')
            sleep(1)
        else:
            print(f'{p1.name} tried to shot {p2.name} that dodged!')
            sleep(1)
    # verify if player choose the Sharp Shot
    elif p1.act == 4:
        p1.rgAtk = int(p1.rgAtk + 0.5 * p1.rgAtk)
        p1.dmg = int(p1.dmg - 0.2 * p1.dmg)
        print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
        if p1.atkroll > 100 - p1.hitchance(p2.ddg, False):
            if p1.critical():
                print('CRITICAL HIT!')
                print(f'{p1.name} hit a Sharp Shot that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            else:
                print(f'{p1.name} hit a Sharp Shot that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            sleep(1)
            print(f'{p2.name} current life is {p2.life}!')
            sleep(1)
        else:
            print(f'{p1.name} tried to hit {p2.name} that dodged!')
            sleep(1)
    # verify if player choose the Chain Hook
    elif p1.act == 5:
        p1.rgAtk = int(p1.rgAtk + 0.25 * p1.rgAtk)
        print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
        if p1.atkroll > 100 - p1.hitchance(p2.ddg, False):
            player1.pos = 0
            if p1.critical():
                print('CRITICAL HIT!')
                print(f'{p1.name} hit a Chain Hook that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))} '
                      f'and pulled {p2.name} closer!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            else:
                print(f'{p1.name} hit a Chain Hook that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))} '
                      f'and pulled {p2.name} closer!')
                p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
            sleep(1)
            print(f'{p2.name} current life is {p2.life}!')
            sleep(1)
        else:
            print(f'{p1.name} threw a hook on {p2.name} that dodged!!')
            sleep(1)
    # verify if player choose the Hit & Run
    elif p1.act == 6:
        p1.dmg = int(p1.dmg + 0.25 * p1.dmg)
        if player1.pos == 1:
            player1.pos = 0
            print(f'Fighters are in close-combat.')
            print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
            if p1.atkroll > 100 - p1.hitchance(p2.blk):
                if p1.critical():
                    print('CRITICAL HIT!')
                    print(f'{p1.name} move close, and hit a strike that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                    p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
                else:
                    print(f'{p1.name} move close, and hit a strike that dealt {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                    p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
                sleep(1)
                print(f'{p2.name} current life is {p2.life}!')
                sleep(1)
            else:
                print(f'{p1.name} move close and tried to hit {p2.name} that blocked!')
                sleep(1)
        elif player1.pos == 0:
            p1.rgAtk = int(p1.rgAtk + 0.25 * p1.rgAtk)
            player1.pos = 1
            print(f'Fighters are far apart.')
            print(f'Chance to hit: {p1.hitchance(p2.blk)}%, {p1.name}: {p1.mlAtk} vs {p2.name}: {p2.blk}')
            if p1.atkroll > 100 - p1.hitchance(p2.ddg, False):
                if p1.critical():
                    print('CRITICAL HIT!')
                    print(f'{p1.name} walked away and hit a shot that deals {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                    p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
                else:
                    print(f'{p1.name} walked away and hit a shot that deals {int(p1.dmg - (p1.dmg * (p2.arm / 100)))}!')
                    p2.life -= int(p1.dmg - (p1.dmg * (p2.arm / 100)))
                sleep(1)
                print(f'{p2.name} current life is {p2.life}!')
                sleep(1)
            else:
                print(f'{p1.name} walked away and shot {p2.name} that dodges!')
                sleep(1)
    return
