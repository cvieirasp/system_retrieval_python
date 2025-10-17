# Sistema de Recuperação de Informação - Curso System Retrieval

Este repositório contém implementações práticas desenvolvidas como parte do aprendizado no curso **System Retrieval**, focando em técnicas fundamentais de recuperação de informação, busca booleana, modelo vetorial e modelo probabilístico.

## 📋 Descrição do Projeto

O projeto implementa três modelos clássicos de recuperação de informação operando sobre um pequeno acervo de notícias internas de empresa. O sistema demonstra conceitos fundamentais de recuperação de informação, incluindo:

- Construção de índices invertidos
- Processamento e normalização de texto
- Implementação de busca booleana com operadores lógicos
- Modelo de espaço vetorial com TF-IDF
- Modelo probabilístico BM25
- Cálculo de similaridade cosseno
- Ranqueamento de documentos por relevância

## 🔧 Funcionalidades

### Boolean Retrieval Model (`boolean-retrieval-model.py`)

**Objetivo**: Implementar um sistema de busca booleana sobre documentos corporativos.

**Características principais**:
- **Índice Invertido**: Mapeamento de termos para IDs de documentos usando Whoosh
- **Preprocessamento de Texto**: 
  - Conversão para minúsculas
  - Remoção de pontuação (preservando hífens)
  - Tokenização com NLTK
  - Remoção de stopwords em português
- **Busca Booleana**: Suporte a operadores `AND`, `OR`, `NOT` e parênteses
- **Dataset**: 15 documentos simulando notícias internas corporativas

### Vector Space Model (`vector-space-model.py`)

**Objetivo**: Implementar um ranqueador VSM com TF-IDF e similaridade cosseno.

**Características principais**:
- **Vetorização TF-IDF**: Conversão de documentos em vetores usando scikit-learn
- **Preprocessamento**: Tokenização, minúsculas e remoção de stopwords (pt-BR)
- **Similaridade Cosseno**: Cálculo de similaridade entre consulta e documentos
- **Ranqueamento**: Retorna top-K documentos mais similares à consulta

### Probabilistic Retrieval Model (`probabilistic-retrieval-model.py`)

**Objetivo**: Implementar um ranqueador probabilístico usando BM25.

**Características principais**:
- **Modelo BM25**: Implementação do algoritmo BM25 (Best Matching 25)
- **Preprocessamento**: Tokenização, minúsculas e remoção de stopwords em português
- **Ranqueamento Probabilístico**: Scoring baseado em probabilidade de relevância
- **Corpus Tokenizado**: Processamento otimizado para documentos corporativos
- **Biblioteca rank-bm25**: Uso da implementação BM25Okapi

## 🛠️ Dependências

```
nltk>=3.8
whoosh>=2.7.4
scikit-learn>=1.3.0
rank-bm25>=0.2.2
numpy>=1.24.0
```

## 🚀 Como Executar

1. **Instalar dependências**:
```bash
uv add nltk whoosh scikit-learn rank-bm25 numpy
```

2. **Executar os scripts**:

```bash
# Modelo Booleano
uv run boolean-retrieval-model.py

# Modelo Vetorial
uv run vector-space-model.py

# Modelo Probabilístico BM25
uv run probabilistic-retrieval-model.py
```

3. **Resultado**: Os scripts executarão automaticamente consultas de exemplo e exibirão os resultados correspondentes.

## 📊 Dataset

O sistema trabalha com 15 documentos simulando comunicados corporativos sobre:
- Políticas de acesso VPN e conectividade
- Benefícios e planos de saúde
- Segurança da informação e phishing
- Políticas de trabalho remoto e jornada
- Procedimentos de TI e help desk
- Backup e armazenamento de dados
- Adequação à LGPD

## 📈 Comparação dos Modelos

| Aspecto | Modelo Booleano | Modelo Vetorial | Modelo Probabilístico |
|---------|----------------|-----------------|--------------------|
| **Tipo de busca** | Exata (sim/não) | Ranqueada por relevância | Ranqueada probabilisticamente |
| **Operadores** | AND, OR, NOT, () | Termos com pesos TF-IDF | Termos com scores BM25 |
| **Resultados** | Conjunto não ordenado | Lista ordenada por similaridade cosseno | Lista ordenada por probabilidade |
| **Flexibilidade** | Consultas precisas | Consultas aproximadas | Balanceamento TF/IDF otimizado |
| **Uso ideal** | Busca específica | Exploração e descoberta | Recuperação de alta precisão |
| **Algoritmo base** | Álgebra booleana | Álgebra linear (vetores) | Teoria da probabilidade |

## 🎯 Objetivos de Aprendizado

- **Implementar** três modelos fundamentais de recuperação de informação
- **Comparar** abordagens booleana, vetorial e probabilística na prática
- **Experimentar** diferentes estratégias de preprocessamento de texto
- **Avaliar** a eficácia de consultas em cenários corporativos reais
- **Compreender** trade-offs entre precisão e recall

## 📝 Estrutura do Projeto

```
├── boolean-retrieval-model.py       # Implementação do modelo booleano
├── vector-space-model.py           # Implementação do modelo vetorial 
├── probabilistic-retrieval-model.py # Implementação do modelo probabilístico BM25
├── pyproject.toml                  # Configurações do projeto
├── README.md                       # Este arquivo
```

---

**Nota**: Este projeto é parte do material de estudo do curso System Retrieval e tem fins exclusivamente educacionais, demonstrando implementações fundamentais de técnicas clássicas de recuperação de informação.
