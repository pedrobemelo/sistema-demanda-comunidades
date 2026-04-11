# Sistema de Demanda de Comunidades (SDC)

## Descrição do Problema

Em muitas comunidades locais, demandas como buracos nas ruas, falta de iluminação pública, lixo acumulado e problemas de infraestrutura são registradas de forma desorganizada, geralmente por meio de conversas informais (como WhatsApp ou comunicação verbal).

Essa falta de organização dificulta o acompanhamento, priorização e resolução desses problemas.

---

## Solução Proposta

O **Sistema de Demanda de Comunidades (SDC)** é uma aplicação de linha de comando (CLI) desenvolvida em Python que permite registrar, organizar e acompanhar demandas de uma comunidade de forma simples e estruturada.

---

## Público-Alvo

*Moradores de comunidades
*Líderes comunitários
*Associações locais
*Pequenos grupos organizados

---

## Funcionalidades

*Criar demanda
*Listar demandas
*Atualizar status (Aberto, Em andamento, Resolvido)
*Remover demanda
*Persistência em arquivo JSON

---

## Interface

A aplicação utiliza uma **interface CLI (linha de comando)** com menu interativo, permitindo que o usuário execute operações diretamente pelo terminal.

---

## Tecnologias Utilizadas

*Python 3
*Pytest (testes automatizados)
*Ruff (lint / análise estática)
*GitHub Actions (integração contínua)

---

## Estrutura do Projeto

```
sistema_demanda_comunidade/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── demand.py
│   └── storage.py
│
├── data/
│   └── demands.json
│
├── tests/
│   └── test_demand.py
│
├── requirements.txt
├── README.md
├── VERSION
└── .github/workflows/ci.yml
```

---

## Instalação

```bash
git clone https://github.com/pedrobemelo/sistema-demanda-comunidades.git
cd sistema_demanda_comunidade
python -m pip install -r requirements.txt
```

---

## Execução

```bash
python -m src.main
```

---

## Testes Automatizados

```bash
python -m pytest
```

Os testes cobrem:

* criação de demanda
* validação de entrada inválida
* atualização de status

---

## Lint (Qualidade de Código)

```bash
python -m ruff check .
```

---

## Integração Contínua (CI)

O projeto utiliza **GitHub Actions** para:

*instalar dependências
*executar lint
*rodar testes automaticamente a cada push ou pull request

---

## Versionamento

Versão atual:

```
1.0.0
```

Seguindo o padrão **SemVer (MAJOR.MINOR.PATCH)**.

---

## Tratamento de Erros

O sistema possui validações importantes:

*impede criação de demandas com título vazio
*trata erros de leitura de JSON (arquivo corrompido ou vazio)

---

## Exemplo de Uso

```
=== Sistema de Demanda de Comunidades ===
1 - Criar demanda
2 - Listar demandas
3 - Atualizar status
4 - Remover demanda
5 - Sair
```

---

## Autor

Pedro Bernardo Eseteves Melo - RA:22505626

---

## Repositório

https://github.com/pedrobemelo/sistema-demanda-comunidades
