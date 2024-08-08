# Engenharia-de-Software

# Projeto: Gerenciador Geral e Financeiro para Loja de Vendas

## Descrição

Este projeto tem como objetivo desenvolver um software de gerenciamento geral e de financias para a facilitação de genrencia de uma loja. O software permitirá melhor monitoramento das dividas e lucros por meio de uma base, tanto de gerenciamento e agendamento de pagamentos, como também de dados das vendas e dos clientes, e da geração de gráficos expositivos a partir dos dados recolhidos. Além de trazer funcionalidades úteis para a gerencia, como uma maior integração com redes sociais, agendamento de tarefas diarias, controle sobre programas de fidelidade,satisfação do cliente e feedback, dentre outras funções.

## Funcionalidades Principais

1. *Cadastro de Clientes*
   -
   - **História:** Como usuário, eu quero poder gerenciar os clientes no sistema para que eu possa adicionar, editar, atualizar e deletar informações dos clientes conforme necessário.
   - **Operações CRUD:** Criar, Ler, Atualizar, Excluir registros de clientes.
   - **Critérios de Aceitação:**
     1. Eu devo ser capaz de criar um novo cliente com informações básicas (nome, e-mail, telefone, endereço).
     2. Eu devo ser capaz de visualizar os detalhes do perfil do cliente.
     3. Eu devo ser capaz de atualizar as informações do cliente (nome, e-mail, telefone, endereço).
     4. Eu devo ser capaz de excluir um cliente do sistema.
     5. O sistema deve validar todas as informações de entrada para garantir a integridade dos dados.
     6. O sistema deve fornecer feedback adequado ao usuário sobre o sucesso ou falha das operações.

2. *Gerenciar Vendas*
   -
   - **História:** Como usuário, eu quero gerenciar as vendas para monitorar o desempenho e os lucros da loja, incluindo a criação, visualização, atualização e exclusão de registros de vendas.
   - **Operações CRUD:** Criar, Ler, Atualizar, Excluir registros de vendas.
   - **Critérios de Aceitação:**
     1. Eu devo ser capaz de criar uma nova venda com informações básicas (produto, quantidade, preço, data).
     2. Eu devo ser capaz de visualizar o histórico de vendas e os detalhes de cada venda.
     3. Eu devo ser capaz de atualizar as informações de uma venda (produto, quantidade, preço).
     4. Eu devo ser capaz de excluir uma venda do sistema.
     5. O sistema deve validar todas as informações de entrada para garantir a integridade dos dados.
     6. O sistema deve fornecer feedback adequado ao usuário sobre o sucesso ou falha das operações.

3. *Analisar e gerar dados de venda/lucro*
   -
   -

4. *Geração de Gráficos a partir de analises de dados de venda/lucro*
   -
   - **História:** Como usuário, eu quero visualizar gráficos a partir dos dados de venda/lucro para entender melhor as tendências e o desempenho.
   - **Operações CRUD:** N/A
   - **Critérios de Aceitação:**
     1. Eu devo ser capaz de visualizar gráficos de vendas diárias, semanais, mensais e anuais.
     2. Eu devo ser capaz de filtrar os dados exibidos nos gráficos por período.
     3. Eu devo ser capaz de exportar os gráficos como imagens ou PDFs.
     4. Os gráficos devem ser atualizados automaticamente com base nos novos dados de venda/lucro.
     5. Os gráficos devem ser interativos, permitindo zoom e detalhes específicos ao passar o mouse.

5. *Agendamento de tarefas diárias*
   - 
   - Operações CRUD: Criar, Ler, Atualizar, Excluir registros de desempenho.

6. *Integracao com redes sociais*
   -
   - **História:** Como um gerente de loja, gostaria de integrar a conta da loja com redes sociais para que eu possa compartilhar novidades, promoções e atualizações diretamente nas redes sociais e alcançar mais clientes.
   - **Operações CRUD:** N/A
   - **Critérios de Aceitação:**
      1. O gerente deve ser capaz de vincular a conta da loja com contas de redes sociais (por exemplo, Facebook, Twitter, Instagram).
      2. O gerente deve ser capaz de compartilhar atualizações, novidades e promoções diretamente nas redes sociais vinculadas.
      3. O gerente deve ter a opção de selecionar quais tipos de conteúdo deseja compartilhar automaticamente e quais deseja compartilhar manualmente.
      4. Após compartilhar uma atualização ou promoção, o sistema deve informar ao gerente que o conteúdo foi compartilhado com sucesso.
      5. Se a tentativa de compartilhamento falhar (por exemplo, devido a problemas de rede ou de API da rede social), o sistema deve informar ao gerente e sugerir tentar novamente mais tarde.

7. *Gerenciar programa de fidelidade*
   -
   - **História:** Como um gerente de loja, gostaria de gerenciar um programa de fidelidade para que eu possa recompensar clientes fiéis e incentivar novas compras.
   - **Operações CRUD:** N/A
   - **Critérios de Aceitação:**
      1. O sistema deve permitir a definição de diferentes níveis de fidelidade
      2. O sistema deve calcular e atualizar automaticamente os pontos de fidelidade dos clientes com base nas compras realizadas.
      3. O gerente deve ter acesso a relatórios detalhados sobre a participação dos clientes no programa de fidelidade, incluindo pontos acumulados, resgatados e expiração de pontos.
      4. O sistema deve fornecer métricas sobre a eficácia do programa, como aumento nas vendas e frequência de visitas dos clientes fiéis.
      5. O sistema deve notificar os clientes sobre suas atividades de fidelidade, incluindo pontos ganhos, mudanças de nível e expiração de pontos.
      6. Se houver um erro durante a configuração do programa, o sistema deve informar ao gerente e fornecer instruções sobre como resolver o problema.

8. *Receber feedback e satisfação do cliente*
   - 
   -

9. *Notificações de estoque*
   -
   -
10. *Gerenciar datas de pagamento/eventos*
    -
      - **História:** Como usuário, eu quero gerenciar as datas de pagamento dos meus funcionários, as datas de reabastecimento do estoque e controle sobre os eventos realizados na loja.
      - **Operações CRUD:** Criar, Ler, Atualizar, Excluir datas específicas no calendário.
      - **Critérios de Aceitação:**
        1. O sistema deve permitir ao usuário adicionar, ler, alterar e excluir um novo evento com campos para título, descrição, data, hora e tipo de evento.
        2. O sistema deve permitir ao usuário registrar, ler, alterar e excluir um novo pagamento com campos para valor, data, destinatário e descrição.
        3. O sistema deve permitir ao usuário criar, ler, alterar e excluir uma nova promoção com campos para título, descrição, percentual de desconto e datas de validade.
    
## Backlog do Produto
   1. Cadastro de Clientes
   2. Gestão de Vendas
   3. Analise e geração de dados de venda/lucro
   4. Geração de Gráficos a partir de analises de dados de venda/lucro
   5. Agendamento de tarefas diárias
   6. Integracao com redes sociais
   7. Gestão de programa de fidelidade
   8. Gestão de feedback e satisfação do cliente
   9. Notificações
   10. Gestão de datas de pagamento

## Backlog da Sprint (Primeira Sprint - 5 Histórias Principais)

1. *Cadastro de Clientes*
   - **Tarefas:**
     - Configurar Banco de Dados
       - Escolher o sistema de gerenciamento de banco de dados.
       - Configurar o banco de dados no servidor de desenvolvimento.
       - Definir o esquema do banco de dados.
       - Implementar migrações.
       - Testar a conexão entre backend e banco de dados.
     - Criar Cliente
       - Criar formulário de entrada.
       - Implementar validação do formulário.
       - Desenvolver API de criação.
       - Integrar frontend com API.
       - Testar criação de cliente.
       - Implementar notificações.
     - Visualizar Clientes
       - Criar página de listagem.
       - Desenvolver API de listagem.
       - Integrar frontend com API.
       - Implementar paginação/filtros.
       - Testar visualização de clientes.
     - Editar Cliente
       - Criar formulário de edição.
       - Implementar validação do formulário.
       - Desenvolver API de atualização.
       - Integrar frontend com API.
       - Testar edição de cliente.
       - Implementar notificações.
     - Deletar Cliente
       - Desenvolver API de deleção.
       - Integrar frontend com API.
       - Implementar confirmação de deleção.
       - Testar deleção de cliente.
       - Implementar notificações.

2. *Gestão de Vendas*
   - **Tarefas:**
     - **Configurar Banco de Dados**
       - Escolher o sistema de gerenciamento de banco de dados.
       - Configurar o banco de dados para registros de vendas.
       - Definir o esquema do banco de dados para vendas.
       - Implementar migrações.
       - Testar a conexão entre backend e banco de dados.
     - **Criar Venda**
       - Criar formulário de entrada para registro de vendas.
       - Implementar validação do formulário de vendas.
       - Desenvolver API de criação de venda.
       - Integrar frontend com API de vendas.
       - Testar criação de venda.
       - Implementar notificações de sucesso e erro.
     - **Visualizar Vendas**
       - Criar página de listagem de vendas.
       - Desenvolver API para listagem de vendas.
       - Integrar frontend com API.
       - Implementar filtros e pesquisa para visualização de vendas.
       - Testar a visualização de vendas.
     - **Editar Venda**
       - Criar formulário de edição de venda.
       - Implementar validação do formulário de edição.
       - Desenvolver API de atualização de venda.
       - Integrar frontend com API.
       - Testar atualização de venda.
       - Implementar notificações de sucesso e erro.
     - **Deletar Venda**
       - Adicionar funcionalidade de exclusão de venda.
       - Desenvolver API para exclusão de venda.
       - Integrar frontend com API.
       - Implementar confirmação de exclusão.
       - Testar exclusão de venda.
       - Implementar notificações de sucesso e erro.

3. *Geração de Gráficos a partir de analises de dados de venda/lucro*
   - **Tarefas:**
     - Configurar Ambiente de Gráficos
       - Escolher a biblioteca de gráficos.
       - Configurar o ambiente de desenvolvimento para suportar gráficos.
     - Desenvolver API de Dados
       - Desenvolver API para fornecer dados de venda/lucro.
       - Implementar endpoints para fornecer dados agregados por dia, semana, mês e ano.
       - Testar a API de dados para garantir a precisão e desempenho.
     - Implementar Tela de Gráficos
       - Criar a interface de usuário para exibir gráficos.
       - Integrar a interface com a API de dados.
       - Implementar filtros de período na interface.
       - Implementar funcionalidade de exportação de gráficos.
     - Testar Gráficos
       - Testar a atualização automática dos gráficos com novos dados.
       - Testar a interatividade dos gráficos (zoom, detalhes ao passar o mouse).
       - Realizar testes de usabilidade para garantir que os gráficos sejam intuitivos.
     - Implementar Notificações
       - Implementar notificações de erro/sucesso para operações de geração e exportação de gráficos.

4. *Gestão de datas de pagamento*
   - **Tarefas:**
      - Desenvolvimento do Módulo de Agendamento de Eventos:
         - Permitir ao usuário inserir, editar e excluir eventos no calendário.
         - Adicionar funcionalidade de lembretes com notificações.
      - Integração com Sistemas de Pagamento:
         - Implementar a funcionalidade de agendamento de pagamentos automáticos para fornecedores e funcionários.
         - Configurar alertas para insuficiência de fundos no caixa da empresa antes da data do pagamento.
      - Monitoramento de Caixa:
         - Criar um painel de controle que mostre o saldo do caixa em tempo real.
         - Incluir previsões de fluxo de caixa com base nos pagamentos e recebimentos programados.
      - Relatórios Financeiros:
         - Desenvolver relatórios financeiros mensais que mostrem todas as transações realizadas, pendentes e programadas.
         - Implementar gráficos e tabelas que ajudam na visualização dos dados financeiros.
      - Personalização da Agenda:
         - Permitir ao usuário personalizar a visualização da agenda (diária, semanal, mensal).
         - Adicionar a possibilidade de categorizar eventos e pagamentos (por exemplo, urgentes, regulares, esporádicos).
      - Notificações e Alertas:
         - Implementar um sistema de notificações para alertar sobre eventos importantes e pagamentos próximos.
         - Personalizar os métodos de notificação (e-mail, SMS, notificações push).
  

5. *Gestão de feedback e satisfação do cliente*
   - **Tarefas:**
     - Criar formulário de satisfação do cliente.
     - Separar avaliações individualmente e somá-las em uma média de satisfação geral.
     - Implementar a recepção dos dados do formulário no aplicativo:
        - Associar o ID ao cliente que preencheu o formulário;
        - Associar entrega à data do formulário.
     - Desenvolver interface de feedback do cliente no aplicativo.
     
## Linguagens/API's Utilizadas:
   - Python

## Mebros e Funções:

  - Gabriel Castro: Backend , Tester
  - Carlos Gabriel: Backend , Banco de Dados
  - Henrique Guimarães: Backend , Tester
  - Patrick Peres: FrontEnd
  - Luan: Full-Stack
  - Gustavo: BackEnd , Bancos de Dados

