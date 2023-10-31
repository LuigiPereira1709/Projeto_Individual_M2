Este é um código Python que permite importar dados de candidatos de um arquivo CSV, definir notas mínimas para quatro áreas (E, T, P e S) e filtrar os candidatos com base nessas notas mínimas. Se houver candidatos que atendam aos critérios, as informações deles serão salvas em um novo arquivo CSV. O código fornece uma interface simples para que o usuário insira os nomes dos arquivos e as notas mínimas desejadas.

Pré-requisitos
Certifique-se de que você tenha os seguintes requisitos atendidos antes de executar o código:

Python: Este código é escrito em Python. Certifique-se de ter uma versão do Python instalada no seu sistema.

Biblioteca pandas: O código utiliza a biblioteca pandas para a leitura e manipulação de dados em formato CSV. Você pode instalá-la com o comando pip install pandas.

Como usar
Siga estas etapas para utilizar o código:

1- Execute o código em um ambiente Python.

2- O código solicitará que você insira o nome do arquivo CSV que deseja importar (sem a extensão .csv). Certifique-se de que o arquivo esteja na mesma pasta que o código ou forneça o caminho correto para o arquivo.

3- Em seguida, você será solicitado a inserir as notas mínimas para as áreas E, T, P e S. Certifique-se de inserir valores numéricos válidos.

4- O código filtrará os candidatos com notas iguais ou superiores às notas mínimas especificadas.

5- Se houver candidatos que atendam aos critérios, você será solicitado a inserir o nome do arquivo de saída para os candidatos filtrados (sem a extensão .csv).

6- Os candidatos filtrados serão salvos em um novo arquivo CSV com o nome especificado.

7- Se nenhum candidato atender aos critérios, você receberá uma mensagem informando que nenhum candidato foi encontrado.

Certifique-se de ajustar o separador do arquivo CSV (definido como ';' no código) se o arquivo de entrada usar um separador diferente.

Este código é uma ferramenta simples e personalizável para filtrar candidatos com base em critérios de notas mínimas. Você pode adaptá-lo de acordo com suas necessidades específicas e usá-lo para análise e processamento de dados de candidatos.
