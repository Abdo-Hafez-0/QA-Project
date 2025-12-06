# QA Project — Schedule, Boards, Repo & Member Instructions

This document contains everything you asked for:

- ✅ A Gantt chart (6-week plan)
- ✅ Trello task board structure (lists, cards, checklists, labels)
- ✅ GitHub folder setup with branches per member and PR workflow
- ✅ Step-by-step instructions for each member (who does what, and how)

> All deliverables reference the filenames and roles we agreed on earlier.

---

# 1. Gantt Chart — 6-week plan (High-level)

The project is organized in 6 calendar weeks. Each week has clear milestones and owners.

| Week | Dates (example) | Key Activities | Owner (primary) | Deliverable / Milestone |
|------|------------------|----------------|------------------|-------------------------|
| Week 1 | Week 1 (Day 1–7) | Project kickoff, dataset review, finalise question & goals, repo + Trello setup | Team Leader + All | Project brief, Trello board, GitHub repo initialized |
| Week 2 | Week 2 (Day 8–14) | Data import & cleaning; initial EDA | Data Engineer + EDA Analyst | `1_data_import.ipynb`, `2_cleaning.ipynb`, initial EDA plots |
| Week 3 | Week 3 (Day 15–21) | Advanced EDA, feature engineering begins, statistical tests | EDA Analyst + Feature Engineer | `3_EDA.ipynb`, `4_features.ipynb` (draft) |
| Week 4 | Week 4 (Day 22–28) | Finish feature engineering, finalize cleaned dataset, baseline models | Feature Engineer + Team Leader | `BankChurners_cleaned.csv`, baseline model results |
| Week 5 | Week 5 (Day 29–35) | Model tuning, cross-validation, interpretability, SHAP/feature importance | Team Leader + Feature Engineer | `6_modeling.ipynb`, evaluation plots, model.pkl |
| Week 6 | Week 6 (Day 36–42) | Final visualizations, documentation, presentation prep, wrap-up & handover | Visualization + Documentation Specialist + All | `7_visualization.ipynb`, PowerPoint, final report PDF |

**Milestone checkpoints:**
- End Week 1: Repo + Board + Project brief
- End Week 3: Cleaned dataset + EDA + features
- End Week 5: Final model + evaluation
- End Week 6: Final report + presentation

---

# 2. Trello Board Structure (Suggested)

**Board name:** `QA_Project_BankChurners`

**Lists (left-to-right):**
1. Backlog (ideas / future tasks)
2. To Do (this sprint/week)
3. In Progress
4. Review / QA (peer review & PR reviews)
5. Blocked / Waiting
6. Done
7. Docs & Deliverables (final files, links, presentations)

**Labels:**
- Red: `High Priority`
- Orange: `Bug / Issue`
- Yellow: `Data`
- Green: `Modeling`
- Blue: `Visualization`
- Purple: `Documentation`

**Example cards & templates:**

Card: `Data import — BankChurners.csv`
- Description: Import raw CSV, inspect columns, save raw copy.
- Checklist:
  - [ ] Load CSV
  - [ ] Check row count
  - [ ] Save raw copy to `data/raw/`
  - [ ] Push to GitHub
- Labels: Yellow
- Members: Data Engineer

Card: `Cleaning & Preprocessing`
- Description: Handle missing values, duplicates, data types, encoding plan.
- Checklist:
  - [ ] Missing values report
  - [ ] Impute / drop strategy
  - [ ] Encode categorical features
  - [ ] Save cleaned CSV to `data/cleaned/`
- Labels: Yellow
- Members: Data Engineer

Card: `Exploratory Data Analysis`
- Description: Produce charts, summary stats, correlation heatmap.
- Checklist:
  - [ ] Descriptive stats
  - [ ] Histograms
  - [ ] Boxplots
  - [ ] Correlation heatmap
  - [ ] Export plots to `presentation/figs/`
- Labels: Blue
- Members: EDA Analyst

Card: `Feature Engineering`
- Description: Create new features, finalize feature set for modeling.
- Checklist:
  - [ ] Candidate features list
  - [ ] Implementation in script
  - [ ] Save `data/engineered/` dataset
- Labels: Yellow + Green
- Members: Feature Engineer

Card: `Modeling — Baseline`
- Description: Train baseline models, record metrics.
- Checklist:
  - [ ] Logistic Regression baseline
  - [ ] Random Forest baseline
  - [ ] Save baseline metrics table
- Labels: Green
- Members: Team Leader

Card: `Presentation & Report`
- Description: Final slides and written report
- Checklist:
  - [ ] Create slides
  - [ ] Write documentation
  - [ ] Export PDF report
- Labels: Purple
- Members: Documentation Specialist

**Automation suggestions (Trello Butler):**
- When a card moves to `Review / QA`, add comment `Please request a PR review`.
- When a card is moved to `Done`, copy to `Docs & Deliverables` and attach final file link.

---

# 3. GitHub Folder Setup & Branch Strategy

**Repository name:** `qa-bankchurners`

**Suggested root structure:**
```
qa-bankchurners/
├── data/
│   ├── raw/                     # original CSVs
│   ├── cleaned/                 # cleaned CSVs
│   └── engineered/              # feature-engineered datasets
├── notebooks/
│   ├── 1_data_import.ipynb
│   ├── 2_cleaning.ipynb
│   ├── 3_EDA.ipynb
│   ├── 4_features.ipynb
│   ├── 5_stats.ipynb
│   ├── 6_modeling.ipynb
│   └── 7_visualization.ipynb
├── scripts/
│   ├── data_import.py
│   ├── clean.py
│   ├── feature_engineer.py
│   └── train.py
├── models/
│   └── model.pkl
├── presentation/
│   └── QA_Project_Presentation.pptx
├── documentation/
│   └── Final_Report.pdf
├── requirements.txt
└── README.md
```

**Branches & naming convention:**
- `main` — stable final code and deliverables
- `dev` — integration branch for merging feature branches
- Feature branches (one per member):
  - `leader/modeling` (Team Leader)
  - `data-engineer/cleaning` (Data Engineer)
  - `eda/exploration` (EDA Analyst)
  - `features/engineering` (Feature Engineer)
  - `docs/presentation` (Visualization & Documentation Specialist)

**Pull Request workflow:**
1. Work locally on your feature branch.
2. Commit frequently with clear messages.
3. Push branch to GitHub: `git push origin <branch>`.
4. Create a Pull Request targeting `dev`.
5. At least one peer reviews the PR (comments + approvals).
6. Merge PR into `dev` after resolving comments.
7. At integration checkpoints (end of Week 3, Week 5), merge `dev` into `main` (Team Leader or Reviewer does this) after final QA.

**Protect `main`:** enable branch protection rules; require PR reviews and passing CI (if available).

---

# 4. Step-by-step Instructions for Each Member

These are actionable steps (commands and notebook tasks) for each of the 5 team members.

## 1) Team Leader — Technical Leader (Modeling)
**Primary files:** `notebooks/6_modeling.ipynb`, `scripts/train.py`

**Weekly focus:** oversee project, implement modeling, final integrations.

**Steps:**
1. Confirm project goal and evaluation metric (e.g., ROC-AUC, F1). Add to `README.md`.
2. Create branch: `git checkout -b leader/modeling`
3. Pull cleaned & engineered dataset from `data/engineered/`.
4. Implement baseline models in `6_modeling.ipynb`:
   - Logistic Regression
   - Random Forest
   - XGBoost (if allowed)
5. Save trained best model as `models/model.pkl` using `joblib.dump()`.
6. Produce evaluation artifacts: confusion matrix, ROC curve, classification report.
7. Push branch, open PR to `dev`. Request reviews from Data Engineer and Feature Engineer.

**Commands:**
```
git checkout -b leader/modeling
git add notebooks/6_modeling.ipynb scripts/train.py
git commit -m "Add baseline models and evaluation"
git push origin leader/modeling
```

**Deliverables:** `models/model.pkl`, `6_modeling.ipynb`, PR merged to `dev`.

---

## 2) Data Engineer — Data Import & Cleaning
**Primary files:** `notebooks/1_data_import.ipynb`, `notebooks/2_cleaning.ipynb`, `scripts/clean.py`

**Steps:**
1. Create branch: `git checkout -b data-engineer/cleaning`
2. Load CSV, inspect types, count rows: `pd.read_csv('data/raw/BankChurners.csv')`.
3. Save a raw copy to `data/raw/` with a timestamped filename.
4. Generate a missing-values report and share in Trello.
5. Implement cleaning rules in `clean.py`:
   - Fix column types
   - Fill or drop missing values (document decision)
   - Remove duplicates
   - Save cleaned CSV to `data/cleaned/BankChurners_cleaned.csv`
6. Push branch and open PR to `dev` for code review.

**Commands:**
```
git checkout -b data-engineer/cleaning
python scripts/clean.py
git add data/cleaned/BankChurners_cleaned.csv scripts/clean.py
git commit -m "Add cleaning script and cleaned dataset"
git push origin data-engineer/cleaning
```

**Deliverables:** `data/cleaned/BankChurners_cleaned.csv`, cleaning script, notebook.

---

## 3) EDA Analyst — Exploratory Data Analysis
**Primary files:** `notebooks/3_EDA.ipynb`

**Steps:**
1. Create branch: `git checkout -b eda/exploration`
2. Load cleaned dataset from `data/cleaned/`.
3. Produce descriptive stats (`df.describe()`, `value_counts()`).
4. Create and save plots to `presentation/figs/`:
   - Churn counts
   - Age distribution
   - Credit limit distribution
   - Correlation heatmap
5. Write short interpretations under each plot in the notebook.
6. Push and open PR to `dev`.

**Commands:**
```
git checkout -b eda/exploration
# run cells, export figures
git add notebooks/3_EDA.ipynb presentation/figs/
git commit -m "Add EDA notebook and figures"
git push origin eda/exploration
```

**Deliverables:** `3_EDA.ipynb`, plots in `presentation/figs/`.

---

## 4) Feature Engineer + Stats Analyst
**Primary files:** `notebooks/4_features.ipynb`, `notebooks/5_stats.ipynb`, `scripts/feature_engineer.py`

**Steps:**
1. Create branch: `git checkout -b features/engineering`
2. Load cleaned dataset from `data/cleaned/`.
3. Propose feature list and implement in `feature_engineer.py`:
   - Examples: `tenure_bins`, `avg_balance_ratio`, `recent_txn_flag`, `engagement_score`.
4. Run statistical tests in `5_stats.ipynb` (chi-square, t-tests) and document p-values.
5. Save engineered dataset to `data/engineered/market_ready.csv`.
6. Push branch and open PR to `dev`.

**Commands:**
```
git checkout -b features/engineering
python scripts/feature_engineer.py
git add data/engineered/ scripts/feature_engineer.py notebooks/4_features.ipynb
git commit -m "Add feature engineering and stats analysis"
git push origin features/engineering
```

**Deliverables:** `data/engineered/market_ready.csv`, features notebook, stats notebook.

---

## 5) Visualization Designer + Documentation Specialist
**Primary files:** `notebooks/7_visualization.ipynb`, `presentation/QA_Project_Presentation.pptx`, `documentation/Final_Report.pdf`

**Steps:**
1. Create branch: `git checkout -b docs/presentation`
2. Pull latest figures from `presentation/figs/` and model evaluation plots.
3. Assemble presentation (10–12 slides):
   - Title & team
   - Objective & dataset
   - EDA highlights
   - Feature engineering summary
   - Modeling results & metrics
   - Conclusion & recommendations
4. Write the final report (3–5 pages): methods, results, conclusions.
5. Export PPTX to `presentation/` and report PDF to `documentation/`.
6. Push branch and open PR to `dev`.

**Commands:**
```
git checkout -b docs/presentation
# create pptx and pdf locally
git add presentation/ documentation/
git commit -m "Add presentation and final report"
git push origin docs/presentation
```

**Deliverables:** final presentation and report.

---

# 5. Code Style & Collaboration Rules (Quick)
- Use `requirements.txt` to pin packages.
- Each notebook must include: header, objective, brief summary, and conclusions.
- Commit messages: `type(scope): short description` e.g. `feat(clean): add missing values report`.
- PR description must list files changed, purpose, and reviewers.
- Reviewer checklist for PRs: tests (if any), notebooks run end-to-end, outputs attached.

---

# 6. Quick Onboarding Checklist (first day)
1. Everyone forks/clones repo.
2. Create your feature branch from `dev`.
3. Set Trello notifications and assign initial cards to yourself.
4. Run `pip install -r requirements.txt`.
5. Run `notebooks/1_data_import.ipynb` to confirm data access.

---

# 7. Extras & Tips
- Use small, descriptive commits (helps review).
- Export final figures as PNG/SVG at 1200px width for presentation clarity.
- If time allows, add a simple CI check (GitHub Actions) that ensures notebooks run without errors.
- Document any data decisions (why you imputed/drop rows) — reviewers love this.

---

If you want, I can now:
- Generate a printable Gantt chart (PNG) inside a notebook and add it to `presentation/figs/`.
- Produce Trello JSON export template.
- Create the GitHub repo with branches (if you give me repo details).

Tell me which of the extras you want and I will add them to the repo and Trello templates.

