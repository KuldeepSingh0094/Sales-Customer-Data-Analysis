# Sales & Customer Data Analysis

End-to-end data analysis project: clean raw retail sales data, load it into PostgreSQL,
analyze it with SQL, and visualize insights with Python.

## Tech Stack
Python, Pandas, NumPy, PostgreSQL, SQL, Matplotlib, Seaborn, Jupyter Notebook

## Project Structure
```
data/
  generate_sample_data.py   # creates raw_sales.csv (swap for a real dataset if you want)
  raw_sales.csv             # messy sample data
  cleaned_sales.csv         # output of the cleaning notebook
notebooks/
  01_cleaning_and_load.ipynb   # clean data, load into PostgreSQL
  02_eda_visualization.ipynb   # EDA and charts
sql/
  queries.sql                # business questions answered in SQL (joins, group by, window functions)
requirements.txt
```

## Setup
```bash
pip install -r requirements.txt

# Create a local Postgres database
createdb sales_db
```
Update the connection string in `01_cleaning_and_load.ipynb`:
```
postgresql://username:password@localhost:5432/sales_db
```

## Workflow
1. `python data/generate_sample_data.py` — generate sample data (or drop in your own CSV as `data/raw_sales.csv`)
2. Run `notebooks/01_cleaning_and_load.ipynb` — cleans data, loads into PostgreSQL
3. Run queries in `sql/queries.sql` directly against Postgres, or via `psycopg2`/`sqlalchemy`
4. Run `notebooks/02_eda_visualization.ipynb` — generates charts and insights

## Key Questions Answered
- Which products generate the most revenue?
- What is the monthly revenue trend?
- How does revenue break down by region and category?
- Who are the top customers by spend?
- What is month-over-month revenue growth? (window function)
- How do products rank within each region? (window function)
