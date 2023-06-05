import mongomock
from behave import *


@when(
    'creo un track del path "{path}" con el uid "{uid}" y created_date "{created_date}"'
)
def step_impl(context, path, uid, created_date):
    """
    :type context: behave.runner.Context
    """
    body = {"path": path, "uid": uid, "created_date": created_date}
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/tracks"

    context.response = context.client.post(url, json=[body], headers=headers)


@then("se me informa que se creo exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201
