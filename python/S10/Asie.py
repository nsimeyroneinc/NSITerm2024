arbre1={'etiquette' :'Conjonctivie jaune',
    'sag':{'etiquette' :'hypercaroténémie',
        'sag':{},
        'sad':{}
          },
    'sad' : {'etiquette' : 'bilirubine',
            'sag' : {'etiquette' : 'spiénomégalie',
               'sag' : {'etiquette' : 'maladie de Gilbert par défaut de glycuro-conjugaison',
                    'sag' : {},
                    'sad' : {}}
                    },
               'sad' : {'etiquette' : 'anémie hémolytique',
                    'sag' : {},
                    'sad' : {}
                    }
                },
            'sad' : {'etiquette' : 'hépatomégalie',
                'sag' : {'etiquette' : 'hépatie',
                    'sag' : {},
                    'sad' : {}
                        },
                'sad' : { 'etiquette' : 'douleur et fièvre',
                    'sag' : {'etiquette' : 'cancer de la tête du pancréas',
                        'sag' : {},
                        'sad' : {}
                            }
                        },
                    'sad' : {'etiquette' : 'lithiase du cholédoque',
                        'sag' : {},
                        'sad' : {}
                            }
                    }
            }



# Printing the tree in a pre-order way.
arbre3={'etiquette' :'a',
            'sag':{ 'etiquette' :'b',
                'sag': {'etiquette' : 'd',
                    'sag' : {},
                    'sad' : {}},
                'sad' : { }},
            'sad': {'etiquette' :'f',
                'sag' : {'etiquette' : 'g',
                    'sag' : {},
                    'sad' : {}},
                'sad' : {} }}

def parcours(arb):
    if arb == {}:
        return None
    parcours(arb['sag'])
    parcours(arb['sad'])
    print(arb['etiquette'])

def parcours_maladies(arb): 
        if arb=={}: 
            return None 
        parcours_maladies (arb['sag']) 
        parcours_maladies (arb['sad']) 
        if arb['sag'] == {} and arb['sad'] == {}: 
            print(arb['etiquette'])


arb_decision={'etiquette' :'Conjonctivie jaune',
    'surChemin': False ,
    'sag':{'etiquette' :'hypercaroténémie',
        'surChemin': False ,
        'sag':{},
        'sad':{}
          },
    'sad' : {'etiquette' : 'bilirubine',
        'surChemin': False ,
            'sag' : {'etiquette' : 'spiénomégalie',
                'surChemin': False ,
               'sag' : {'etiquette' : 'maladie de Gilbert par défaut de glycuro-conjugaison',
                   'surChemin': False ,
                    'sag' : {},
                    'sad' : {}}
                    },
               'sad' : {'etiquette' : 'anémie hémolytique',
                    'surChemin': False ,
                    'sag' : {},
                    'sad' : {}
                    }
                },
            'sad' : {'etiquette' : 'hépatomégalie',
                'surChemin': False ,
                'sag' : {'etiquette' : 'hépatie',
                    'surChemin': False ,
                    'sag' : {},
                    'sad' : {}
                        },
                'sad' : { 'etiquette' : 'douleur et fièvre',
                    'surChemin': False ,
                    'sag' : {'etiquette' : 'cancer de la tête du pancréas',
                        'surChemin': False ,
                        'sag' : {},
                        'sad' : {}
                            }
                        },
                    'sad' : {'etiquette' : 'lithiase du cholédoque',
                    'surChemin': False ,
                        'sag' : {},
                        'sad' : {}
                            }
                    }
            }



def symptomes(arb, mal): 
    if arb['sag'] != {}: 
        symptomes(arb['sag'], mal) 

    if arb['sad'] != {}: 
        symptomes(arb['sad'], mal) 

    if arb['etiquette'] == mal: 
        arb['surChemin'] = True 
        print('symptômes de', arb['etiquette'],':') 

    else : 
        if arb['sad'] != {} and arb['sad']['surChemin']: 
            print(arb['etiquette']) 
            arb['surChemin'] = True 

        if arb['sag'] != {} and arb['sag']['surChemin']: 
            print('pas de ',arb['etiquette']) 
            arb['surChemin'] = True

#print(arb_decision)
#parcours(arbre1)
#parcours_maladies(arbre1)
symptomes(arb_decision, 'anémie hémolytique')