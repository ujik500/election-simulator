import random
import os

#https://github.com/JonathanBaby/python_svg_batch_tools/blob/master/svg_style_updater.py

# fields "State Abbreviation": (EV Count, Chance of D Victory)
states_dict = {
"CA": [54, 0.99],
"TX": [40, 0.2],
"FL": [30, 0.15],
"NY": [28, 0.97],
"PA": [19, 0.6],
"IL": [19, 0.97],
"OH": [17, 0.1],
"GA": [16, 0.45],
"NC": [16, 0.35],
"MI": [15, 0.6],
"NJ": [14, 0.91],
"VA": [13, 0.76],
"WA": [12, 0.95],
"IN": [11, 0.03],
"TN": [11, 0.02],
"MA": [11, 0.99],
"AZ": [11, 0.6],
"CO": [10, 0.91],
"MO": [10, 0.06],
"MD": [10, 0.99],
"WI": [10, 0.55],
"MN": [10, 0.78],
"AL": [9, 0.01],
"SC": [9, 0.04],
"OR": [8, 0.94],
"LA": [8, 0.04],
"KY": [8, 0.02],
"OK": [7, 0.01],
"CT": [7, 0.93],
"NV": [6, 0.5],
"UT": [6, 0.05],
"MS": [6, 0.04],
"KS": [6, 0.06],
"AR": [6, 0.01],
"IA": [6, 0.12],
"NM": [5, 0.89],
"NE-AL": [2, 0.04],
"NE-1": [1, 0.06],
"NE-2": [1, 0.79],
"NE-3": [1, 0.01],
"ID": [4, 0.02],
"MT": [4, 0.06],
"HI": [4, 0.99],
"RI": [4, 0.95],
"WV": [4, 0.01],
"NH": [4, 0.87],
"ME-AL": [2, 0.93],
"ME-1": [1, 0.95],
"ME-2": [1, 0.26],
"AK": [3, 0.2],
"WY": [3, 0.01],
"ND": [3, 0.01],
"SD": [3, 0.02],
"DE": [3, 0.94],
"VT": [3, 0.97],
"DC": [3, 0.999]
}

def run_simulation(states_dct):
    dem_evs = 0
    rep_evs = 0
    for state in states_dct:
        seed = random.randint(0, 100) / 100
        if seed >= states_dct[state][1]:
            rep_evs += states_dct[state][0]
            #print("Republicans just won", state)
        else:
            dem_evs += states_dct[state][0]
            #print("Democrats just won", state)
        #print(str(dem_evs) + "D - " + str(rep_evs) + "R")
    if dem_evs > rep_evs:
        print("Democrats won this time")
    elif rep_evs > dem_evs:
        print("Republicans won this time")
    else:
        print("It's an electoral college tie. Up to the House to decide...")
    return (dem_evs, rep_evs)

def run_many_simulations(states_dct, num_iterations):
    dem_wins = 0
    rep_wins = 0
    ties = 0
    for i in range(num_iterations):
        dem_evs, rep_evs = run_simulation(states_dct)
        print(f'{dem_evs}D - {rep_evs}R')
        if dem_evs > rep_evs:
            dem_wins += 1
        elif rep_evs > dem_evs:
            rep_wins += 1
        else:
            ties += 1
        print()
    print("Democrats won", dem_wins, "times", "(" + str(round(100* dem_wins/num_iterations, 3)) + "% of simulations)")
    print("Republicans won", rep_wins, "times", "(" + str(round(100* rep_wins/num_iterations, 3)) + "% of simulations)")
    print("The Electoral College was tied", ties, "times", "(" + str(round(100* ties/num_iterations, 3)) + "% of simulations)")

run_many_simulations(states_dict, 1170)

#run_simulation(states_dict)

os.startfile("usa-presidential-2024-blank.svg")
#os.startfile("usa-presidential-2024-takeall.svg")