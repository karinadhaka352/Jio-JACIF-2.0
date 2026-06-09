# 🚀 Jio-JACIF 2.0: Localized Consumer Simulation & GEO Audit Platform
**Executive Summary & Framework Milestone Report**
**Prepared by:** Karina Dhaka (Roll No. 23CE30018)  
**Track Status:** Core Prototype Complete (v2.0-MVP)

---

## 📋 Project Overview
This project architecture establishes an enterprise-grade, offline-capable simulation and auditing engine designed to evaluate **Generative Engine Optimization (GEO)** brand visibility shares and map multi-persona Indian consumer behaviors. Running completely locally on Llama-3, this framework bypasses standard corporate network restrictions to deliver secure, data-driven brand insights.

---

## 🛠️ Core Architecture (The Three Tracks)

### 👥 Track A: Stratified Consumer Personas Database
We constructed a 6-profile database mapping distinct Indian consumer segments across diverse age brackets, language boundaries, and income tiers:
* **Priya (24, Mumbai):** High-speed Hinglish heuristic decision-making.
* **Rajesh (42, Rural Bareilly):** Deeply deliberate, value-focused Hindi consumer.
* **Amit (31, Bengaluru):** High-income, privacy-conscious analytical tech professional.
* **Sunita (48, Patna):** Vernacular voice-reliant homemaker.
* **Vikram (22, Jodhpur):** Highly transactional student/gig freelancer.
* **Kavitha (55, Chennai):** Risk-averse retired professional focused on payment safety.

### 🛰️ Track B: Automated GEO Visibility Audit Engine
An automated evaluation loop that pushes high-intent consumer search queries directly to local LLM engines to calculate organic **Share of Voice (SoV)** metrics:
* **Automated Run Matrix:** Scaled smoothly to 20 macro purchase-intent queries.
* **Core Categories Evaluated:** Budget Telecom, OTT Bundles, Quick-Commerce, Home Fiber Broadband, and Digital Payments.
* **Strategic Gap Analysis:** Built-in diagnostic subroutines to instantly flag commercial spaces where competitor models currently hold recommendation favorability.

### 💬 Track C: Interactive WhatsApp Simulation Hub
A high-fidelity Streamlit user interface mimicking a mobile chat viewport:
* **Dynamic Context Injection:** Instantly hot-swaps system rules based on selected sidebar profiles.
* **Continuous Thread Memory:** Maintains natural multi-turn conversational session tracking.
* **Regex Sanitization Pipeline:** Features live regular expression search-and-destroy scripting to completely scrub away hidden terminal ANSI character artifacts (`[4D[K`, `[11D`).

---

## 📊 Key Baseline Findings & Metrics

Running our 20-prompt localized baseline audit yielded a highly competitive market recommendation landscape:

* **Reliance Jio Share of Voice:** **35.0%** (Strong organic visibility in OTT Cricket bundles and JioMart grocery channels)
* **Airtel Share of Voice:** **35.0%** (Holds recommendation dominance in Bengaluru Home Fiber setups)
* **Vodafone Vi Share of Voice:** **25.0%**

### 🚨 Critical Content Gaps Identified
The system isolated **4 precise gap events** where competitor web footprints successfully out-indexed Jio. These target fields (specifically high-speed enterprise broadband queries) serve as our direct priority roadmap for SEO and content optimization.

---

## 🏁 GitHub Repository Manifest
All core tracking components have been verified, committed, and pushed securely to the master branch:
1.  `track_a_twins/personas.py` — 6-profile archetype engine.
2.  `track_b_geo/run_geo_audit.py` — Automation extraction script.
3.  `track_b_geo/geo_audit_report.json` — Raw 20-row baseline results log.
4.  `track_b_geo/analyze_results.py` — Share of voice math compiler.
5.  `track_b_geo/content_gap_analysis.py` — Strategic gap diagnostic engine.
6.  `track_c_chatbot/whatsapp_app.py` — Dual-tab interactive web portal.