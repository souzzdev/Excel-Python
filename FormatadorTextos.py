import re

def formatar_texto(texto):
    """Remove espaços extras e separa o texto por palavras, depois ordena."""
    palavras = [palavra.strip() for palavra in texto.split() if palavra.strip()]
    return sorted(palavras)

def formatar_telefone(telefones):
    """Encontra todos os padrões de telefone válidos e ordena."""
    padrao_telefone = re.compile(
        r'\+?\d{1,3}\s??\d{2,3}?\s?\d{4,5}-?\d{4}'
    )
    telefones_validos = padrao_telefone.findall(telefones)
    telefones_validos = [
        tel for tel in telefones_validos if validar_digitos_telefone(tel)
    ]
    return sorted(telefones_validos)

def validar_digitos_telefone(telefone):
    """Valida o número de dígitos do telefone."""
    telefone_limpo = re.sub(r'\D', '', telefone)
    return 10 <= len(telefone_limpo) <= 15

def formatar_email(emails):
    """Encontra todos os padrões de email válidos e ordena."""
    padrao_email = re.compile(
        r'[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?'
    )
    emails_validos = padrao_email.findall(emails)
    emails_validos = [
        email for email in emails_validos if validar_email(email)
    ]
    return sorted(emails_validos)

def validar_email(email):
    """Valida o formato de um email."""
    padrao_email = re.compile(
        r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
    )
    return bool(padrao_email.match(email))

def formatar_url(urls):
    """Encontra todos os padrões de URL válidos e ordena."""
    padrao_url = re.compile(r'https?://(?:www\.)?[\w\.-]+\.\w+')
    urls_validas = padrao_url.findall(urls)
    return sorted(urls_validas)

def formatar_endereco(enderecos):
    """Formata e valida endereços."""
    padrao_endereco = re.compile(
        r'\d+\s[\w\s,.]+(?:\s[A-Z]{2})?'  # Formato básico de endereço
    )
    enderecos_validos = padrao_endereco.findall(enderecos)
    return sorted(enderecos_validos)

def formatar_codigo_postal(codigos):
    """Formata e valida códigos postais."""
    padrao_codigo_postal = re.compile(
        r'\d{5}-\d{3}|\d{5}'  # Formatos como 12345 ou 12345-678
    )
    codigos_validos = padrao_codigo_postal.findall(codigos)
    return sorted(codigos_validos)

def formatar_geral(entrada, tipo):
    """Chama a função de formatação adequada com base no tipo de dado informado."""
    if tipo == "texto":
        return formatar_texto(entrada)
    elif tipo == "telefone":
        return formatar_telefone(entrada)
    elif tipo == "email":
        return formatar_email(entrada)
    elif tipo == "url":
        return formatar_url(entrada)
    elif tipo == "endereco":
        return formatar_endereco(entrada)
    elif tipo == "codigo_postal":
        return formatar_codigo_postal(entrada)
    else:
        raise ValueError("Tipo não suportado. Use 'texto', 'telefone', 'email', 'url', 'endereco' ou 'codigo_postal'.")

def obter_entrada_usuario():
    """Captura a entrada do usuário para os dados a serem formatados e o tipo de dado."""
    entrada = input("Digite os dados contínuos (sem vírgulas): ")
    tipo = input("Digite o tipo de dado (texto, telefone, email, url, endereco, codigo_postal): ").lower()
    return entrada, tipo

def salvar_dados_em_arquivo(dados_formatados, tipo):
    """Salva os dados formatados em um arquivo de texto."""
    with open(f'dados_formatados_{tipo}.txt', 'a') as arquivo:
        for dado in dados_formatados:
            arquivo.write(f"{dado}\n")
    print(f"Dados salvos em 'dados_formatados_{tipo}.txt'.")

def main():
    """Função principal que coordena a execução do programa."""
    while True:
        entrada, tipo = obter_entrada_usuario()
        try:
            dados_formatados = formatar_geral(entrada, tipo)
            dados_separados = "; ".join(dados_formatados)
            print(f"Dados formatados e separados ({tipo}): {dados_separados}")
            
            salvar_opcao = input("Deseja salvar esses dados em um arquivo? (s/n): ").lower()
            if salvar_opcao == 's':
                salvar_dados_em_arquivo(dados_formatados, tipo)
        except ValueError as e:
            print(e)
        
        continuar = input("Deseja formatar outro conjunto de dados? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()