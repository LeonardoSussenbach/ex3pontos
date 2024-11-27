import re

def verificar_senha(senha):
    # Inicializando a pontuação
    pontos = 0
    
    # Regras de adições
    n_caracteres = len(senha)
    pontos += n_caracteres * 4  # Adição por número de caracteres
    
    maiusculas = len([c for c in senha if c.isupper()])
    minusculas = len([c for c in senha if c.islower()])
    numeros = len([c for c in senha if c.isdigit()])
    simbolos = len([c for c in senha if not c.isalnum()])

    pontos += (n_caracteres - maiusculas) * 2  # Adição para minúsculas
    pontos += (n_caracteres - minusculas) * 2  # Adição para maiúsculas
    pontos += numeros * 4  # Adição para números
    pontos += simbolos * 6  # Adição para símbolos
    
    # Adições por números e símbolos no meio
    if re.search(r'[0-9!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`~]', senha[1:-1]):
        pontos += (numeros + simbolos) * 2
    
    regras_atendidas = 0
    if n_caracteres >= 8:
        regras_atendidas += 1
    if maiusculas >= n_caracteres * 0.75 or minusculas >= n_caracteres * 0.75 or numeros >= n_caracteres * 0.75 or simbolos >= n_caracteres * 0.75:
        regras_atendidas += 1
    pontos += regras_atendidas * 2
    
    # Regras de deduções
    # Somente letras
    if all(c.isalpha() for c in senha):
        pontos -= n_caracteres
    # Somente números
    if all(c.isdigit() for c in senha):
        pontos -= n_caracteres
    # Caracteres repetidos
    caracteres_repetidos = len(senha) - len(set(senha.lower()))
    pontos -= caracteres_repetidos
    
    # Maiúsculas repetidas consecutivas
    maiusculas_repetidas = len(re.findall(r'([A-Z])\1+', senha))
    pontos -= maiusculas_repetidas * 2
    
    # Minúsculas repetidas consecutivas
    minusculas_repetidas = len(re.findall(r'([a-z])\1+', senha))
    pontos -= minusculas_repetidas * 2
    
    # Números consecutivos
    numeros_consecutivos = len(re.findall(r'(\d)\1+', senha))
    pontos -= numeros_consecutivos * 2
    
    # Letras sequenciais
    sequencias_letras = len(re.findall(r'(abc|def|ghi|jkl|mno|pqr|stu|vwx|yz)', senha, re.IGNORECASE))
    pontos -= sequencias_letras * 3
    
    # Números sequenciais
    sequencias_numeros = len(re.findall(r'(123|234|345|456|567|678|789|890)', senha))
    pontos -= sequencias_numeros * 3
    
    # Símbolos sequenciais
    sequencias_simbolos = len(re.findall(r'(!@#|$%&|^*|()|_+|{}|\[\]|<>)', senha))
    pontos -= sequencias_simbolos * 3
    
    # Resultado final
    if pontos < 20:
        return "Muito fraca"
    elif 20 <= pontos < 40:
        return "Fraca"
    elif 40 <= pontos < 60:
        return "Boa"
    elif 60 <= pontos < 80:
        return "Forte"
    else:
        return "Muito forte"

senha = input("Digite uma senha para avaliação: ")
print(verificar_senha(senha))
