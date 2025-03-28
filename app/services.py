import requests
from flask import current_app
import random

class BookService:
    """Service for interacting with the Open Library API."""
    
    BASE_URL = "https://openlibrary.org"
    SEARCH_URL = f"{BASE_URL}/search.json"
    COVERS_URL = "https://covers.openlibrary.org"
    
    @staticmethod
    def search_books(query, page=1, limit=10):
        params = {
            'q': query,
            'page': page,
            'limit': limit,
            'fields': 'key,title,author_name,cover_i,first_publish_year,edition_count'
        }
        
        response = requests.get(BookService.SEARCH_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            current_app.logger.error(f"Error searching books: {response.status_code}")
            return {'error': 'Failed to search books', 'status_code': response.status_code}
    
    @staticmethod
    def get_book_cover_url(cover_id, size='M'):
        if not cover_id:
            return None
        
        return f"{BookService.COVERS_URL}/b/id/{cover_id}-{size}.jpg"
    
    @staticmethod
    def get_author_books(author_name, limit=5):
        params = {
            'author': author_name,
            'limit': limit,
            'fields': 'key,title,author_name,cover_i,first_publish_year'
        }
        
        response = requests.get(BookService.SEARCH_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            current_app.logger.error(f"Error getting author books: {response.status_code}")
            return {'error': 'Failed to get author books', 'status_code': response.status_code}
    
    @staticmethod
    def get_similar_books(title, exclude_key=None, limit=5):
        keywords = ' '.join([word for word in title.split() if len(word) > 3])
        
        params = {
            'title': keywords,
            'limit': limit + 5,
            'fields': 'key,title,author_name,cover_i,first_publish_year'
        }
        
        response = requests.get(BookService.SEARCH_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            
            if exclude_key and 'docs' in data:
                data['docs'] = [doc for doc in data['docs'] if doc.get('key') != exclude_key]
                data['docs'] = data['docs'][:limit]
                
            return data
        else:
            current_app.logger.error(f"Error getting similar books: {response.status_code}")
            return {'error': 'Failed to get similar books', 'status_code': response.status_code}
    
    @staticmethod
    def get_recommendations(book_data):
        recommendations = []
        
        if 'author_name' in book_data and book_data['author_name']:
            author_name = book_data['author_name'][0]
            author_books = BookService.get_author_books(author_name)
            if 'docs' in author_books and author_books['docs']:
                other_books = [b for b in author_books['docs'] if b.get('key') != book_data.get('key')]
                if other_books:
                    recommendations.append({
                        'type': 'author',
                        'description': f"More books by {author_name}",
                        'books': other_books[:3]
                    })
        
        if 'title' in book_data:
            similar_books = BookService.get_similar_books(book_data['title'], book_data.get('key'))
            if 'docs' in similar_books and similar_books['docs']:
                recommendations.append({
                    'type': 'similar',
                    'description': "Books with similar titles",
                    'books': similar_books['docs'][:3]
                })
        
        if 'first_publish_year' in book_data:
            year = book_data['first_publish_year']
            start_year = year - 5
            end_year = year + 5
            params = {
                'q': f'first_publish_year:[{start_year} TO {end_year}]',
                'limit': 5,
                'fields': 'key,title,author_name,cover_i,first_publish_year'
            }
            
            response = requests.get(BookService.SEARCH_URL, params=params)
            if response.status_code == 200:
                time_period_books = response.json()
                if 'docs' in time_period_books and time_period_books['docs']:
                    other_books = [b for b in time_period_books['docs'] if b.get('key') != book_data.get('key')]
                    if other_books:
                        recommendations.append({
                            'type': 'time_period',
                            'description': f"Books from around {year}",
                            'books': random.sample(other_books, min(3, len(other_books)))
                        })
        
        return recommendations
