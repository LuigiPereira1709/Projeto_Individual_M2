Este código é projetado para ler informações de candidatos de um arquivo CSV chamado 'candidatos.csv', permitir que o usuário especifique notas mínimas para quatro áreas (E, T, P e S) e, em seguida, filtrar os candidatos com notas iguais ou superiores a essas notas mínimas. Se houver candidatos que atendam aos critérios, as informações deles serão salvas em um novo arquivo CSV chamado 'candidatos_filtrados.csv'.

Pré-requisitos

Antes de executar o código, certifique-se de que você tenha o seguinte instalado:

Python: Certifique-se de que você tenha uma versão do Python instalada em seu sistema.
Biblioteca pandas: Você pode instalá-la usando o comando pip install pandas.

Como usar
Coloque seu arquivo CSV de candidatos com os dados na mesma pasta que este código ou forneça o caminho correto para o arquivo no código.

Execute o código em um ambiente Python.

O código solicitará que você insira as notas mínimas para as áreas E, T, P e S. Certifique-se de inserir valores numéricos válidos.

O código filtrará os candidatos com notas iguais ou superiores às notas mínimas especificadas.

Se houver candidatos que atendam aos critérios, as informações deles serão salvas em um arquivo CSV chamado 'candidatos_filtrados.csv' na mesma pasta do código.

Se nenhum candidato atender aos critérios, você receberá uma mensagem informando que nenhum candidato foi encontrado.

Certifique-se de ajustar o separador do arquivo CSV (';' no código) se o arquivo CSV de entrada usar um separador diferente.

Lembre-se de que esse código assume que o arquivo CSV 'candidatos.csv' contém colunas com os nomes 'e', 't', 'p' e 's' para as notas nas áreas E, T, P e S, respectivamente. Certifique-se de ajustar o código se os nomes das colunas forem diferentes no seu arquivo de candidatos.

Esse é um código simples para filtrar candidatos com base em critérios de notas mínimas. Você pode personalizá-lo de acordo com suas necessidades específicas e até mesmo adicionar mais recursos, como cálculos estatísticos ou visualizações dos candidatos filtrados.




