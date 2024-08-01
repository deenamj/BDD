from behave import *

from features.pages.RegisterPage import register_Page


@given(u'I land into Register page')
def step_impl(context):
    context.rg = register_Page(context.driver)
    context.rg.landing_page()





@when(u'I entering the below details')
def step_impl(context):
    for row in context.table:
        context.rg.register_details(row["firstname"],
                                row["lastname"],
                                row["email"],
                                row["telephone"],
                                row["password"],
                                row["confirm"])



@when(u'Click on the Continue button')
def step_impl(context):
    context.rg.click_Continue()


@then(u'I Should get valid Message "Your Account Has Been Created!"')
def step_impl(context):
    context.rg.error_message("First Name must be between 1 and 32 characters!")
