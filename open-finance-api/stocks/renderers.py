from django.template.loader import render_to_string

from .services import get_stock_data, clean_data_format

def render_json(ticker: str, start: str, end: str) -> dict:
    data: dict = get_stock_data(ticker, start, end)
    return clean_data_format(data)

def render_svg(ticker: str, start: str, end: str, color: str) -> str:
    # data: dict = get_stock_data(ticker, start, end)
    # clean_data: dict = clean_data_format(data)

    svg: str = f'''
        <svg width='250' height='100' xmlns='http://www.w3.org/2000/svg'>
            <rect width='250' height='100' fill='{color}' rx='10' ry='10'>
                <animate attributeName='fill-opacity' values='1;0.85;1' dur='3s' repeatCount='indefinite'/>
            </rect>

            <text x='125' y='25' font-size='14' text-anchor='middle' fill='white' font-family='Arial' font-weight='bold'>
                Acción de {ticker}
            </text>

            <text x='125' y='55' font-size='24' text-anchor='middle' fill='white' font-family='Arial'>
                ${270.5}
            </text>

            <text x='125' y='85' font-size='12' text-anchor='middle' fill='white' font-family='Arial'>
                {'2025-10-31'}
            </text>
        </svg>
    '''
    return svg

def render_html(ticker: str, start: str, end: str) -> str:
    data: dict = get_stock_data(ticker, start, end)
    
    html: str = render_to_string('stocks.html', {
        'ticker': ticker,
        'data': data,
        'start': start,
        'end': end
    })
    return html