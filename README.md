# Agentic AI Science Playbook

> **A hands-on tutorial series for building domain-aware AI agents in scientific research**
> Built on patterns from NVIDIA Research — covering environmental science, healthcare, and bioinformatics.

---

## What Is This Playbook?

This playbook teaches you to build **production-quality AI agents** for scientific research. It is domain-agnostic at the foundation layer and then dives into three scientific domains:

| Domain | Focus |
|--------|-------|
| **Evidence-Oriented Programming (EOP)** | Traceable research software for computational science |
| **Healthcare** | Clinical NLP, medical literature, and trial assistance |
| **Bioinformatics** | Sequence analysis, variant interpretation, pathway reasoning |

Whether you are a PhD student, research engineer, or scientist-turned-developer, the labs build from first principles (what is an LLM?) to production patterns (multi-step workflows, evaluation, and recovery).

---

## Repository Structure

```
agentic-ai-science-playbook/
├── README.md                         # This file
├── GETTING_STARTED.md                # Setup guide: API keys, Colab, first run
├── Glossary.md                       # All key terms defined
├── requirements.txt                  # Python dependencies
├── shared/
│   └── agent_utils.py                # Shared client setup and helpers
├── foundation/                       # Generic agentic skills (domain-agnostic)
│   ├── Lab0_Agent_Prototype.ipynb        # Build a minimal agent from scratch
│   ├── Lab1_Anatomy_of_a_Decision.ipynb  # Prompt structure and tool selection
│   ├── Lab2_Contract_of_a_Tool.ipynb     # Pydantic schemas for tool calls
│   ├── Lab3_Persistent_Agent.ipynb       # Memory and multi-turn state
│   ├── Lab4_Graphs_Cycles_Recovery.ipynb # LangGraph orchestration and recovery
│   └── Lab5_LLM_as_Judge.ipynb           # Evaluation with LLM-as-judge
└── domains/
    ├── eop/                          # Evidence-Oriented Programming
    │   ├── Lab_EOP1_Evidence_Chain_Extraction.ipynb
    │   ├── Lab_EOP2_Claim_Contingent_Disclosure.ipynb
    │   └── Lab_EOP3_EOP_Spokesperson.ipynb
    ├── healthcare/                   # Healthcare AI
    │   ├── Lab_HC1_Clinical_NLP_Agent.ipynb
    │   ├── Lab_HC2_Medical_Literature_Agent.ipynb
    │   └── Lab_HC3_Clinical_Trial_Assistant.ipynb
    └── bioinformatics/               # Bioinformatics AI
        ├── Lab_BIO1_Sequence_Analysis_Agent.ipynb
        ├── Lab_BIO2_Variant_Interpretation.ipynb
        └── Lab_BIO3_Pathway_Analysis_Agent.ipynb
```

---

## Learning Paths

### Path A: Agent Engineering Fundamentals (any domain)

Start here if you want the core engineering patterns. All six foundation labs are domain-agnostic.

```
Lab 0 (optional warm-up)
    |
Lab 1 --> Lab 2 --> Lab 3 --> Lab 4 --> Lab 5
(prompt)  (schema) (memory) (graph)  (eval)
```

### Path B: AI for Environmental / Computational Science

Best for PhD students in computational science, physics, or climate research.

```
Foundation Labs 0-4
    |
EOP1 --> EOP2 --> EOP3
```

### Path C: AI for Healthcare

Best for biomedical informatics, clinical research, or health tech developers.

```
Foundation Labs 0-4
    |
HC1 --> HC2 --> HC3
```

### Path D: AI for Bioinformatics

Best for genomics, proteomics, or systems biology researchers.

```
Foundation Labs 0-4
    |
BIO1 --> BIO2 --> BIO3
```

### Path E: Cross-Domain (Full Playbook)

For those who want a complete picture across all scientific domains.

```
Foundation: Lab 0 --> Lab 1 --> Lab 2 --> Lab 3 --> Lab 4 --> Lab 5
                                                               |
                                              ┌────────────────┼────────────────┐
                                              |                |                |
                                          EOP1-3           HC1-3           BIO1-3
```

---

## Open in Colab

### Foundation Labs

| Lab | Description | Open |
|-----|-------------|------|
| Lab 0 | Agent Prototype — build from scratch | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab0_Agent_Prototype.ipynb) |
| Lab 1 | Anatomy of a Decision — prompt structure | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab1_Anatomy_of_a_Decision.ipynb) |
| Lab 2 | Contract of a Tool — Pydantic schemas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab2_Contract_of_a_Tool.ipynb) |
| Lab 3 | Persistent Agent — memory and state | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab3_Persistent_Agent.ipynb) |
| Lab 4 | Graphs, Cycles & Recovery — LangGraph | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab4_Graphs_Cycles_Recovery.ipynb) |
| Lab 5 | LLM-as-Judge — evaluation patterns | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab5_LLM_as_Judge.ipynb) |

### EOP Domain

| Lab | Description | Open |
|-----|-------------|------|
| EOP 1 | Evidence Chain Extraction | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_EOP1_Evidence_Chain_Extraction.ipynb) |
| EOP 2 | Claim-contingent Disclosure | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_EOP2_Claim_Contingent_Disclosure.ipynb) |
| EOP 3 | EOP Spokesperson | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_EOP3_EOP_Spokesperson.ipynb) |

### Healthcare Domain

| Lab | Description | Open |
|-----|-------------|------|
| HC 1 | Clinical NLP Agent — extract from clinical notes | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_HC1_Clinical_NLP_Agent.ipynb) |
| HC 2 | Medical Literature Agent — search and summarize | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_HC2_Medical_Literature_Agent.ipynb) |
| HC 3 | Clinical Trial Assistant — protocol and eligibility | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_HC3_Clinical_Trial_Assistant.ipynb) |

### Bioinformatics Domain

| Lab | Description | Open |
|-----|-------------|------|
| BIO 1 | Sequence Analysis Agent — DNA/protein tools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_BIO1_Sequence_Analysis_Agent.ipynb) |
| BIO 2 | Variant Interpretation — genomic variant analysis | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_BIO2_Variant_Interpretation.ipynb) |
| BIO 3 | Pathway Analysis Agent — gene ontology and pathways | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/virginiakm1988/agentic-ai-playbook/blob/master/Lab_BIO3_Pathway_Analysis_Agent.ipynb) |


---

## Foundation Labs — Summary

| Lab | Core Skill | Key Concept |
|-----|-----------|-------------|
| **Lab 0** | Build a minimal agent prototype | Prompt → LLM → parse → execute |
| **Lab 1** | Anatomy of a decision | Prompt structure conditions tool selection probability |
| **Lab 2** | Contract of a tool | Pydantic schemas enforce structured tool call arguments |
| **Lab 3** | Persistent agent | Conversation history and external memory for multi-turn coherence |
| **Lab 4** | Graphs, cycles & recovery | LangGraph state machines for orchestrated, recoverable workflows |
| **Lab 5** | LLM-as-judge | Automated evaluation of agent output quality |

## Domain Labs — Summary

### EOP (Evidence-Oriented Programming)

| Lab | Core Skill |
|-----|-----------|
| **EOP 1** | Given a messy research repo, identify ECF's seven artifacts and suggest restructuring |
| **EOP 2** | Given scientific claims of varying strength, determine required disclosure scope |
| **EOP 3** | Advocate EOP to cross-disciplinary audiences; LLM-as-judge evaluation |

### Healthcare

| Lab | Core Skill |
|-----|-----------|
| **HC 1** | Extract medications, diagnoses, and vitals from unstructured clinical notes |
| **HC 2** | Search medical literature and produce evidence-graded summaries |
| **HC 3** | Analyze clinical trial protocols; check patient eligibility criteria |

### Bioinformatics

| Lab | Core Skill |
|-----|-----------|
| **BIO 1** | Analyze DNA/RNA/protein sequences: GC content, motif search, ORF detection |
| **BIO 2** | Classify genomic variants (SNPs, indels); assess pathogenicity with evidence |
| **BIO 3** | Pathway enrichment from gene lists; identify drug targets and build interaction networks |

---

## Technical Stack

| Component | Choice | Reason |
|-----------|--------|--------|
| LLM provider | OpenAI API / NVIDIA NIM | Both supported via env flag |
| Agent framework | Raw API (Labs 0-3), LangGraph (Lab 4+) | Gradual complexity increase |
| Schema validation | Pydantic v2 | Industry-standard structured output |
| Evaluation | LLM-as-judge (Lab 5) | Scalable automated quality signal |
| Notebook format | Jupyter / Google Colab | Zero-friction reproducibility |

---

## Prerequisites

| Background | Minimum Needed |
|------------|---------------|
| Python | Basic (functions, dicts, classes) |
| AI/ML | None for Labs 0-2; helpful from Lab 3 onward |
| Domain knowledge | None required — each domain lab includes background |

See [GETTING_STARTED.md](GETTING_STARTED.md) for setup instructions.

---

## Contributing

Domain labs are designed to be self-contained. To add a new domain:

1. Create `domains/<your_domain>/` directory
2. Add `Lab_<DOMAIN>1_...ipynb`, `Lab_<DOMAIN>2_...ipynb`, `Lab_<DOMAIN>3_...ipynb`
3. Follow the lab template structure (Setup → Background → Tools → Experiments → Summary)
4. Add your domain to the README tables

---

## References

- Zhang, H. et al. "Research software as scientific evidence: clarifying missing specifications." (EOP/ECF framework)
- Zhang, H. et al. "Reviewability and Supportability." *Computational and Structural Biotechnology Journal* 23 (2024)
- Anthropic Claude API documentation
- NVIDIA NIM API documentation
- LangGraph documentation (LangChain)
