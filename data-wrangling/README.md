# AI / Data Science Salary Analysis

Exploratory data analysis of AI and data science job salaries from 2020–2022, using a dataset of 607 records spanning multiple countries, experience levels, and work arrangements.

## Dataset

**File:** `ds_salaries.csv`  
**Records:** 607 rows, 12 columns  
**Source columns:**

| Column | Description |
|--------|-------------|
| `work_year` | Year the salary was recorded (2020–2022) |
| `experience_level` | EN (Entry), MI (Mid), SE (Senior), EX (Executive) |
| `employment_type` | FT / PT / CT / FL |
| `job_title` | Role title (e.g. Data Scientist, ML Engineer) |
| `salary` | Salary in original currency |
| `salary_currency` | ISO currency code |
| `salary_in_usd` | Salary normalized to USD |
| `employee_residence` | Employee's country (ISO code) |
| `remote_ratio` | 0 = On-site, 50 = Hybrid, 100 = Remote |
| `company_location` | Company's country (ISO code) |
| `company_size` | S / M / L |

## Notebook

`ai_jobs_analysis.ipynb` — end-to-end analysis covering data loading, cleaning, and 5 visualizations.

### Analysis steps

1. **Data loading & inspection** — shape, dtypes, null check, descriptive statistics
2. **Data cleaning** — map coded values to readable labels (`EN` → `Entry`, `S` → `Small`, `0` → `On-site`, etc.)
3. **Visualizations:**
   - Top 10 highest paying job titles (median USD)
   - Salary distribution by experience level (box plot)
   - Salary distribution by work arrangement — On-site / Hybrid / Remote (box plot)
   - Median salary trend over time, 2020–2022 (line chart)
   - Top 10 highest paying countries — raw and filtered (min. 10 data points)
   - Heatmap: median salary by experience level × work arrangement

### Key findings

- **Lead and domain-specialized roles pay the most** — leadership and business-facing titles outperform pure technical titles.
- **Experience level has the biggest salary impact** — executive roles earn significantly more, but senior-level spread is wide (company and location matter more at that stage).
- **Remote work pays slightly more than on-site** — executive + remote is the highest-paying combination.
- **Salaries trended upward** from 2020 to 2022, reflecting growing demand for AI talent.
- **The US dominates global compensation** after filtering for statistical validity (≥ 10 data points per country).
- **Small samples mislead** — Russia appeared highest paying initially but had only 2 records.

## Setup

```bash
pip install -r requirements.txt
jupyter notebook ai_jobs_analysis.ipynb
```

**Core dependencies:** `pandas`, `numpy`, `matplotlib`, `seaborn`
