# 📊 A/B Testing & Experimentation Framework

## 🚀 Project Overview

The **A/B Testing & Experimentation Framework** is a data analytics project designed to compare two versions of a product, feature, or user experience using data-driven experimentation.

It compares **Group A (Control)** and **Group B (Variant)** to evaluate user conversion, purchases, revenue, and performance across different devices. The goal is to help businesses make informed decisions using statistical analysis and interactive visualizations.

## 🎯 Objectives

- Compare conversion rates between Group A and Group B.
- Analyze purchase behavior and revenue performance.
- Calculate conversion rate, revenue per user, and relative lift.
- Perform statistical hypothesis testing.
- Visualize experiment results using Power BI.
- Generate data-driven business recommendations.

## 🛠️ Technologies Used

- **Python** — Data analysis and statistical testing
- **Pandas & NumPy** — Data cleaning and manipulation
- **SciPy / Statistical Methods** — Hypothesis testing
- **SQL** — Data querying and analysis
- **Power BI** — Interactive dashboard and visualization
- **Jupyter Notebook** — Exploratory data analysis

## 📂 Project Structure

```text
AB-Testing-Experimentation-Framework/
│
├── data/
│   └── ab_test_users.csv
│
├── notebooks/
│   └── ab_testing_analysis.ipynb
│
├── AB_Testing_Dashboard.pbix
├── analysis.sql
├── requirements.txt
└── README.md
```

*Update the filenames above to match the actual files in your repository.*

## 📈 Key Performance Indicators (KPIs)

- **Total Users:** Number of users participating in the experiment.
- **Total Purchases:** Number of users who completed a purchase.
- **Conversion Rate:** Percentage of users who purchased.
- **Relative Lift:** Percentage improvement in conversion rate for Group B compared with Group A.
- **Revenue per User:** Total revenue divided by the number of users.

## 📊 Dashboard Highlights

The Power BI dashboard includes:

- KPI cards for experiment performance.
- Conversion rate comparison between A and B.
- Total revenue comparison by experiment group.
- Device-wise conversion analysis.
- User distribution across experiment groups.
- Interactive filters for device and experiment group.

## 🧪 Statistical Testing

The experiment uses hypothesis testing to evaluate whether the observed conversion-rate difference is statistically significant.

**Null hypothesis (H₀):** There is no difference in conversion rates between Group A and Group B.

**Alternative hypothesis (H₁):** The conversion rates differ between Group A and Group B.

The analysis uses a significance level of **0.05**. The p-value helps determine whether the observed difference provides sufficient evidence to reject the null hypothesis.

Statistical significance should be evaluated before concluding that one variant performs better.

## 📌 Initial Results

Based on the current dashboard:

| Metric | Group A | Group B |
|---|---:|---:|
| Total Users | 5,076 | 4,924 |
| Total Purchases | 433 | 512 |
| Conversion Rate | 8.53% | 10.40% |
| Revenue per User | 106.51 | 127.30 |

**Initial observation:** Group B has a higher observed conversion rate and revenue per user than Group A. Statistical testing is needed before deciding whether the difference is significant.

## 💡 Business Value

This project demonstrates how experimentation can help organizations:

- Evaluate product changes using data.
- Understand customer behavior.
- Identify better-performing variants.
- Measure conversion and revenue impact.
- Make evidence-based product decisions.

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/saheranjumm13/AB-Testing-Experimentation-Framework.git
   ```

2. Open the project folder:

   ```bash
   cd AB-Testing-Experimentation-Framework
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Open Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Open the analysis notebook and run the cells in order.

6. Open the `.pbix` dashboard file using Microsoft Power BI Desktop.

## 👩‍💻 Author

**Saheranjum Makandar**

B.Tech — Computer Science & Engineering (Data Science)

- GitHub: [@saheranjumm13](https://github.com/saheranjumm13)
- LinkedIn: [Saheranjum Makandar](https://www.linkedin.com/in/saheranjum-makandar)

---

⭐ If you find this project useful, feel free to explore the repository and share feedback.
