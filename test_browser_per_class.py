import pytest


@pytest.mark.usefixtures("login")
class Test1:
    def test_1(self, sb):
        sb.wait(1)
        sb.assert_text("PRODUCTS", "span.title")

    def test_2(self, sb):
        sb.wait(1)
        assert False
        sb.assert_element("div.inventory_list")


@pytest.mark.usefixtures("login")
class Test2:
    def test_3(self, sb):
        sb.wait(1)
        sb.assert_text("PRODUCTS", "span.title")

    def test_4(self, sb):
        sb.wait(1)
        sb.assert_element("div.inventory_list")
