# Network Tool

## Instruções
### Configurando ambiente
- Instale os seguintes programas e certifique-se de que as **versões** usadas estão sempre corretas e os serviços estão **ativos**:
    - [Python 3.6.1](https://www.python.org/downloads/release/python-361) (mas provavelmente qualquer versão acima de 3.3 irá servir)
        - Tenha certeza de que seu Python3 tem o ```pip``` adequado a ele (no Linux, às vezes é pip3), com módulo ```virtualenv``` instalado
- Prepare o ambiente virtual:
    - Crie o ambiente virtual via console usando ```python -m venv env```
- Ative o ambiente virtual (e você irá **precisar refazer este único passo sempre que executar usar a aplicação**):
    - No Windows, execute no prompt (cmd): ```env\Scripts\activate.bat```
    - No Unix ou MacOS, execute no terminal (bash): ```source env/bin/activate```
- Rode o ```pip``` para instalar as dependências do sistema com ```pip install -r requirements.txt```.

### Rodando a aplicação
#### Executando casos base
Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar os casos base do sistema:
- Execute novamente o passo de ativação do ambiente virtual
- Dentro da pasta ```engine/``` execute o comando ```python coordinator.py```
    - Escolha as opções do menu seguindo as instruções

#### Executando caso de teste grande
Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o caso de teste de carga do sistema:
- Execute novamente o passo de ativação do ambiente virtual
- Dentro da pasta ```big_input/``` execute o comando ```python big_input_generator.py```

## Referencias
- [**Weighted sum model**](https://en.wikipedia.org/wiki/Weighted_sum_model)
- [**Dijkstra**](https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra)

