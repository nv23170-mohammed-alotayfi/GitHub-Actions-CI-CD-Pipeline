def test_app_import():
    from app import app
    assert app is None  # break test


def test_app_responds():
    """Smoke test: app responds to a request."""
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as c:
        rv = c.get('/')
    assert rv.status_code in [200, 302]
