import pytest
from app import app

@pytest.fixture
def client():
    """
    Create a test client using Flask's test_client() method.
    This fixture will be used by each test function.
    """
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    """
    Test the / route of the Flask application.
    """
    # Make a GET request to the / route
    response = client.get('/')
    # Assert that the status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response data matches the expected output
    assert response.data.decode('utf-8') == "I am almost a Devops Engineer!"

# You can add more test functions for other routes or scenarios here
# For example:
# def test_another_route(client):
#     response = client.get('/another_route')
#     assert response.status_code == 200
#     assert b"Another route" in response.data

# Entry point for running the tests using pytest
if __name__ == "__main__":
    pytest.main()
