# Controle de Queimadas

**Número da Lista**: 4<br>
**Conteúdo da Disciplina**: Dividir e conquistar<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0006872  |  Gabriela Chaves de Moraes |
| 16/0012961  |  Lucas Arthur Lermen |

## Sobre 
<p align="justify">Essa lista consiste de um analisador de focos de incêndio baseado no dataset <a href="https://www.kaggle.com/new-york-state/nys-forest-ranger-wildland-fire-reporting">NYS Forest Ranger Wildland Fire Reporting
</a>. Após definida uma distância de segurança, serão procurados os dois focos de distância mais próximos para que as autoridades sejam alertadas sobre o risco de expansão. Esse processo será repetido até que não existam mais incêndios com distâncias menores que a considerada segura.

## Instalação 

**Linguagem**: Python v3.6 ou superior <br>

### Executando o projeto

#### Pré-requisitos

``` console
$ pip3 install pandas

$ pip3 install matplotlib

$ pip3 install networkx
```

#### Comandos para executar

``` console
$ python3 monitoramento.py

```
## Uso 
Ao executar o comando será inicializado um menu com 2 opções  
1 - Monitorar focos de incêndio  
0 - Sair  

Ao ser selecionada a opção de monitoramento, os focos de incêndio com menores distâncias serão apresentados com todas as informações e esses pares também serão mostrados em um gráfico contendo todos os focos de incêndio.


