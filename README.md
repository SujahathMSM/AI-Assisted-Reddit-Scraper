# 📘 **AI-Assisted Reddit Scraper**

Transform fuzzy natural-language interests into a structured, continuously updated Reddit dataset.
This system uses **LLM-driven discovery**, **remote asynchronous scraping**, and **event-driven ingestion** to build a resilient Reddit data pipeline.

---

## 🚀 **Project Goal (Short Version)**

Convert an ambiguous user interest (e.g., *"I like camping using an RV"*) into:

1. A list of relevant Reddit communities
2. Repeated scraping jobs for each community
3. A structured, queryable dataset of Reddit posts stored in PostgreSQL

All powered by an intelligent, decoupled, event-driven architecture.

---

## 🧠 **High-Level Architecture**

```
User Query → LLM Discovery → SERP Search → Subreddit List
                  ↓
           Django Orchestration
                  ↓
   Asynchronous Scrape Jobs (Bright Data)
                  ↓
       Job Completion (Webhook / Polling)
                  ↓
      Snapshot Download → JSON Parsing
                  ↓
       Upsert into PostgreSQL (RedditPost)
```

### Core Components

| Component               | Purpose                                                        |
| ----------------------- | -------------------------------------------------------------- |
| **Django**              | Orchestration core: models, admin, API/webhooks, task triggers |
| **Google Gemini (LLM)** | Converts fuzzy input → structured topics, parses SERP data     |
| **Bright Data**         | Reliable remote scraper & SERP API provider                    |
| **Celery + Redis**      | Async tasks, scraping job polling, ingestion workflows         |
| **PostgreSQL**          | Primary datastore for communities, jobs, posts                 |
| **Docker / WSL2**       | Local development environment                                  |

---

## 🧩 **How the Pipeline Works**

### **1. AI-Powered Community Discovery**

A user runs:

```
python manage.py query "I like camping using an RV"
```

The system:

* Uses Gemini to extract topics
* Calls Bright Data SERP to find relevant subreddits
* Forces strict Pydantic schema validation
* Saves structured results into PostgreSQL (`RedditCommunity`)

---

### **2. Asynchronous Scraping**

For each community marked `trackable`, Django triggers a remote scraping job on Bright Data.

This job runs **off your machine**, solving:

* IP blocking
* Proxy rotation
* HTML changes
* JavaScript rendering

Django only acts as the **orchestrator**, not the scraper.

---

### **3. Job Monitoring & Data Ingestion**

Two mechanisms detect job completion:

* **Celery polling** (periodic)
* **Webhook callback** from Bright Data (recommended)

When a snapshot is ready:

* Download JSON
* Parse essential fields (post_id, url, title, score, comments)
* `update_or_create` into `RedditPost` for long-term analysis

---

### **4. Automation Framework**

The system uses:

* **Django signals** → Immediately scrape newly tracked communities
* **Celery Beat (cron)** → Daily scraping of all trackable communities
* **Management command** → `python manage.py track` to trigger manual scraping

---

## 🛠️ **Development Setup**

### **Requirements**

* Windows 11 + **WSL2 Ubuntu**
* Docker Desktop (WSL integration on)
* Python 3.12 (inside WSL)
* Bright Data API key (later)
* Google Gemini key (later)

---

### **1. Clone & Enter Repository**

```bash
git clone https://github.com/yourname/ai-reddit-scraper.git
cd ai-reddit-scraper
```

---

### **2. Python Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### **3. Copy Environment File**

```bash
cp .env.example .env
```

Edit `.env` and add your real keys later.

---

### **4. Start Local Infrastructure**

```bash
docker compose up -d
```

This starts:

* Postgres
* Redis
* Django container scaffold (not running server yet)

---

### **5. Apply Migrations**

```bash
docker compose exec web bash
python manage.py migrate
```

---

## 📚 **Project Structure**

```
ai-reddit-scraper/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env.example
│
├── project/           ← Django project
└── scraper/           ← Core app (discovery, scraping, ingestion)
```

---

## 🧪 **Future Extensions**

* Add metrics + Prometheus/Grafana dashboards
* Build analytics endpoints for processed posts
* Deploy to AWS (ECS/K8s/Fargate)
* Add tracing with OpenTelemetry
* Stream snapshots to S3 for long-term storage

---

## 🤝 **Contributing**

All contributions are welcome. Use PRs, issues, or discussions to propose improvements.

---

## 📜 **License**

MIT License.


