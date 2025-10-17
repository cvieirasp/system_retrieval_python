# Sistema de Recuperação de Informação - Curso System Retrieval

Este repositório contém implementações práticas desenvolvidas como parte do aprendizado no curso **System Retrieval**, focando em técnicas fundamentais de recuperação de informação e busca booleana.

## 📋 Descrição do Projeto

O projeto implementa um **mini-buscador booleano** que opera sobre um pequeno acervo de notícias internas de empresa. O sistema demonstra conceitos fundamentais de recuperação de informação, incluindo:

- Construção de índices invertidos
- Processamento e normalização de texto
- Implementação de busca booleana com operadores lógicos
- Uso da biblioteca Whoosh para indexação e busca

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

### Exemplos de Consultas Suportadas

```python
# Busca por documentos que contenham "vpn" E "acesso", mas NÃO "jornada"
'("vpn" AND "acesso") AND NOT "jornada"'

# Busca por documentos com "benefícios" OU a combinação de "plano" E "saúde"
'"benefícios" OR ("plano" AND "saúde")'

# Busca por "single-sign-on" excluindo documentos com "senha"
'"single-sign-on" AND NOT "senha"'
```

## 📚 Conceitos de System Retrieval Aplicados

Este projeto demonstra aplicação prática dos seguintes conceitos estudados no curso:

1. **Modelo Booleano**: Implementação de recuperação baseada em lógica booleana
2. **Índices Invertidos**: Estrutura fundamental para busca eficiente em texto
3. **Preprocessamento de Texto**: Normalização para melhorar a qualidade da busca
4. **Análise Lexical**: Tokenização e tratamento de stopwords
5. **Expressões de Consulta**: Parsing e execução de consultas complexas

## 🛠️ Dependências

```
nltk>=3.8
whoosh>=2.7.4
```

## 🚀 Como Executar

1. **Instalar dependências**:
```bash
uv add nltk whoosh
```

2. **Executar o script**:
```bash
uv run boolean-retrieval-model.py
```

3. **Resultado**: O script executará automaticamente as consultas de exemplo e exibirá os resultados correspondentes.

## 📊 Dataset

O sistema trabalha com 15 documentos simulando comunicados corporativos sobre:
- Políticas de acesso VPN
- Benefícios e planos de saúde
- Segurança da informação
- Políticas de trabalho remoto
- Procedimentos de TI

## 🎯 Objetivos de Aprendizado

- Compreender a implementação prática de sistemas de recuperação de informação
- Aplicar conceitos teóricos de indexação e busca em código Python
- Experimentar com diferentes estratégias de preprocessamento de texto
- Avaliar a eficácia de consultas booleanas em cenários reais

## 📝 Estrutura do Projeto

```
system_retrieval/
├── boolean-retrieval-model.py    # Implementação do modelo booleano
├── main.py                       # Script principal (se aplicável)
├── pyproject.toml               # Configurações do projeto
├── README.md                    # Este arquivo
└── indexdir/                    # Diretório do índice Whoosh (gerado automaticamente)
```

---

**Nota**: Este projeto é parte do material de estudo do curso System Retrieval e tem fins exclusivamente educacionais, demonstrando implementações fundamentais de técnicas de recuperação de informação.
