 E-commerce Sales Analysis Capstone Project

 Project Overview
This project is a **comprehensive end-to-end data analysis** of an e-commerce dataset (Amazon-style) containing sales, products, customers, and transaction information.  
The primary goal is to analyze the dataset to extract actionable business insights, identify trends, and provide recommendations for improving sales and revenue.

Objectives:
- Analyze top-selling products and high-value customers.
- Understand revenue patterns by region, category, and month.
- Assess the impact of discounts and promotions on sales.
- Identify upsell and cross-sell opportunities.
- Deliver actionable business recommendations backed by data.



 Dataset
The dataset consists of **1,000+ rows** and **15 columns**, including:

| Column Name       | Description                              |
|------------------|------------------------------------------|
| orderid           | Unique identifier for each order         |
| customerid        | Unique customer ID                        |
| customername      | Name of the customer                      |
| productname       | Name of the product                       |
| category          | Product category                          |
| subcategory       | Product subcategory                       |
| quantity          | Number of items purchased                 |
| price             | Unit price of the product                 |
| discount          | Discount applied (%)                       |
| tax               | Tax applied                               |
| shippingcost      | Shipping cost                             |
| paymentmethod     | Payment method used                        |
| region            | Customer region                            |
| orderdate         | Order date                                 |
| total_sales       | Computed total sales for each order       |

The raw data includes **inconsistencies, missing values, and formatting errors**, which are addressed during data cleaning.

---

 Project Structure
```

project_folder/
│
├─ data/
│   ├─ amazon_data.xlsx        # Raw dataset
│   └─ cleaned_data.xlsx       # Cleaned dataset
│
├─ notebooks/
│   ├─ 1_data_cleaning.py      # Data cleaning and preprocessing
│   ├─ 2_eda.py                # Exploratory Data Analysis and visualization
│   └─ 3_analysis.py           # Advanced analysis and recommendations
│
├─ reports/
│   ├─ executive_summary.pdf   # 1-page business summary
│   └─ technical_report.pdf    # Detailed analysis report
│
├─ presentations/
│   └─ business_presentation.pptx  # Slide deck
│
├─ requirements.txt            # Python dependencies
└─ README.md                   # Project documentation

````

---

## Setup Instructions

1. **Clone the repository**:
```bash
git clone <repository_url>
cd project_folder
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run data cleaning**:

```bash
python notebooks/1_data_cleaning.py
```

4. **Run EDA**:

```bash
python notebooks/2_eda.py
```

5. **Run analysis & recommendations**:

```bash
python notebooks/3_analysis.py
```

6. **View reports**:

* Executive summary: `reports/executive_summary.pdf`
* Technical report: `reports/technical_report.pdf`
* Presentation: `presentations/business_presentation.pptx`

---

## Code Structure

* `1_data_cleaning.py`: Handles missing values, inconsistent formats, type conversions, duplicate removal, and creates `total_sales`.
* `2_eda.py`: Generates visualizations for product sales, revenue by region, payment distribution, monthly trends, and category/region analysis.
* `3_analysis.py`: Performs advanced analysis, correlation studies, discount impact, top customers, upsell opportunities, and generates business recommendations.

---

## Visual Documentation

Sample charts generated during analysis:

* Top 10 products by quantity sold
* Revenue by region
* Payment method distribution
* Monthly sales trends
* Revenue heatmap by category and region
* Discount vs total sales scatterplot
* Top customers by revenue

*(Charts are included in the presentation and technical report.)*

---

## Technical Details

* **Data Cleaning**: Handled missing and null values, negative or malformed numbers, inconsistent text formats, and duplicates.
* **Algorithms / Calculations**:

  * `total_sales = (price * quantity * (1 - discount/100)) + tax + shippingcost`
  * Correlation analysis between numeric columns
  * Pivot tables for heatmap visualizations
  * Scatterplots for discount impact
* **Libraries Used**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `python-pptx` (optional for presentation)

---

## Testing & Validation

* Checked for missing values and inconsistencies after cleaning.
* Validated numeric conversions for `price`, `quantity`, `discount`, `tax`, and `shippingcost`.
* Ensured `total_sales` calculation aligns with expected business logic.
* Visualizations were reviewed for readability and accuracy.

---

## Key Business Recommendations

1. Promote high-quantity, low-revenue products via bundling or cross-selling.
2. Focus marketing campaigns in high-revenue regions.
3. Monitor top-selling products for inventory management.
4. Offer loyalty incentives to top customers identified in analysis.

---

## Contact

For questions or further collaboration:
**Name:** Vinay
**Email:** vinaytivarekar1403@gmail.com





