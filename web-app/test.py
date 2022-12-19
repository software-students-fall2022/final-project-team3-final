
import pytest
import sys
from app import app

class Tests:
    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Sanity test to return true
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_Homepage(flask_app):
        response = flask_app.get('/')
        assert response.request.path == "/"
        assert response.status_code == 200

    def test_resultspage(flask_app):
        response = flask_app.get('/results')
        assert response.request.path == "/results"
        assert response.status_code == 200