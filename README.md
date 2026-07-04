# Global Tech Layoffs & Market Trends Analysis

An interactive enterprise-grade Tableau data analytics platform engineered to isolate, track, and visualize macroeconomic restructuring indicators across global technology ecosystems from 2020 to 2026.

## 📊 Live Interactive Dashboard
👉 **[Click Here to View the Live Interactive Dashboard](https://public.tableau.com/app/profile/shabbir.rajgarh/viz/Global_Tech_Layoffs_Dashboard/Dashboard1?publish=yes)**

---

## 🖥️ Dashboard Architecture
![Global Tech Layoffs Dashboard](Screenshot%202026-07-04%20182516.png)

---

## 🛠️ Technical Workflow & Tooling
* **Data Engineering (Python / Pandas):** Programmed a modular ETL pipeline (`etl_pipeline.py`) to extract raw multi-variable records, standardize chronological datetime fields, impute missing null values, and clean categorical text strings.
* **Data Layer:** Feeds a high-performance, cleaned CSV output directly into the visualization workspace.
* **Aggregation Metrics:** Engineered optimized calculated fields and explicit counts (`CNT(Event Id)`) inside Tableau to extract precise frequency volumes without adding dimension clutter.
* **UI/UX & Interactivity:** Developed bidirectional Dashboard Actions ("Use as Filter"), allowing end-users to click any region on the spatial heatmap or tech sector to dynamically filter the entire workspace globally in real time.
* **Deployment:** Packaged and published the analytics file via Tableau Public (`.twbx`) for flawless cross-platform compliance and executive review.## 🚀 Key Analytical Insights
* **Macro Temporal Trends:** Tracks the cyclical wave of workforce restructuring across the global tech sector, highlighting pivotal spikes and normalization phases over a multi-year timeline.
* **Sector-Specific Vulnerability:** Pinpoints which business models (e.g., Fintech, Social Media, E-commerce) faced the highest frequency of organizational restructuring.
* **Geographical Distribution:** A complete spatial heatmap mapping the density of restructuring actions across international tech hubs, enabling rapid regional impact assessment.

---

