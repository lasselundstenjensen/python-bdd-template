from behave import given, when, then, step

@given('a non-empty text {text:S}')
def step_impl(context, text):
    assert text != ""
    context.text = text

@when('executing')
def step_impl(context):
    pass

@then('print the text')
def step_impl(context):
    assert context.failed is False
    print(context.text)