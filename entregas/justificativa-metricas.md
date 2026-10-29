# Justificativa das métricas — Dashboard 2

**Dataset:** 868 pilotos de Fórmula 1 (1950–2020), uma linha por piloto.

**Público-alvo do Dashboard 2:** fãs e profissionais de comunicação esportiva (redatores, produtores de conteúdo e narradores) que querem contextualizar a carreira dos pilotos sem ler histograma, boxplot ou correlação. Não se espera conhecimento de estatística, só interesse em F1.



## Métrica 1: Pilotos
- **Variável:** `Driver` (contagem de linhas), filtrada por década de estreia (`Decade`), `Nationality` e `Status_Campeao`.
- **O que mede:** quantos pilotos estão na seleção atual. Sem filtros são 868.
- **Por que foi escolhida:** é o denominador de todas as outras métricas. Sem saber o tamanho do grupo, "34 campeões" ou "1.083 vitórias" não têm escala. Ela também avisa quando o filtro ficou pequeno demais para tirar conclusões (por exemplo, brasileiros estreados desde 2010 são só 6).
- **Público-alvo:** fãs e produtores de conteúdo.
- **Qual decisão pode ser apoiada por essa métrica?** Decidir se a amostra é grande o bastante para uma matéria ou comparação. 
- **O que comunica ao público-alvo:** "este recorte tem X pilotos". É o ponto de partida para ler os demais números.

## Métrica 2: Campeões
- **Variável:** `Champion` e `Championships`.
- **O que mede:** quantos pilotos da seleção foram campeões mundiais e que percentual isso representa. 
- **Por que foi escolhida:** o título é a conquista mais reconhecida do esporte e o público dentro da ramo do automobilismo.
- **Público-alvo:** fãs e redatores esportivos.
- **Qual decisão pode ser apoiada por essa métrica?** decidir entre os melhores pilotos que já sao campeoes quais são os mais ganhadores. 
- **O que comunica ao público-alvo:** ser campeão é raro, e a raridade muda conforme o recorte (época, país).

## Métrica 3: Vitórias
- **Variável:** `Race_Wins` (soma) e a proporção de pilotos com `Race_Wins > 0`.
- **O que mede:** o total de vitória e a parcela de pilotos que venceu pelo menos uma corrida.
- **Por que foi escolhida:** só o total de vitórias não conta a história inteira. Ele não mostra que a maioria dos pilotos passou pela F1 sem nunca vencer. Por isso mostro também a parcela que venceu pelo menos uma vez. Juntos, os dois números deixam claro o quanto vencer é raro: os campeões são só 3,9% dos pilotos, mas somam cerca de 75% das vitórias. Se o painel mostrasse só o total, essa desigualdade passaria batida.
- **Público-alvo:** fãs e produtores de conteúdo.
- **Qual decisão pode ser apoiada por essa métrica?** Escolher o ângulo da pauta: "vencer é para poucos" (13%) ou "a era moderna é mais disputada", já que nas décadas de 2010–2020 a parcela de vencedores sobe bastante (em especial pela alta quantidade de pilotos que vencem de forma constante, chegando a um marco de um ano de 25 vitorias 22 serem de um piloto)
- **O que comunica ao público-alvo:** a maioria dos pilotos nunca venceu, e as vitórias se concentram em poucos nomes.

## Métrica 4: Pontos por corrida (mediana)
- **Variável:** `Points_Per_Entry` (pontos divididos por corridas disputadas).
- **O que mede:** o desempenho típico por corrida, em pontos, usando a **mediana**, com a média ao lado para comparação. Sem filtros a mediana é 0,00 e a média é 0,48.
- **Por que foi escolhida:** compara pilotos de carreiras de tamanhos muito diferentes (de 1 a 359 corridas), o que o total de pontos não faz. Ela mostra com clareza a diferença entre mediana e média: a mediana é zero (metade dos pilotos nunca pontuou) enquanto a média é puxada pelos campeões. A média só aparece para evidenciar a distância.
- **Público-alvo:** fãs e redatores, que precisam de um número simples de desempenho.
- **Qual decisão pode ser apoiada por essa métrica?** Comparar grupos de forma justa, como décadas ou nacionalidades. A mediana sobe de 0,00 para 0,43 ao filtrar 2010–2020, o que indica um grupo mais competitivo. Também apoia a escolha de quais pilotos tratar como "referência" numa comparação.
- **O que comunica ao público-alvo:** o piloto típico pontua pouco ou nada, e quem pontua com regularidade já está acima da maioria.

## Métrica 5: Top 10 pilotos (vitórias, pódios ou pontos)
- **Variável:** `Race_Wins`, `Podiums` ou `Points`, escolhida em um seletor, ordenadas de forma decrescente, com cor por `Status_Campeao`.
- **O que mede:** os 10 pilotos com maior valor na métrica escolhida dentro da seleção atual. Sem filtros, na métrica de vitórias, lideram Lewis Hamilton (103), Michael Schumacher (91) e Sebastian Vettel (53); em pódios, Hamilton (191), Schumacher (155) e Vettel (122).
- **Por que foi escolhida:** é o único elemento que dá nome aos números. Um ranking de 10 é fácil de ler e responde à pergunta mais comum: "quem são os maiores?". A cor mostra que ser campeão e estar no topo andam juntos, mas não são a mesma coisa. Trocar a métrica evita que o público conclua que o "melhor" depende de uma única medida.
- **Público-alvo:** fãs, narradores e produtores de conteúdo.
- **Qual decisão pode ser apoiada por essa métrica?** Escolher quem destacar numa matéria, transmissão e verificar uma afirmação ("quem mais venceu no Brasil?") com o filtro de nacionalidade.
- **O que comunica ao público-alvo:** quem lidera cada critério e quão grande é a distância entre o primeiro e os demais.
