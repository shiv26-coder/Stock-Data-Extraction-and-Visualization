# 📈 Stock Data Extraction and Visualization

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green?style=for-the-badge)
![yfinance](https://img.shields.io/badge/Yahoo%20Finance-yfinance-red?style=for-the-badge)

</p>

---

## 📌 Overview

This project demonstrates how to extract, clean, analyze, and visualize financial data using Python.

It combines **API-based data extraction** with **web scraping** to retrieve:

* 📈 Historical stock prices using the Yahoo Finance API (`yfinance`)
* 💰 Quarterly revenue data extracted from HTML webpages using BeautifulSoup
* 📊 Comparative visualizations using Matplotlib

Although this project showcases **Tesla (TSLA)** and **GameStop (GME)** as examples, the same workflow can be applied to **any publicly traded company supported by Yahoo Finance** by simply changing the stock ticker and revenue source.

---

## 🚀 Features

* Historical stock price extraction
* Revenue data extraction through web scraping
* Data cleaning and preprocessing
* Financial trend visualization
* Reusable workflow for different companies
* Beginner-friendly and modular Python code

---

## 🛠 Technologies Used

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming Language |
| Pandas        | Data Manipulation    |
| yfinance      | Stock Market Data    |
| Requests      | Download HTML Pages  |
| BeautifulSoup | Web Scraping         |
| Matplotlib    | Data Visualization   |

---

## 📂 Project Structure

```text
Stock-Data-Extraction-and-Visualization/
│
├── stock_analysis.py
├── README.md
├── requirements.txt
├── screenshots/
│   ├── tesla_graph.png
│   └── gamestop_graph.png
└── output/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shiv26-coder/Stock-Data-Extraction-and-Visualization.git
```

Move into the project directory:

```bash
cd Stock-Data-Extraction-and-Visualization
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the project using:

```bash
python stock_analysis.py
```

The script will:

* Download historical stock prices
* Extract revenue information
* Clean and preprocess the data
* Generate stock price and revenue graphs

---

## 📈 Example Companies

This repository demonstrates the workflow using:

* Tesla (TSLA)
* GameStop (GME)

The same approach can be extended to other companies such as:

* Apple (AAPL)
* Microsoft (MSFT)
* Amazon (AMZN)
* NVIDIA (NVDA)
* Google (GOOGL)
* Reliance Industries
* Tata Motors

Simply update the ticker symbol and provide the appropriate revenue data source.

---

## 📊 Sample Output

### Tesla Analysis



```text
screenshots/tesla_graph.png
```

### GameStop Analysis


```text
screenshots/gamestop_graph.png
```

---

## 📚 Learning Outcomes

This project demonstrates practical experience in:

* Financial data extraction
* API integration
* Web scraping
* Data cleaning
* Exploratory data analysis
* Data visualization
* Python programming

---

## 📦 Requirements

```text
pandas
yfinance
requests
beautifulsoup4
matplotlib
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Interactive Plotly dashboards
* Support for multiple companies simultaneously
* Automatic revenue extraction for additional companies
* Export charts as images and PDF reports
* Build an interactive dashboard using Streamlit
* Perform financial trend and statistical analysis

---

## 👨‍💻 Author

**Shivansh Misra**

Electronics and Communication Engineering (ECE) Student
SRM Institute of Science and Technology

---

⭐ If you found this project helpful, consider giving the repository a star!
