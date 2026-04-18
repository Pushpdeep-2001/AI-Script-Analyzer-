# AI Script Analyzer 🚀

AI Script Analyzer is a high-performance, multi-dimensional analysis tool designed to help content creators, scriptwriters, and producers evaluate their scripts using modern Large Language Models.

---

## 🌟 Features

- **Parallel Analysis**: Simultaneously analyzes Summary, Emotions, Engagement, Cliffhangers, and Improvements using specialized AI workers or agents.
- **Clean UI**: A modern, tabbed interface for structured and easy-to-read results.
- **Robust Backend**: Built with FastAPI, featuring validation, async orchestration, and structured logging.
- **Production-Oriented Design**: Includes retry logic, health checks, and log rotation for reliability.

---

## 🏗️ Overall Approach

The system follows an **Orchestrator-Worker/Agent Pattern**:

1. **Validation Layer**  
   Ensures the script meets minimum structural and length requirements (e.g., must include a "Title").

2. **Context Builder**  
   Generates a shared context so all workers operate on the same input.

3. **Parallel Orchestration**  
   The orchestrator triggers multiple specialized AI workers/agents concurrently for faster execution.

4. **Specialized Workers**  
   Each worker focuses on a single task:
   - Summary
   - Emotion Analysis
   - Engagement Scoring
   - Cliffhanger Detection
   - Optimization Suggestions

5. **Structured Output**  
   Responses are validated using Pydantic schemas to ensure consistency and reliability.

---

## 🔍 Design Philosophy

The system is intentionally designed as a **lightweight, modular pipeline**, inspired by LangChain-style architectures.

Instead of introducing heavy frameworks, a **custom orchestrator-worker system** was implemented to:
- maintain full control over execution
- ensure predictable performance
- simplify debugging and observability

This approach keeps the system efficient while remaining **easily extensible**.

If scaled further, this architecture can integrate with frameworks like :contentReference[oaicite:0]{index=0} for:
- advanced prompt management
- structured output parsing
- dynamic workflow orchestration

---

## 🧠 Engineering Decisions

### Why Multi-Worker Architecture?
Instead of a single large LLM call, the system uses specialized workers/Agent to:
- improve focus and depth of analysis
- reduce prompt complexity
- enable parallel execution for better performance

---

### Why Keep It Simple?
Heavy frameworks (like LangChain or LlamaIndex) were intentionally avoided in the core system to:
- reduce unnecessary abstraction
- improve transparency
- allow fine-grained control over prompts and outputs

This reflects a conscious trade-off:
> **Clarity and control over abstraction**

---

### When Would This Be Scaled?

For production-grade systems, the following improvements would be introduced:
- pipeline orchestration frameworks (LangChain-style)
- caching layers for repeated queries
- queue-based processing (Celery, Redis)
- observability tools (Prometheus, OpenTelemetry)
- rate limiting and request control

---

## 🤖 Prompt & Model Interaction Design

The system uses carefully designed prompts to ensure **structured and reliable outputs**:

- **Persona-Based Prompting**  
  Each worker acts as a domain expert (e.g., Emotional Analyst, Script Doctor).

- **Strict JSON Enforcement**  
  All responses are generated in JSON format for seamless parsing.

- **Grounded Reasoning**  
  The model is instructed to rely only on the provided script, minimizing hallucinations.

- **Task-Specific Temperature Control**  
  Different workers use different temperature settings to balance determinism and creativity.

---

## 🛠️ Tools & Technologies

- **LLM Engine**: :contentReference[oaicite:1]{index=1} (`llama-3.3-70b-versatile`)
- **Backend**: :contentReference[oaicite:2]{index=2}
- **Validation**: :contentReference[oaicite:3]{index=3}
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Logging**: Python logging with `TimedRotatingFileHandler`

---

## ⚠️ Limitations

- **Model Constraints**  
  The system uses a free-tier LLM, which may have:
  - limited context window
  - occasional variability in responses

- **Context Window Limit**  
  Scripts are truncated beyond ~4,000 characters to fit model limits.

- **Single Script Context**  
  No memory across multiple scripts or sessions.

- **No File Upload Support (Yet)**  
  Currently accepts only raw text input (no PDF or document ingestion).

- **Worker Independence**  
  Parallel workers may occasionally produce slightly inconsistent interpretations.

---

## 🚀 Possible Improvements

- **PDF / Document Upload Support**  
  Allow users to upload scripts via PDF or text files with parsing.

- **Long Script Handling**  
  Implement chunking + summarization pipelines for full-length scripts.

- **Consistency Layer**  
  Cross-worker validation to align outputs (e.g., summary vs emotions).

- **Better Models**  
  Upgrade to higher reasoning models (GPT-4.x / Claude).

- **Vector Database (RAG)**  
  Enable querying large scripts using semantic search.

- **Character Analysis**  
  Add worker for character arcs and development.

- **Batch Processing**  
  Analyze multiple scripts and compare engagement.

- **Export Feature**  
  Download reports as PDF or shareable links.

---

## 🔮 Future Architecture Vision

This system is designed as a **foundation for a scalable AI content intelligence platform**.

With further development, it can evolve into:
- a **RAG-based system** for large script analysis
- a **multi-modal platform** (text + audio + video)
- a **collaborative tool** for writers and production teams

The modular architecture ensures these features can be added without major refactoring.

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-script-analyzer
````

---

### 2. Create a `.env` file

```env
GROQ_API_KEY=your_api_key
MODEL=llama-3.3-70b-versatile
HOST=127.0.0.1
PORT=8000
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the project

```bash
python run.py
```

---

### 5. Health Check

```
GET http://127.0.0.1:8000/health
```

---

## 🎯 Summary

This project demonstrates:

* practical LLM system design
* structured output handling
* parallel AI orchestration
* thoughtful engineering trade-offs

The focus is not just on using AI, but on **building a reliable and extensible AI system**.
```
