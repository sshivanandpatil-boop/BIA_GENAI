# The AI Engineer's Journey: Sessions 1–14 Recap
## Dual Certificate Program in Generative AI & Agentic AI Development

> **BIA® School of Technology & AI — Pune-Kharadi Campus**
> A complete recap of what you've learned, why it matters, and how every piece connects.

---

## How to Use This Document

This isn't just a summary of slides. It's structured around three questions:

1. **What did we learn?** — A concise recap of each session's core ideas
2. **Why does it matter?** — The real-world angle you won't find in the slides
3. **How does it all connect?** — The thread that ties 14 sessions into one coherent skill set

Read it before interviews. Read it before your capstone. Read it when you're stuck on a project and can't remember which session covered that one concept you need.

---

## Part 1: The Foundation Layer (Sessions 1–5)

### Session 1: Induction
**Module 1 — Getting Started**

You set up your tools (Python, Jupyter, API keys) and got oriented. But the real takeaway was understanding *what this course is*: not a machine learning course, not a data science course — an **AI engineering** course. You're learning to build systems that use AI, not to train models from scratch.

**The one thing to remember:** AI engineering is about *orchestration* — connecting models, tools, data, and users into something useful.

---

### Session 2: AI & Gen AI Primer
**Module 2 — Foundations of Agentic AI & Generative Intelligence**

You learned the landscape: Classical ML predicts from data (regression, classification). Generative AI *creates* new content (text, images, code). The transformer architecture (2017) made it all possible. You explored open vs closed models, tried Hugging Face, and ran a local Mistral demo.

**The one thing to remember:** Every LLM is just a next-token predictor. Everything we build in this course — prompting, RAG, agents — is about steering that prediction in useful directions.

**Key distinctions you should be able to explain:**

| | Classical ML | Generative AI |
|---|---|---|
| **Goal** | Predict/classify | Generate new content |
| **Training data** | Labeled datasets | Massive text corpora |
| **Output** | Numbers/categories | Text, code, images |
| **Example** | "Is this email spam?" | "Write a reply to this email" |

---

### Session 3: What Makes an Agent?
**Module 2 — Foundations (continued)**

This is where the course's "agentic AI" identity kicked in. You learned that an agent isn't just a chatbot — it's a system that can **perceive** (read inputs), **reason** (decide what to do), and **act** (use tools, call APIs). You built a simple reflex mood-bot and saw planning graphs for the first time.

**The one thing to remember:** An agent = LLM + Tools + Loop. The LLM thinks, tools act, and the loop keeps going until the task is done.

**Agent anatomy:**
```
┌──────────────────────────────┐
│         User Query           │
└──────────┬───────────────────┘
           ▼
┌──────────────────────────────┐
│     LLM (The Brain)         │  ← Perceive + Reason
│  "What should I do next?"   │
└──────────┬───────────────────┘
           ▼
┌──────────────────────────────┐
│     Tools (The Hands)        │  ← Act
│  search(), calculate(),      │
│  get_weather(), send_email() │
└──────────┬───────────────────┘
           ▼
┌──────────────────────────────┐
│  Observation → Back to LLM   │  ← The Loop
│  "Here's what happened..."   │
└──────────────────────────────┘
```

---

### Session 4: LLM Anatomy
**Module 2 — Foundations (continued)**

You went inside the transformer: tokenization (text → numbers), self-attention (how the model relates words to each other), and the full architecture (encoder-decoder, decoder-only). You got a preview of fine-tuning (Full vs PEFT) and alignment techniques (RLHF, DPO).

**The one thing to remember:** Self-attention is why LLMs can understand context. When the model reads "The bank of the river was muddy," attention helps it know "bank" means riverbank, not a financial institution. Everything else — prompting, RAG, fine-tuning — works because of this mechanism.

---

### Session 5: Agent Architectures in Practice
**Module 2 — Foundations (continued)**

You compared the major frameworks: LangChain (the Swiss Army knife), CrewAI (role-based teams), AutoGen (conversation-driven), and LangGraph (state machines). You learned about memory back-ends, tool abstraction, and the trade-offs between flexibility and simplicity.

**The one thing to remember:** There's no "best" framework — only the right one for your use case. LangChain for general-purpose, CrewAI when you think in roles, LangGraph when you need precise control over flow.

---

## Part 2: The Prompting Layer (Sessions 6–8)

This is where you stopped being a user of AI and started becoming an *engineer* of AI. Sessions 6-8 taught you to control LLM behavior precisely.

### Session 6: Prompt Essentials
**Module 3 — Prompt Engineering & Autonomous Reasoning**

You learned that prompting isn't about asking nicely — it's about engineering inputs for predictable outputs. Zero-shot (just ask), few-shot (show examples), sampling parameters (temperature, top_p), system messages, and prompt templates with variable injection.

**Core techniques you should know cold:**

| Technique | When to Use | Example |
|-----------|-------------|---------|
| **Zero-shot** | Simple, well-defined tasks | "Translate this to French" |
| **Few-shot** | When format/style matters | "Here are 3 examples, now do the 4th" |
| **System message** | Set persona/constraints | "You are a legal expert. Be precise." |
| **Temperature** | Control creativity vs precision | 0.0 for facts, 0.7 for creative writing |

**The code pattern that ties it all together:**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful study assistant."),
    ("human", "{question}")
])

chain = prompt | llm
response = chain.invoke({"question": "What is gradient descent?"})
```

---

### Session 7: Structured Prompting
**Module 3 — Prompt Engineering (continued)**

You leveled up from "one prompt, one answer" to structured reasoning. Chain-of-Thought (think step by step), ReAct (Thought → Action → Observation), Tree-of-Thought (explore multiple paths), and Graph-of-Thought (non-linear reasoning with dependencies).

**The one thing to remember:** ReAct is the pattern behind every agent you'll build. The agent thinks about what to do, takes an action (calls a tool), observes the result, and decides the next step. This is the loop from Session 3, now with a name.

**The reasoning spectrum:**
```
Simple Question ──────────────────────────────── Complex Problem
     │                                                │
  Zero-shot          CoT           ReAct        Tree/Graph-of-Thought
  "Just answer"   "Think step    "Think, act,    "Explore multiple
                   by step"      observe, repeat"  paths/branches"
```

---

### Session 8: Self-Reflection & Critique
**Module 3 — Prompt Engineering (continued)**

The most underrated session. You learned that LLMs don't know when they're wrong — so you make them check their own work. The Self-Refine pattern (Generate → Critique → Revise), the Reflexion algorithm (longer-term learning from mistakes), and using a separate LLM call as a judge.

**The one thing to remember:** The Generate → Critique → Refine loop is one of the most practical patterns in production AI. It costs one extra LLM call but dramatically improves output quality. You used this in the Smart Study Assistant's `evaluator.py`.

**The pattern:**
```python
# Step 1: Generate
answer = llm.invoke("Answer this question: ...")

# Step 2: Critique
critique = llm.invoke(f"Critique this answer for accuracy: {answer}")

# Step 3: Refine (only if critique found issues)
if "no issues" not in critique.lower():
    improved = llm.invoke(f"Improve this answer based on critique: {critique}")
```

---

## Part 3: The Agent Layer (Session 9)

### Session 9: Mini-Project Sprint
**Module 3 — Prompt Engineering (continued)**

Everything from Sessions 6-8 came together. You built a Travel Planner agent with real tools: weather lookup, flight search, hotel finder, currency conversion. Then you went further — a Manager/Worker (Supervisor) pattern where one agent delegates to specialized sub-agents.

**The three levels you built:**

| Level | What | Pattern |
|-------|------|---------|
| **Mock tools** | Functions that return fake data | `@tool` decorator |
| **Single agent** | One agent with multiple tools | `create_react_agent()` |
| **Multi-agent** | Manager delegates to workers | Supervisor pattern |

**The code pattern:**
```python
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return f"Weather in {city}: 28°C, sunny"

agent = create_react_agent(model=llm, tools=[get_weather])
response = agent.invoke({"messages": [{"role": "user", "content": "Weather in Pune?"}]})
```

---

## Part 4: The Data Layer (Sessions 10–13)

This is the biggest module and the most directly useful for your career. RAG (Retrieval-Augmented Generation) is what most companies are building right now.

### Session 10: Vector Search 101
**Module 4 — Retrieval-Augmented Generation & Multimodal Systems**

The fundamental question: *How do you make an LLM answer questions about YOUR data?* The answer starts with embeddings — turning text into numbers (vectors) that capture meaning. You learned cosine similarity, Euclidean distance, dot product, and built a FAISS index from scratch.

**The mental model:** Think of embeddings as coordinates in "meaning space." "Happy" and "Joyful" land near each other. "Happy" and "Refrigerator" land far apart. Search becomes: "find the points nearest to my question."

**Key numbers to remember:**

| Model | Dimensions | Cost per 1M tokens |
|-------|-----------|-------------------|
| Mistral Embed | 1024 | $0.01 |
| OpenAI text-embedding-3-small | 1536 | $0.02 |
| OpenAI text-embedding-3-large | 3072 | $0.13 |
| Google embedding-001 | 768 | $0.15 |
| Google gemini-embedding-002 | 3072 | $0.20 |

**The code pattern:**
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector = embeddings.embed_query("What is machine learning?")
# Result: [0.023, -0.041, 0.087, ...] — 768 numbers that capture the meaning
```

---

### Session 11: Vector DB Landscape
**Module 4 — RAG (continued)**

You moved from raw FAISS (good for learning) to production vector databases. ChromaDB (embedded, free, great for prototypes), Pinecone (managed, scales to billions), Weaviate (hybrid search, GraphQL). You learned hybrid search (combine keyword + semantic), and when to migrate between databases.

**The decision framework:**

| Stage | Database | Why |
|-------|----------|-----|
| **Learning/POC** | ChromaDB | Free, embedded, zero config |
| **Startup MVP** | Weaviate | Hybrid search, self-hosted |
| **Enterprise scale** | Pinecone | Managed, billions of vectors |

**The code pattern:**
```python
from langchain_community.vectorstores import Chroma

# Create
vectorstore = Chroma.from_texts(chunks, embeddings, persist_directory="./chroma_db")

# Load existing
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# Search
docs = vectorstore.similarity_search("What is supervised learning?", k=3)
```

---

### Session 12: Text-RAG Pipeline
**Module 4 — RAG (continued)**

The session that tied everything together into a working pipeline. You learned chunking strategies (RecursiveCharacterTextSplitter, 512 tokens, 50-100 overlap), built the full retriever → prompt → LLM chain using LCEL, added a router to classify queries, and evaluated with Precision@k, Recall@k, and F1.

**This is the most important architecture in the course:**
```
Document → Chunks → Embeddings → Vector DB → Retriever
                                                  │
User Question → Embedding → Similarity Search ────┘
                                                  │
                                    Retrieved Chunks + Question
                                                  │
                                          Prompt Template
                                                  │
                                              LLM (Gemini)
                                                  │
                                              Answer
```

**The LCEL chain — memorize this pattern:**
```python
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

answer = chain.invoke("What is gradient descent?")
```

**Chunking best practices:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # ~125 tokens — sweet spot for most use cases
    chunk_overlap=50   # Prevents cutting context at boundaries
)
chunks = splitter.split_text(full_document)
```

**Evaluation metrics you should know:**
- **Precision@k** = (relevant docs in top-k) / k — "Of what I retrieved, how much was useful?"
- **Recall@k** = (relevant docs in top-k) / total relevant — "Of all useful docs, how many did I find?"
- **F1@k** = Harmonic mean of the two — the balanced score

---

### Session 13: Multimodal RAG
**Module 4 — RAG (continued)**

You extended RAG beyond text. Images get processed through "Describe-Then-Embed" (use an LLM to describe the image, then embed the description). YouTube videos get transcribed and chunked. The retriever doesn't care about the original modality — everything becomes text and vectors.

**The Describe-Then-Embed strategy:**
```
Image → LLM describes it → Text description → Embed → Store in vector DB
                                                           │
Query → Embed → Similarity Search ─────────────────────────┘
                                                           │
                                          Retrieved description + original image
                                                           │
                                                    LLM generates answer
```

**Why this matters:** Real-world data isn't just text. Company documents have charts, diagrams, photos. A multimodal RAG pipeline can handle all of it using the same architecture you already know.

---

## Part 5: The Adaptation Layer (Session 14)

### Session 14: Full & PEFT Fine-Tuning
**Module 5 — Fine-Tune LLMs**

A high-level, interview-focused session. You learned *when* to fine-tune (almost never — try prompting and RAG first), *how* it works conceptually (update model weights with your data), and *why PEFT changed everything* (train 0.1% of parameters, get 90-95% of the quality).

**The decision framework — most asked interview question:**
```
Can prompting solve it?
    ├── YES → Use prompt engineering (cheapest, fastest)
    └── NO → Does the model need external/recent data?
                ├── YES → Use RAG (add a knowledge base)
                └── NO → Does the model need to change its behavior/style?
                            ├── YES → Fine-tune (expensive but powerful)
                            └── NO → Re-evaluate the problem
```

**LoRA in one sentence:** Instead of updating all 7 billion parameters, insert two tiny matrices (rank 16) into each layer and only train those — reduces trainable parameters by 99%.

**Key terms for interviews:**
- **Full Fine-Tuning** — Update all parameters. Needs massive GPU. Risk of catastrophic forgetting.
- **LoRA** — Low-Rank Adaptation. Freeze original weights, train small adapter matrices. W = W₀ + BA.
- **QLoRA** — LoRA + 4-bit quantization. Fine-tune a 65B model on a single GPU.
- **Catastrophic Forgetting** — Model loses general knowledge when fine-tuned on narrow data.
- **RLHF** — Reinforcement Learning from Human Feedback. How models learn to be helpful/harmless.
- **DPO** — Direct Preference Optimization. Simpler alternative to RLHF — no reward model needed.

---

## Part 6: How Everything Connects

This is the section that doesn't exist in any individual session's slides. It's the bird's-eye view.

### The Three Pillars of AI Engineering

Everything you've learned falls into three pillars:

```
┌──────────────────────────────────────────────────────────────────┐
│                    AI ENGINEERING                                │
├──────────────────┬──────────────────┬────────────────────────────┤
│   PROMPTING      │     DATA         │     ORCHESTRATION          │
│   (Control)      │    (Knowledge)   │     (Systems)              │
│                  │                  │                            │
│  Session 6:      │  Session 10:     │  Session 3: Agent basics   │
│   Basics         │   Embeddings     │  Session 5: Frameworks     │
│  Session 7:      │  Session 11:     │  Session 9: Multi-agent    │
│   Structured     │   Vector DBs    │  Session 14: Fine-tuning   │
│  Session 8:      │  Session 12:     │                            │
│   Self-Reflect   │   RAG Pipeline   │  Smart Study Assistant:    │
│                  │  Session 13:     │   Everything combined      │
│                  │   Multimodal     │                            │
├──────────────────┴──────────────────┴────────────────────────────┤
│  Foundation: Sessions 1-2, 4 (LLM internals, transformer arch)  │
└──────────────────────────────────────────────────────────────────┘
```

### The Data Flow: From Question to Answer

Here's how a complete AI system processes a user query, using concepts from every session:

```
User: "Explain gradient descent from my ML notes"
  │
  ▼
[Session 12: Router] ─── classify_query() ─── "This is a study_question"
  │
  ▼
[Session 10: Embeddings] ─── embed the question ─── [0.02, -0.04, ...]
  │
  ▼
[Session 11: Vector DB] ─── similarity_search(k=3) ─── find 3 closest chunks
  │
  ▼
[Session 12: RAG Chain] ─── inject chunks into prompt template
  │
  ▼
[Session 6: Prompt] ─── system message + context + question → LLM
  │
  ▼
[Session 4: LLM] ─── self-attention processes tokens → generates answer
  │
  ▼
[Session 8: Self-Refine] ─── critique the answer → refine if needed
  │
  ▼
[Session 9: Agent] ─── if the question needs tools, call them (summarize, quiz)
  │
  ▼
Final Answer → displayed in Streamlit UI
```

Every single session contributed a piece of this pipeline.

### The Concept Dependency Map

Some concepts build directly on others. Here's the dependency chain:

```
Tokenization (Session 4)
    └── Embeddings (Session 10)
            └── Vector Search (Session 10)
                    └── Vector DBs (Session 11)
                            └── RAG Pipeline (Session 12)
                                    └── Multimodal RAG (Session 13)

Prompt Basics (Session 6)
    └── Structured Prompting (Session 7)
            └── Self-Reflection (Session 8)
                    └── Agent Loops (Session 9)
                            └── Tool Design (Session 9)

Agent Basics (Session 3)
    └── Frameworks Overview (Session 5)
            └── ReAct Pattern (Session 7)
                    └── Single Agent (Session 9)
                            └── Multi-Agent (Session 9)

RAG Pipeline (Session 12) + Agent (Session 9) + Self-Reflection (Session 8)
    └── Smart Study Assistant Project
            └── Streamlit UI (Phase 7)
```

### The Six Patterns That Matter Most

If you remember nothing else from 14 sessions, remember these six patterns. They're what you'll use in every AI project:

**Pattern 1: The Prompt Template** (Session 6)
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are {role}. {constraints}"),
    ("human", "{input}")
])
```
*Use when:* You need consistent, reusable prompts with variable injection.

**Pattern 2: The LCEL Chain** (Session 12)
```python
chain = prompt | llm | StrOutputParser()
```
*Use when:* You need to pipe data through multiple processing steps.

**Pattern 3: The RAG Retrieval** (Session 12)
```python
{"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm
```
*Use when:* The LLM needs to answer questions about specific documents or data.

**Pattern 4: The @tool Decorator** (Session 9)
```python
@tool
def my_function(input: str) -> str:
    """Description the agent reads to decide when to use this tool."""
    return result
```
*Use when:* You want an agent to be able to call custom functions.

**Pattern 5: The ReAct Agent** (Sessions 7, 9)
```python
agent = create_react_agent(model=llm, tools=[tool1, tool2])
response = agent.invoke({"messages": [{"role": "user", "content": query}]})
```
*Use when:* A task requires reasoning + acting in a loop (most agent tasks).

**Pattern 6: Generate → Critique → Refine** (Session 8)
```python
answer = generate(question)
critique = critique(question, answer)
refined = refine(question, answer, critique)
```
*Use when:* You need higher quality answers and can afford an extra LLM call.

---

### Where Each Concept Lives in the Smart Study Assistant

The project you're building isn't random — every file maps to a session:

```
Smart Study Assistant
│
├── config.py              ← Session 6:  API keys, model config, parameters
│
├── loader.py              ← Session 12: Document loading + chunking
│   └── RecursiveCharacterTextSplitter (chunk_size=500, overlap=50)
│
├── vectorstore.py         ← Sessions 10-11: Embeddings + ChromaDB
│   └── GoogleGenerativeAIEmbeddings → Chroma.from_texts()
│
├── retriever.py           ← Session 12: The RAG chain (LCEL)
│   └── retriever | format_docs → prompt → llm → StrOutputParser
│
├── tools.py               ← Session 9: Custom @tool functions
│   └── summarize_topic, generate_flashcards, quiz_me
│
├── evaluator.py           ← Session 8 + 12: Self-Refine + Precision/Recall
│   └── critique_response → refine_response → precision_at_k
│
├── router.py              ← Session 12: Query classification + routing
│   └── classify_query → route to RAG, tools, or agent
│
├── agent.py               ← Session 9: ReAct agent with tools
│   └── create_react_agent(model, tools, prompt)
│
├── main.py                ← All sessions: CLI bringing everything together
│
└── app.py                 ← Phase 7: Streamlit UI (same backend, new face)
```

---

## Part 7: Interview-Ready Quick Reference

### "Explain RAG in 30 seconds"

> RAG stands for Retrieval-Augmented Generation. Instead of relying on the LLM's training data alone, you first search a knowledge base (using vector similarity) to find relevant documents, then inject those documents into the prompt as context. The LLM generates its answer based on this retrieved context. This gives you accurate, up-to-date answers grounded in your specific data, without fine-tuning the model.

### "What's the difference between prompting, RAG, and fine-tuning?"

> Prompting controls *what you ask* — it's cheap and fast. RAG controls *what the model knows* at query time — add external data without changing the model. Fine-tuning changes *how the model behaves* — update its weights with your data. Start with prompting, add RAG if you need knowledge, fine-tune only if behavior needs to change.

### "What is an embedding?"

> An embedding is a numerical representation of text (or images, audio) as a vector — a list of numbers. Similar meanings produce similar vectors. This lets you do math on meaning: search for "similar" text, cluster topics, find relevant documents. Models like Google's embedding-001 produce 768-dimensional vectors.

### "How does an agent work?"

> An agent is an LLM in a loop. It receives a task, reasons about what to do (Thought), calls a tool or API (Action), observes the result (Observation), then decides whether to continue or return the answer. This is called the ReAct pattern. Frameworks like LangGraph implement this with `create_react_agent()`.

### "What is LoRA and why does it matter?"

> LoRA (Low-Rank Adaptation) lets you fine-tune a large model by only training two small matrices inserted into each transformer layer, instead of updating all billions of parameters. This reduces memory by 10-20x and makes fine-tuning possible on a single GPU. QLoRA adds 4-bit quantization on top, pushing it even further.

### "How do you evaluate a RAG system?"

> Three key metrics: Precision@k (of the k documents retrieved, how many were relevant), Recall@k (of all relevant documents, how many were retrieved), and F1@k (the harmonic mean). You also evaluate the generated answer for faithfulness (does it match the sources?) and relevance (does it answer the question?).

### "What is LCEL?"

> LangChain Expression Language is a way to compose chains using the pipe operator (`|`). You connect components like `prompt | llm | parser` to create data processing pipelines. It supports parallel execution with `RunnableParallel`, conditional routing with `RunnableBranch`, and custom logic with `RunnableLambda`.

### "When would you NOT use RAG?"

> When the question can be answered from the model's general knowledge (no specific documents needed), when the data changes too frequently for a vector store to keep up (use live API calls instead), when the task requires behavioral changes rather than knowledge (use fine-tuning), or when your context fits entirely in the prompt window (just paste it in, no retrieval needed).

---

## Part 8: The Technology Stack

Here's every tool and library you've used, organized by purpose:

### LLM & Embeddings
| Tool | Purpose | Used In |
|------|---------|---------|
| `ChatGoogleGenerativeAI(model="gemini-2.5-flash")` | Text generation | Every session |
| `GoogleGenerativeAIEmbeddings(model="models/embedding-001")` | Text → vectors | Sessions 10-13 |

### LangChain Ecosystem
| Package | Purpose | Used In |
|---------|---------|---------|
| `langchain-core` | Prompts, parsers, runnables, tools | Sessions 6-13 |
| `langchain-google-genai` | Google Gemini integration | Every session |
| `langchain-community` | ChromaDB, third-party integrations | Sessions 11-13 |
| `langchain-text-splitters` | Document chunking | Session 12-13 |
| `langgraph` | Agent orchestration, state machines | Session 9 |

### Data & Storage
| Tool | Purpose | Used In |
|------|---------|---------|
| ChromaDB | Vector database (embedded) | Sessions 11-13 |
| FAISS | Raw vector search (learning tool) | Session 10 |

### Key Decorators & Functions
| Code | What It Does |
|------|-------------|
| `@tool` | Turns a function into an agent-callable tool |
| `create_react_agent()` | Creates a ReAct agent from LLM + tools |
| `ChatPromptTemplate.from_messages()` | Creates a reusable prompt template |
| `RunnablePassthrough()` | Passes input through unchanged in a chain |
| `StrOutputParser()` | Extracts string from LLM response |
| `RecursiveCharacterTextSplitter()` | Splits text into overlapping chunks |
| `Chroma.from_texts()` | Creates a vector store from text chunks |

---

## Part 9: What's Coming Next

You've covered 14 of 35 sessions. Here's what the remaining modules build on:

| What's Next | Builds On |
|-------------|-----------|
| **Sessions 15-17:** LangChain Patterns, AutoGen, CrewAI & LangGraph | Sessions 5, 9 (frameworks + agents) |
| **Sessions 18-20:** Project Refactor, Role Design, Team Research Bot | Sessions 8, 9 (error handling + multi-agent) |
| **Sessions 21-22:** Webhooks, FastAPI, Streaming | Sessions 9, 12 (agents + real-time data) |
| **Sessions 23-25:** Observability, Guardrails, Deployment | All sessions (production-readiness) |
| **Sessions 26-27:** Voice + Avatar Agents | New modality (builds on Session 13 multimodal thinking) |
| **Sessions 28-32:** Evaluation, Domain Use-Cases, MCP | Sessions 8, 12 (eval + real-world RAG) |
| **Sessions 33-35:** Career Enhancement, Capstone | Everything — your chance to prove it |

The foundation is solid. Everything from here builds on what you already know.

---

## Part 10: One-Page Cheat Sheet

**Cut this out and keep it at your desk.**

```
┌──────────────────────────────────────────────────────────┐
│                AI ENGINEER CHEAT SHEET                    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  PROMPTING                                               │
│  ─────────                                               │
│  Zero-shot: Just ask                                     │
│  Few-shot: Show examples first                           │
│  CoT: "Think step by step"                               │
│  ReAct: Think → Act → Observe → Repeat                   │
│  Self-Refine: Generate → Critique → Improve              │
│                                                          │
│  RAG PIPELINE                                            │
│  ────────────                                            │
│  Load → Chunk (500, overlap 50) → Embed → Store → Search │
│  Chain: retriever | format_docs + question → prompt → llm│
│  Eval: Precision@k, Recall@k, F1@k                      │
│                                                          │
│  AGENTS                                                  │
│  ──────                                                  │
│  @tool decorator → create_react_agent() → invoke()       │
│  Single agent: 1 LLM + multiple tools                    │
│  Multi-agent: Manager delegates to worker agents         │
│                                                          │
│  DECISION FRAMEWORK                                      │
│  ──────────────────                                      │
│  1. Try prompting first (cheapest)                       │
│  2. Add RAG if you need specific knowledge               │
│  3. Fine-tune only if behavior must change               │
│  4. LoRA/QLoRA for fine-tuning (never full FT)           │
│                                                          │
│  KEY MODELS                                              │
│  ──────────                                              │
│  LLM: gemini-2.5-flash                                   │
│  Embeddings: models/embedding-001 (768 dims)             │
│  Vector DB: ChromaDB (dev), Pinecone (prod)              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

*This recap covers Sessions 1-14 of the Dual Certificate Program in Generative AI & Agentic AI Development at BIA® School of Technology & AI, Pune-Kharadi. Created April 2026.*
