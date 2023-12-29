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
<FINAL_CODE>