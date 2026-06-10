# Jio Institute Summer Research Fellowship 2026
## Mid-Term Progress Report: AI Consumer Twins & GEO Share of Voice Analytics

**Project Title:** Simulating Indian Consumer Purchase Intent and Generative Engine Optimization (GEO) Compliance Frameworks  
**Author:** Karina Dhaka (Summer Research Intern)  
**Track Focus:** Track B (GEO Search Audits) & Track C (Behavioral Sandbox)  
**Status:** Software Sprints 100% Complete / Transitioning to Empirical Modeling  

---

## 1. Executive Summary
This research project builds an automated evaluation framework to study Indian consumer interactions with Generative AI engines. By deploying synthetic "Consumer Twins" across targeted commercial demographics, we analyze brand recommendation visibility (Share of Voice) while testing behavioral trust shifts under varying experimental transparency conditions.

---

## 2. Completed Milestones & System Architecture

### Track B: GEO Search Optimization Audit Engine
- **Automated Pipeline:** Built an execution loop in `run_geo_audit.py` that systematically pipes user intent matrices directly into a local Llama-3 model instance.
- **Dataset Scaling:** Expanded the prompt baseline repository (`prompts_dataset.py`) to cover diverse localized consumer queries across core sectors (Telecom, OTT Streaming, E-Commerce, and Fiber Broadband).
- **Dynamic Analytics:** Structured a live analytics dashboard view (`whatsapp_app.py` under Tab 2) that parses raw search logs into an interactive brand visibility metric board.

### Track C: Interactive Behavioral Twin Sandbox
- **Persona Emulation:** Configured localized Indian user profiles (e.g., *Priya — Tier 3 Mumbai Corporate*) using authentic linguistic Hinglish patterns.
- **Three-Arm Empirical Design:** Fully implemented three distinct system prompt conditions inside the chatbot execution loop:
  1. *Condition A (Transactional Baseline):* Flat, purely factual brand responses.
  2. *Condition B (Emotional Mirroring):* Empathetic, peer-to-peer style communication.
  3. *Condition C (Emotional AI + DPDP Disclosure):* Blends conversational warmth with explicit data usage transparency notices under the **Digital Personal Data Protection (DPDP) Act 2023**.

---

## 3. Preliminary Empirical Observations
Initial dry-run processing of user intent queries reveals strong operational variance across the experimental configurations:
- **Condition A** keeps recommendation paths direct but lacks engagement hooks.
- **Condition B** significantly lowers psychological reactance by adopting peer vernacular (*"Yaar"*, *"Na"*).
- **Condition C** successfully introduces strict data compliance mechanisms into the conversational layout without creating user drop-off or interface friction.

---

## 4. Statistical Validation & Next Steps
- **Data Collection Sheet:** Created `experimental_log_matrix.csv` to log real conversational responses and score them using a 1–5 Likert scale across key TAM and Privacy Calculus constructs.
- **Analytical Engine:** Implemented `analyze_empirical_data.py` to ingest observations and automatically compute Kullback-Leibler (KL) Divergence and Kolmogorov-Smirnov (KS) distribution alignment tests.
- **Next Phase Goal:** Scale the log matrix data collection across the entire prompt repository to generate the statistical volume required for final modeling checks.