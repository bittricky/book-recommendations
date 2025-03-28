from flask import Blueprint, render_template, request, jsonify
from .services import BookService
import random

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    result = BookService.search_books(query, page, limit)
    
    if 'docs' in result:
        for book in result['docs']:
            if 'cover_i' in book:
                book['cover_url'] = BookService.get_book_cover_url(book['cover_i'])
    
    return jsonify(result)

@bp.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    random_year = random.randint(1900, 2023)
    
    if random.choice([True, False]):
        query = f'first_publish_year:{random_year}'
    else:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        query = random.choice(letters)
    
    result = BookService.search_books(query, page=1, limit=10)
    
    if 'docs' in result:
        for book in result['docs']:
            if 'cover_i' in book:
                book['cover_url'] = BookService.get_book_cover_url(book['cover_i'])
    
    return jsonify(result)


