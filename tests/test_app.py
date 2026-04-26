from main import app
def test_home_page_loads():
  app.config["TESTING"] = True
  client = app.test_client()

  response = client.get("/")

  assert response.status_code == 200
  assert b"Contacts" in response.data
