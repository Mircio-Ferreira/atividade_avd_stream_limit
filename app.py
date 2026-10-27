import altair as alt
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
NACIONALIDADES = sorted(df["Nationality"].unique())
# Métrica do Top 10 do Dashboard 2: rótulo -> coluna do dataset
METRICAS_TOP = {"Vitórias": "Race_Wins", "Pódios": "Podiums", "Pontos": "Points"}

# Abas criadas antes da sidebar para a sidebar saber qual dashboard está aberto.
# on_change="rerun" ativa a execução só da aba selecionada (propriedade .open).
tab_correlacao, tab_kpis = st.tabs(
    ["Dashboard 1: correlação e distribuição", "Dashboard 2: KPIs"],
    key="aba",
    on_change="rerun",
)

CHAVES_D1 = ["f1_variaveis", "f1_decadas", "f1_poles", "f1_pontos", "f1_win_rate", "f1_status"]
CHAVES_D2 = ["kpi_decadas", "kpi_nacionalidades", "kpi_status", "kpi_metrica_top"]


def manter_estado(chaves):
    """Widgets não renderizados perdem o valor; reatribuir mantém o filtro da outra aba."""
    for chave in chaves:
        if chave in st.session_state:
            st.session_state[chave] = st.session_state[chave]


# Sidebar: mostra só os filtros do dashboard que está aberto
with st.sidebar:
    if tab_correlacao.open:
        st.header("Filtros do Dashboard 1")

        variaveis = st.multiselect(
            "Variáveis",
            options=VARS_QUANT,
            default=VARS_QUANT,
            key="f1_variaveis",
            help="Variáveis quantitativas usadas nos gráficos.",
        )

        decada_inicio, decada_fim = st.select_slider(
            "Intervalo de décadas",
            options=decadas,
            value=(decadas[0], decadas[-1]),
            key="f1_decadas",
            help="Mantém só os pilotos cuja década de estreia está no intervalo.",
        )

        poles_min, poles_max = st.slider(
            "Intervalo de pole positions",
            min_value=int(df["Pole_Positions"].min()),
            max_value=int(df["Pole_Positions"].max()),
            value=(int(df["Pole_Positions"].min()), int(df["Pole_Positions"].max())),
            key="f1_poles",
        )

        pontos_min, pontos_max = st.slider(
            "Intervalo de pontos",
            min_value=float(df["Points"].min()),
            max_value=float(df["Points"].max()),
            value=(float(df["Points"].min()), float(df["Points"].max())),
            step=0.5,
            key="f1_pontos",
        )

        win_rate_min, win_rate_max = st.slider(
            "Intervalo de win rate",
            min_value=0.0,
            max_value=float(df["Win_Rate"].max()),
            value=(0.0, float(df["Win_Rate"].max())),
            step=0.01,
            key="f1_win_rate",
            help="Proporção de vitórias por corrida disputada (0 a 1).",
        )

        status = st.segmented_control(
            "Status",
            options=STATUS_OPCOES,
            default="Todos",
            key="f1_status",
            help="Filtra por pilotos campeões (Vencedor) ou não (Não Vencedor).",
        )
    else:
        manter_estado(CHAVES_D1)

    if tab_kpis.open:
        st.header("Filtros do Dashboard 2")

        kpi_decada_inicio, kpi_decada_fim = st.select_slider(
            "Intervalo de décadas",
            options=decadas,
            value=(decadas[0], decadas[-1]),
            key="kpi_decadas",
            help="Mantém só os pilotos cuja década de estreia está no intervalo.",
        )

        kpi_nacionalidades = st.multiselect(
            "Nacionalidade",
            options=NACIONALIDADES,
            placeholder="Todas",
            key="kpi_nacionalidades",
            help="Vazio = todas as nacionalidades.",
        )

        kpi_status = st.segmented_control(
            "Status",
            options=STATUS_OPCOES,
            default="Todos",
            key="kpi_status",
        )

        metrica_top = st.segmented_control(
            "Métrica do Top 10",
            options=list(METRICAS_TOP),
            default="Vitórias",
            key="kpi_metrica_top",
        )
    else:
        manter_estado(CHAVES_D2)

if tab_correlacao.open:
    # Aplica os filtros
    df_filtrado = df[
        df["Decade"].between(decada_inicio, decada_fim)
        & df["Pole_Positions"].between(poles_min, poles_max)
        & df["Points"].between(pontos_min, pontos_max)
        & df["Win_Rate"].between(win_rate_min, win_rate_max)
    ]
    if status in ("Vencedor", "Não Vencedor"):
        df_filtrado = df_filtrado[df_filtrado["Status_Campeao"] == status]

    # Dashboard 1: correlação (heatmap) em cima, distribuição (histograma) embaixo
    with tab_correlacao:
        st.caption(f"{len(df_filtrado)} de {len(df)} pilotos com os filtros do Dashboard 1.")

        with st.container(border=True):
            st.subheader("Correlação")
            st.caption("Heatmap da correlação entre as variáveis selecionadas.")

            if len(variaveis) < 2:
                st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
            elif len(df_filtrado) < 2:
                st.warning("Poucos pilotos com os filtros atuais para calcular a correlação.")
            else:
                corr = (
                    df_filtrado[variaveis]
                    .corr()
                    .reset_index(names="var_x")
                    .melt(id_vars="var_x", var_name="var_y", value_name="corr")
                )
                # Só o triângulo inferior: a matriz é simétrica, então o resto repete valores
                posicao = {v: i for i, v in enumerate(variaveis)}
                corr = corr[corr["var_y"].map(posicao) >= corr["var_x"].map(posicao)]
                base = alt.Chart(corr).encode(
                    x=alt.X("var_x:N", title=None, sort=variaveis),
                    y=alt.Y("var_y:N", title=None, sort=variaveis),
                )
                heatmap = base.mark_rect().encode(
                    color=alt.Color(
                        "corr:Q",
                        title="Correlação",
                        scale=alt.Scale(domain=[-1, 1], scheme="redblue", reverse=True),
                    ),
                    tooltip=["var_x", "var_y", alt.Tooltip("corr:Q", format=".2f")],
                )
                rotulos = base.mark_text().encode(
                    text=alt.Text("corr:Q", format=".2f"),
                    color=alt.condition(
                        "abs(datum.corr) > 0.6", alt.value("white"), alt.value("black")
                    ),
                )
                st.altair_chart(
                    heatmap + rotulos,
                    alt="Heatmap da correlação entre as variáveis quantitativas selecionadas",
                )

        with st.container(border=True):
            st.subheader("Distribuição")
            st.caption("Histograma de cada variável selecionada.")

            if not variaveis:
                st.warning("Selecione pelo menos 1 variável para ver a distribuição.")
            else:
                colunas = st.columns(2)
                for i, variavel in enumerate(variaveis):
                    histograma = (
                        alt.Chart(df_filtrado)
                        .mark_bar()
                        .encode(
                            x=alt.X(f"{variavel}:Q", bin=alt.Bin(maxbins=30), title=variavel),
                            y=alt.Y("count()", title="Pilotos"),
                            tooltip=[
                                alt.Tooltip(f"{variavel}:Q", bin=alt.Bin(maxbins=30), title=variavel),
                                alt.Tooltip("count()", title="Pilotos"),
                            ],
                        )
                        .properties(title=variavel, height=220)
                    )
                    with colunas[i % 2]:
                        st.altair_chart(histograma, alt=f"Histograma da variável {variavel}")

if tab_kpis.open:
    # Dashboard 2: filtros próprios (década, nacionalidade, status)
    df_kpi = df[df["Decade"].between(kpi_decada_inicio, kpi_decada_fim)]
    if kpi_nacionalidades:
        df_kpi = df_kpi[df_kpi["Nationality"].isin(kpi_nacionalidades)]
    if kpi_status in ("Vencedor", "Não Vencedor"):
        df_kpi = df_kpi[df_kpi["Status_Campeao"] == kpi_status]

    # Dashboard 2: KPIs
    with tab_kpis:
        st.caption(f"{len(df_kpi)} de {len(df)} pilotos com os filtros do Dashboard 2.")

        if df_kpi.empty:
            st.warning("Nenhum piloto com os filtros atuais. Amplie a seleção na sidebar.")
        else:
            n_pilotos = len(df_kpi)
            n_campeoes = int(df_kpi["Champion"].sum())
            n_vitorias = int(df_kpi["Race_Wins"].sum())
            n_vencedores = int((df_kpi["Race_Wins"] > 0).sum())
            ppc_mediana = df_kpi["Points_Per_Entry"].median()
            ppc_media = df_kpi["Points_Per_Entry"].mean()

            with st.container(horizontal=True):
                st.metric(
                    "Pilotos",
                    f"{n_pilotos:,}".replace(",", "."),
                    help="Pilotos que estrearam na janela de décadas e passam pelos filtros.",
                    border=True,
                )
                st.metric(
                    "Campeões",
                    n_campeoes,
                    delta=f"{n_campeoes / n_pilotos:.1%} dos pilotos",
                    delta_color="off",
                    help="Pilotos com pelo menos um título mundial.",
                    border=True,
                )
                st.metric(
                    "Vitórias",
                    f"{n_vitorias:,}".replace(",", "."),
                    delta=f"{n_vencedores / n_pilotos:.1%} dos pilotos venceram",
                    delta_color="off",
                    help="Soma de vitórias; o delta mostra a parcela que venceu ao menos uma corrida.",
                    border=True,
                )
                st.metric(
                    "Pontos por corrida (mediana)",
                    f"{ppc_mediana:.2f}",
                    delta=f"média {ppc_media:.2f}",
                    delta_color="off",
                    help="Mediana de Points_Per_Entry. A mediana é usada porque a maioria dos pilotos tem 0 pontos e a média é puxada pelos campeões.",
                    border=True,
                )

            coluna_top = METRICAS_TOP[metrica_top or "Vitórias"]
            with st.container(border=True):
                st.subheader(f"Top 10 pilotos por {(metrica_top or 'Vitórias').lower()}")
                top10 = df_kpi.nlargest(10, coluna_top)[["Driver", coluna_top, "Status_Campeao"]]
                if top10[coluna_top].max() == 0:
                    st.info("Nenhum piloto da seleção pontuou nesta métrica.")
                else:
                    grafico_top = (
                        alt.Chart(top10)
                        .mark_bar()
                        .encode(
                            x=alt.X(f"{coluna_top}:Q", title=metrica_top or "Vitórias"),
                            y=alt.Y("Driver:N", sort="-x", title=None),
                            color=alt.Color("Status_Campeao:N", title="Status"),
                            tooltip=["Driver", alt.Tooltip(f"{coluna_top}:Q", title=metrica_top), "Status_Campeao"],
                        )
                        .properties(height=320)
                    )
                    st.altair_chart(grafico_top, alt="Top 10 pilotos pela métrica escolhida")

            with st.container(border=True):
                st.subheader("Pilotos por década de estreia")
                por_decada = df_kpi.groupby("Decade", as_index=False).size().rename(columns={"size": "Pilotos"})
                grafico_decada = (
                    alt.Chart(por_decada)
                    .mark_bar()
                    .encode(
                        x=alt.X("Decade:O", title="Década de estreia"),
                        y=alt.Y("Pilotos:Q"),
                        tooltip=["Decade", "Pilotos"],
                    )
                    .properties(height=240)
                )
                st.altair_chart(grafico_decada, alt="Quantidade de pilotos por década de estreia")
