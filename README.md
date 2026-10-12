# ShooterGame

# 🚀 Cosmic Void (Python & Pygame)

Projeto desenvolvido como parte das atividades práticas da faculdade, utilizando Python, Pygame e integração com SQLite para persistência de dados e placar de recordes (Top 10).

---

# 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python 3.x**
* **Pygame** (Desenvolvimento do jogo, áudio e renderização gráfica)
* **SQLite3** (Armazenamento local de pontuações e histórico em banco de dados)
* **Padrões de Projeto:** Arquitetura orientada a objetos com separação em camadas (`Game`, `Level`, `Entity`, `Menu`, `Score`, `DBProxy`)

---

## 🎮 Funcionalidades do Sistema
* **Modos de Jogo:** Suporte para 1 Jogador ou 2 Jogadores.
* **Progressão de Fases:** Transição dinâmica entre níveis (`Level 1` e `Level 2`) mantendo o estado de vida e pontuação acumulada (`player_health` e `player_score`).
* **Sistema de Score Persistente:** Banco de dados SQLite integrado para capturar o nome do jogador (ou da dupla), pontuação final e carimbo de data/hora (`datetime`).
* **Tela de Recordes (Top 10):** Consulta automatizada dos 10 melhores scores ordenados de forma decrescente direto do banco de dados.

---

## 📂 Estrutura do Projeto
```text
├── Asset/             # Imagens, fontes, músicas e efeitos sonoros
├── Model/             # Classes e lógica principal do jogo
│   ├── const.py       # Constantes globais (telas, velocidades, entidades, posições)
│   ├── game.py        # Controlador principal do fluxo do jogo
│   ├── level.py       # Gerenciamento de fases, colisões e entidades
│   ├── entity.py      # Comportamento de jogadores, tiros e inimigos
│   ├── menu.py        # Navegação do menu principal
│   ├── score.py       # Gerenciamento da tela de vitória e exibição do Top 10
│   └── DBProxy.py     # Camada de comunicação com o banco de dados SQLite
└── main.py            # Ponto de entrada (Execution entry point)