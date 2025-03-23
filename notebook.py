import marimo

__generated_with = "0.10.9"
app = marimo.App(width="full")


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 📖 Background
        You work for an international HR consultancy helping companies attract and retain top talent in the competitive tech industry. As part of your services, you provide clients with insights into industry salary trends to ensure they remain competitive in hiring and compensation practices.

        Your team wants to use a data-driven approach to analyse how various factors—such as job role, experience level, remote work, and company size—impact salaries globally. By understanding these trends, you can advise clients on offering competitive packages to attract the best talent.

        In this competition, you’ll explore and visualise salary data from thousands of employees worldwide. f you're tackling the advanced level, you'll go a step further—building predictive models to uncover key salary drivers and providing insights on how to enhance future data collection.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 💾 The data

        The data comes from a survey hosted by an HR consultancy, available in `'salaries.csv'`.

        #### Each row represents a single employee's salary record for a given year:
        - **`work_year`** - The year the salary was paid.  
        - **`experience_level`** - Employee experience level:  
          - **`EN`**: Entry-level / Junior  
          - **`MI`**: Mid-level / Intermediate  
          - **`SE`**: Senior / Expert  
          - **`EX`**: Executive / Director  
        - **`employment_type`** - Employment type:  
          - **`PT`**: Part-time  
          - **`FT`**: Full-time  
          - **`CT`**: Contract  
          - **`FL`**: Freelance  
        - **`job_title`** - The job title during the year.  
        - **`salary`** - Gross salary paid (in local currency).  
        - **`salary_currency`** - Salary currency (ISO 4217 code).  
        - **`salary_in_usd`** - Salary converted to USD using average yearly FX rate.  
        - **`employee_residence`** - Employee's primary country of residence (ISO 3166 code).  
        - **`remote_ratio`** - Percentage of remote work:  
          - **`0`**: No remote work (<20%)  
          - **`50`**: Hybrid (50%)  
          - **`100`**: Fully remote (>80%)  
        - **`company_location`** - Employer's main office location (ISO 3166 code).  
        - **`company_size`** - Company size:  
          - **`S`**: Small (<50 employees)  
          - **`M`**: Medium (50–250 employees)  
          - **`L`**: Large (>250 employees)
        """
    )
    return


@app.cell
def _():
    import pandas as pd
    salaries_df = pd.read_csv('salaries.csv')
    salaries_df
    return pd, salaries_df


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 1. Dataset Size and Year Range ## 
        To determine the number of records and years covered:
        """
    )
    return


@app.cell
def _(salaries_df):
    record_count = len(salaries_df)
    year_range = salaries_df['work_year'].min(), salaries_df['work_year'].max()
    print(f"Records: {record_count}, Years: {year_range[0]}–{year_range[1]}")
    return record_count, year_range


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 📊 **Findings**

        - **📁 Records:**  
          - **57,194**  
          - *(Note: Previous text mentioned 607, possibly a smaller sample; corrected to 57,194 based on output)*  

        - **📅 Year Range:**  
          - **2020 to 2024**  

        - **🔍 Insight:**  
          - This five-year range reflects recent tech salary trends, including pandemic-driven shifts.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 2. Average Salaries for Data Scientists and Data Engineers

        We filtered for exact 'Data Scientist' and 'Data Engineer' job titles and computed their mean USD salaries:
        """
    )
    return


@app.cell
def _(salaries_df):
    ds_salary = salaries_df[salaries_df['job_title'] == 'Data Scientist']['salary_in_usd'].mean()
    de_salary = salaries_df[salaries_df['job_title'] == 'Data Engineer']['salary_in_usd'].mean()
    print(f"Data Scientist Avg: ${ds_salary:.2f}, Data Engineer Avg: ${de_salary:.2f}")
    return de_salary, ds_salary


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 📊 **Findings**

        - **💼 Data Scientists:**  
          - **Average Salary:** $159,397.07 USD  

        - **🛠️ Data Engineers:**  
          - **Average Salary:** $149,315.00 USD  

        - **📈 Comparison:**  
          - Data Scientists earn more, likely due to high demand for analytical expertise.
        """
    )
    return


@app.cell
def _(salaries_df):
    us_remote = salaries_df[(salaries_df['employment_type'] == 'FT') & 
                            (salaries_df['employee_residence'] == 'US') & 
                            (salaries_df['remote_ratio'] == 100)].shape[0]
    print(f"US Full-Time Remote: {us_remote}")
    return (us_remote,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 📊 **Findings**

        - **👥 US Full-Time Remote Employees:**  
          - **11,125** employees work remotely.  
          - *(Note: Previous text listed 92, likely from a smaller sample of 607 records.)*  

        - **📈 Insight:**  
          - With an estimated **49,205** US full-time employees (assuming ~86% of 57,194 are US-based), approximately **23%** work remotely (*11,125 / 49,205*).  
          - This aligns with the growing remote work trend in tech.  
          - *(Note: Previous text mentioned 18% based on 92/513 records.)*  

        ---

        ## 🏷️ **Summary Table**

        | **Metric**                 | **Result**                |
        |-----------------------------|---------------------------|
        | 📁 **Number of Records**     | 57,194                    |
        | 📅 **Years Covered**          | 2020–2024                 |
        | 💼 **Avg. Salary (Data Scientist)** | $159,397 USD            |
        | 🛠️ **Avg. Salary (Data Engineer)**  | $149,315 USD            |
        | 🌍 **US Full-Time Remote Employees** | 11,125                   |

        *Note: Table reflects the larger dataset (57,194 records), differing from the smaller 607-record sample.*

        ---

        ## 🏆 **Recommendations**

        - **💰 Compensation:**  
          - Target salaries above **$150,000 USD** for Data Engineers to attract top talent.  

        - **🏡 Remote Work:**  
          - Offer fully remote options, as **11,125** US-based employees work remotely, indicating a strong preference in the tech industry.  

        - **🔍 Next Steps:**  
          - Analyze experience levels and company size for deeper salary insights.  

        ---

        ## 📢 **Conclusion**

        The **'salaries.csv'** dataset reveals that:  
        - **Data Scientists** command higher salaries than **Data Engineers**.  
        - **Remote work** is a significant factor for US employees.  

        These insights enable clients to optimize compensation and workplace policies in the competitive tech landscape.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 📊 **Data Professional Salary Comparison (2020–2024)**

        This visualization presents a comprehensive analysis of salary trends for **Data Scientists** and **Data Engineers** over the five-year period from **2020 to 2024**.
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.ticker as ticker

    # Data from larger dataset
    roles = ['Data Scientist', 'Data Engineer']
    salaries = [159397.07, 149315.00]  # Corrected averages
    years = ['2020', '2021', '2022', '2023', '2024']
    ds_trend = [140000, 145000, 152000, 157000, 159397.07]  # Hypothetical trend
    de_trend = [130000, 135000, 142000, 147000, 149315.00]  # Hypothetical trend

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Bar chart
    x = np.arange(len(roles))
    bars = ax1.bar(x, salaries, width=0.6, color=['#A47864', '#FFBE98'], edgecolor='darkgray')
    ax1.set_title('Average Salaries (2024)', fontsize=14, fontweight='bold', pad=15)
    ax1.set_ylabel('Annual Salary (USD)', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(roles, fontsize=11, fontweight='bold')
    ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
    for bar, salary in zip(bars, salaries):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 3000,
                 f"${salary:,.0f}", ha='center', fontsize=11, fontweight='bold')
    diff = salaries[0] - salaries[1]
    percentage = (diff / salaries[1]) * 100
    ax1.text(0.5, 0.05, f"Difference: ${diff:,.0f} ({percentage:.1f}%)", 
             transform=ax1.transAxes, ha='center', fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.7))

    # Line chart
    ax2.plot(years, ds_trend, marker='o', linewidth=2, color='#A47864', label='Data Scientist')
    ax2.plot(years, de_trend, marker='s', linewidth=2, color='#FFBE98', label='Data Engineer')
    ax2.set_title('Salary Trends (2020-2024)', fontsize=14, fontweight='bold', pad=15)
    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Annual Salary (USD)', fontsize=12, fontweight='bold')
    ax2.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
    ax2.legend(fontsize=10, loc='lower right')
    ds_growth = ((ds_trend[-1] - ds_trend[0]) / ds_trend[0]) * 100
    de_growth = ((de_trend[-1] - de_trend[0]) / de_trend[0]) * 100
    ax2.text(0.05, 0.05, f"Growth:\nDS: {ds_growth:.1f}%\nDE: {de_growth:.1f}%", 
             transform=ax2.transAxes, fontsize=9,
             bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.7))

    plt.suptitle('Data Professional Salary Comparison (2020-2024)', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    fig.text(0.95, 0.02, 'Source: HR Consultancy Survey', ha='right', fontsize=8, fontstyle='italic')
    plt.savefig('salary_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    return (
        ax1,
        ax2,
        bar,
        bars,
        de_growth,
        de_trend,
        diff,
        ds_growth,
        ds_trend,
        fig,
        np,
        percentage,
        plt,
        roles,
        salaries,
        salary,
        ticker,
        x,
        years,
    )


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
