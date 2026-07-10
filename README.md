# 🌌 Universal Semantic Engine

> **Ultimate Goal:** Beyond simple summarization, the AI swarm identifies extreme connective points within any unfamiliar data to automatically generate a perfect, semantic-based mind map topology.

This repository serves as the core universal engine for the LLM-Wiki ecosystem.

## 🛡️ Data Isolation Architecture
To maintain privacy and universal applicability, this repository **only contains the engine code**. 
All specific research data (sources, concepts, and entities) and the dashboard (`index.md`) are explicitly ignored by Git and must be generated locally by the user.

## 📁 Structure
- `.agents/`: Contains the global system rules and `AGENTS.md` (the Constitution).
- `scripts/`: Contains Python scripts (Parsers, Academic Search APIs, Vector DB).
- `.obsidian/`: Pre-configured Obsidian vault settings (Semantic color graphs).
- `wiki/`: The empty directories where your local AI agent will generate and link knowledge nodes.

## 🚀 How to use
1. Clone this repository locally.
2. Open the folder as a Vault in **Obsidian**.
3. Summon your AI agent to begin ingesting PDFs into the `raw/sources/` folder. The AI will autonomously build your private semantic network!
