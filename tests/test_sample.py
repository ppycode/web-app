def test_content():
    with open("index.html") as f:
        assert "Deployed" in f.read()
