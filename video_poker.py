#!/usr/bin/env python
import random
import pandas as pd
import sys


deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
len(deck)

def argent():
    print("Combien veux mettre dans ta bankroll?")
    bankroll = int(input())
    print("Tu as", bankroll, "$ dans ta bankroll")
    print("combien veux tu miser?")
    mise = int(input())
    if mise <= bankroll:
        print("Tu as miser",mise,"$")
        bankroll = bankroll - mise
    else:
        print("Tu ne peux pas miser plus que ta Bankroll !")
        sys.exit(0);
    return bankroll, mise


"""
def mise_depart(mise):
    bankroll = input()
    if bankroll <= mise:
        print("Merci et Bonne chance")
    else:
        print("Vous ne pouvez pas miser plus que",mise,"$")

"""

def premier_tirage(deck):
    tirage = random.sample(deck, 5)
    for i in tirage:
        deck.remove(i)
    return tirage, deck



def choix_cartes(tirage):
    print(tirage)
    jeu = []
    for i in tirage:
        print(i)
        choix = input('Voulez vous garder la carte y/n:')
        if choix == 'y':
            jeu.append(i)
    return jeu



def deuxieme_tirage(jeu, deck):
    nb_carte = len(jeu)
    reste = 5 - nb_carte
    tirage_2 = random.sample(deck, reste)
    for i in tirage_2:
        jeu.append(i)
    return jeu



"""
def machine():
    deck = ['2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h', 'J-h', 'Q-h', 'K-h', 'A-h', '2-d', '3-d',
            '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d', 'J-d', 'Q-d', 'K-d', 'A-d', '2-c', '3-c', '4-c', '5-c',
            '6-c', '7-c', '8-c', '9-c', '10-c', 'J-c', 'Q-c', 'K-c', 'A-c', '2-s', '3-s', '4-s', '5-s', '6-s', '7-s',
            '8-s', '9-s', '10-s', 'J-s', 'Q-s', 'K-s', 'A-s']
    tirage1, deck = premier_tirage(deck)
    print(tirage1)
    jeu = choix_cartes(tirage1)
    tirage_final = deuxieme_tirage(jeu, deck)
    print(tirage_final)
    return tirage_final

tirage_finale = machine()
"""

def decompose_jeu(jeu):
        dic = {}
        keys = [1,2,3,4,5]
        valeur = []
        couleur = []
        for i,k in zip(jeu, keys):
            dic[k] = i.split('-')
        for key in dic.keys():
            valeur.append(dic[key][0])
            couleur.append(dic[key][1])
        return valeur, couleur



def convert_carte(valeur):
    for e,i in zip(valeur, range(0,5)):
        try:
            valeur[i] = int(e)
        except:
            if e == 'J':
                valeur[i] = 11
            elif e == 'Q':
                valeur[i] = 12
            elif e == 'K':
                valeur[i] = 13
            elif e == 'A':
                valeur[i] = 1
            else:
                continue
    return valeur



#9
def quinte_flush_royal(jeu):
    valeur_gagnante = ['10','J','Q','K','A']
    """valeur_gagnante = decompose_jeu(tirage)"""
    valeur, couleur = decompose_jeu(jeu)
    if sorted(valeur_gagnante) == sorted(valeur) and couleur.count(couleur[0]) == 5:
        print("GG")
        return True
    else:
        #print("Pas de quinte_flush_royal")
        print("------------------------")
        return False



#8
def quinte_flush(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('true')
    if suite.count('True') ==  4 and couleur.count(couleur[0]) == 5:
        return True
    else:
        #print("Pas de quinte_flush")
        print("------------------------")
        return False



#7
def carre(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [1, 4]:
        return True
    else:
        #print("Pas de Carré")
        print("------------------------")
        return False



#6
def full(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 2 and sorted(count) == [2, 3]:
        return True
    else:
        #print("pas de full")
        print("------------------------")
        return False



#5
def flush(jeu):
    valeur, couleur = decompose_jeu(jeu)
    if couleur.count(couleur[0]) == 5:
        return True
    else:
        #print("Pas de flush")
        print("------------------------")
        return False




#1
def pair(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
        return True
    else:
        #print("pas de pair")
        print("------------------------")
        return False



#2
def double_pair(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 4 and sorted(count) == [1, 2, 2]:
        return True
    else:
        #print("pas de double_pair")
        print("------------------------")
        return False



#3
def brelan(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur1 = pd.Series(valeur)
    uniques = valeur1.unique()
    count = []
    for i in uniques:
        count.append(valeur.count(i))
    if len(uniques) == 3 and sorted(count) == [1, 1, 3]:
        return True
    else:
        #print("pas de brelan")
        print("------------------------")
        return False


#4
def quinte(jeu):
    valeur, couleur = decompose_jeu(jeu)
    valeur = convert_carte(valeur)
    valeur = sorted(valeur)
    suite = []
    for e, i in zip(valeur[0:-1], range(len(valeur)-1)):
        if e+1 == valeur[i+1]:
            suite.append('true')
    if suite.count('True') ==  4 :
        return True
    else:
        #print("Pas de quinte")
        print("------------------------")
        return False



"""
def pair(tirage):
    nb_carte = []
    valeur, couleur = decompose_jeu(tirage)
    for i in set(valeur):
        nb_carte.append(valeur.count(i))
        nb_carte2=len(nb_carte)
    if 3 < nb_carte2 < 5:
        #mise = mise * 2
        return True
        print("Tu as une pair")
    else:
        #print("Tu n'a pas de pair")
        print("------------------------")
        return False

pair(tirage)

def double_pair(tirage):
    nb_carte = []
    valeur, couleur = decompose_jeu(tirage)
    for i in set(valeur):
        nb_carte.append(valeur.count(i))
        nb_carte2=len(nb_carte)
    if 1 < nb_carte2 < 4:
        #print("Tu as une double pair")
        #mise == mise * 2
        return True
    else:
        #print("Tu n'a pas de double pair")
        print("------------------------")

double_pair(tirage)
"""

def mise_final(mise):
    misef = 0
    if pair(jeu) == True:
        misef = mise * 1
        print("Tu as une pair, tu as maintenant", misef,"$")
    elif double_pair(jeu) == True:
        misef = mise * 2
        print("Tu as double pair, tu as maintenant",misef,"$")
    elif brelan(jeu) == True:
        misef = mise * 3
        print("Tu as un brelan, tu as maintenant",misef,"$")
    elif quinte(jeu) == True:
        misef = mise * 4
        print("Tu as une quinte, tu as maintenant",misef,"$")
    elif flush(jeu) == True:
        misef = mise * 6
        print("Tu as une flush, tu as maintenant",misef,"$")
    elif full(jeu) == True:
        misef = mise * 9
        print("Tu as un full, tu as maintenant",misef,"$")
    elif carre(jeu) == True:
        misef = mise * 25
        print("Tu as un carre, tu as maintenant",misef,"$")
    elif quinte_flush(jeu) == True:
        misef = mise * 50
        print("Tu as une quinte_flush, tu as maintenant",misef,"$")
    elif quinte_flush_royal(jeu) == True:
        misef = mise * 250
        print("Tu as une quinte_flush_royal, tu as maintenant",misef,"$")
    return misef


def bankroll_final(misef, bankroll):
    bankroll = bankroll + misef
    print("Ta bankroll est maintenant égale à",bankroll,"$")
    print("Voulez vous rejouer? yes/no")
    reponse = input()
    if reponse == 'y':
        print("On relance le jeu")
    elif reponse == 'n':
        print("Vous repartez avec",bankroll,"$ Merci et Bonne journée!")
        sys.exit(0);
    return bankroll

print("Voulez vous jouer? yes/no")
reponse = input()

def mise_suivante(bankroll):
    print("Tu as", bankroll, "$ dans ta bankroll")
    print("combien veux tu miser?")
    mise = int(input())
    if mise <= bankroll:
        print("Tu as miser", mise, "$")
        bankroll = bankroll - mise
    else:
        print("Tu ne peux pas miser plus que ta Bankroll !")
        sys.exit(0);
    return bankroll, mise


bankroll, mise = argent()
while reponse == 'y':
    tirage, deck = premier_tirage(deck)
    jeu = choix_cartes(tirage)
    jeu = deuxieme_tirage(jeu, deck)
    print(jeu)
    valeur, couleur = decompose_jeu(jeu)
    convert_carte(valeur)
    quinte_flush_royal(jeu)
    quinte_flush(jeu)
    carre(jeu)
    full(tirage)
    flush(tirage)
    pair(jeu)
    double_pair(jeu)
    brelan(jeu)
    quinte(jeu)
    misef = mise_final(mise)
    print(misef)
    bankroll = bankroll_final(misef, bankroll)
    bankroll, mise = mise_suivante(bankroll)




"""
def pair(tirage):
    nb_carte = []
    valeur, couleur = decompose_jeu(tirage)
    i=0
    if i=0
        set(valeur)
        nb_cart.append(valeur.count(i))
    return True
"""


