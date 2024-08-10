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
     1. O gerente deve ser capaz de criar um novo cliente com informações básicas (nome, e-mail, telefone, endereço).
     2. O gerente deve ser capaz de visualizar os detalhes do perfil do cliente.
     3. O gerente deve ser capaz de atualizar as informações do cliente (nome, e-mail, telefone, endereço).
     4. O gerente deve ser capaz de excluir um cliente do sistema.
     5. O sistema deve validar todas as informações de entrada para garantir a integridade dos dados.
     6. O sistema deve fornecer feedback adequado ao usuário sobre o sucesso ou falha das operações.

2. *Gerenciar Vendas*
   -
   - **História:** Como usuário, eu quero gerenciar as vendas para monitorar o desempenho e os lucros da loja, incluindo a criação, visualização, atualização e exclusão de registros de vendas.
   - **Operações CRUD:** Criar, Ler, Atualizar, Excluir registros de vendas.
   - **Critérios de Aceitação:**
     1. O gerente deve ser capaz de criar uma nova venda com informações básicas (produto, quantidade, preço, data).
     2. O gerente deve ser capaz de visualizar o histórico de vendas e os detalhes de cada venda.
     3. O gerente deve ser capaz de atualizar as informações de uma venda (produto, quantidade, preço).
     4. O gerente deve ser capaz de excluir uma venda do sistema.
     5. O sistema deve validar todas as informações de entrada para garantir a integridade dos dados.
     6. O sistema deve fornecer feedback adequado ao usuário sobre o sucesso ou falha das operações.

3. *Analisar e gerar dados de venda/lucro*
   -
   - **História:** Como usuário, eu quero gerar dados a partir das vendas registradas no sistema para visualizar o lucro gerado em determinada data.
   - **Operações CRUD:** N/A
   - **Critérios de Aceitação:**
     1. O gerente deve ser capaz de visualizar o total de lucro gerado em determinada data, já contabilizando os custos atrelados.
     2. O gerente deve ser capaz de gerar uma nota de qualquer período com os lucros associados.

4. *Geração de Gráficos a partir de analises de dados de venda/lucro*
   -
   - **História:** Como usuário, eu quero visualizar gráficos a partir dos dados de venda/lucro para entender melhor as tendências e o desempenho.
   - **Operações CRUD:** N/A
   - **Critérios de Aceitação:**
     1. O gerente deve ser capaz de visualizar gráficos de vendas diárias, semanais, mensais e anuais.
     2. O gerente deve ser capaz de filtrar os dados exibidos nos gráficos por período.
     3. O gerente deve ser capaz de exportar os gráficos como imagens ou PDFs.
     4. Os gráficos devem ser atualizados automaticamente com base nos novos dados de venda/lucro.
     5. Os gráficos devem ser interativos, permitindo zoom e detalhes específicos ao passar o mouse.

5. *Agendamento de tarefas diárias*
   - 
   - **História:** Como um gerente de loja, gostaria de poder ter uma agenda digital para visualizar e criar eventos para tarefas diárias próprias.
   - **Operações CRUD:** Criar, Ler, Atualizar, Excluir tarefas.
     1. O gerente deve ser capaz de criar uma tarefa e afixar um horário para ela.
     2. O gerente deve ser capaz de atualizar uma tarefa ou mudar o horário dela.
     3. O gerente deve ser capaz de apagar uma tarefa.

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
   - **História:** Como um gerente de loja, gostaria de receber feedback e satisfação do cliente por meio de formulários do Google Forms que estariam disponiveis no site da loja.
   - **Operações CRUD:** Ler e Excluir respostas.
   - **Critérios de Aceitação:**
      1. O sistema deve acessar as respostas enviadas pelo Google Forms e registrar o feedback no banco de dados interno.
      2. O gerente deve ser capaz de apagar formulários ja lidos.
      3. O sistema deve ser capaz de apagar formulários automaticamente após certa quantidade.
      4. O gerente deve visualizar um resumo das respostas.
      5. O sistema deve permitir a exportação das respostas para análise mais detalhada em formatos comuns (CSV, Excel, etc.).
      6. O sistema deve notificar o gerente quando uma nova resposta de feedback é recebida.

9. *Notificações de estoque*
   -
   - **História:** Como um gerente de loja, gostaria de receber ntificações sobre o estado do estoque de cada produto.
   - **Operações CRUD:** Criar, Ler, Atualizar, Excluir estoque de certo produto.
   - **Critérios de Aceitação:**
      1. O gerente deve ser adicionar o estoque de cada produto e um limite critíco para o mesmo.
      2. O gerente deve ser capaz de atualizar o estoque.
      3. O sistema deve ser capaz de apagar estoque não existente.
      4. O gerente deve ser capaz de visualizar o estoque e receber notificações quando em estado crítico.
      5. O sistema deve ser capaz de gerar notificações "pop-ups" para notificar sobre a situação atual do estoque.
         
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
     - **Configurar Banco de Dados**
       - Escolher o sistema de gerenciamento de banco de dados. Responsáveis: Carlos
       - Configurar o banco de dados no servidor de desenvolvimento. Responsáveis: Gustavo
       - Definir o esquema do banco de dados. Responsáveis: Gustavo
       - Implementar migrações. Responsáveis: Carlos
       - Testar a conexão entre backend e banco de dados. Responsáveis: Henrique
     - **Criar Cliente**
       - Criar formulário de entrada. Responsáveis: Gabriel
       - Implementar validação do formulário. Responsáveis: Gabriel
       - Desenvolver API de criação. Responsáveis: Gabriel
       - Integrar frontend com API.   Responsáveis: Luan
       - Testar criação de cliente. Responsáveis: Henrique
       - Implementar notificações.   Responsáveis: Patrick
     - **Visualizar Clientes**
       - Criar página de listagem. Responsáveis: Gabriel
       - Desenvolver API de listagem. Responsáveis: Gustavo
       - Integrar frontend com API.   Responsáveis:Luan
       - Implementar paginação/filtros. Responsáveis: Gabriel
       - Testar visualização de clientes.   Responsáveis: Patrick
     - **Editar Cliente**
       - Criar formulário de edição. Responsáveis: Carlos
       - Implementar validação do formulário. Responsáveis: Gustavo
       - Desenvolver API de atualização. Responsáveis: Gustavo
       - Integrar frontend com API.   Responsáveis: Luan
       - Testar edição de cliente. Responsáveis: Henrique
       - Implementar notificações.   Responsáveis: Luan
     - **Deletar Cliente**
       - Desenvolver API de deleção. Responsáveis: Gustavo
       - Integrar frontend com API.   Responsáveis: Patrick
       - Implementar confirmação de deleção. Responsáveis: Henrique
       - Testar deleção de cliente. Responsáveis: Henrique
       - Implementar notificações.   Responsáveis: Luan

2. *Gestão de Vendas*
   - **Tarefas:**
     - **Configurar Banco de Dados**
       - Escolher o sistema de gerenciamento de banco de dados. Responsáveis: Carlos
       - Configurar o banco de dados para registros de vendas. Responsáveis: Carlos
       - Definir o esquema do banco de dados para vendas. Responsáveis: Carlos
       - Implementar migrações. Responsáveis: Carlos
       - Testar a conexão entre backend e banco de dados. Responsáveis: Henrique
     - **Criar Venda**
       - Criar formulário de entrada para registro de vendas. Responsáveis: Gabriel
       - Implementar validação do formulário de vendas. Responsáveis: Carlos
       - Desenvolver API de criação de venda. Responsáveis: Carlos
       - Integrar frontend com API de vendas. Responsáveis: Gabriel
       - Testar criação de venda. Responsáveis: Henrique
       - Implementar notificações de sucesso e erro.Responsáveis: Gabriel
     - **Visualizar Vendas**
       - Criar página de listagem de vendas. Responsáveis: Gabriel
       - Desenvolver API para listagem de vendas. Responsáveis: Carlos
       - Integrar frontend com API.   Responsáveis: Patrick
       - Implementar filtros e pesquisa para visualização de vendas.
       - Testar a visualização de vendas. Responsáveis: Henrique
     - **Editar Venda**
       - Criar formulário de edição de venda. Responsáveis: Gustavo
       - Implementar validação do formulário de edição. Responsáveis: Gustavo
       - Desenvolver API de atualização de venda. Responsáveis: Gustavo
       - Integrar frontend com API.   Responsáveis: Patrick
       - Testar atualização de venda. Responsáveis: Henrique
       - Implementar notificações de sucesso e erro.   Responsáveis: Luan
     - **Deletar Venda**
       - Adicionar funcionalidade de exclusão de venda. Responsáveis: Gustavo
       - Desenvolver API para exclusão de venda. Responsáveis: Gustavo
       - Integrar frontend com API.   Responsáveis: Patrick
       - Implementar confirmação de exclusão. Responsáveis: Henrique
       - Testar exclusão de venda. Responsáveis: Henrique
       - Implementar notificações de sucesso e erro.   Responsáveis: Luan

3. *Geração de Gráficos a partir de analises de dados de venda/lucro*
   - **Tarefas:**
     - **Configurar Ambiente de Gráficos**
       - Escolher a biblioteca de gráficos. Responsáveis: Carlos
       - Configurar o ambiente de desenvolvimento para suportar gráficos. Responsáveis: Carlos
     - **Desenvolver API de Dados** 
       - Desenvolver API para fornecer dados de venda/lucro. Responsáveis: Gustavo
       - Implementar endpoints para fornecer dados agregados por dia, semana, mês e ano. Responsáveis: Carlos
       - Testar a API de dados para garantir a precisão e desempenho. Responsáveis: Henrique
     - **Implementar Tela de Gráficos**
       - Criar a interface de usuário para exibir gráficos.   Responsáveis: Patrick
       - Integrar a interface com a API de dados.   Responsáveis: Patrick
       - Implementar filtros de período na interface.   Responsáveis: Luan
       - Implementar funcionalidade de exportação de gráficos. Responsáveis: Gabriel
     - **Testar Gráficos**
       - Testar a atualização automática dos gráficos com novos dados. Responsáveis: Gabriel
       - Testar a interatividade dos gráficos (zoom, detalhes ao passar o mouse). Responsáveis: Gabriel
       - Realizar testes de usabilidade para garantir que os gráficos sejam intuitivos. Responsáveis: Gabriel
     - **Implementar Notificações**
       - Implementar notificações de erro/sucesso para operações de geração e exportação de gráficos.   Responsáveis: Luan

4. *Gestão de datas de pagamento*
   - **Tarefas:**
      - **Desenvolvimento do Módulo de Agendamento de Eventos:**
         - Permitir ao usuário inserir, editar e excluir eventos no calendário. Responsáveis: Henrique
         - Adicionar funcionalidade de lembretes com notificações. Responsáveis: Henrique
      - **Integração com Sistemas de Pagamento:**
         - Implementar a funcionalidade de agendamento de pagamentos automáticos para fornecedores e funcionários. Responsáveis: Henrique
         - Configurar alertas para insuficiência de fundos no caixa da empresa antes da data do pagamento. Responsáveis: Gabriel
      - **Monitoramento de Caixa:**
         - Criar um painel de controle que mostre o saldo do caixa em tempo real.   Responsáveis: Luan
         - Incluir previsões de fluxo de caixa com base nos pagamentos e recebimentos programados. Responsáveis: Gustavo
      - **Relatórios Financeiros:**
         - Desenvolver relatórios financeiros mensais que mostrem todas as transações realizadas, pendentes e programadas. Responsáveis: Gustavo
         - Implementar gráficos e tabelas que ajudam na visualização dos dados financeiros. Responsáveis: Gabriel
      - **Personalização da Agenda:**
         - Permitir ao usuário personalizar a visualização da agenda (diária, semanal, mensal).   Responsáveis: Luan
         - Adicionar a possibilidade de categorizar eventos e pagamentos (por exemplo, urgentes, regulares, esporádicos). Responsáveis: Gustavo
      - **Notificações e Alertas:**
         - Implementar um sistema de notificações para alertar sobre eventos importantes e pagamentos próximos.   Responsáveis: Luan
         - Personalizar os métodos de notificação (e-mail, SMS, notificações push).   Responsáveis: Luan
      - **Desenvolver interface geral de feedback de gestão no aplicativo.**   Responsáveis: Patrick e Luan
  

5. *Gestão de feedback e satisfação do cliente*
   - **Tarefas:**
     - **Criar formulário de satisfação do cliente.** Responsáveis: Gustavo
     - **Separar avaliações individualmente e somá-las em uma média de satisfação geral.**   Responsáveis: Luan
     - **Implementar a recepção dos dados do formulário no aplicativo:** Responsáveis: Gustavo
        - Associar o ID ao cliente que preencheu o formulário; Responsáveis: Gabriel
        - Associar entrega à data do formulário. Responsáveis: Gabriel
     - **Implementar funções de apagar respostas** Responsáveis: Gustavo
     - **Implementar funções de conversão de resposta em arquivo de texto**   Responsáveis: Luan
     - **Desenvolver notificações pop-ups**   Responsáveis: Luan
     - **Desenvolver interface de feedback do cliente no aplicativo.**   Responsáveis: Patrick
     
## Linguagens/API's Utilizadas:
   - Python

## Mebros e Funções:

  - Gabriel Castro: Backend , Tester
  - Carlos Gabriel: Backend , Banco de Dados
  - Henrique Guimarães: Backend , Tester
  - Patrick Peres: FrontEnd
  - Luan: Full-Stack
  - Gustavo: BackEnd , Bancos de Dados

