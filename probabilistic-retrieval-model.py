"""
Enunciado:

Implemente um ranqueador BM25 para um pequeno acervo de notícias internas de empresa.
Os documentos estarão em memória como uma lista de dicionários: [{ "id": "DOC1", "titulo": "...", "texto": "..." }, ...].
Pipeline de texto: tokenização simples, minúsculas, remoção de stopwords.
Vetorize os documentos usando o modelo BM25.
Calcule a pontuação BM25 entre a consulta e os documentos.
Retorne os documentos mais relevantes à consulta.
"""

import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from rank_bm25 import BM25Okapi

nltk.download("punkt_tab")
nltk.download("stopwords")

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


# Pré-processamento: tokenização, minúsculas e remoção de stopwords
def preprocessar_texto(texto):
    texto = texto.lower()
    tokens = word_tokenize(texto)
    stop_words = set(stopwords.words("portuguese"))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return tokens


# Construir modelo BM25
def construir_bm25(documentos):
    corpus = [preprocessar_texto(doc["texto"]) for doc in documentos]
    bm25 = BM25Okapi(corpus)
    return bm25


# Pesquisar usando BM25
def pesquisar_bm225(consulta, bm25):
    consulta_tokens = preprocessar_texto(consulta)
    scores = bm25.get_scores(consulta_tokens)
    return scores


# Exemplo de consulta
consulta = "plano de saúde"

# Construir modelo BM25
bm25 = construir_bm25(documentos)

# Pesquisar usando BM25
resultados = pesquisar_bm225(consulta, bm25)

# Exibir resultados
for i in np.argsort(resultados)[::-1]:
    print(f"Documento: {i}: {documentos[i]}")
