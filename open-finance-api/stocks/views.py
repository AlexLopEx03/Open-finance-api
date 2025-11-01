from django.http import JsonResponse, HttpResponse

from datetime import datetime

from .renderers import render_json, render_svg, render_html

def stock_view(request, ticker: str):
    try:
        data_format: str = request.GET.get('format', 'json').lower()
        if data_format not in { 'json', 'svg', 'html' }:
            return JsonResponse({ 'error': f'Invalid format: {data_format.lower()}' }, status=400)
        
        start_date = str(request.GET.get('start', datetime.now().date()))
        end_date = str(request.GET.get('end', datetime.now().date()))
        
        if data_format == 'json':
            return JsonResponse(render_json(ticker, start_date, end_date))
        elif data_format == 'svg':
            color: str = request.GET.get('color', '#000000')
            return HttpResponse(render_svg(ticker, start_date, end_date, color), content_type='image/svg+xml')
        elif data_format == 'html':
            return HttpResponse(render_html(ticker, start_date, end_date))
    except ValueError:
        return JsonResponse({ 'error': 'Invalid dates' })
    except Exception as error:
        return JsonResponse({ 'error': f'Unexpected error: {str(error)}' }, status=500)