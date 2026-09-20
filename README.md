# Steam Games Analysis

Projeto de análise de dados sobre o catálogo de jogos da plataforma Steam, explorando a relação entre preço, popularidade, aprovação do público, engajamento em tempo real (CCU) e o desempenho de desenvolvedores e publishers.

[!IMPORTANT]
> Este projeto me ajudou muito a desenvolver minha habilidade em transformar dados em métricas e apresentar isso de uma forma mais clara para o usuário
>
> Dentro do projeto estruturei algumas perguntas de mercado que vão guiando tanto eu quanto o usuário as todas as etapas de análise

[!TIP]
> Acesse o arquivo data_analysis.ipynb para ver o código principal com os gráficos

---

## 📌 Sobre o Projeto

O objetivo deste projeto é extrair insights a partir de dados coletados diretamente da API pública do **SteamSpy**. O fluxo é dividido em três etapas principais:

1. **Coleta de Dados**: script em Python que consome a API do SteamSpy com paginação e rate limiting seguro.
2. **Limpeza e Tratamento**: remoção de duplicados, tratamento de valores nulos e estruturação das variáveis em um formato pronto para análise.
3. **Análise Exploratória (EDA)**: estudo aprofundado por meio de gráficos e métricas com foco em:
   - Distribuição de preços e concentração de mercado (*owners*).
   - Relação entre modelos de monetização (Free-to-Play vs. Pagos) e aprovação.
   - Impacto de descontos e busca pela "faixa de preço ideal".
   - Análise de estúdios independentes vs. grandes *publishers*.
   - Retenção e engajamento de jogadores ativos simultâneos (*peak CCU*).

---

## 📁 Estrutura do Repositório

```text
steam-games-analysis/
├── data/
│   ├── steamspy_raw.json        # Dados brutos coletados da API
│   └── steam_games_clean.csv    # Dataset limpo e estruturado para análise
├── notebooks/
│   ├── data_exploration_01.ipynb # Limpeza, tratamento e validação inicial
│   └── data_analysis.ipynb      # Análises estatísticas e visualizações
├── src/
│   └── collect_steamspy.py       # Script de coleta via SteamSpy API
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do projeto
```

---

## 🚀 Como Executar

### 1. Pré-requisitos
- **Python 3.10** ou superior instalado.

### 2. Configurar o Ambiente Virtual

No terminal (PowerShell / Bash), navegue até a pasta do projeto:

```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar no Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Ou ativar no Linux/macOS
source .venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

---

## ⚙️ Executando as Etapas

### Passo 1: Coleta de Dados (Opcional)
> *Nota: os dados já estão salvos na pasta `data/`, portanto esta etapa só é necessária se quiser atualizar a base.*

Para coletar páginas da API do SteamSpy (cada página contém cerca de 1.000 títulos):

```bash
python src/collect_steamspy.py --pages 5
```

### Passo 2: Limpeza e Preparação dos Dados
Abra o notebook [`notebooks/data_exploration_01.ipynb`](notebooks/data_exploration_01.ipynb) em seu ambiente Jupyter ou VS Code e execute as células para gerar o arquivo [`data/steam_games_clean.csv`](data/steam_games_clean.csv).

### Passo 3: Visualizar as Análises
Abra o notebook [`notebooks/data_analysis.ipynb`](notebooks/data_analysis.ipynb) para visualizar os gráficos, correlações e conclusões do estudo.
