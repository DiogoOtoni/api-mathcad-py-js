import win32com.client as win32
import psycopg2

DIRETORIO_WORKSHEET="DIRETORIO DO TEMPLATE DO MATHCAD .mcdx"

#FUNÇÃO DE MANIPULAÇÃO DO BANCO DE DADOS
def save_to_postgresql(valor):
    conn = psycopg2.connect("dbname=NOME DO BANCO DE DADOS user=postgres password=admin")
    cursor = conn.cursor()
    sql = "INSERT INTO inputs (input1, input2, input3, result1) VALUES (%s, 2, 2, 2)"
    cursor.execute(sql, (valor,))
    conn.commit()
    cursor.close()
    conn.close()

def calculate_with_mathcad():
    #CRIA UMA INSTANCIA DO MATHCAD VIA COM
    mathcad = win32.Dispatch("MathcadPrime.Application")

    #CAPTURA O WORKSHEET ATIVO PARA MANIPULAÇÃO DE DADOS DE ACORDO COM A API COM DO MATHCAD
    worksheet = mathcad.ActiveWorksheet

    #PEGA TODOS OS INPUTS E OUTPUTS DO WORKSHEET
    todosInputs = worksheet.Inputs
    todosOutputs = worksheet.Outputs

    #PEGA OS VALORES DOS INPUTS
    #PRIMEIRO pega o 'alias' do input pelo vetor de inputs, depois pega o valor real do input, de acordo com o TIPO do input (valor numero, matrix, etc...)
    print("quantidade de inputs sao: ", todosInputs.count)
    input1 = todosInputs.GetAliasByIndex(0)
    valorInput1 = worksheet.InputGetRealValue(input1).RealResult
    print(valorInput1)
    input2 = todosInputs.GetAliasByIndex(1)
    print("alias do input 2 : ", input2)
    valorInput2 = worksheet.InputGetMatrixValue(input2).Units
    print(valorInput2)
    print(" -------------------- ----------------------- ----------------------")
    print("quantidade de outputs sao: ", todosOutputs.count)
    output1 = todosOutputs.GetAliasByIndex(0)
    valorOutput1 = worksheet.OutputGetRealValue(output1).RealResult
    print(valorOutput1)
    output2 = todosOutputs.GetAliasByIndex(1)
    valorOutput2 = worksheet.OutputGetRealValue(output2).RealResult
    print(valorOutput2)
    #chama função de salvar no banco de dados
    save_to_postgresql(valorInput1+3)

calculate_with_mathcad()




