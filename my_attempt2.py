# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:54:43 2026

@author: berze
"""

import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output, State, callback, html
import numpy as np

exec(open('cFA_hardcode_data.py').read())

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
    app.run(debug=False, host="0.0.0.0")