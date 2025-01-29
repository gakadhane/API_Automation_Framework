# Common Verification

# HTTP Status Code
# Headers
# Data Verification
# JSON schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed to match status Code"

def verify_response_headers(response_data, expected_data):
    assert response_data.headers == expected_data, "Failed to match headers"

def verify_response_data(response_data, expected_data):
    assert response_data.data == expected_data, "Failed to match data"

def verify_response_json(response_data, expected_data):
    assert response_data.json() == expected_data, "Failed to match json"

def verify_response_text(response_data, expected_data):
    assert response_data.text == expected_data, "Failed to match text"

def verify_response_content(response_data, expected_data):
    assert response_data.content == expected_data, "Failed to match content"

def verify_response_content_type(response_data, expected_data):
    assert response_data.headers['Content-Type'] == expected_data, "Failed to match content type"

def verify_response_content_length(response_data, expected_data):
    assert response_data.headers['Content-Length'] == expected_data, "Failed to match content length"

def verify_response_content_encoding(response_data, expected_data):
    assert response_data.headers['Content-Encoding'] == expected_data, "Failed to match content encoding"

def verify_response_content_type_json(response_data):
    assert response_data.headers['Content-Type'] == 'application/json', "Failed to match content type"

def verify_response_content_type_text(response_data):
    assert response_data.headers['Content-Type'] == 'text/plain', "Failed to match content type"

def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to match the key"

def verify_response_key_not_equal(key, expected_data):
    assert key != expected_data, "Failed to match the key"

def verify_json_key_not_null(key):
    assert key != 0, "Failed Key is null"

def verify_json_key_not_none(key):
    assert key is not None

def verify_json_key_gr_zero(key):
    assert key > 0, "Failed Key is not > 0"

def verify_response_delete(response):
    assert "Created" in response

def verify_response_post(response):
    assert "Created" in response

def verify_response_put(response):
    assert "Created" in response

def verify_response_patch(response):
    assert "Created" in response

def verify_response_get(response):
    assert "OK" in response