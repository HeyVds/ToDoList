### Sobre o projeto

Este projeto é uma aplicação de lista de tarefas (To-Do List) desenvolvida em Python utilizando o Tkinter para a interface gráfica.
Ele permite que o usuário crie, edite, exclua e marque tarefas como concluídas.
As tarefas são armazenadas em um arquivo JSON para que sejam persistentes entre as sessões.

### Objetivo

Desenvolver um aplicativo simples de controle de tarefas utilizando a biblioteca Tkinter para interface gráfica.
O aplicativo permitirá ao usuário adicionar, listar, excluir e marcar tarefas como concluídas.

### Estrutura do Projeto

O projeto está dividido em dois arquivos principais:
funcoes.py: Contém toda a lógica e funções necessárias para o funcionamento do programa.
interface.py: Responsável pela criação e organização da interface gráfica.

### Como Executar

Certifique-se de ter o Python e o Tkinter instalados.
Execute o arquivo interface.py
Adicione, edite, marque ou exclua tarefas conforme desejado.
As alterações serão salvas automaticamente.

### Funcionalidades

# Adicionar Tarefa

O usuário digita o nome da tarefa em um campo de entrada e clica no botão “Adicionar Tarefa”.
A tarefa é adicionada a um dicionário onde o nome da tarefa é a chave e seu estado (“concluída” ou “pendente”) é o valor.

# Marcar Tarefa como Concluída

Cada tarefa é exibida com um checkbox.
Quando marcado, o texto da tarefa muda de cor e estilo para indicar que foi concluída.

# Editar Tarefa

Cada tarefa tem um botão “Editar”.
Ao clicar, uma nova janela é aberta permitindo alterar o nome da tarefa.

# Excluir Tarefa

Cada tarefa tem um botão “Excluir” que remove a tarefa do dicionário.

# Persistência de Dados

Todas as tarefas são salvas automaticamente em um arquivo JSON ao serem modificadas.
Ao abrir o programa novamente, as tarefas são carregadas do arquivo JSON.

### Conclusão

Minha primeira vez utilizando o tkinter para interface gráfica, foi bastante complicado cada passo,
pois não é tão simples interagir com ele, a cada passo evoluindo o projeto foi mais desafiador,
pois precisava de algo que ele não tem suporte e precisava ajustes técnicos. No geral, a lógica em si
com python foi "tranquila". Desenvolver a parte gráfica funcional e estilizar ela foi bastante desafiadora.
Acredito que a parte mais dificil foi o checkbox, pois envolvia muita lógica e interação com todo o sistema.

### Contribuidores

VICTOR DOS SANTOS MAFRA
