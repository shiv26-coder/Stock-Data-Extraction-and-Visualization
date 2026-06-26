# 📈 Stock Market Data Extraction & Visualization

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green?style=for-the-badge)
![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-yfinance-red?style=for-the-badge)

</p>

---

# 📌 Overview

This project demonstrates how to **extract, clean, and visualize financial market data** using Python by combining API-based data retrieval with web scraping.

The workflow includes:

* 📈 Downloading historical stock prices using the **Yahoo Finance API (`yfinance`)**
* 🌐 Extracting company revenue data through **BeautifulSoup web scraping**
* 🧹 Cleaning and preprocessing financial datasets using **Pandas**
* 📊 Visualizing stock prices and revenue trends with **Matplotlib**

The repository demonstrates the workflow using **Tesla (TSLA)** and **GameStop (GME)** as example companies. The stock data currently covers the **last two years** available from Yahoo Finance, while the revenue data comes from an educational web-scraping dataset provided in the IBM Data Science course.

> **Note:** Since the stock price data and the educational revenue dataset cover different time periods, the visualizations are intended to demonstrate data extraction, preprocessing, and visualization techniques rather than direct time-aligned financial comparison.

---

# 🚀 Features

* Download the latest two years of historical stock prices
* Extract revenue data from HTML webpages
* Clean and preprocess financial data
* Generate stock price visualizations
* Generate historical revenue visualizations
* Modular and reusable code structure
* Easily adaptable for other stock tickers

---

# 🛠 Technologies Used

| Technology    | Purpose              |
| ------------- | -------------------- |
| Python        | Programming Language |
| Pandas        | Data Manipulation    |
| yfinance      | Stock Market Data    |
| Requests      | HTTP Requests        |
| BeautifulSoup | Web Scraping         |
| Matplotlib    | Data Visualization   |

---

# 📂 Project Structure

```text
Stock-Data-Extraction-and-Visualization/
│
├── stock_analysis.py
├── README.md
├── requirements.txt
├── screenshots/
│   ├── tesla_graph.png
│   ├── gamestop_graph.png
│   └── terminal_output.png
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shiv26-coder/Stock-Data-Extraction-and-Visualization.git
```

Navigate to the project directory:

```bash
cd Stock-Data-Extraction-and-Visualization
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the project:

```bash
python stock_analysis.py
```

The script will:

* Download the latest two years of stock prices
* Retrieve revenue data through web scraping
* Clean the datasets
* Generate stock price and revenue graphs

---

# 📊 Example Companies

This repository demonstrates the workflow using:

* Tesla (TSLA)
* GameStop (GME)

The same approach can be extended to other companies supported by Yahoo Finance, such as:

* Apple (AAPL)
* Microsoft (MSFT)
* Amazon (AMZN)
* NVIDIA (NVDA)
* Alphabet (GOOGL)

For other companies, you would also need an appropriate revenue data source.

---

# 📷 Sample Output

## Tesla Analysis

![Tesla Graph](screenshots/tesla_graph.png)

---

## GameStop Analysis

![GameStop Graph](screenshots/gamestop_graph.png)

---

## Program Output

![Terminal Output](screenshots/terminal_output.png)

---

# 📚 Learning Outcomes

This project demonstrates practical experience in:

* Financial data extraction
* API integration
* Web scraping
* Data cleaning
* Exploratory Data Analysis (EDA)
* Financial data visualization
* Python programming

---

# 📦 Requirements

```text
pandas
yfinance
requests
beautifulsoup4
matplotlib
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

* Fetch real-time company revenue through financial APIs
* Synchronize stock price and revenue over matching time periods
* Compare multiple companies simultaneously
* Add technical indicators (SMA, EMA, RSI, MACD)
* Export charts automatically
* Develop an interactive Streamlit dashboard

---

# 👨‍💻 Author

**Shivansh Misra**

B.Tech in Electronics and Communication Engineering (ECE)

SRM Institute of Science and Technology

---

⭐ If you found this project useful, consider giving it a star on GitHub.
