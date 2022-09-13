## Importações;
import random
import re

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Verificadores, retorna variavel False or True;

## Senhas, 1- Maior ou igual a 8 digitos / 2- Conter 1 ou mais caracteres especiais / 3- Conter 3 ou mais números;
def verificarSenha(Senha):
    ## Definindo Variaveis;
    caracter = 0
    numero = 0
    senhaL = []
    Verificação = False
    ## Separando letra por letra da Senha;
    for i in Senha:
        senhaL.append(i)
    ## Tamanho da Senha;
    if len(Senha) < 8:
        print("\033[31mSenha Inválida - Erro na quantidade de Caracteres\033[37m")
        return
    for i in range(0,len(senhaL)):
        if senhaL[i] == "@" or senhaL[i] == "!" or senhaL[i] == "&" or senhaL[i] == "/" or senhaL[i] == "?" or senhaL[i] == "_" or senhaL[i] == "*" or senhaL[i] == "#" or senhaL[i] == "%" or senhaL[i] == "$" or senhaL[i] == "|":
            caracter += 1
        if senhaL[i] == "0" or senhaL[i] == "1" or senhaL[i] == "2" or senhaL[i] == "3" or senhaL[i] == "4" or senhaL[i] == "5" or senhaL[i] == "6" or senhaL[i] == "7" or senhaL[i] == "8" or senhaL[i] == "9": 
            numero += 1 
    if numero >= 3 and caracter >= 1:
        Verificação = True
    else:
        print("\033[31mSenha Inválida - Sua senha não segue as regras!\033[37m")
    return Verificação

## Emails, 1- Deve conter '@' / 2- Deve conter ".com" / 3- Pode ou não conter ".br" no final / 4- Não contem limite de letras e Números / 5- Não pode conter caracter especial além do "@";
def verificarEmail(Email):
    Verificação = False
    emailRegex = '^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.+[a-z]+)?$'
    if re.search(emailRegex,Email):
        Verificação = True
    else:
        print("\033[31mEmail Inválido\033[37m")
    return Verificação

## CPF;
def verificarCPF(cpf):
    ## Criando as Variavéis para a primeira conta;
    Verificação = True
    cpf_1 = []
    total = 0
    n1 = 10
    e = 0
    igualdade = 0
    ## Adicionando CPF em Lista;
    for i in cpf:
        i = int(i)
        cpf_1.append(i)
    for i in cpf_1:
        if(cpf_1.count(i) > 10):
            igualdade = 1
        else:
            pass
    ## 1º Multiplicação;
    for i in range(2, 11):
        total += (cpf_1[e]*n1)
        n1 -= 1
        e += 1                  
    ## Verificando o 1º Digito;
    digito1 = (11- (total % 11))
    if digito1 > 9:
        digito1 = 0          
    if (digito1 == cpf_1[-2]):
        if (igualdade == 1):
            print("\033[31m CPF invalido!\033[37m")
            Verificação = False
            return
    else:
        print("\033[31m CPF invalido!\033[37m")
        Verificação = False
        return
    ## Zerando as Variaveis;
    n1 = 11
    e = 0
    total = 0
    ## 2º Multiplicação;
    for i in range(2, 12):
        total += (cpf_1[e]*n1)
        n1 -= 1
        e += 1
    ## Verificando o 2º Digito;    
    digito2 = (11- (total % 11))
    if digito2 > 9:
        digito2 = 9
    if (digito2 == cpf_1[-1]):
            Confirmação_2 = False  
    else:
        print("\033[31m CPF invalido!\033[37m")
        Verificação = False
    
    return Verificação

## Telefone, Digitar apenas os Digitos, incluindo o DDD; 
def verificarTelefone(Telefone):
    ## Váriaveis;
    Verificação = False
    tel = str(Telefone)
    ddds = ["61","62","64","65","66","67","82","71","73","74","75","77","85","88","98","99","83","81","87","86","89","84","79","68","96","92","97","91","93","94","95","69","63","27","28","21","31","32","33","34","35","37","38","22","24","11","12","13","14","15","16","17","18","19","41","42","43","44","45","46","51","53","54","55","47","48","49"]
    confirma = 0
    ## Validando Tamanho;
    if len(tel) == 11:
        pass
    else:
        print("\033[31mNúmero Incorreto - Quantidade de Digitos incorreta!\033[37m")
        return
    ## Validando DDD;
    ddd = tel[0]+tel[1]
    for i in range(0,len(ddds)):
        if ddd == ddds[i]:
            confirma += 1
        else:
            confirma += 0
    match confirma:
        case 0:
            print("\033[31mNúmero Incorreto - DDD Inexistente!\033[37m")
        case 1:
            Verificação = True
    return Verificação

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Geradores, retornam as informações;

## Primeiro Nome;
def gerarPrimeiroNome():
    vogais = ["a","e","i","o","u",""]
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","w","z",""]
    nomeL = []
    nome = ""
    silabas = random.randint(1,5)

    for i in range(0,silabas):
        nomeL += random.choices(consoantes)
        nomeL += random.choices(vogais)

    nome =''.join(nomeL)
    nome = nome.capitalize()
    return nome

## Apenas um Sobrenome;
def gerarSobrenome():
    sobrenomeL = ["Phareman","Boschetti","Scariot","Thybaut","Gautzelin","Godfree","Girardus","Gerould","Gualterius","Gocelinus","Urhan","Ugovras","Azadium","Chavez","Olzoxon","Da Silva","Santos","Nubis","Skullblood","Geimadra"]
    sobrenome = random.choices(sobrenomeL)
    sobrenome = ''.join(sobrenome)
    
    return sobrenome

## Um Nome Completo, com Nome + Sobrenome;
def gerarNomeCompleto():
    PrimeiroNome = gerarPrimeiroNome()
    sobrenome = gerarSobrenome()

    nome = (f"{PrimeiroNome} {sobrenome}")
    
    return nome

## Token de Segurança Aleatório;
def gerarTokens():
    vogais = ["a","e","i","o","u"]
    consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","w","z"]
    numeros = ["1","2","3","4","5","6","7","8","9"]
    outros = ["@","!","&","/","?","_"]
    tokenL = []
    token = ""

    for i in range(1,10):
        valor = random.randint(1,3)
        match valor:
            case 1:
                tokenL += random.choices(vogais)
            case 2:
                tokenL += random.choices(consoantes)
            case 3:
                tokenL += random.choices(numeros)
            case 4:
                tokenL += random.choices(outros)

    token =''.join(tokenL)
    return token

def gerarDataAniversário():
    pass

def gerarCPF():
    Verificação = False
    while not Verificação:
        ## Declarando Váriaveis;
        cpf1 = []
        contador = 0
        ## Criação de CPF;
        for i in range (1,12):
            i = random.randint(0,9)
            cpf1.append(i)
        cpf = "".join(cpf1)
        print(cpf)


 ## Declarando Váriaveis;
cpf1 = []
## Criação de CPF;
for i in range (1,12):
    i = random.randint(0,9)
    cpf1.append(i)
cpf1 = str(cpf1)
cpf = "".join(cpf1)
print(cpf)
        

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Modo de Uso;

# Importe o arquivo "Ferramentas.py";
# Crie um variavel para receber a informação da função EX: nome = gerarNome() ;
# Nos métodos de Verificação, é nescessário inserir a informação na função, e ela vai te retornar True ou False;
# Faça um bom uso e fique a vontade para acrescentar outras informações no código;