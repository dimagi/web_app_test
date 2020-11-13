

def log_in_testy(page):

    # Go to http://localhost:8000/a/demo/login/?next=/a/demo/cloudcare/apps/v2/#apps
    page.goto("http://localhost:8000/a/demo/login/?next=/a/demo/cloudcare/apps/v2/#apps")

    # Click input[name="auth-username"]
    page.click("input[name=\"auth-username\"]")

    # Fill input[name="auth-username"]
    page.fill("input[name=\"auth-username\"]", "testy@demo.commcarehq.org")

    # Press Tab
    page.press("input[name=\"auth-username\"]", "Tab")

    # Fill input[name="auth-password"]
    page.fill("input[name=\"auth-password\"]", "123")

    # Click //button[normalize-space(.)='Sign In']
    page.click("//button[normalize-space(.)='Sign In']")

    assert page.url == "http://localhost:8000/a/demo/cloudcare/apps/v2/#apps"


def test_reg_woman(page):

    log_in_testy(page)

    # Click //div[normalize-space(.)='DHIS2 Tracked Entities']/i
    page.click("//div[normalize-space(.)='DHIS2 Tracked Entities']/i")
    # assert page.url() == "http://localhost:8000/a/demo/cloudcare/apps/v2/#{"appId":"dc52289b5dbe447ba86830b65d2a68ea"}"

    # Click text="Case List"
    page.click("text=\"Case List\"")
    # assert page.url() == "http://localhost:8000/a/demo/cloudcare/apps/v2/#{"appId":"dc52289b5dbe447ba86830b65d2a68ea","steps":[0],"page":null,"search":null}"

    # Click text="Register woman"
    page.click("text=\"Register woman\"")
    # assert page.url() == "http://localhost:8000/a/demo/cloudcare/apps/v2/#{"appId":"dc52289b5dbe447ba86830b65d2a68ea","steps":[0,0],"page":null,"search":null}"

    # Click textarea[id="str62"]
    page.click("textarea[id=\"str62\"]")

    # Fill textarea[id="str62"]
    page.fill("textarea[id=\"str62\"]", "Alice")

    # Click textarea[id="str63"]
    page.click("textarea[id=\"str63\"]")

    # Fill textarea[id="str63"]
    page.fill("textarea[id=\"str63\"]", "Apple")

    # Click input[type="text"]
    page.click("input[type=\"text\"]")

    # Triple click input[type="text"]
    page.click("input[type=\"text\"]", clickCount=3)

    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "1/1/1980")

    # Press Enter
    page.press("input[type=\"text\"]", "Enter")

    # Click text=/.*Submit.*/
    # with page.expect_navigation(url="http://localhost:8000/a/demo/cloudcare/apps/v2/#{"appId":"dc52289b5dbe447ba86830b65d2a68ea","sessionId":null,"steps":null,"page":null,"search":null,"queryDict":null,"sortIndex":null}"):
    with page.expect_navigation():
        page.click("text=/.*Submit.*/")

    # Click text="Case List"
    page.click("text=\"Case List\"")
    # assert page.url() == "http://localhost:8000/a/demo/cloudcare/apps/v2/#{"appId":"dc52289b5dbe447ba86830b65d2a68ea","sessionId":null,"steps":[0],"page":null,"search":null,"queryDict":null,"sortIndex":null}"

    # Click text="ANC visit"
    page.click("text=\"ANC visit\"")
    # assert page.url() == "http://localhost:8000/a/demo/cloudcare/apps/v2/#{"appId":"dc52289b5dbe447ba86830b65d2a68ea","sessionId":null,"steps":[0,1],"page":null,"search":null,"queryDict":null,"sortIndex":null}"

    # Click text="Alice APPLE"
    page.click("text=\"Alice APPLE\"")

    # Close page
    page.close()

