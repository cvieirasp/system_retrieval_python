# Sistema de Recuperação de Informação - Curso System Retrieval

Este repositório contém implementações práticas desenvolvidas como parte do aprendizado no curso **System Retrieval**, focando em técnicas fundamentais de recuperação de informação, busca booleana e modelo vetorial.

## 📋 Descrição do Projeto

O projeto implementa dois modelos clássicos de recuperação de informação operando sobre um pequeno acervo de notícias internas de empresa. O sistema demonstra conceitos fundamentais de recuperação de informação, incluindo:

- Construção de índices invertidos
- Processamento e normalização de texto
- Implementação de busca booleana com operadores lógicos
- Modelo de espaço vetorial com TF-IDF
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
- **Snippets**: Exibição de trechos relevantes dos documentos encontrados

## 🔍 Exemplos de Uso

### Consultas Booleanas

```python
# Busca por documentos que contenham "vpn" E "acesso", mas NÃO "jornada"
'("vpn" AND "acesso") AND NOT "jornada"'

# Busca por documentos com "benefícios" OU a combinação de "plano" E "saúde"
'"benefícios" OR ("plano" AND "saúde")'

# Busca por "single-sign-on" excluindo documentos com "senha"
'"single-sign-on" AND NOT "senha"'
```

### Consultas Vetoriais

```python
# Busca ranqueada por relevância
consulta = "plano de saúde"
# Retorna: documentos ordenados por similaridade cosseno

consulta = "segurança VPN acesso"
# Retorna: top-5 documentos mais similares com scores
```

## 📚 Conceitos de System Retrieval Aplicados

Este projeto demonstra aplicação prática dos seguintes conceitos estudados no curso:

### Modelo Booleano
1. **Recuperação Exata**: Implementação de lógica booleana estrita
2. **Índices Invertidos**: Estrutura fundamental para busca eficiente
3. **Expressões Complexas**: Parsing e execução de consultas com parênteses

### Modelo Vetorial
1. **TF-IDF**: Cálculo de peso dos termos baseado em frequência e raridade
2. **Espaço Vetorial**: Representação de documentos como vetores numéricos
3. **Similaridade Cosseno**: Medida de similaridade angular entre vetores
4. **Ranqueamento**: Ordenação de resultados por relevância

### Processamento de Texto
1. **Normalização**: Conversão para minúsculas e remoção de pontuação
2. **Tokenização**: Divisão do texto em unidades lexicais
3. **Stopwords**: Remoção de palavras funcionais em português
4. **Preservação Contextual**: Manutenção de termos compostos com hífen

## 🛠️ Dependências

```
nltk>=3.8
whoosh>=2.7.4
scikit-learn>=1.3.0
```

## 🚀 Como Executar

1. **Instalar dependências**:
```bash
uv add nltk whoosh scikit-learn
```

2. **Executar os scripts**:

```bash
# Modelo Booleano
uv run boolean-retrieval-model.py

# Modelo Vetorial
uv run vector-space-model.py
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

| Aspecto | Modelo Booleano | Modelo Vetorial |
|---------|----------------|-----------------|
| **Tipo de busca** | Exata (sim/não) | Ranqueada por relevância |
| **Operadores** | AND, OR, NOT, () | Termos com pesos TF-IDF |
| **Resultados** | Conjunto não ordenado | Lista ordenada por score |
| **Flexibilidade** | Consultas precisas | Consultas aproximadas |
| **Uso ideal** | Busca específica | Exploração e descoberta |

## 🎯 Objetivos de Aprendizado

- **Implementar** dois modelos fundamentais de recuperação de informação
- **Comparar** abordagens booleana vs. vetorial na prática
- **Experimentar** diferentes estratégias de preprocessamento de texto
- **Avaliar** a eficácia de consultas em cenários corporativos reais
- **Compreender** trade-offs entre precisão e recall

## 📝 Estrutura do Projeto

```
system_retrieval/
├── boolean-retrieval-model.py    # Implementação do modelo booleano
├── vector-space-model.py         # Implementação do modelo vetorial TF-IDF
├── pyproject.toml               # Configurações do projeto
├── README.md                    # Este arquivo
└── indexdir/                    # Diretório do índice Whoosh (gerado automaticamente)
```

---

**Nota**: Este projeto é parte do material de estudo do curso System Retrieval e tem fins exclusivamente educacionais, demonstrando implementações fundamentais de técnicas clássicas de recuperação de informação.
