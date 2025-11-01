import yfinance

import json

import ast

def clean_data_format(data: dict) -> dict:
    result = {}
    for date, values in data.items():
        simple_date = date[:10]
        result[simple_date] = {}
        for key, value in values.items():
            column, _ = ast.literal_eval(key)
            result[simple_date][column] = round(value, 2)
    return result

def get_stock_data(ticker: str, start: str, end: str) -> dict:
    try:
        return json.loads(yfinance.download(ticker, start=start, end=end).to_json(orient='index', date_format='iso'))
    except ValueError:
        raise ValueError('Invalid dates')
    except:
        return {}