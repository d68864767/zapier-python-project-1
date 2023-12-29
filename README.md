# Google Sheets to Slack Sales Data Analysis

This project is a simple Python script that fetches sales data from a Google Sheet, performs some basic calculations, and posts the results to a Slack channel. The data is in a tabular format with columns for 'Date', 'Product', 'Quantity', and 'Sale Amount'. The script calculates the monthly sales total and average sale amount per product.

## Setup

1. Set up a Google Sheets document with your sales data. The data should be in a tabular format with columns for 'Date', 'Product', 'Quantity', and 'Sale Amount'.

2. Set up a Slack workspace and channel where you want to post the results.

3. Install the necessary Python libraries with pip:

```bash
pip install slack_sdk datetime
```

4. Set up your environment variables. You'll need to set `SLACK_API_TOKEN` to your Slack API token.

## Usage

Run the script with Python:

```bash
python script.py
```

The script will fetch the latest data from the Google Sheet, perform the calculations, and post the results to the specified Slack channel.

## Code Overview

The script is divided into several sections:

1. **Data Fetching**: The script fetches the latest sales data from the Google Sheet.

2. **Data Processing**: The script processes the data, performing calculations to determine the monthly sales total and average sale amount per product.

3. **Data Output**: The script formats the results and posts them to the specified Slack channel.

Here's a simplified version of the script:

```python
import datetime
import json
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Sample input data
input_data = {
    'Date': '2023-12-01',
    'Product': 'Widget',
    'Quantity': 10,
    'Sale Amount': 200
}

# Assuming input_data is the row data from Google Sheets
date = datetime.datetime.strptime(input_data['Date'], '%Y-%m-%d')
product = input_data['Product']
quantity = int(input_data['Quantity'])
sale_amount = float(input_data['Sale Amount'])

# Perform calculations - this is simplified, in reality, you'd aggregate data over a period
monthly_sales_total = quantity * sale_amount
average_sale_amount = sale_amount / quantity

# Output data
output = {
    'month': date.strftime('%B'),
    'product': product,
    'monthly_sales_total': monthly_sales_total,
    'average_sale_amount': average_sale_amount
}

# Post to Slack
slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="sales-data",
        text=json.dumps(output)
    )
except SlackApiError as e:
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
```

## Testing

You can test the script by running it and checking the output in your Slack channel. If there are any issues, the script will raise an exception with a helpful error message.
