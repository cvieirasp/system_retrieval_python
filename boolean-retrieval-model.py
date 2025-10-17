"""Enunciado:

Implemente um mini-buscador booleando sobre um pequeno acervo de notícias internas de empresa.
Os documentos estarão em memória como uma lista de dicionários: [{ "id": "DOC1", "titulo": "...", "texto": "..." }, ...].
Construa um índice invertido de termos → {ids de documentos}.
Implemente uma função buscar_booleana(consulta_str) que aceite expressões com AND, OR, NOT (maiúsculas), parênteses e termos simples.

Exemplos de consulta:
("vpn" AND "acesso") AND NOT "jornada"
"benefícios" OR ("plano" AND "saúde")

Normalização mínima: minúsculas, remoção de pontuação simples e acentos; preserve palavras com hífen como uma única unidade (ex.: “single-sign-on”).

Saída: lista ordenada por id dos documentos que satisfazem exatamente a lógica booleana.
"""

import os
import nltk
import shutil
import string
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

nltk.download("punkt_tab")
nltk.download("stopwords")

import warnings

# Suprimir avisos de sintaxe do Whoosh
warnings.filterwarnings("ignore", category=SyntaxWarning)

# Exemplo de documentos
documentos = [
    {
        "id": "DOC1",
        "titulo": "Acesso VPN para Trabalho Remoto",
        "texto": "TI informa: o acesso à VPN estará disponível 24h a partir de hoje. Para conectar, use o aplicativo corporativo e a autenticação de dois fatores. Evite uso pessoal durante a jornada de trabalho.",
    },
    {
        "id": "DOC2",
        "titulo": "Benefícios 2026: Plano de Saúde e Odonto",
        "texto": "RH comunica atualização dos benefícios: novo plano de saúde com coparticipação reduzida e inclusão de telemedicina. Dúvidas serão respondidas no portal do colaborador.",
    },
    {
        "id": "DOC3",
        "titulo": "Política de Jornada e Banco de Horas",
        "texto": "Nova política de jornada entra em vigor. Registro de ponto obrigatório para equipes híbridas. Banco de horas com compensação em até 90 dias.",
    },
    {
        "id": "DOC4",
        "titulo": "Single-Sign-On (SSO) nas Aplicações Internas",
        "texto": "Foi ativado o single-sign-on para meios de acesso ao e-mail, wiki e ferramentas de suporte. Senhas serão sincronizadas automaticamente.",
    },
    {
        "id": "DOC5",
        "titulo": "Guia de Reset de Senha",
        "texto": "Se você esqueceu a senha, acesse o portal de autoatendimento e escolha 'reset de senha'. Não compartilhe códigos de verificação por e-mail ou telefone.",
    },
    {
        "id": "DOC6",
        "titulo": "Alerta de Phishing",
        "texto": "Segurança alerta: e-mails falsos simulando suporte de VPN estão circulando. Não clique em links suspeitos e reporte ao SOC imediatamente.",
    },
    {
        "id": "DOC7",
        "titulo": "Acesso ao Wi-Fi Corporativo",
        "texto": "Para acesso à rede sem fio, use o SSID 'Empresa-Staff' e autentique-se com suas credenciais. O uso de VPN no escritório não é necessário.",
    },
    {
        "id": "DOC8",
        "titulo": "Política de Home Office",
        "texto": "Funcionários elegíveis podem optar por home office duas vezes por semana. É obrigatório manter disponibilidade durante a jornada e usar a VPN para sistemas internos.",
    },
    {
        "id": "DOC9",
        "titulo": "Atualização de Proxy e Bloqueio de Sites",
        "texto": "O proxy corporativo foi atualizado. Alguns sites de streaming tiveram o acesso bloqueado durante o horário comercial para priorizar banda.",
    },
    {
        "id": "DOC10",
        "titulo": "Férias e Regras de Marcação",
        "texto": "RH: solicitação de férias deve ser feita com 30 dias de antecedência. Benefícios como plano de saúde e vale-alimentação permanecem ativos durante o período.",
    },
    {
        "id": "DOC11",
        "titulo": "Backup de Arquivos no OneDrive",
        "texto": "TI recomenda salvar documentos de projetos no OneDrive corporativo. Backups automáticos rodam diariamente; acesso externo requer VPN.",
    },
    {
        "id": "DOC12",
        "titulo": "Treinamento: Boas Práticas de Segurança",
        "texto": "Inscrições abertas para treinamento de segurança: senhas fortes, dupla autenticação, uso correto de VPN e cuidados com phishing.",
    },
    {
        "id": "DOC13",
        "titulo": "Comunicado Jurídico: Adequação à LGPD",
        "texto": "A equipe jurídica informa novas diretrizes de retenção de dados e bases legais. O acesso a dados pessoais deve ser restrito a necessidade comprovada.",
    },
    {
        "id": "DOC14",
        "titulo": "Plano de Saúde: Inclusão de Dependentes",
        "texto": "Aberto o período para inclusão de dependentes no plano de saúde. Envie documentos no portal até o dia 20. Benefícios entram em vigor no mês seguinte.",
    },
    {
        "id": "DOC15",
        "titulo": "Mudança no Processo de Help Desk",
        "texto": "Chamados de TI agora devem ser abertos pelo portal. Para acesso VPN, selecione a categoria 'Rede > VPN'. Chamados por e-mail serão descontinuados.",
    },
]


# Função para preprocessar o texto: minúsculas, remoção de pontuação (exceto hífen), tokenização e remoção de stopwords.
def preprocessar_texto(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation.replace("-", "")))
    tokens = nltk.word_tokenize(texto, language="portuguese")
    tokens = [word for word in tokens if word.isalnum() or "-" in word]
    stopwords = set(nltk.corpus.stopwords.words("portuguese")) - {
        "e",
        "ou",
        "não",
        "nunca",
        "sem",
        "nem",
    }
    tokens = [word for word in tokens if word not in stopwords]
    return tokens


# Função para construir o índice invertido usando Whoosh
def construir_indice_invertido(docs):
    if os.path.exists("indexdir"):
        shutil.rmtree("indexdir")
    os.mkdir("indexdir")

    schema = Schema(
        id=ID(stored=True), titulo=TEXT(stored=True), texto=TEXT(stored=True)
    )
    index = create_in("indexdir", schema)

    writer = index.writer()
    for doc in docs:
        writer.add_document(id=doc["id"], titulo=doc["titulo"], texto=doc["texto"])
    writer.commit()
    return index


# Função de busca booleana
def buscar_booleana(query):
    parser = QueryParser("texto", schema=index.schema)
    parsed_query = parser.parse(query)

    with index.searcher() as searcher:
        results = searcher.search(parsed_query, limit=None)
        return sorted([(hit["id"], hit["texto"]) for hit in results])


# Preparar documentos
for doc in documentos:
    doc["texto"] = " ".join(preprocessar_texto(doc["texto"]))

# Construir índice invertido
index = construir_indice_invertido(documentos)

# Exemplos de consultas
consultas = [
    '("vpn" AND "acesso") AND NOT "jornada"',
    '"benefícios" OR ("plano" AND "saúde")',
    '"single-sign-on" AND NOT "senha"',
    '("plano" OR "benefícios") AND "saúde"',
    'NOT "phishing" AND "segurança"',
]

for consulta in consultas:
    resultados = buscar_booleana(consulta)
    # Retornar apenas doc_text
    resultados = [doc_text for doc_id, doc_text in resultados]
    print(f"Consulta: {consulta}\nResultados: {resultados}\n")
