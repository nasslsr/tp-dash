
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

df_ratp = pd.read_csv('ratp.csv', sep=';')
df_ratp_sorted = df_ratp.sort_values(by=df_ratp.columns[3], ascending=False)
df_top_stations = df_ratp_sorted.head(10)
df_top_cities = df_ratp.groupby('Ville', as_index=False)['Trafic'].sum().nlargest(5, 'Trafic')

df_idf = pd.read_csv('idf.csv', sep=';')
df_exploitants = df_idf.groupby('exploitant', as_index=False)['nom_iv'].count()
df_ligne = df_idf.groupby('ligne', as_index=False)['nom_iv'].count()


df_idf[['latitude', 'longitude']] = df_idf['Geo Point'].str.split(',', expand=True)
df_idf['latitude'] = df_idf['latitude'].astype(float)
df_idf['longitude'] = df_idf['longitude'].astype(float)

stations = df_idf[['latitude', 'longitude', 'nom_long']]

couleurs = {
    'RER A': 'red',
    'RER B': 'blue',
    'RER C': 'yellow',
    'RER D': 'green',
    'RER E': 'pink',
    'METRO 1': '#FFCD00',
    'METRO 2': '#003CA6',
    'METRO 3': '#837902',
    'METRO 3bis': '#6EC4E8',
    'METRO 4': '#CF009E',
    'METRO 5': '#FF7E2E',
    'METRO 6': '#6ECA97',
    'METRO 7': '#FA9ABA',
    'METRO 7bis': '#6ECA97',
    'METRO 8': '#E19BDF',
    'METRO 9': '#B6BD00',
    'METRO 10': '#C9910D',
    'METRO 11': '#704B1C',
    'METRO 12': '#007852',
    'METRO 13': '#6E6E9C',
    'METRO 14': '#62259D',
    'TRAM 1': '#8CC63F',
    'TRAM 2': '#007852',
    'TRAM 3a': '#F5A81C',
    'TRAM 3b': '#F5A81C',
    'TRAM 4': '#0072C6',
    'TRAM 5': '#FDCB58',
    'TRAM 6': '#A9B7C1',
    'TRAM 7': '#6EC4E8',
    'TRAM 8': '#F15A24',
    'TRAM 9': '#339CFF',
    'TRAIN J': '#E74C3C',
    'TRAIN N': '#2980B9',
    'TRAIN L': '#2ECC71',
    'TRAIN K': '#8E44AD',
    'TRAIN U': '#F1C40F',
    'TRAIN H': '#34495E',
    'TRAIN P': '#E67E22',
    'Orlyval': '#7F8C8D'
}


app.layout = html.Div(children=[
    html.H1("RATP Analysis", style={
        'color': 'green',
        'font-size': '45px',
        'margin': 'auto',
        'text-align': 'center',
        'box-shadow': '2px 2px 5px grey',
        'border': '1px solid black',
        'font-family': 'Georgia, serif',
        'background-color': 'black',
        'padding': '10px'}),
    html.Br(),
    dcc.Dropdown(
        id='category-filter',
        options=[{'label': station, 'value': station} for station in df_top_stations['Station']],
        value=None,
        placeholder='Select the station'
    ),
    html.Div(children=[
        dcc.Graph(
            id='bar-chart1',
            figure=px.bar(df_top_stations, x='Station', y='Trafic', color_discrete_sequence=['#339CFF'],
                          title='Top 10 des stations avec le plus de trafic').update_layout(
                plot_bgcolor='white',
                xaxis_title_font=dict(size=25),
                yaxis_title_font=dict(size=25),
                xaxis_title_font_color='green',
                yaxis_title_font_color='green'
            )
        ),
        dcc.Graph(
            id='pie-chart',
            figure=px.pie(df_top_cities, names='Ville', values='Trafic',
                          title='Top 5 des villes avec le plus de trafic').update_layout(plot_bgcolor='white'

            ).update_traces(textposition='outside', hoverinfo='label+percent', textinfo='value', textfont_size=13,
                            marker=dict(colors=colors, line=dict(color='#000000', width=3))),
            style={'margin-top': '50px'}
        )
    ], style={'display': 'flex'
              })
])


if __name__ == '__main__':
    app.run_server(debug=True)
