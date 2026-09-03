# Métodos de Pesquisa e Ordenação — Anotações

Anotações das aulas da disciplina.

## Índice

- [Aula 1 — Conceitos Iniciais (30/07/2026)](#aula-1--conceitos-iniciais-30072026)
- [Aula 2 — Padrão MVC](#aula-2--padrão-mvc)

---

## Aula 1 — Conceitos Iniciais (30/07/2026)

### Conteúdos da disciplina

- Ordenação: conceitos e algoritmos
- Pesquisa: conceitos e algoritmos
- Pesquisa digital: algoritmos
- Tabelas Hash: conceitos e algoritmos
- Balanceamento em árvores
- Árvores B

---

### Conceitos Fundamentais

#### Ordenação

É o processo de organizar uma estrutura de dados (como listas ou vetores) utilizando uma ou mais chaves.

**Objetivo:**
- Otimizar operações de busca e pesquisa.

#### Pesquisa

Consiste em localizar um elemento dentro de uma estrutura de dados por meio de uma chave.

**Recuperação de dados:**
- Busca informações considerando sua relevância ou significado.

---

### Complexidade de Algoritmos

A complexidade representa o esforço computacional necessário para executar um algoritmo.

- **Alta complexidade:** maior consumo de recursos para atender o esforço imposto → `tempo`
- **Baixa complexidade:** menor consumo de recursos.

#### Notação Big-O

| Complexidade    | Nível        |
| --------------- | ------------ |
| `O(n!)`         | Muito alta   |
| `O(n^x)`        | Alta         |
| `O(n + log n)`  | Média        |
| `O(n)`          | Linear       |
| `O(log n)`      | Baixa        |

---

### Estabilidade

Refere-se ao comportamento da estrutura durante o processo de ordenação, indicando o quanto os elementos precisam ser reorganizados até que a estrutura esteja ordenada.

---

### Bubble Sort (Ordenação por Bolha)

É um método básico da programação para organizar uma lista de números:

- Compara dois itens vizinhos por vez.
- Troca-os de lugar caso estejam na ordem errada.
- Repete o processo até que a lista esteja ordenada.

---

### Dúvidas

- Como equilibrar o custo de um sistema de alta complexidade quando ele precisa lidar com muitas tarefas simples ao mesmo tempo?

---

### Desafio

Criar uma classe que tenha métodos para:

- ler dados de arquivo (inseridos um abaixo do outro) e popular em uma lista
- exibir a lista populada

Fazer um programa principal que tenha um menu:

- Carregar arquivo
- Mostrar dados do arquivo

---

## Aula 2 — Padrão MVC

Conceitos do padrão **MVC (Model-View-Controller)** e sua importância na organização dos códigos.

Apresentação da ideia do projeto **IdeiaMVC**, utilizando essa arquitetura para desenvolver os trabalhos da disciplina.

A organização será dividida em:

- **Model:** responsável pelos dados e regras do sistema.
- **View:** responsável pela exibição das informações.
- **Controller:** responsável por controlar a comunicação entre Model e View.

**Objetivo:** manter o código mais organizado e separado por responsabilidades.

---

# Aula 3 - Métodos de Ordenação

Nesta aula foram estudados os seguintes métodos de ordenação:

- Bubble Sort (Ordenação por Bolha)
- Selection Sort (Ordenação por Seleção)
- Insertion Sort (Ordenação por Inserção)
- `List.Sort()` — método nativo de ordenação
do C#

# Aula 3 - Métodos de Ordenação

Métodos de ordenação são algoritmos usados para **organizar os elementos de uma lista**, por exemplo, colocando números em ordem crescente.

## 1. Bubble Sort — Ordenação por Bolha

Compara **dois elementos vizinhos** e troca eles de posição quando estão na ordem errada.

Exemplo:

`[5, 2, 4]`

- Compara `5` e `2` → troca → `[2, 5, 4]`
- Compara `5` e `4` → troca → `[2, 4, 5]`

Repete esse processo até que a lista esteja ordenada.

**Fácil de lembrar:**
> Compara os vizinhos e vai empurrando os maiores para o final.

---

## 2. Selection Sort — Ordenação por Seleção

Procura o **menor elemento** da parte que ainda não está ordenada e coloca ele na posição correta.

Exemplo:

`[5, 2, 4]`

- Procura o menor → `2`
- Coloca `2` na primeira posição → `[2, 5, 4]`
- Procura o menor restante → `4`
- Coloca `4` na segunda posição → `[2, 4, 5]`

**Fácil de lembrar:**
> Procura o menor e coloca no lugar.

---

# Aula 3 - Métodos de Ordenação

Nesta aula foram estudados os seguintes métodos de ordenação:

- Bubble Sort (Ordenação por Bolha)
- Selection Sort (Ordenação por Seleção)
- Insertion Sort (Ordenação por Inserção)
- `List.Sort()` — método nativo de ordenação do C#

Métodos de ordenação são algoritmos usados para **organizar os elementos de uma lista**, por exemplo, colocando números em ordem crescente.

## 1. Bubble Sort — Ordenação por Bolha

Compara **dois elementos vizinhos** e troca eles de posição quando estão na ordem errada.

Exemplo:

`[5, 2, 4]`

- Compara `5` e `2` → troca → `[2, 5, 4]`
- Compara `5` e `4` → troca → `[2, 4, 5]`

Repete esse processo até que a lista esteja ordenada.

**Fácil de lembrar:**

> Compara os vizinhos e vai empurrando os maiores para o final.

---

## 2. Selection Sort — Ordenação por Seleção

Procura o **menor elemento** da parte que ainda não está ordenada e coloca ele na posição correta.

Exemplo:

`[5, 2, 4]`

- Procura o menor → `2`
- Coloca `2` na primeira posição → `[2, 5, 4]`
- Procura o menor restante → `4`
- Coloca `4` na segunda posição → `[2, 4, 5]`

**Fácil de lembrar:**

> Procura o menor e coloca no lugar.

---

## 3. Insertion Sort — Ordenação por Inserção

Pega um elemento por vez e **insere ele na posição correta** entre os elementos que já estão ordenados.

É parecido com **organizar cartas na mão**.

Exemplo:

`[5, 2, 4]`

- `5` já está ordenado.
- Pega `2` e coloca antes do `5` → `[2, 5, 4]`
- Pega `4` e coloca entre `2` e `5` → `[2, 4, 5]`

**Fácil de lembrar:**

> Pega um elemento e insere no lugar certo.

---

## 4. `List.Sort()` — Ordenação Nativa

É o método de ordenação já disponível no **C#**.

Em vez de implementar um algoritmo manualmente, podemos simplesmente usar:

```csharp
lista.Sort();
```

## Aula 4
Aplicação de avaliação prática para consolidação dos conceitos de algoritmos de pesquisa e métodos de ordenação de dados.


# Aula 5 — Pesquisa e Ordenação

## Pente — Comb Sort

O **Comb Sort** é baseado no **Bubble Sort**, buscando melhorar seu desempenho.

A principal diferença é que ele realiza comparações entre elementos com uma **distância X**, fazendo uma pré-organização da lista e reduzindo a quantidade de comparações e trocas.

### Características

- **Instável**
- **Memória interna**
- Baseado no **Bubble Sort**
- Utiliza comparações com uma **distância**
- Adequado para listas/estruturas prontas

### Variáveis

- `i` → controla a posição da lista
- `houveTroca` → verifica se ocorreu troca
- `tmp` → auxiliar para troca
- `distancia` → distância entre os elementos comparados

### Distância

A distância começa com o tamanho da lista e é reduzida por `1.3`:

```java
distancia = (int) (distancia / 1.3);

Quando for menor que 1, passa a ser 1.

Exemplo:

7 → 5 → 3 → 2 → 1

Quando chega em 1, passa a comparar elementos vizinhos, como no Bubble Sort.

Exemplo
7  1  4  2  3  9  8
2  1  4  7  3  9  8
2  1  3  7  4  9  8
1  2  3  4  7  8  9

### Código

```java
void pente(List<Integer> lista) {
    boolean houveTroca;
    int tmp;
    int distancia = lista.size();

    do {
        distancia = (int) (distancia / 1.3);

        if (distancia < 1) {
            distancia = 1;
        }

        houveTroca = false;

        for (int i = 0; i + distancia < lista.size(); i++) {
            if (lista.get(i) > lista.get(i + distancia)) {
                houveTroca = true;

                tmp = lista.get(i);
                lista.set(i, lista.get(i + distancia));
                lista.set(i + distancia, tmp);
            }
        }

    } while (houveTroca || distancia > 1);
}
```



