Below is **exactly what each member will do** *based specifically on the Bank Churners dataset* AND the requirements of your **QA Project (9 steps)**.

This is the **most precise, role-based breakdown** tailored to your dataset.

---

# 🔥 **Dataset Reminder: BankChurners.csv**

It contains:

* **10,000+ customers**
* Features: Age, Gender, Credit Limit, Total Transactions, Education Level, Marital Status, Income Category, Months on Book, etc.
* **Target:** Attrition_Flag (Churn vs Existing Customer)

Your project must include: cleaning, EDA, feature engineering, statistical analysis, modeling, visualization, interpretation, documentation.

---

# ✅ **1 — Data Engineer (Starts First)**

### **Exact responsibilities based on your dataset**

This member prepares the entire dataset for the team.

### ✔️ Tasks

1. **Import the dataset** into a Jupyter notebook.
2. **Inspect structure:**

   * Check number of rows/columns
   * Check nulls
   * Check data types
3. **Clean the dataset:**

   * Fix inconsistent types
   * Remove duplicates
   * Handle missing values
4. **Encode categorical columns** (if needed for exploration):

   * Gender
   * Education_Level
   * Income_Category
   * Marital_Status
   * Card_Category
5. **Save cleaned dataset** → `data/cleaned/BankChurners_cleaned.csv`
6. Write notes on how each column was cleaned and why.
7. Push notebook + cleaned dataset to GitHub for the next members.

### 🎯 **Output**

* `1_data_import.ipynb`
* `2_cleaning.ipynb`
* Cleaned CSV
* Cleaning decisions documented
* Ready-to-use data for EDA

---

# ✅ **2 — EDA Analyst (Starts After Cleaned Data)**

### **Exact responsibilities based on your dataset**

This member explores the customer behavior and churn characteristics.

### ✔️ Tasks

1. Load **cleaned** dataset.

2. Compute **descriptive statistics**:

   * Average credit limit
   * Average months on book
   * Mean transaction count

3. Create visualizations:

   * Churn distribution
   * Customer age distribution
   * Credit limit histogram
   * Total transaction histogram
   * Churn vs transaction count
   * Churn vs age

4. Generate **correlation heatmap**.

5. Identify patterns such as:

   * “Low transaction customers churn more”
   * “Longer tenure → lower churn”

6. Save all plots into `presentation/figs/`.

### 🎯 **Output**

* `3_EDA.ipynb`
* 6–10 plots
* A summary of the discovered patterns

---

# ✅ **3 — Feature Engineer + Statistical Analyst**

### **Exact responsibilities based on your dataset**

This member transforms the raw fields into meaningful model inputs.

### ✔️ **Feature Engineering Tasks**

Create NEW columns such as:

#### ✳️ **1. Activity Ratio**

```
Total_Trans_Amt / Total_Trans_Ct
```

#### ✳️ **2. Engagement Score** (example)

```
(Months_on_book + Contacts_Count_12_mon + Total_Trans_Ct)
```

#### ✳️ **3. High Credit Flag**

```
1 if Credit_Limit > median else 0
```

#### ✳️ **4. Transaction Frequency Group**

Bin:

* Low
* Medium
* High

#### ✳️ **5. Tenure Group**

Bucket `Months_on_book` into:

* New (<= 24 months)
* Medium
* Loyal (> 48 months)

### ✔️ **Statistical Analysis Tasks**

Perform statistical tests such as:

1. **Chi-square**

   * Categorical features vs Churn
     Example: Gender vs Attrition_Flag
2. **T-test or ANOVA:**

   * Compare averages between churn vs non-churn groups
     Example: Is Credit Limit significantly different?
3. Document statistical significance findings (p-values).

### 🎯 **Output**

* `4_features.ipynb`
* `5_stats.ipynb`
* Engineered dataset:
  `data/engineered/BankChurners_engineered.csv`

---

# ✅ **4 — Team Leader / Modeling Engineer**

### **Exact responsibilities based on your dataset**

This is the most technical role besides engineering.
Leader trains and compares ML models.

### ✔️ Tasks

1. Load engineered dataset.

2. Split data (train/test).

3. Train baseline models:

   * Logistic Regression
   * Decision Tree
   * Random Forest

4. Evaluate models:

   * Accuracy
   * Precision/Recall
   * F1
   * Confusion Matrix
   * ROC Curve / AUC

5. Select best model.

6. Tune hyperparameters (GridSearchCV).

7. Save final model → `models/model.pkl`.

8. Provide interpretation:

   * Feature importances
   * Which features influence churn most
     (e.g., *low transaction frequency = high churn*)

### 🎯 **Output**

* `6_modeling.ipynb`
* Best model saved
* Evaluation plots
* Modeling interpretation summary

---

# ✅ **5 — Visualization & Documentation Specialist**

### **Exact responsibilities based on your dataset**

This member creates the final presentation and writes the report.

### ✔️ Visualization Tasks

Use results from EDA & modeling:

1. Attractive final charts:

   * Customer demographics
   * Churn comparison
   * Key EDA plots
   * Feature importance bar chart
   * Confusion matrix (styled)
   * ROC curve
2. Clean, labeled, readable charts for the final slides.

### ✔️ Documentation Tasks

1. Create the **PowerPoint presentation**:

   * Project overview
   * Dataset summary
   * Cleaning steps
   * EDA highlights
   * Feature engineering
   * Modeling results
   * Insights & recommendations

2. Write the **Final Report (PDF)**:

   * Methods
   * Analysis
   * Results
   * Interpretation
   * What the business can decide based on your findings

3. Update README.md with:

   * Project description
   * Folder structure
   * How to run the notebooks

### 🎯 **Output**

* `7_visualization.ipynb`
* PowerPoint (10–12 slides)
* Final Report (3–5 pages)
* Updated README

---

# 🎉 **Final Summary: Who Does What?**

| Member                                          | Exactly What They Do Based on Dataset                                             |
| ----------------------------------------------- | --------------------------------------------------------------------------------- |
| **1. Data Engineer**                            | Clean dataset, handle missing values, encode categories, export cleaned file      |
| **2. EDA Analyst**                              | Distributions, correlations, churn patterns, plots                                |
| **3. Feature Engineer + Stats**                 | New features (Engagement, Activity), bins, chi-square, t-test, engineered dataset |
| **4. Team Leader / Modeling Engineer**          | Train models, evaluate, tune, interpret feature importance, save best model       |
| **5. Visualization + Documentation Specialist** | Final charts, presentation, report, README                                        |

---

