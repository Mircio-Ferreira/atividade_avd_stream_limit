# Justificativa das métricas — Dashboard 2

**Dataset:** 868 pilotos de Fórmula 1 (1950–2020), uma linha por piloto.

**Público-alvo do Dashboard 2:** fãs e profissionais de comunicação esportiva (redatores, produtores de conteúdo e narradores) que querem contextualizar a carreira dos pilotos sem ler histograma, boxplot ou correlação. Não se espera conhecimento de estatística, só interesse em F1.



## Métrica 1: Pilotos
- **Variável:** `Driver` (contagem de linhas), filtrada por década de estreia (`Decade`), `Nationality` e `Status_Campeao`.
- **O que mede:** quantos pilotos estão na seleção atual. Sem filtros são 868.
- **Por que foi escolhida:** é o denominador de todas as outras métricas. Sem saber o tamanho do grupo, "34 campeões" ou "1.083 vitórias" não têm escala. Ela também avisa quando o filtro ficou pequeno demais para tirar conclusões (por exemplo, brasileiros estreados desde 2010 são só 6).
- **Público-alvo:** fãs e produtores de conteúdo.
- **Qual decisão pode ser apoiada por essa métrica?** Decidir se a amostra é grande o bastante para uma matéria ou comparação. Com 6 pilotos o redator deve citar casos individuais, não "tendências".
- **O que comunica ao público-alvo:** "este recorte tem X pilotos". É o ponto de partida para ler os demais números.

## Métrica 2: Campeões
- **Variável:** `Champion` (booleano, soma) e `Championships`.
- **O que mede:** quantos pilotos da seleção foram campeões mundiais e que percentual isso representa. Sem filtros são **34 de 868 (3,9%)**, com 73 títulos no total.
- **Por que foi escolhida:** o título é a conquista mais reconhecida do esporte e o público a entende sem explicação. O percentual mostra como é raro: menos de 1 em cada 25 pilotos chegou lá.
- **Público-alvo:** fãs e redatores esportivos.
- **Qual decisão pode ser apoiada por essa métrica?** Dar peso a uma conquista: um texto pode dizer "um entre cada 25 pilotos" em vez de só "campeão". Também apoia comparar épocas ou países. Entre os brasileiros, 3 de 32 (9,4%) foram campeões, mais que o dobro da média geral.
- **O que comunica ao público-alvo:** ser campeão é raro, e a raridade muda conforme o recorte (época, país).

## Métrica 3: Vitórias
- **Variável:** `Race_Wins` (soma) e a proporção de pilotos com `Race_Wins > 0`.
- **O que mede:** o total de vitórias da seleção (**1.083** sem filtros) e a parcela de pilotos que venceu pelo menos uma corrida (**13%**).
- **Por que foi escolhida:** o total mostra o volume de resultados e a parcela mostra o quanto ele é concentrado. Os dois juntos contam que poucos pilotos ganham quase tudo: os campeões somam cerca de 75% das vitórias, embora sejam 3,9% dos pilotos. Mostrar só o total esconderia essa desigualdade.
- **Público-alvo:** fãs e produtores de conteúdo.
- **Qual decisão pode ser apoiada por essa métrica?** Escolher o ângulo da pauta: "vencer é para poucos" (13%) ou "a era moderna é mais disputada", já que nas décadas de 2010–2020 a parcela de vencedores sobe para 23,8%. Também ajuda a decidir que recorte merece destaque.
- **O que comunica ao público-alvo:** a maioria dos pilotos nunca venceu, e as vitórias se concentram em poucos nomes.

## Métrica 4: Pontos por corrida (mediana)
- **Variável:** `Points_Per_Entry` (pontos divididos por corridas disputadas).
- **O que mede:** o desempenho típico por corrida, em pontos, usando a **mediana**, com a média ao lado para comparação. Sem filtros a mediana é 0,00 e a média é 0,48.
- **Por que foi escolhida:** compara pilotos de carreiras de tamanhos muito diferentes (de 1 a 359 corridas), o que o total de pontos não faz. Ela mostra com clareza a diferença entre mediana e média: a mediana é zero (metade dos pilotos nunca pontuou) enquanto a média é puxada pelos campeões. A mediana é a medida correta para o "piloto típico"; a média só aparece para evidenciar a distância.
- **Público-alvo:** fãs e redatores, que precisam de um número simples de desempenho.
- **Qual decisão pode ser apoiada por essa métrica?** Comparar grupos de forma justa, como décadas ou nacionalidades. A mediana sobe de 0,00 para 0,43 ao filtrar 2010–2020, o que indica um grupo mais competitivo. Também apoia a escolha de quais pilotos tratar como "referência" numa comparação.
- **O que comunica ao público-alvo:** o piloto típico pontua pouco ou nada, e quem pontua com regularidade já está acima da maioria.

## Métrica 5: Top 10 pilotos (vitórias, pódios ou pontos)
- **Variável:** `Race_Wins`, `Podiums` ou `Points`, escolhida em um seletor, ordenadas de forma decrescente, com cor por `Status_Campeao`.
- **O que mede:** os 10 pilotos com maior valor na métrica escolhida dentro da seleção atual. Sem filtros, na métrica de vitórias, lideram Lewis Hamilton (103), Michael Schumacher (91) e Sebastian Vettel (53); em pódios, Hamilton (191), Schumacher (155) e Vettel (122).
- **Por que foi escolhida:** é o único elemento que dá nome aos números. Um ranking de 10 é fácil de ler e responde à pergunta mais comum: "quem são os maiores?". A cor mostra que ser campeão e estar no topo andam juntos, mas não são a mesma coisa. Trocar a métrica evita que o público conclua que o "melhor" depende de uma única medida.
- **Público-alvo:** fãs, narradores e produtores de conteúdo.
- **Qual decisão pode ser apoiada por essa métrica?** Escolher quem destacar numa matéria, vinheta ou transmissão, e verificar uma afirmação ("quem mais venceu no Brasil?") com o filtro de nacionalidade.
- **O que comunica ao público-alvo:** quem lidera cada critério e quão grande é a distância entre o primeiro e os demais.

=