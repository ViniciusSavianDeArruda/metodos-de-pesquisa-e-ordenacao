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

# Aula 6

Mergesort
    - Categoria de codificacao complexa
    - Complexidade: O(n * log n)
    - Implementado no ecossistema Java
    - Metodo recursivo que divide a estrtura para ordenar(principio de arvore)
        - primeiro metodo = recrusao
        - segundo metodo: Intercalacao --> aqui ocorre a ordenacao e é o retorno e é chamada na volta do empilhamento ou da chamada recursiva

Quicksort
    - Categoria de codificacao complexa
    - Complexidade: O(n * log n)
    - Implementado no ecossistema C#
    - Metodo recursivo que divide a estrtura para ordenar(principio de arvore)
        - primeiro metodo: recursao
        - segundo metodo: posicionar o pivo na estrutura
        - NUNCA divide a estrutura de forma uniforme(PIVO)



Obs: Medir o esforco é complexidade \ troca
O(h!) --> pior de todos

---

# Aula 7 — Métodos de Ordenação

## 1. Introdução

A **ordenação** organiza elementos de uma estrutura de dados e pode facilitar operações de busca e pesquisa.

## 2. Categorias de algoritmos de ordenação

### 2.1. Simplicidade de implementação

A classificação abaixo considera a facilidade de compreender e implementar os métodos (não necessariamente seu desempenho).

| Mais simples | Mais elaborados |
| --- | --- |
| Bolha (Bubble Sort) | Merge Sort |
| Seleção (Selection Sort) | Quick Sort |
| Inserção (Insertion Sort) | |
| Agitação (Shaker Sort) | |
| Pente (Comb Sort) | |

### 2.2. Estabilidade

Um algoritmo é **estável** quando preserva a ordem relativa dos elementos que possuem chaves iguais.

| Estáveis (implementações usuais) | Instáveis (implementações usuais) |
| --- | --- |
| Bolha | Seleção |
| Agitação | Pente |
| Inserção | Quick Sort |
| Merge Sort | |

> A estabilidade depende da implementação. No Pente, mesmo que a distância (`gap`) chegue a 1, as trocas feitas anteriormente podem ter alterado a ordem de elementos iguais. Por isso, o algoritmo completo continua sendo considerado instável. O mesmo cuidado vale para o Shell Sort.

### 2.3. Complexidade

A complexidade descreve como o esforço de execução cresce conforme aumenta o tamanho da entrada (`n`). Na análise de algoritmos de ordenação, é comum observar a **quantidade de comparações**, a **quantidade de trocas ou movimentações** e o tempo de execução.

| Notação | Classificação |
| --- | --- |
| `O(n!)` | Fatorial |
| `O(n^k)` | Polinomial (para `k` constante positivo) |
| `O(n²)` | Quadrática (caso particular da polinomial) |
| `O(n log n)` | Linearítmica |
| `O(n)` | Linear |
| `O(log n)` | Logarítmica |

> **Atenção:** `O(n²)` não é exponencial; uma complexidade exponencial típica é `O(2^n)`. Nem todo algoritmo com árvores tem complexidade `O(log n)` para a operação completa.

## 3. Particularidades dos métodos

- **Bolha, Agitação e Inserção:** em versões apropriadas, quando os dados já estão ordenados, podem realizar apenas `O(n)` operações no melhor caso. No Bolha e na Agitação, isso exige uma verificação de trocas para encerrar antecipadamente.
- **Pente:** usa uma distância (`gap`) entre os elementos comparados, reduzindo-a progressivamente. Quando `gap = 1`, passa a executar comparações adjacentes semelhantes às do Bolha, mas o método completo não se torna estável.
- **Seleção:** em sua implementação tradicional, continua realizando aproximadamente a mesma quantidade de comparações mesmo quando o vetor já está ordenado: `O(n²)`.
- **Merge Sort e Quick Sort:** são normalmente implementados por **divisão e conquista**, utilizando recursão.
  - **Merge Sort:** divide os dados recursivamente e ordena durante a **intercalação** das partes, na volta das chamadas recursivas.
  - **Quick Sort:** escolhe um **pivô**, particiona os elementos ao seu redor e ordena recursivamente as partições. O pivô não precisa estar na posição final em todas as variantes da partição.

> **Sobre linguagens:** Java e C# possuem bibliotecas de ordenação próprias, cujos algoritmos variam conforme o tipo de coleção e a versão da plataforma. Não é correto afirmar, de forma geral, que Java sempre utiliza Merge Sort ou C# sempre utiliza Quick Sort.

## 4. Outros métodos de ordenação

- **Shell Sort:** evolução do Inserção; realiza inserções entre elementos separados por uma distância (`gap`), que diminui até chegar a 1. É, em geral, **instável**, mesmo que a etapa final seja uma inserção com distância 1.
- **Heap Sort:** usa a estrutura lógica de uma **árvore heap**, que pode ser representada dentro de um vetor ou lista.
- **Bucket Sort:** distribui os elementos em **baldes (buckets)**, ordena cada balde e reúne os resultados. Não deve ser confundido com ordenação por dígitos.
- **Radix Sort:** ordena usando sucessivamente **dígitos ou posições** das chaves, frequentemente com um método estável de distribuição, como Counting Sort.

## 5. Exemplo de código em C# — Pente (Comb Sort)

O exemplo das anotações usa uma distância que é dividida por `1,3` a cada passagem. Portanto, representa o **Pente (Comb Sort)**, apesar de ter sido nomeado `bolha` no código original.

```csharp
using System.Collections.Generic;

public static void Pente(List<int> lista)
{
    int dist = lista.Count;
    bool houveTroca;

    do
    {
        dist = (int)(dist / 1.3);
        if (dist < 1)
        {
            dist = 1;
        }

        houveTroca = false;

        for (int i = 0; i + dist < lista.Count; i++)
        {
            if (lista[i] > lista[i + dist])
            {
                int tmp = lista[i];
                lista[i] = lista[i + dist];
                lista[i + dist] = tmp;
                houveTroca = true;
            }
        }
    } while (dist > 1 || houveTroca);
}
```

**Correção importante:** o limite do `for` é `i + dist < lista.Count`. No código original, `i + dist < lista.Count() - 1` deixava de comparar o último elemento em cada passagem.

### Como funciona

1. A distância começa no tamanho da lista.
2. A cada passagem, a distância é reduzida por um fator de `1,3`, até atingir 1.
3. Elementos separados pela distância são comparados e trocados se estiverem fora de ordem.
4. O processo termina quando a distância é 1 e uma passagem completa ocorre sem trocas.

---

### Aula 8 - Introducao a Pesquisa/ / Busca

Pesquisa ou busca é o processo de localizar um elemento específico dentro de uma coleção de dados. Existem diferentes métodos de pesquisa, cada um com suas próprias características e eficiências. A escolha do método de pesquisa adequado depende do tipo de dados, da estrutura da coleção e dos requisitos de desempenho.

Exemplos de métodos de pesquisa incluem:

- **Pesquisa Linear (Busca Sequencial)**: Examina cada elemento da coleção, um por um, até encontrar o elemento desejado ou chegar ao final da coleção. É simples, mas pode ser ineficiente para grandes conjuntos de dados.

- **Pesquisa Binária**: Requer que a coleção esteja ordenada. Divide repetidamente a coleção ao meio, comparando o elemento do meio com o elemento desejado, até encontrar o elemento ou determinar que ele não está presente. É muito eficiente para grandes conjuntos de dados ordenados.

- **Pesquisa por Interpolação**: Semelhante à pesquisa binária, mas estima a posição do elemento desejado com base em uma função de interpolação. Pode ser mais eficiente que a pesquisa binária em certas distribuições de dados.

- **Pesquisa em Árvores**: Utiliza estruturas de dados em árvore, como árvores binárias de busca, para localizar elementos. A eficiência depende da altura da árvore e da distribuição dos elementos.

- **Pesquisa em Hashing**: Utiliza funções de hash para mapear elementos a índices em uma tabela de hash, permitindo acesso rápido aos elementos. A eficiência depende da qualidade da função de hash e da gestão de colisões.

- **Pesquisa em Grafos**: Utiliza algoritmos específicos para explorar grafos, como busca em largura (BFS) e busca em profundidade (DFS), para localizar elementos ou caminhos dentro de uma estrutura de grafo.






