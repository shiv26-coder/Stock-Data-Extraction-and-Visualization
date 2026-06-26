import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# The make_graph function has been modified to use Matplotlib for static graphs. 
# Earlier, it used Plotly to generate interactive dashboards, which caused issues when uploading the notebook in the MARK assignment submission.

import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

tesla=yf.Ticker("TSLA")

tesla_data=tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head(5) 
print(tesla_data.head(5))

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data=requests.get(url).text
soup=BeautifulSoup(html_data,'html.parser')
tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")

    if len(col) > 0:
        date = col[0].text
        revenue = col[1].text

        tesla_revenue = pd.concat(
            [
                tesla_revenue,
                pd.DataFrame({"Date":[date], "Revenue":[revenue]})
            ],
            ignore_index=True
        )


tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r'[$,]', '', regex=True)
tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail(5))


# The stock is GameStop and its ticker symbol is GME.
game_stop=yf.Ticker("GME")
game_stop_data=game_stop.history(period="max")
game_stop_data.reset_index(inplace=True)
game_stop_data.head(5)
print(game_stop_data.head(5))

url2= " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data2=requests.get(url2).text
soup2=BeautifulSoup(html_data2,'html.parser')
game_stop_revenue=pd.DataFrame(columns=['Date', 'Revenue'])
for row in soup2.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")

    if len(col) > 0:
        date = col[0].text
        revenue = col[1].text

        game_stop_revenue = pd.concat(
            [
                game_stop_revenue,
                pd.DataFrame({"Date":[date], "Revenue":[revenue]})
            ],
            ignore_index=True
        )


game_stop_revenue["Revenue"] = game_stop_revenue["Revenue"].str.replace(r'[$,]', '', regex=True)
game_stop_revenue.dropna(inplace=True)
game_stop_revenue = game_stop_revenue[game_stop_revenue['Revenue'] != ""]
print(game_stop_revenue.tail(5))


# plot tesla and game stop stock graphs
make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(game_stop_data, game_stop_revenue, 'GameStop')
