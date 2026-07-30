# Métodos de Pesquisa e Ordenação

## Aula 1 — Conceitos Iniciais (30/07/2026)

### Conteúdos da disciplina

- Ordenação: conceitos e algoritmos
- Pesquisa: conceitos e algoritmos
- Pesquisa digital: algoritmos
- Tabelas Hash: conceitos e algoritmos
- Balanceamento em árvores
- Árvores B

---

## Conceitos Fundamentais

### Ordenação

É o processo de organizar uma estrutura de dados (como listas ou vetores) utilizando uma ou mais chaves.

**Objetivo:**
- Otimizar operações de busca e pesquisa.

### Pesquisa

Consiste em localizar um elemento dentro de uma estrutura de dados por meio de uma chave.

**Recuperação de dados:**
- Busca informações considerando sua relevância ou significado.

---

## Complexidade de Algoritmos

A complexidade representa o esforço computacional necessário para executar um algoritmo.

- **Alta complexidade:** maior consumo de recursos para atender o esforco imposta -> `tempo`
- **Baixa complexidade:** menor consumo de recursos.

### Notação Big-O

| Complexidade    | Nível        |
| --------------- | ------------ |
| `O(n!)`         | Muito alta   |
| `O(n^x)`        | Alta         |
| `O(n + log n)`  | Média        |
| `O(n)`          | Linear       |
| `O(log n)`      | Baixa        |

---

## Estabilidade

Refere-se ao comportamento da estrutura durante o processo de ordenação, indicando o quanto os elementos precisam ser reorganizados até que a estrutura esteja ordenada.

---

## Bubble Sort (Ordenação por Bolha)

É um método básico da programação para organizar uma lista de números:
- Compara dois itens vizinhos por vez.
- Troca-os de lugar caso estejam na ordem errada.
- Repete o processo até que a lista esteja ordenada.

---

## Dúvidas

- Como equilibrar o custo de um sistema de alta complexidade quando ele precisa lidar com muitas tarefas simples ao mesmo tempo?

# Desafio
- Criar uma classe que tenha metodos para:
  - ler dados de arquivo (inseridos um abaixo do outro) e popular em uma lista
  - exibir a lista populada
- Fazer um programa principal que tenha um menu:
  - Carregar arquivo
  - Mostrar dados do arquivo
  opcao:
