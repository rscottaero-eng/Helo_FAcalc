# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:54:43 2026

@author: berze
"""

import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, State, callback
import numpy as np
import pandas as pd

cFA_db_cols = ['Aircraft', 'Manufacturer', 'Price26', 'WE', 'SHP', 'Nbl', 'NMR', 'Neng', 'GasTurb', 'LG', 'Mil', 'Attack', 'UAS', 'PreProd', 'ScTerm', 'Piston', 'Single', 'LightTwin', 'MedTwin', 'Heavy', 'Military']

cFA_db = pd.DataFrame([
[              'R-22 Beta II',              'Robinson',  3.750000e+05,    882.000,    145.000000,  2.0,    0,   1.0,        0,   0,    0,       0,    0,        0,    94.682417,       1,        0,          0,        0,      0,         0],
[          'Guimbal Cabri G2',               'Guimbal',  4.500000e+05,    924.000,    145.000000,  3.0,    0,   1.0,        0,   0,    0,       0,    0,        0,    95.736971,       1,        0,          0,        0,      0,         0],
[                  'S-300CBi',             'Schweizer',  5.500000e+05,   1140.000,    190.000000,  3.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   118.044626,       1,        0,          0,        0,      0,         0],
[                    'S-300C',             'Schweizer',  6.200000e+05,   1150.000,    180.000000,  3.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   114.577172,       1,        0,          0,        0,      0,         0],
[                'R-44 Cadet',              'Robinson',  5.200000e+05,   1437.000,    260.000000,  2.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   150.086498,       1,        0,          0,        0,      0,         0],
[              'R-44 Raven I',              'Robinson',  5.535000e+05,   1452.000,    260.000000,  2.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   150.458041,       1,        0,          0,        0,      0,         0],
[             'R-44 Raven II',              'Robinson',  6.460000e+05,   1510.000,    260.000000,  2.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   151.867727,       1,        0,          0,        0,      0,         0],
[                     'F-28F',               'Enstrom',  4.660000e+05,   1640.000,    225.000000,  3.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   142.221646,       1,        0,          0,        0,      0,         0],
[                    '280 FX',               'Enstrom',  4.800000e+05,   1670.000,    225.000000,  3.0,    0,   1.0,        0,   0,    0,       0,    0,        0,   142.836810,       1,        0,          0,        0,      0,         0],
[     'R66 Turbine (Utility)',              'Robinson',  1.176000e+06,   1292.000,    300.000000,  2.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   159.222069,       0,        1,          0,        0,      0,         0],
[       'R66 NxG (Southwood)',              'Robinson',  1.456000e+06,   1385.000,    300.000000,  2.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   161.879080,       0,        1,          0,        0,      0,         0],
[                   'MD 520N',         'MD Helicopter',  2.552000e+06,   1585.000,    450.000000,  5.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   212.330504,       0,        1,          0,        0,      0,         0],
[                   'MD 500E',         'MD Helicopter',  2.445000e+06,   1657.000,    419.739842,  5.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   205.955006,       0,        1,          0,        0,      0,         0],
[                     'S-333',             'Schweizer',  1.800000e+06,   1140.000,    420.000000,  3.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   188.477753,       0,        1,          0,        0,      0,         0],
[                      '480B',              'Enstrom ',  1.470000e+06,   1693.000,    420.000000,  3.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   207.087357,       0,        1,          0,        0,      0,         0],
[                   'MD 530F',         'MD Helicopter',  2.500000e+06,   1723.000,    650.000000,  5.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   269.060790,       0,        1,          0,        0,      0,         0],
[              'HC50 - Fixed',                  'Hill',  1.459343e+06,   1874.000,    500.000000,  3.0,    0,   1.0,        1,   0,    0,       0,    0,        1,   235.138295,       0,        1,          0,        0,      0,         0],
[                   'MD 600N',         'MD Helicopter',  3.430000e+06,   1930.000,    650.000000,  6.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   276.427908,       0,        1,          0,        0,      0,         0],
[                  'Bell 505',                 ' Bell',  2.200000e+06,   2180.000,    475.000000,  2.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   236.495334,       0,        1,          0,        0,      0,         0],
[                      'H120',                'Airbus',  2.000000e+06,   2191.000,    504.000000,  3.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   245.202521,       0,        1,          0,        0,      0,         0],
[                   '407 GXi',                  'Bell',  3.430000e+06,   2700.000,    674.000000,  4.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   305.904958,       0,        1,          0,        0,      0,         0],
[                      'H125',                'Airbus',  3.283000e+06,   2812.000,    802.000000,  3.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   342.242832,       0,        1,          0,        0,      0,         0],
[                      'AW09',              'Leonardo',  3.900000e+06,   2866.000,   1006.000000,  5.0,    0,   1.0,        1,   0,    0,       0,    0,        1,   392.970680,       0,        1,          0,        0,      0,         0],
[          'H130 (EC-130 T2)',                'Airbus',  3.861000e+06,   3113.000,    801.000000,  3.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   350.372453,       0,        1,          0,        0,      0,         0],
[           'AW119 Kx (MKII)',              'Leonardo',  3.626000e+06,   3269.000,    917.258951,  4.0,    0,   1.0,        1,   0,    0,       0,    0,        0,   383.978220,       0,        1,          0,        0,      0,         0],
[                       'R88',              'Robinson',  3.300000e+06,   5000.000,    950.000000,  2.0,    0,   1.0,        1,   0,    0,       0,    0,        1,   433.743904,       0,        1,          0,        0,      0,         0],
[                     'K-MAX',                 'Kaman',  8.000000e+06,   5145.000,   1350.000000,  2.0,    1,   1.0,        1,   0,    0,       0,    0,        0,   537.294431,       0,        1,          0,        0,      0,         0],
[                 'H135 (P3)',                'Airbus',  7.298000e+06,   3267.000,   1334.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   478.847004,       0,        0,          1,        0,      0,         0],
[                 'H135 (T3)',                'Airbus',  7.163000e+06,   3267.000,   1320.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   475.876181,       0,        0,          1,        0,      0,         0],
[              '902 Explorer',         'MD Helicopter',  7.642000e+06,   3375.000,   1292.000000,  5.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   473.548314,       0,        0,          1,        0,      0,         0],
[             'AW109 Trekker',              'Leonardo',  6.950000e+06,   3523.613,   1470.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   516.281058,       0,        0,          1,        0,      0,         0],
[            'AW109 GrandNew',              'Leonardo',  7.800000e+06,   3648.613,   1470.000000,  4.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   520.584063,       0,        0,          1,        0,      0,         0],
[  'EC145T1(H145 Arriel 1E2)',                'Airbus',  6.564000e+06,   3951.000,   1416.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   518.962476,       0,        0,          1,        0,      0,         0],
[   'EC145T2(H145 Arriel 2E)',                'Airbus',  1.089700e+07,   4231.000,   1788.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   605.304841,       0,        0,          1,        0,      0,         0],
[      'H145M D3 (Arriel 2E)',                'Airbus',  1.089700e+07,   4177.717,   1788.000000,  5.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   603.481088,       0,        0,          1,        0,      0,         0],
[                  'Bell 429',                  'Bell',  6.150000e+06,   4486.000,   1196.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   484.183265,       0,        0,          1,        0,      0,         0],
[              'Bell 429 IGW',                  'Bell',  6.860000e+06,   4506.700,   1196.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   484.714285,       0,        0,          1,        0,      0,         0],
[              'Bell 429 WLG',                  'Bell',  7.350000e+06,   4751.000,   1196.000000,  4.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   490.845144,       0,        0,          1,        0,      0,         0],
[        'Bell 429 WLG (IGW)',                  'Bell',  7.350000e+06,   4771.700,   1196.000000,  4.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   491.353493,       0,        0,          1,        0,      0,         0],
[                      'H155',                'Airbus',  1.356900e+07,   5772.000,   1870.000000,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   669.232238,       0,        0,          0,        1,      0,         0],
[                     'AW169',              'Leonardo',  9.680000e+06,   5823.000,   1698.000000,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   633.531002,       0,        0,          0,        1,      0,         0],
[              'Bell 412 EPX',                  'Bell',  1.156400e+07,   6815.000,   1856.000000,  4.0,    0,   2.0,        1,   0,    0,       0,    0,        0,   693.150930,       0,        0,          0,        1,      0,         0],
[                    'S-76 D',              'Sikorsky',  1.330000e+07,   6963.000,   1606.000000,  4.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   639.713147,       0,        0,          0,        1,      0,         0],
[                     'AW139',              'Leonardo',  1.117200e+07,   7985.000,   2200.000000,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   795.739799,       0,        0,          0,        1,      0,         0],
[                      'H160',                'Airbus',  1.800000e+07,   8928.630,   2282.419203,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,   835.109102,       0,        0,          0,        1,      0,         0],
[                      'H215',                'Airbus',  1.890000e+07,   9942.746,   3639.533324,  4.0,    0,   2.0,        1,   1,    0,       0,    0,        0,  1128.257935,       0,        0,          0,        0,      1,         0],
[                      'H175',                'Airbus',  2.131900e+07,  10148.000,   3552.000000,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,  1117.595266,       0,        0,          0,        0,      1,         0],
[                     'AW189',              'Leonardo',  1.592500e+07,  10307.000,   3970.000000,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,  1197.826941,       0,        0,          0,        0,      1,         0],
[                     'AW149',              'Leonardo',  3.460800e+07,  10400.000,   3970.000000,  5.0,    0,   2.0,        1,   1,    1,       0,    0,        0,  1200.391480,       0,        0,          0,        0,      1,         0],
[                     'AW609',              'Leonardo',  3.000000e+07,  10505.000,   3880.000000,  3.0,    1,   2.0,        1,   1,    0,       0,    0,        1,  1187.099397,       0,        0,          0,        0,      1,         0],
[                      'H225',                'Airbus',  2.500000e+07,  11621.000,   4202.000000,  5.0,    0,   2.0,        1,   1,    0,       0,    0,        0,  1274.534096,       0,        0,          0,        0,      1,         0],
[                    'S-92A+',              'Sikorsky',  3.225000e+07,  15662.000,   5390.000000,  4.0,    0,   2.0,        1,   1,    0,       0,    0,        0,  1584.877782,       0,        0,          0,        0,      1,         0],
[                     'AW101',              'Leonardo',  5.340000e+07,  20502.000,   7581.000000,  5.0,    0,   3.0,        1,   1,    0,       0,    0,        0,  2066.453032,       0,        0,          0,        0,      1,         0],
[                    'UH-72A',                'Airbus',  7.808000e+06,   3951.000,   1416.000000,  4.0,    0,   2.0,        1,   0,    1,       0,    0,        0,   518.962476,       0,        0,          0,        0,      0,         1],
[                    'UH-72B',                'Airbus',  1.400000e+07,   4177.717,   1788.000000,  5.0,    0,   2.0,        1,   0,    1,       0,    0,        0,   603.481088,       0,        0,          0,        0,      0,         1],
[                      'OH-1',              'Kawasaki',  2.430000e+07,   5401.000,   1768.000000,  4.0,    0,   2.0,        1,   0,    1,       1,    0,        0,   637.291297,       0,        0,          0,        0,      0,         1],
[                     'AW159',              'Leonardo',  3.340000e+07,   7275.000,   2686.000000,  4.0,    0,   2.0,        1,   0,    1,       0,    0,        0,   875.538956,       0,        0,          0,        0,      0,         1],
[                     'LAH-1',                   'KAI',  2.360000e+07,   7496.000,   2048.000000,  5.0,    0,   2.0,        1,   0,    1,       1,    0,        0,   751.441586,       0,        0,          0,        0,      0,         1],
[                   'MH-139A',             'Leondardo',  2.624900e+07,   7985.000,   2200.000000,  5.0,    0,   2.0,        1,   1,    1,       0,    0,        0,   795.739799,       0,        0,          0,        0,      0,         1],
[               'Tiger (HAP)',                'Airbus',  3.492200e+07,   9259.000,   2570.000000,  4.0,    0,   2.0,        1,   0,    1,       1,    0,        0,   903.444904,       0,        0,          0,        0,      0,         1],
[               'Tiger (HAD)',                'Airbus',  4.604500e+07,   9590.000,   2934.000000,  4.0,    0,   2.0,        1,   0,    1,       1,    0,        0,   985.072493,       0,        0,          0,        0,      0,         1],
[                     'KUH-1',                   'KAI',  2.600000e+07,  11323.000,   3710.000000,  4.0,    0,   2.0,        1,   0,    1,       0,    0,        0,  1176.963124,       0,        0,          0,        0,      0,         1],
[                     'UH-1Y',                  'Bell',  2.753000e+07,  11840.000,   3780.000000,  4.0,    0,   2.0,        1,   0,    1,       0,    0,        0,  1202.730238,       0,        0,          0,        0,      0,         1],
[                     'AW249',              'Leonardo',  4.375300e+07,  12130.000,   5006.000000,  5.0,    0,   2.0,        1,   0,    1,       1,    0,        1,  1427.697427,       0,        0,          0,        0,      0,         1],
[                     'AH-1Z',                  'Bell',  3.434300e+07,  12300.000,   3780.000000,  4.0,    0,   2.0,        1,   0,    1,       1,    0,        0,  1213.694909,       0,        0,          0,        0,      0,         1],
[                    'AH-64E',                'Boeing',  3.240500e+07,  11400.000,   3988.000000,  4.0,    0,   2.0,        1,   0,    1,       1,    0,        0,  1230.198155,       0,        0,          0,        0,      0,         1],
[                    'UH-60M',              'Sikorsky',  2.566000e+07,  12500.000,   3988.000000,  4.0,    0,   2.0,        1,   0,    1,       0,    0,        0,  1257.477260,       0,        0,          0,        0,      0,         1],
[                'NH90 (TTH)',         'NH Industries',  3.798300e+07,  13126.000,   4776.000000,  4.0,    0,   2.0,        1,   1,    1,       0,    0,        0,  1414.968411,       0,        0,          0,        0,      0,         1],
[             'CH-47F Bk. II',                'Boeing',  5.713600e+07,  26300.000,   9554.000000,  3.0,    1,   2.0,        1,   0,    1,       0,    0,        0,  2513.259269,       0,        0,          0,        0,      0,         1],
[                    'MV-22B',         'Bell / Boeing',  8.488600e+07,  33140.000,  12300.000000,  3.0,    1,   2.0,        1,   1,    1,       0,    0,        0,  3082.221150,       0,        0,          0,        0,      0,         1],
[                    'CH-53K',              'Sikorsky',  1.273560e+08,  43878.000,  21996.000000,  7.0,    0,   3.0,        1,   1,    1,       0,    0,        0,  4642.980362,       0,        0,          0,        0,      0,         1],
[                     'MQ-8B',  'Schweizer / Sikorsky',  9.267000e+06,   2000.000,    420.000000,  4.0,    0,   1.0,        1,   0,    1,       0,    1,        0,   215.469258,       0,        0,          0,        0,      0,         0],
[                     'MQ-8C',             'Bell / NG',  1.820000e+07,   3200.000,    674.000000,  4.0,    0,   1.0,        1,   0,    1,       0,    1,        0,   318.533210,       0,        0,          0,        0,      0,         0]

], columns = cFA_db_cols)

#print(cFA_db)

Cost_LABEL  = 'Flyaway Price, USD (2026)'
WE_LABEL  = 'Empty Weight, lb'
ScT_LABEL  = 'WE<sup>0.4796</sup>SHP<sup>0.5649</sup>'
TITLE    = ''

def build_WE_figure():
    cFA_WE    = go.Figure()
    Piston     = cFA_db[cFA_db['Piston']==1]
    Single     = cFA_db[cFA_db['Single']==1]
    Light_Twin = cFA_db[cFA_db['LightTwin']==1]
    Med_Twin   = cFA_db[cFA_db['MedTwin']==1]
    Heavy      = cFA_db[cFA_db['Heavy']==1]
    Military   = cFA_db[cFA_db['Military']==1]
    UAS        = cFA_db[cFA_db['UAS']==1]
    
    piston_style        = dict(color='blue', size=9,  symbol='circle',
                           line=dict(color='black', width=0.8))
    
    cFA_WE.add_trace(go.Scatter(x=Piston['WE'], y=Piston['Price26'],  
                               mode='markers', name='Piston',
                               marker=piston_style))
    
    single_turb_style   = dict(color='red', size=9,  symbol='diamond',
                           line=dict(color='black', width=0.8))

    cFA_WE.add_trace(go.Scatter(x=Single['WE'], y=Single['Price26'],  
                               mode='markers', name='Single Turbine',
                               marker=single_turb_style))
    
    light_twin_style    = dict(color='green', size=9,  symbol='square',
                            line=dict(color='black', width=0.8))

    cFA_WE.add_trace(go.Scatter(x=Light_Twin['WE'], y=Light_Twin['Price26'],  
                               mode='markers', name='Light Twin',
                               marker=light_twin_style))
    
    med_twin_style      = dict(color='palegreen', size=9,  symbol='triangle-up',
                            line=dict(color='black', width=0.8))

    cFA_WE.add_trace(go.Scatter(x=Med_Twin['WE'], y=Med_Twin['Price26'],  
                               mode='markers', name='Medium Twin',
                               marker=med_twin_style))
    
    heavy_style    = dict(color='firebrick', size=9,  symbol='cross',
                            line=dict(color='black', width=0.8))

    cFA_WE.add_trace(go.Scatter(x=Heavy['WE'], y=Heavy['Price26'],  
                               mode='markers', name='Heavy Turbine',
                               marker=heavy_style))

    mil_style           = dict(color='darkgreen', size=9,  symbol='diamond-tall',
                            line=dict(color='black', width=0.8))

    cFA_WE.add_trace(go.Scatter(x=Military['WE'], y=Military['Price26'],  
                               mode='markers', name='Military',
                               marker=mil_style))

    UAS_style           = dict(color='purple', size=9,  symbol='x',
                            line=dict(color='purple', width=0.8))

    cFA_WE.add_trace(go.Scatter(x=UAS['WE'], y=UAS['Price26'],  
                               mode='markers', name='UAS',
                               marker=UAS_style))
    
    # -- Placeholder user point (keeps trace count stable across callbacks) --
    cFA_WE.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        name='User Point',
        marker=dict(color='gold', size=13, symbol='star',
                    line=dict(color='black', width=1.2)),
    ))
 
    cFA_WE.update_layout(
        xaxis=dict(type='log', title=WE_LABEL, showgrid=True,
                   gridcolor='#e5e7eb', minor=dict(showgrid=True)),
        yaxis=dict(type='log', title=Cost_LABEL, showgrid=True,
                   gridcolor='#e5e7eb', minor=dict(showgrid=True), minorloglabels='none'),
        legend=dict(bgcolor='white', bordercolor='#d1d5db', borderwidth=1),
        plot_bgcolor='#fafafa',
        paper_bgcolor='white',
        margin=dict(l=60, r=20, t=50, b=60),
        title=dict(text=TITLE, font=dict(size=15)),
    )

    return cFA_WE

WE_FIGURE = build_WE_figure()

def build_ATLAS_figure():
    cFA_Atlas = go.Figure()
    Piston     = cFA_db[cFA_db['Piston']==1]
    Single     = cFA_db[cFA_db['Single']==1]
    Light_Twin = cFA_db[cFA_db['LightTwin']==1]
    Med_Twin   = cFA_db[cFA_db['MedTwin']==1]
    Heavy      = cFA_db[cFA_db['Heavy']==1]
    Military   = cFA_db[cFA_db['Military']==1]
    UAS        = cFA_db[cFA_db['UAS']==1]



    piston_style        = dict(color='blue', size=9,  symbol='circle',
                           line=dict(color='black', width=0.8))
    

    cFA_Atlas.add_trace(go.Scatter(x=Piston['ScTerm'], y=Piston['Price26'],  
                               mode='markers', name='Piston',
                               marker=piston_style))

    single_turb_style   = dict(color='red', size=9,  symbol='diamond',
                           line=dict(color='black', width=0.8))

    cFA_Atlas.add_trace(go.Scatter(x=Single['ScTerm'], y=Single['Price26'],  
                               mode='markers', name='Single Turbine',
                               marker=single_turb_style))


    light_twin_style    = dict(color='green', size=9,  symbol='square',
                            line=dict(color='black', width=0.8))

    cFA_Atlas.add_trace(go.Scatter(x=Light_Twin['ScTerm'], y=Light_Twin['Price26'],  
                               mode='markers', name='Light Twin',
                               marker=light_twin_style))

    med_twin_style      = dict(color='palegreen', size=9,  symbol='triangle-up',
                            line=dict(color='black', width=0.8))

    cFA_Atlas.add_trace(go.Scatter(x=Med_Twin['ScTerm'], y=Med_Twin['Price26'],  
                               mode='markers', name='Medium Twin',
                               marker=med_twin_style))

    heavy_style    = dict(color='firebrick', size=9,  symbol='cross',
                            line=dict(color='black', width=0.8))

    cFA_Atlas.add_trace(go.Scatter(x=Heavy['ScTerm'], y=Heavy['Price26'],  
                               mode='markers', name='Heavy Turbine',
                               marker=heavy_style))

    mil_style           = dict(color='darkgreen', size=9,  symbol='diamond-tall',
                            line=dict(color='black', width=0.8))

    cFA_Atlas.add_trace(go.Scatter(x=Military['ScTerm'], y=Military['Price26'],  
                               mode='markers', name='Military',
                               marker=mil_style))

    UAS_style           = dict(color='purple', size=9,  symbol='x',
                            line=dict(color='purple', width=0.8))

    cFA_Atlas.add_trace(go.Scatter(x=UAS['ScTerm'], y=UAS['Price26'],  
                               mode='markers', name='UAS',
                               marker=UAS_style))

    # -- Placeholder user point (keeps trace count stable across callbacks) --
    cFA_Atlas.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        name='User Point',
        marker=dict(color='gold', size=13, symbol='star',
                    line=dict(color='black', width=1.2)),
    ))
 
    cFA_Atlas.update_layout(
        xaxis=dict(type='log', title=ScT_LABEL, showgrid=True,
                   gridcolor='#e5e7eb', minor=dict(showgrid=True), minorloglabels='none'),
        yaxis=dict(type='log', title=Cost_LABEL, showgrid=True,
                   gridcolor='#e5e7eb', minor=dict(showgrid=True), minorloglabels='none'),
        legend=dict(bgcolor='white', bordercolor='#d1d5db', borderwidth=1),
        plot_bgcolor='#fafafa',
        paper_bgcolor='white',
        margin=dict(l=60, r=20, t=50, b=60),
        title=dict(text=TITLE, font=dict(size=15)),
    )
    
    return cFA_Atlas
    
    
ATLAS_FIGURE = build_ATLAS_figure()

# =============================================================================
# STYLES
# =============================================================================
 
PANEL_STYLE   = {'width': '280px', 'flexShrink': '0', 'display': 'flex',
                 'flexDirection': 'column', 'gap': '14px'}
SECTION_STYLE = {'padding': '12px 14px', 'backgroundColor': '#f9fafb',
                 'border': '1px solid #e5e7eb', 'borderRadius': '8px'}
LABEL_STYLE   = {'fontSize': '12px', 'fontWeight': '600',
                 'color': '#374151', 'marginBottom': '5px', 'display': 'block'}
INPUT_STYLE   = {'width': '100%', 'fontSize': '13px', 'padding': '5px 8px',
                 'border': '1px solid #d1d5db', 'borderRadius': '5px',
                 'boxSizing': 'border-box'}
BTN_STYLE     = {'width': '100%', 'padding': '8px', 'fontSize': '13px',
                 'fontWeight': '600', 'backgroundColor': '#2563eb',
                 'color': 'white', 'border': 'none', 'borderRadius': '6px',
                 'cursor': 'pointer'}
 
def labeled_input(label, id_, placeholder, default, min_val=None, max_val=None, step=None):
    return html.Div([
        html.Label(label, style=LABEL_STYLE),
        dcc.Input(id=id_, type='number', placeholder=placeholder,
                  value=default, debounce=True, style=INPUT_STYLE,
                  min=min_val, max=max_val, step=step),
    ])

def labeled_slider(label, id_, min_val, max_val, default, step=1):
    return html.Div([
        html.Label(label, style=LABEL_STYLE),
        dcc.Slider(id=id_, min=min_val, max=max_val, step=step, value=default,
                   marks={i: str(i) for i in range(min_val, max_val + 1)},
                   tooltip={"placement": "bottom", "always_visible": True}),
    ], style={'marginBottom': '10px'})

def labeled_radio(label, id_, default_val):
    return html.Div([
        html.Label(label, style=LABEL_STYLE),
        dcc.RadioItems(
            id=id_, options=[
                {'label': ' Yes', 'value': 1},
                {'label': ' No', 'value': 0}
            ], value=default_val,
            inline=True,
            style={'fontSize': '13px', 'display': 'flex', 'gap': '15px'}
        ),
    ], style={'marginBottom': '8px'})
 
# =============================================================================
# APP LAYOUT
# =============================================================================
 
app = dash.Dash(__name__)
server = app.server   # expose for deployment (gunicorn, etc.)
 
app.layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '1200px',
           'margin': '30px auto', 'padding': '0 20px'},
    children=[
 
        html.H2(TITLE, style={'marginBottom': '20px', 'color': '#111827'}),
 
        html.Div(style={'display': 'flex', 'gap': '24px',
                        'alignItems': 'flex-start'}, children=[
 
            # ---- Side panel ----
            html.Div(style=PANEL_STYLE, children=[
 
                html.Div(style=SECTION_STYLE, children=[
                    html.P('CALCULATION INPUTS',
                           style={**LABEL_STYLE,
                                  'textTransform': 'uppercase',
                                  'letterSpacing': '0.06em',
                                  'color': '#6b7280',
                                  'marginBottom': '12px'}),
                    
                    # -- Number field inputs (x1, x2, x12) --
                    labeled_input('Weight Empty, lb. (range 800–45,000)', 'x1-input',
                                  'e.g. 5000', 800, min_val=800, max_val=45000),
                    html.Div(style={'marginTop': '10px'}),
                    labeled_input('Installed Power, hp (range 140–22,000)', 'x2-input',
                                  'e.g. 1000', 800, min_val=140, max_val=22000),
                    html.Div(style={'marginTop': '12px'}),
                    
                    # -- Sliders (x3, x4) --
                    labeled_slider('Blades per Main Rotor', 'x3-slider', 2, 7, 2, step=1),
                    labeled_slider('Number of Engines', 'x4-slider', 1, 4, 1, step=1),
                    
                    # -- Radio buttons (x5-x11) --
                    labeled_radio('Multirotor', 'x5-radio', 0),
                    labeled_radio('Turbine Engine', 'x6-radio', 0),
                    labeled_radio('Retractable Landing Gear', 'x7-radio', 0),
                    labeled_radio('Military Acquisition', 'x8-radio', 0),
                    labeled_radio('Attack Helicopter', 'x9-radio', 0),
                    labeled_radio('UAS', 'x10-radio', 0),
                    labeled_radio('Pre-Production Price', 'x11-radio', 0),
                    
                    html.Div(style={'marginTop': '10px'}),
                    labeled_input('Tech Factor (0.6–1.4)', 'x12-input',
                                  'e.g. 1.0', 1.0, min_val=0.6, max_val=1.4, step=0.01),
                    
                    html.Div(id='calculated-point-label',
                             style={'marginTop': '14px', 'fontSize': '12px',
                                    'color': '#374151', 'padding': '8px',
                                    'backgroundColor': '#f0fdf4',
                                    'border': '1px solid #bbf7d0',
                                    'borderRadius': '4px'}),
                    
                    html.Button('Clear All', id='clear-all-btn',
                                n_clicks=0,
                                style={**BTN_STYLE,
                                       'marginTop': '10px',
                                       'backgroundColor': '#6b7280',
                                       'fontSize': '12px'}),
                ]),
 
                # ---- Axis range overrides (optional) ----
                html.Div(style=SECTION_STYLE, children=[
                    html.P('AXIS RANGES  (optional)',
                           style={**LABEL_STYLE,
                                  'textTransform': 'uppercase',
                                  'letterSpacing': '0.06em',
                                  'color': '#6b7280',
                                  'marginBottom': '10px'}),
                    html.Label('X min / X max', style=LABEL_STYLE),
                    html.Div(style={'display': 'flex', 'gap': '8px'}, children=[
                        dcc.Input(id='xmin', type='number', placeholder='auto',
                                  debounce=True,
                                  style={**INPUT_STYLE, 'width': '50%'}),
                        dcc.Input(id='xmax', type='number', placeholder='auto',
                                  debounce=True,
                                  style={**INPUT_STYLE, 'width': '50%'}),
                    ]),
                    html.Div(style={'marginTop': '10px'}),
                    html.Label('Y min / Y max', style=LABEL_STYLE),
                    html.Div(style={'display': 'flex', 'gap': '8px'}, children=[
                        dcc.Input(id='ymin', type='number', placeholder='auto',
                                  debounce=True,
                                  style={**INPUT_STYLE, 'width': '50%'}),
                        dcc.Input(id='ymax', type='number', placeholder='auto',
                                  debounce=True,
                                  style={**INPUT_STYLE, 'width': '50%'}),
                    ]),
                ]),
            ]),
 
            # ---- Graph ----
            html.Div(style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 
                           'gap': '20px'}, children=[
                html.Div([
                    html.H3('', style={'marginBottom': '10px', 'fontSize': '14px', 'color': '#374151'}),
                    dcc.Graph(id='fig1-graph', figure=WE_FIGURE,
                              style={'height': '600px'}),
                ]),
                html.Div([
                    html.H3('', style={'marginBottom': '10px', 'fontSize': '14px', 'color': '#374151'}),
                    dcc.Graph(id='fig2-graph', figure=ATLAS_FIGURE,
                              style={'height': '600px'}),
                ]),
            ]),
        ]),
    ]
)
 
# =============================================================================
# CALLBACKS
# =============================================================================
# -- Enforce x8 dependency: x8 must be 1 if x9 or x10 is 1 --
@callback(
    Output('x8-radio', 'value'),
    Input('x9-radio', 'value'),
    Input('x10-radio', 'value'),
    Input('x8-radio', 'value'),
    prevent_initial_call=True,
)
def enforce_x8_dependency(x9, x10, x8):
    """Force x8 to 1 if x9 or x10 is 1; otherwise keep x8's current value."""
    # If either x9 or x10 is 1, force x8 to 1
    if x9 == 1 or x10 == 1:
        return 1
    # Otherwise, keep whatever x8 is currently set to
    return x8

 
@callback(
    Output('fig1-graph', 'figure'),
    Output('fig2-graph', 'figure'),
    Output('calculated-point-label', 'children'),
    Input('x1-input', 'value'),
    Input('x2-input', 'value'),
    Input('x3-slider', 'value'),
    Input('x4-slider', 'value'),
    Input('x5-radio', 'value'),
    Input('x6-radio', 'value'),
    Input('x7-radio', 'value'),
    Input('x8-radio', 'value'),
    Input('x9-radio', 'value'),
    Input('x10-radio', 'value'),
    Input('x11-radio', 'value'),
    Input('x12-input', 'value'),
    Input('clear-all-btn', 'n_clicks'),
    Input('xmin', 'value'),
    Input('xmax', 'value'),
    Input('ymin', 'value'),
    Input('ymax', 'value'),
    State('fig1-graph', 'figure'),
    State('fig2-graph', 'figure'),
    prevent_initial_call=True,
)
def update_graph(WE, SHP, Nbl, Neng, kMR, kTurb, kLG, kMil, kAttack, kUAS, kPreP, tech,
                 clear_clicks, xmin, xmax, ymin, ymax, current_fig1, current_fig2):
 
    from dash import ctx
    triggered = ctx.triggered_id
 
    fig1 = go.Figure(current_fig1)
    fig2 = go.Figure(current_fig2)
 
    # Always re-apply log scale
    x_range = ([np.log10(xmin), np.log10(xmax)]
               if (xmin and xmax and xmin > 0 and xmax > 0) else None)
    y_range = ([np.log10(ymin), np.log10(ymax)]
               if (ymin and ymax and ymin > 0 and ymax > 0) else None)
 
    fig1.update_layout(
        xaxis=dict(type='log', range=x_range),
        yaxis=dict(type='log', range=y_range),
    )
    
    fig2.update_layout(
        xaxis=dict(type='log', range=x_range),
        yaxis=dict(type='log', range=y_range),
    )
 
    # The user-point is always the last trace
    point_msg = ''
    
    if triggered == 'clear-all-btn':
        # Clear the point
        fig1.data[-1].x = [None]
        fig1.data[-1].y = [None]
        fig2.data[-1].x = [None]
        fig2.data[-1].y = [None]
        point_msg = ''
    else:
        # Calculate X and Y from the inputs
        # X = x1 (the first input field)
        # Y = sum of x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12
        
        if WE is not None and SHP is not None and tech is not None:
            # Ensure all radio button values are set (default to 0 if None)
            kMR_val     = kMR if kMR is not None else 0
            kTurb_val   = kTurb if kTurb is not None else 0
            kLG_val     = kLG if kLG is not None else 0
            kMil_val    = kMil if kMil is not None else 0
            kAttack_val = kAttack if kAttack is not None else 0
            kUAS_val    = kUAS if kUAS is not None else 0
            kPreP_val   = kPreP if kPreP is not None else 0
            Neng_val    = Neng if Neng is not None else 2
            Nbl_val     = Nbl if Nbl is not None else 1
            
            # Calculate X and Y
            
            x_coord2 = WE**.238096 * SHP**0.589888
            #y_coord = x1 + x2 + x3_val + x4_val + x5_val + x6_val + x7_val + x8_val + x9_val + x10_val + x11_val + x12
            y_coord2 = tech * np.exp(8.063375) * x_coord2 * Nbl**0.25923 * Neng**0.548174 * np.exp(kMR_val*0.369341) * np.exp(kTurb_val*0.803768) \
                * np.exp(kLG_val*0.1378) * np.exp(kMil_val*0.369421) * np.exp(kAttack_val*0.45207) * np.exp(kUAS_val*1.215252) * np.exp(kPreP_val*-0.13344) 
            
            x_coord1 = WE
            y_coord1 =  tech * np.exp(8.063375) * x_coord2 * Nbl**0.25923 * Neng**0.548174 * np.exp(kMR_val*0.369341) * np.exp(kTurb_val*0.803768) \
                * np.exp(kLG_val*0.1378) * np.exp(kMil_val*0.369421) * np.exp(kAttack_val*0.45207) * np.exp(kUAS_val*1.215252) * np.exp(kPreP_val*-0.13344) 
            
            if x_coord1 > 0 and y_coord1 > 0:
                fig1.data[-1].x = [x_coord1]
                fig1.data[-1].y = [y_coord1]
                
            if x_coord2 > 0 and y_coord2 > 0:
                fig2.data[-1].x = [x_coord2]
                fig2.data[-1].y = [y_coord2]

                point_msg = html.Div([
                    html.Div(f'Weight Empty, lb: {x_coord2:,.2f}', style={'marginBottom': '4px', 'fontWeight': '600'}),
                    html.Div(f'Est. FLyaway Price: {y_coord2:,.0f}', style={'marginBottom': '4px', 'fontWeight': '600'}),
                    html.Div('(Automatically calculated)', style={'fontSize': '11px', 'color': '#059669', 'marginTop': '4px'}),
                ])
            else:
                point_msg = '⚠ Values must result in positive coordinates.'
        else:
            point_msg = '⚠ Fill in all required fields.'
 
    return fig1, fig2, point_msg
 
 
if __name__ == '__main__':
    app.run(debug=True)