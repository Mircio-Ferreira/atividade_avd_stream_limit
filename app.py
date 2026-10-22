import streamlit as st

from src.data_loader import load_data

st.set_page_config(
    page_title="Pilotos de Fórmula 1",
    layout="wide",
)

st.title("Pilotos de Fórmula 1")
st.caption("Análise do desempenho histórico dos pilotos (1950–2020).")

df = load_data()

# Variáveis quantitativas disponíveis para correlação e distribuição
VARS_QUANT = [
    "Race_Entries",
    "Pole_Positions",
    "Race_Wins",
    "Podiums",
    "Points",
    "Years_Active",
]
STATUS_OPCOES = ["Todos", "Vencedor", "Não Vencedor"]
decadas = sorted(df["Decade"].unique())

# Sidebar: filtros (variáveis + intervalo)
with st.sidebar:
    st.header("Filtros")

    variaveis = st.multiselect(
        "Variáveis",
        options=VARS_QUANT,
        default=VARS_QUANT,
        help="Variáveis quantitativas usadas nos gráficos.",
    )

    decada_inicio, decada_fim = st.select_slider(
        "Intervalo de décadas",
        options=decadas,
        value=(decadas[0], decadas[-1]),
        help="Mantém só os pilotos cuja década de estreia está no intervalo.",
    )

    poles_min, poles_max = st.slider(
        "Intervalo de pole positions",
        min_value=int(df["Pole_Positions"].min()),
        max_value=int(df["Pole_Positions"].max()),
        value=(int(df["Pole_Positions"].min()), int(df["Pole_Positions"].max())),
    )

    pontos_min, pontos_max = st.slider(
        "Intervalo de pontos",
        min_value=float(df["Points"].min()),
        max_value=float(df["Points"].max()),
        value=(float(df["Points"].min()), float(df["Points"].max())),
        step=0.5,
    )

    win_rate_min, win_rate_max = st.slider(
        "Intervalo de win rate",
        min_value=0.0,
        max_value=float(df["Win_Rate"].max()),
        value=(0.0, float(df["Win_Rate"].max())),
        step=0.01,
        help="Proporção de vitórias por corrida disputada (0 a 1).",
    )

    status = st.segmented_control(
        "Status",
        options=STATUS_OPCOES,
        default="Todos",
        help="Filtra por pilotos campeões (Vencedor) ou não (Não Vencedor).",
    )

# Aplica os filtros
df_filtrado = df[
    df["Decade"].between(decada_inicio, decada_fim)
    & df["Pole_Positions"].between(poles_min, poles_max)
    & df["Points"].between(pontos_min, pontos_max)
    & df["Win_Rate"].between(win_rate_min, win_rate_max)
]
if status in ("Vencedor", "Não Vencedor"):
    df_filtrado = df_filtrado[df_filtrado["Status_Campeao"] == status]

st.caption(f"{len(df_filtrado)} de {len(df)} pilotos com os filtros atuais.")

tab_correlacao, tab_kpis = st.tabs(
    ["Dashboard 1: correlação e distribuição", "Dashboard 2: KPIs"]
)

# Dashboard 1: correlação (heatmap) em cima, distribuição (histograma) embaixo
with tab_correlacao:
    with st.container(border=True):
        st.subheader("Correlação")
        st.caption("Heatmap da correlação entre as variáveis selecionadas.")

        if len(variaveis) < 2:
            st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
        else:
            # TODO: df_filtrado[variaveis].corr() + heatmap (plotly px.imshow)
            pass

    with st.container(border=True):
        st.subheader("Distribuição")
        st.caption("Histograma de uma variável à escolha.")

        if not variaveis:
            st.warning("Selecione pelo menos 1 variável para ver a distribuição.")
        else:
            variavel_hist = st.selectbox("Variável do histograma", options=variaveis)
            # TODO: histograma de variavel_hist (plotly px.histogram)

# Dashboard 2: KPIs
with tab_kpis:
    with st.container(horizontal=True):
        st.metric("Pilotos", "—", border=True)
        st.metric("Campeões", "—", border=True)
        st.metric("Vitórias", "—", border=True)
        st.metric("Pontos", "—", border=True)

    with st.container(border=True):
        st.subheader("Top 10 pilotos")
        # TODO: gráfico de barras com os 10 pilotos de mais Race_Wins
