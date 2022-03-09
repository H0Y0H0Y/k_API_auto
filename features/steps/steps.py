from email import header
import json

from behave import Given, When, Then
import requests

@Given("I set url to {url}")
def set_url(context, url):
    context.url = url
    context.payload = {}
    context.headers = {'Content-Type': 'application/json;charset=UTF-8'}

@Given("set request body to the following")
def set_body(context):
    context.body = context.text

@Given("set {param_name} parameter as {param_value}")
def set_param(context, param_name, param_value):
    context.params = {param_name: param_value}

@When("I send a post request")
def send_post_request(context):
    context.response = requests.post(url=context.url, data=context.body, headers=context.headers)

@When("I send a get request")
def send_get_request(context):
    context.response = requests.get(url=context.url, params=context.params)

@Then("response should return a status code {code:d}")
def verify_response_status_code(context, code):
    assert context.response.status_code == code

@Then("response should return {field} with value {value}")
def verify_add_book_response(context, field, value):
    response_json = context.response.json()
    assert response_json[field] == value

@Then("Get Book API response should return {field} with value {value}")
def verify_get_book_response(context, field, value):
    response_json = context.response.json()
    assert response_json[0][field] == value
