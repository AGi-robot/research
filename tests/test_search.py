from unittest.mock import Mock, patch

import pytest
from agi_research import search


def test_invalid_limit_does_not_send_request():
    with patch('agi_research.httpx.get') as get:
        for limit in [True, 1.5, 0, 11]:
            with pytest.raises(ValueError):
                search('query', base_url='http://search.invalid', limit=limit)
        get.assert_not_called()


def test_invalid_results_are_reported_and_valid_snippets_work():
    response = Mock()
    with patch('agi_research.httpx.get', return_value=response):
        for data in [[], {'results': None}, {'results': {}}]:
            response.json.return_value = data
            with pytest.raises(ValueError, match='results array'):
                search('query', base_url='http://search.invalid')
        response.json.return_value = {'results': [None, {'title': 'Title', 'url': 'https://example.com', 'content': 'Text'}]}
        assert search('query', base_url='http://search.invalid') == [
            {'title': 'Title', 'url': 'https://example.com', 'snippet': 'Text'}]
