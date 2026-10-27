# Declaração de Uso de IA

**Nome:** Mircio Ferreira
**Data:** 27/10/2026

## Ferramenta

Claude Code (Anthropic), modelo Claude Sonnet 5.5, usado no terminal dentro do repositório.

## Prompt usado

Prompts reais enviados ao Claude Code (com a ortografia corrigida):

1. **Rascunho do Dashboard 1 (imagem):** "Rascunho minimalista de dashboard em preto e branco sobre fundo totalmente branco. À esquerda, uma caixa vertical arredondada com o texto 'Sidebar' e 'Filtros: variáveis + intervalo'. À direita, duas caixas horizontais sobrepostas: a superior com 'Correlação (heatmap)' e a inferior com 'Distribuição (histograma)'. Design vetorial simples, linhas pretas finas e sem sombras."
2. **Dashboard 1:**  "Ajusta a correlação para mostrar as métricas apenas em triângulo, porque a matriz de correlação não precisa ser tudo igual."
3. **Sidebar:** "Faz com que a barra lateral seja ajustável a partir de qual dashboard o usuário está vendo, se é o dashboard ou o KPI."
4. **Estética:** "Faz uma mudança estética e deixa com as cores temáticas da F1." / "Faz uma leve melhora no tamanho dos textos, tem alguns que são meio pequenos." / "O mapa de correlação acho que pode fugir da temática da F1 e ficar normal de correlação."


## Como a IA foi usada

A IA escreveu a maior parte do código do `app.py` (gráficos, KPIs, filtros e tema) e o ajusta os textos de `entregas/justificativa-metricas.md`, pedi para gerar os racunhos com base em prompots e fazer ajustes esteticos na apliação, assim como melhorias de usabilidade.

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:**
  - Heatmap e histogramas em Altair, com `@st.cache_data`, como o roteiro recomenda.
  - Dashboard 2 com 4 KPIs, Top 10 e gráfico de pilotos por década.
  - Sidebar que mostra só os filtros do dashboard aberto.
  - Tema escuro com as cores da F1.
- **Modificado:**
  - Pedi histogramas de todas as variáveis selecionadas, e não de uma por vez.
  - Pedi textos maiores, porque alguns estavam pequenos.
- **Rejeitado:**
  - O mapa-múndi coroplético, porque o resultado não ficou bom. 
  - As cores da F1 no heatmap de correlação, que voltou à escala vermelho e azul convencional.

