# API MathCad Prime + Javascript + Python + .bat + Postgresql

Esse é um projeto de um teste feito para usar a API do Mathcad Prime 10.0.0 

## Arquivos .js

São arquivos de scripts em javascript que as vezes leem os scripts python (por meio da biblioteca python-shell) e são executados por meio de arquivos .bat

## Arquivos .py

São os arquivos em python que fazem o uso da API do Mathcad por meio de COM (component object model) com a biblioteca `win32com.client`

## Arquivos .bat

São apenas a execução dos scripts .js. Um simples executavel

#### Melhorias e complementos:

- Deve ter um arquivo para variaveis de uso global do projeto - por exemplo o caminho do diretorio, dados do banco de dados - .env
- Deve ser criado novos arquivos tanto .py quando .js e consequentemente .bat para cada funcionalidade necessitada de acordo com o template
- Poderá ser criado uma interface javascript/html para que nao necessite de arquivos .bat e possa utilizar botoes para cada funcionalidade de cada arquivo .py
- TBD
