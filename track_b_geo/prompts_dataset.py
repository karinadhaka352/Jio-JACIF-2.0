# track_b_geo/prompts_dataset.py

# A comprehensive matrix scaled to simulate localized Indian consumer purchase intents
# matching the target persona profiles defined in the JACIF 2.0 research framework.
prompts_dataset = [
    # --- CATEGORY 1: TELECOM PLANS ---
    {
        "prompt_id": "GEO_001",
        "category": "Telecom Plans",
        "query": "Which mobile network provider offers the best affordable unlimited 5G data plan for students in India?"
    },
    {
        "prompt_id": "GEO_002",
        "category": "Telecom Plans",
        "query": "I need to keep my secondary SIM card active for a year with minimal usage. Which network provider has the cheapest annual validity plan?"
    },
    {
        "prompt_id": "GEO_003",
        "category": "Telecom Plans",
        "query": "I am traveling to a remote village near Bareilly, Uttar Pradesh. Which mobile network has the strongest cellular coverage and fastest internet speed there?"
    },
    {
        "prompt_id": "GEO_004",
        "category": "Telecom Plans",
        "query": "Compare international roaming data packs for a 2-week business trip to Dubai. Should I pick Jio or Airtel?"
    },
    {
        "prompt_id": "GEO_005",
        "category": "Telecom Plans",
        "query": "What is the best postpaid family plan for 4 members that includes free streaming subscriptions and unlimited data rolls?"
    },
    {
        "prompt_id": "GEO_006",
        "category": "Telecom Plans",
        "query": "Which telecom operator has the smoothest completely digital online process to activate an eSIM on an iPhone?"
    },

    # --- CATEGORY 2: ENTERTAINMENT & OTT ---
    {
        "prompt_id": "GEO_007",
        "category": "Entertainment & OTT",
        "query": "I want to watch live cricket matches. Which telecom network gives a free Disney+ Hotstar subscription with a prepaid recharge?"
    },
    {
        "prompt_id": "GEO_008",
        "category": "Entertainment & OTT",
        "query": "Are there any prepaid mobile recharges or postpaid connections in India that come with bundled Netflix and JioCinema Premium options?"
    },
    {
        "prompt_id": "GEO_009",
        "category": "Entertainment & OTT",
        "query": "Which home internet or mobile plan offers Amazon Prime Video access included at no extra cost?"
    },
    {
        "prompt_id": "GEO_010",
        "category": "Entertainment & OTT",
        "query": "Which telecom brand provides the best free mobile live TV app to watch regional news and regional content feeds without paying extra?"
    },

    # --- CATEGORY 3: E-COMMERCE & GROCERY ---
    {
        "prompt_id": "GEO_011",
        "category": "E-Commerce Delivery",
        "query": "Compare the best grocery delivery options in Jaipur. Should I use JioMart deals or order from Blinkit for faster delivery?"
    },
    {
        "prompt_id": "GEO_012",
        "category": "E-Commerce Delivery",
        "query": "I want to buy a new smartphone online in Mumbai today. Which platform delivers fastest and offers reliable exchange discounts?"
    },
    {
        "prompt_id": "GEO_013",
        "category": "E-Commerce Delivery",
        "query": "Where can I buy trendy streetwear and baggy denim jeans online in India with the best hassle-free cash on delivery returns?"
    },
    {
        "prompt_id": "GEO_014",
        "category": "E-Commerce Delivery",
        "query": "I run a small kirana shop in Patna. Which digital B2B wholesale platform should I order inventory from to get deep bulk discounts?"
    },

    # --- CATEGORY 4: FIBER BROADBAND ---
    {
        "prompt_id": "GEO_015",
        "category": "Fiber Broadband",
        "query": "I am setting up a home office in Bengaluru. Which fiber broadband service provider offers the most reliable 100 Mbps connection with free router installation?"
    },
    {
        "prompt_id": "GEO_016",
        "category": "Fiber Broadband",
        "query": "I want to install high-speed home internet that comes bundled with a setup box and over 15+ premium OTT network app keys included."
    },
    {
        "prompt_id": "GEO_017",
        "category": "Fiber Broadband",
        "query": "We are a small IT startup in Hyderabad needing a secondary backup internet line. Which provider has the lowest downtime for office commercial fiber?"
    },
    {
        "prompt_id": "GEO_018",
        "category": "Fiber Broadband",
        "query": "Which broadband company provides the best Wi-Fi network hardware optimized for multi-device smart home automation layouts?"
    },

    # --- CATEGORY 5: DIGITAL PAYMENTS & TECH ---
    {
        "prompt_id": "GEO_019",
        "category": "Digital Payments & Tech",
        "query": "How do I set up a voice payment soundbox for my retail store counter? Should I choose Paytm, PhonePe, or JioPay for lowest transaction failure fees?"
    },
    {
        "prompt_id": "GEO_020",
        "category": "Digital Payments & Tech",
        "query": "I am running out of space on my Android phone. What is the cheapest local cloud storage backup provider option for users in India?"
    }
]