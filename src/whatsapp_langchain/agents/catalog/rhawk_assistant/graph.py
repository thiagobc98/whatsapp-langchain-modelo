"""Grafo para uso com langgraph dev.

Este arquivo exporta uma variável `graph` para integração com `langgraph dev`.
O servidor de produção usa `build_graph()` de agent.py, passando o checkpointer
e store reais.

Em dev, a LangGraph API fornece o store (e checkpointer) automaticamente e
rejeita grafos compilados com store próprio. As tools de memória recebem o
store da plataforma via InjectedStore.
"""

from whatsapp_langchain.agents.catalog.rhawk_assistant.agent import build_graph

# Sem store/checkpointer: a plataforma injeta os seus em runtime
graph = build_graph(enable_memory=True)
