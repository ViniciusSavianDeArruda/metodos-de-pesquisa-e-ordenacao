# Pesquisa de Nomes em Java

Projeto desenvolvido em **Java**, utilizando a arquitetura **MVC (Model-View-Controller)** e uma interface gráfica com **Java Swing**, criada no NetBeans.

O sistema permite cadastrar nomes, impedir cadastros duplicados e realizar pesquisas por prefixo utilizando os algoritmos de pesquisa sequencial e Trie.

## Funcionalidades

- Cadastro de nomes.
- Verificação de nomes duplicados.
- Pesquisa automática enquanto o usuário digita.
- Busca por prefixo utilizando Trie.
- Pesquisa que ignora letras maiúsculas, minúsculas e acentos.
- Exibição dos resultados em uma tabela (`JTable`).

## Estrutura do projeto

O projeto foi dividido em duas partes:

### 1. PesquisaLib — Biblioteca de algoritmos

Contém os algoritmos utilizados pelo sistema.

- **Normalizador.java:** padroniza os textos, removendo acentos, diferenças entre maiúsculas e minúsculas e espaços excedentes.
- **PesquisaSequencial.java:** percorre a lista de nomes para verificar se um nome já está cadastrado.
- **Trie.java:** implementa a estrutura Trie para pesquisar nomes pelas letras iniciais.

A biblioteca é compilada em um arquivo `PesquisaLib.jar`, utilizado pela aplicação principal.

### 2. PesquisaView — Aplicação MVC

Responsável pelo cadastro, pela interface gráfica e pela comunicação com a biblioteca.

- **NomesModel.java:** armazena os nomes em uma lista e utiliza os algoritmos da biblioteca.
- **NomesView.java:** contém a interface gráfica desenvolvida com Java Swing, incluindo campos de texto, botão de cadastro e tabela de resultados.
- **NomesController.java:** recebe as ações do usuário e faz a comunicação entre o Model e a View.
- **Main.java:** inicia o programa e conecta as classes do MVC.

## Tecnologias utilizadas

- Java
- Java Swing
- Apache NetBeans
- Arquitetura MVC
- Estrutura de dados Trie
- Pesquisa sequencial
- Biblioteca JAR

## Como executar

1. Abra os projetos no Apache NetBeans.
2. Compile a biblioteca `PesquisaLib`.
3. Adicione o arquivo `PesquisaLib.jar` às bibliotecas da aplicação principal.
4. Execute a classe `Main.java`.

## Observações

Os nomes são armazenados apenas durante a execução do programa, sem utilização de banco de dados.

O projeto foi desenvolvido para praticar algoritmos de pesquisa, estruturas de dados, criação de interfaces gráficas e organização de código utilizando MVC.
