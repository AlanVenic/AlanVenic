from random import choice
from time import sleep
from auxiliar import Fighter, Action

meliodas = Fighter('Meliodas', 80, 60, 60, 1)
escanor = Fighter('Escanor', 95, 15, 80, 1)
king = Fighter('King', 5, 55, 90, 1)
ban = Fighter('Ban', 70, 30, 30, 1)
merlin = Fighter('Merlin', 10, 20, 90, 1)
diane = Fighter('Diane', 65, 15, 30, 1)

choiceP1 = int(input('[1]Meliodas: STRENGTH 80, AGILITY 60, POWER 60, LEVEL 10\n'
                     '[2]Escanor: STRENGTH 95, AGILITY 15, POWER 80, LEVEL 9\n'
                     '[3]King: STRENGTH 5, AGILITY 55, POWER 90, LEVEL 8\n'
                     '[4]Ban: STRENGTH 70, AGILITY 30, POWER 30, LEVEL 7\n'
                     '[5]Merlin: STRENGTH 10, AGILITY 20, POWER 90, LEVEL 6\n'
                     '[6]Diane: STRENGTH 65, AGILITY 15, POWER 30, LEVEL 5\n'
                     'Choose your champion: '))
if choiceP1 == 1:
    player1 = meliodas
    player1.dmg = int(player1.dmg * 1.3)
    player1.mlAtk = int(player1.mlAtk * 1.2)
elif choiceP1 == 2:
    player1 = escanor
    player1.rgAtk = player1.strg * 1.5
elif choiceP1 == 3:
    player1 = king
    player1.blk = player1.agi * 5
    player1.ddg = player1.agi * 5
elif choiceP1 == 4:
    player1 = ban
    player1.mlAtk = player1.strg * 4
    player1.life = player1.life * 2
elif choiceP1 == 5:
    player1 = merlin
    player1.arm = int(player1.pwr * 0.9)
    player1.rgAtk = player1.pwr * 2
else:
    player1 = diane
    player1.mlAtk = player1.strg * 3
    player1.dmg = player1.strg * 4.5

opponent = [1, 2, 3, 4, 5, 6]
opponent.remove(choiceP1)

sleep(1)
print('Your opponent is choosing his character...')
choiceP2 = choice(opponent)
if choiceP2 == 1:
    player2 = meliodas
    player2.dmg = int(player2.dmg * 1.3)
    player2.mlAtk = int(player2.mlAtk * 1.2)
elif choiceP2 == 2:
    player2 = escanor
    player2.rgAtk = player2.strg * 1.5
elif choiceP2 == 3:
    player2 = king
    player2.blk = player2.agi * 5
    player2.ddg = player2.agi * 5
elif choiceP2 == 4:
    player2 = ban
    player2.mlAtk = player1.strg * 4
    player2.life = player2.life * 2
elif choiceP2 == 5:
    player2 = merlin
    player2.arm = int(player2.pwr * 0.9)
    player2.rgAtk = int(player2.pwr * 2)
else:
    player2 = diane
    player2.mlAtk = player2.strg * 3
    player2.dmg = player2.strg * 4
sleep(1)
print('Your foe will be... ')
sleep(1)
print(f'{player2.name}!')

distance = player1.pos
print(f'{player1.name}: STRENGTH {player1.strg}, AGILITY {player1.agi}, POWER {player1.pwr}\n'
      f'melee attack: {player1.mlAtk:.0f}, block: {player1.blk}, life: {player1.life}\n'
      f'ranged attack: {player1.rgAtk:.0f}, speed: {player1.spd:.0f}, dodge: {player1.ddg}\n'
      f'critical: {player1.crit}%, damage: {player1.dmg}-{player1.dmg * 1.66:.0f}, armor: {player1.arm}%')
print()
print(f'{player2.name}: STRENGTH {player2.strg}, AGILITY {player2.agi}, POWER {player2.pwr}\n'
      f'melee attack: {player2.mlAtk:.0f}, block: {player2.blk}, life: {player2.life}\n'
      f'ranged attack: {player2.rgAtk:.0f}, speed: {player2.spd:.0f}, dodge: {player2.ddg}\n'
      f'critical: {player2.crit}%, damage: {player2.dmg}-{player2.dmg * 1.66:.0f}, armor: {player2.arm}%')
next = str(input('Go to battle? [Y/N] ')).upper()
if next == 'N':
    quit()
print('THE BATTLE WILL BEGIN!')

melee = (0, 0)
ranged = (0, 0)

if player2 == meliodas:
    melee = (0, 1, 2, 6)
    ranged = (3, 4, 5, 6)
elif player2 == escanor:
    melee = (0, 1, 2)
    ranged = (5, 6)
elif player2 == king:
    melee = (6, 6)
    ranged = (3, 4)
elif player2 == ban:
    melee = (0, 1, 2)
    ranged = (5, 6)
elif player2 == merlin:
    melee = (6, 6)
    ranged = (3, 4)
elif player2 == diane:
    melee = (0, 1, 2)
    ranged = (6, 6)
if player1.name == 'King' or player1.name == 'Merlin':
    melee = (0, 1, 2, 6)
    ranged = (3, 4, 5)
count = 0
action = 0

while player2.life > 0 and player1.life > 0 and action != 7:
    player1.reroll()
    player2.reroll()
    count += 1
    if player1.pos == 0:
        print(f'The fighters are in close-combat.')
    else:
        print(f'The fighters are far apart.')
    print(f'Round {count}, FIGHT!')
    print(f'Speeds {player1.name} = {player1.spd} VS {player2.name} = {player2.spd}')
    sleep(1)
    if player1.spd >= player2.spd:
        print(f'{player1.name} was faster!')
        sleep(1)
        while True:
            action = int(input('ACTIONS:\n'
                               '[0]Strong Strike(melee): -20% attack, +50% damage   '
                               '[4]Sharp Shot(ranged): +50% attack, -20% damage\n'
                               '[1]Fast Strike(melee): +50% attack, -20% damage     '
                               '[5]Chain Hook(ranged): +25% attack; pull enemy if hit\n'
                               '[2]Shove(melee): +24% damage; push enemy if hit     '
                               '[6]Hit & Run(melee/ranged): move close and strike (+25% damage) OR walk away and shot (+25% attack)\n'
                               '[3]Power Shot(ranged): -20% attack, +50% damage     [7]Quit Fight\n'
                               'Your action is? '))
            if player1.pos == 1 and action <= 2:
                print("You can't hit a enemy that is far away! Move closer or shot")
            elif player2.name == 'King' or player2.name == 'Merlin' and action == 6:
                print("You can't move closer to your enemy! He or she is flying!")
            elif action == 7:
                print('You quit the fight!')
                break
            elif player1.pos == 0:
                player1.act = action
                Action(player1, player2)
                break
            elif player1.pos == 1 and action >= 3:
                player1.act = action
                Action(player1, player2)
                break
        if player2.life <= 0:
            break
        print(f"Its {player2.name}'s turn!")
        if player1.pos == 0:
            player2.act = choice(melee)
            Action(player2, player1)
        else:
            player2.act = choice(ranged)
            Action(player2, player1)
        if player1.life <= 0:
            break
        print('The round is over!')
    else:
        print(f'{player2.name} was faster!')
        sleep(1)
        if player1.pos == 0:
            player2.act = choice(melee)
            Action(player2, player1)
        else:
            player2.act = choice(ranged)
            Action(player2, player1)
        if player1.life <= 0:
            break
        print(f"Now is {player1.name}'s turn!")
        while True:
            action = int(input('ACTIONS:\n'
                               '[0]Strong Strike(melee): -20% attack, +50% damage   '
                               '[4]Sharp Shot(ranged): +50% attack, -20% damage\n'
                               '[1]Fast Strike(melee): +50% attack, -20% damage     '
                               '[5]Chain Hook(ranged): +25% attack; pull enemy if hit\n'
                               '[2]Shove(melee): +24% damage; push enemy if hit     '
                               '[6]Hit & Run(melee/ranged): move close and strike (+25% damage) OR walk away and shot (+25% attack)\n'
                               '[3]Power Shot(ranged): -20% attack, +50% damage     [7]Quit Fight\n'
                               'Your action is? '))
            if player1.pos == 1 and action <= 2:
                print("You can't hit a enemy that is far away! Move closer or shot")
            elif player2.name == 'King' or player2.name == 'Merlin' and action == 6:
                print("You can't move closer to your enemy! He or she is flying!")
            elif action == 7:
                print('You quit the fight!')
                break
            elif player1.pos == 0:
                player1.act = action
                Action(player1, player2)
                break
            elif player1.pos == 1 and action >= 3:
                player1.act = action
                Action(player1, player2)
                break
        if player2.life <= 0:
            break
        print('The round is over!')
if player2.life <= 0:
    print('You win the duel!')
    print('GAME OVER!')
else:
    print(f'{player2.name} win the duel!')
    print('GAME OVER!')
