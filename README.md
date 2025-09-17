# 🐍 Snake Game

tag: q-developer-quest-tdc-2025

Um jogo clássico da cobrinha desenvolvido em Python usando Streamlit.

## 📋 Descrição

Jogo Snake simples e funcional onde você controla uma cobra que cresce ao comer maçãs. O objetivo é conseguir a maior pontuação possível sem colidir com as bordas ou com o próprio corpo.

## 🎮 Como Jogar

- Use os botões direcionais para mover a cobra:
  - ⬆️ **Cima**
    - ⬇️ **Baixo** 
      - ⬅️ **Esquerda**
        - ➡️ **Direita**
        - Colete as maçãs 🍎 para crescer e aumentar sua pontuação
        - Evite colidir com as bordas ou com o corpo da cobra
        - Use 🔄 **Reset** para reiniciar o jogo

        ## 🚀 Instalação e Execução

        ### Pré-requisitos
        - Python 3.7+
        - pipx (recomendado)

        ### Instalação
        ```bash
        # Instalar pipx (se não tiver)
        sudo apt install pipx

        # Instalar Streamlit
        pipx install streamlit
        ```

        ### Executar o Jogo
        ```bash
        streamlit run game_snake.py
        ```

        ## 📁 Estrutura do Projeto

        ```
        snake-game/
        ├── game_snake.py           # Código principal do jogo
        ├── snake_game_diagram.drawio # Diagrama de fluxo do jogo
        └── README.md               # Este arquivo
        ```

        ## 🎯 Funcionalidades

        - ✅ Movimento da cobra em 4 direções
        - ✅ Sistema de pontuação
        - ✅ Detecção de colisões
        - ✅ Geração aleatória de comida
        - ✅ Interface visual com emojis
        - ✅ Botão de reset
        - ✅ Grid 20x20

        ## 🎨 Elementos Visuais

        - 🔴 **Cabeça da cobra**
        - 🟢 **Corpo da cobra**
        - 🍎 **Comida**
        - ⬜ **Espaço vazio**

        ## 🔧 Tecnologias Utilizadas

        - **Python 3**
        - **Streamlit** - Framework web para aplicações Python
        - **Random** - Geração de posições aleatórias
        - **Time** - Controle de velocidade do jogo

        ## 📊 Diagrama de Fluxo

        O arquivo `snake_game_diagram.drawio` contém o diagrama completo do fluxo do jogo. Para visualizar:

        1. Acesse [draw.io](https://app.diagrams.net/)
        2. Abra o arquivo `snake_game_diagram.drawio`
        3. Visualize o fluxo completo do jogo

        ## 🎮 Regras do Jogo

        1. A cobra começa com tamanho 1 na posição central
        2. A cobra se move continuamente na direção atual
        3. Ao comer uma maçã, a cobra cresce e a pontuação aumenta
        4. O jogo termina se a cobra colidir com:
           - As bordas do grid
              - Seu próprio corpo
              5. Use o botão Reset para jogar novamente

              ## 🏆 Pontuação

              - +1 ponto para cada maçã coletada
              - Objetivo: conseguir a maior pontuação possível

              ## ☁️ Deploy na AWS

              Para hospedar o jogo na nuvem de forma econômica, recomendamos as seguintes opções:

              ### 🏆 Opção Recomendada: AWS Elastic Beanstalk
              **Custo:** ~$5-15/mês (Free Tier: 750h/mês grátis no primeiro ano)

              ```bash
              # Instalar EB CLI
              pip install awsebcli

              # Configurar aplicação
              eb init snake-game --platform python-3.9
              eb create snake-game-env
              eb deploy
              ```

              ### 💰 Opção Mais Econômica: AWS Lambda + API Gateway
              **Custo:** ~$0.20-2.00/mês (Free Tier: 1M requests/mês)
              - Requer conversão de Streamlit para Flask/FastAPI
              - Pay-per-request (só paga quando usado)

              ### 🎯 Opção Preço Fixo: Amazon Lightsail
              **Custo:** $3.50-5.00/mês
              - Preço fixo previsível
              - Inclui 1TB de transferência
              - Interface simples

              ## 🚀 Próximos Passos

              ### Fase 1: Preparação para Deploy
              - [ ] Criar arquivo `application.py` (renomear `game_snake.py`)
              - [ ] Configurar `requirements.txt` com versões específicas
              - [ ] Testar aplicação localmente
              - [ ] Criar conta AWS (se não tiver)

              ### Fase 2: Deploy AWS Elastic Beanstalk
              - [ ] Instalar AWS CLI e EB CLI
              - [ ] Configurar credenciais AWS
              - [ ] Inicializar aplicação EB
              - [ ] Deploy inicial
              - [ ] Configurar domínio personalizado (opcional)

              ### Fase 3: Otimizações
              - [ ] Configurar CloudFront para CDN
              - [ ] Implementar monitoramento com CloudWatch
              - [ ] Configurar backup automático
              - [ ] Otimizar custos com Reserved Instances

              ### Fase 4: Melhorias do Jogo
              - [ ] Adicionar sistema de high scores
              - [ ] Implementar multiplayer
              - [ ] Adicionar diferentes níveis de dificuldade
              - [ ] Criar sistema de autenticação

              ## 📊 Estimativa de Custos AWS

              | Serviço | Custo Mensal | Free Tier |
              |---------|--------------|----------|
              | Elastic Beanstalk | $5-15 | ✅ 750h/mês |
              | Lambda + API Gateway | $0.20-2.00 | ✅ 1M requests |
              | Lightsail | $3.50-5.00 | ❌ |
              | CloudFront (opcional) | $0.50-2.00 | ✅ 50GB/mês |

              ## 📝 Licença

              Este projeto é de código aberto e está disponível sob a licença MIT.
