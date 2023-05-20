import os
import plotly.express as px  # interactive charts
import plotly.graph_objects as go
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import numpy as np
from random import randint
import streamlit_authenticator as stauth

MONGO_URL=os.getenv("MONGO_URL")
MONGO_DB=os.getenv("MONGO_DB")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# user authentication pass abc123, def456
# Database connection
config = {
    'credentials': {
        'usernames': {
            'pparker': {
                'email': 'pparker@mail.com',
                'name': 'Peter Parker',
                'password': '$2b$12$Z4FkfLLsQV2hP8GMvR9hDumpApg8mmSQZClwbKdbfsF9CHh.8Nsv.'
            },
            'rmiller': {
                'email': 'rmiller@mail.com',
                'name': 'Rebecca Miller',
                'password': '$2b$12$woA3HzlJclJoHqEOe1sL/OMxet9Tf4hvMoujxnnYebXSMZq9zEXVm'
            }
        }
    },
    'cookie': {
        'expiry_days': 30,
        'key': 'abcdef',
        'name': 'dashboard_estado_fijo'
    }
}
authenticator = stauth.Authenticate(config['credentials'],
                                    config['cookie']['name'],
                                    config['cookie']['key'],
                                    config['cookie']['expiry_days'])
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.error("Please enter your username and password")
if authentication_status:

    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.sidebar.success("Starplastic")

    # Update tables on frontend
    st.markdown(f'### Estado actual de las Máquinas (Actualización: XXXXXXX)')
    # create three columns
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    style_metric_cards(border_left_color="#1E1E1E")
    # colores labels metric: blue, green, orange, red, violet

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label=":gear: :green[MÁQUINA001]", 
        value="OK",
        delta="5 horas activas"
    )

    # color_discrete_sequence=px.colors.sequential.Peach
    # color_discrete_sequence=px.colors.sequential.Darkmint (verde)
    data = [('Producido', randint(100, 1000)),
            ('Por producir', randint(100, 1000))]
    df = pd.DataFrame(data, columns=['product', 'quantity'])
    fig = px.pie(df, values='quantity', names='product', hole=.4,
                color_discrete_sequence=px.colors.sequential.Darkmint)
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    fig.update_layout(showlegend=False)
    kpi1.plotly_chart(fig, theme="streamlit", use_container_width=True)

    kpi1.info("Órden 345 (35%)")
    # kpi1.success("Máquina001 OK (5 horas activas)")
    kpi2.metric(
        label=":no_entry: :red[MÁQUINA002]", 
        value="OFF",
        delta="-5 minutos parada"
    )
    data = [('Producido', randint(100, 1000)),
            ('Por producir', randint(100, 1000))]
    df = pd.DataFrame(data, columns=['product', 'quantity'])
    fig = px.pie(df, values='quantity', names='product', hole=.4,
                color_discrete_sequence=px.colors.sequential.Peach)
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    fig.update_layout(showlegend=False)
    kpi2.plotly_chart(fig, theme="streamlit", use_container_width=True)

    kpi3.metric(
        label=":gear: :green[MÁQUINA003]", 
        value="ON",
        delta="3 horas activas"
    )
    data = [('Producido', randint(100, 1000)),
            ('Por producir', randint(100, 1000))]
    df = pd.DataFrame(data, columns=['product', 'quantity'])
    fig = px.pie(df, values='quantity', names='product', hole=.4,
                color_discrete_sequence=px.colors.sequential.Darkmint)
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    fig.update_layout(showlegend=False)
    kpi3.plotly_chart(fig, theme="streamlit", use_container_width=True)

    kpi4.metric(
        label=":warning: :orange[MÁQUINA004]", 
        value="MANTENIMIENTO",
        delta="Desconocido",
        delta_color="off"
    )
    data = [('Producido', randint(100, 1000)),
            ('Por producir', randint(100, 1000))]
    df = pd.DataFrame(data, columns=['product', 'quantity'])
    fig = px.pie(df, values='quantity', names='product', hole=.4,
                color_discrete_sequence=px.colors.sequential.Peach)
    fig.update_traces(textposition='inside', textinfo='value+percent+label')
    fig.update_layout(showlegend=False)
    kpi4.plotly_chart(fig, theme="streamlit", use_container_width=True)

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"])

    kpi4.bar_chart(chart_data)

    st.write("---")
    # Row 2
    # st.markdown('### Funcionamiento histórico (últimos 30 días)')
    # dfmachine1 = df2[df2.machine == "machine01"]
    # dfmachine2 = df2[df2.machine == "machine02"]
    # dfmachine3 = df2[df2.machine == "machine03"]

    # fig1 = px.pie(dfmachine1, values='qty', names='val_desc', title='Utilización Máquina 1')
    # fig2 = px.pie(dfmachine2, values='qty', names='val_desc', title='Utilización Máquina 2')
    # fig3 = px.pie(dfmachine3, values='qty', names='val_desc', title='Utilización Máquina 3')

    # # create two columns for charts
    # fig_col1, fig_col2 = st.columns(2)
    # fig_col1.write(fig1)
    # fig_col2.write(fig2)

    # fig_col3, fig_col4 = st.columns(2)
    # fig_col3.write(fig3)
    # fig_col4.dataframe(df2)
