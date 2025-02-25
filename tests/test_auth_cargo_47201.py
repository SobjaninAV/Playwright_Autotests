import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_auth_caro_47201(page):
    page.goto("https://servicetest.b2b-logist.com/cargo/47201/ru_RU/")
    page.locator("#userName").click()
    page.locator("#userName").fill("472ulsu@gmail.com")
    page.locator("#userPassword").click()
    page.locator("#userPassword").fill("123")
    page.get_by_role("button", name="Войти").click()
    page.locator("#openedCell_itemBox_0").get_by_text("Исходящие Заказы").click()
    page.locator("[id=\"form1_ФормаСоздать\"]").click()
    page.get_by_text("Выберите тип заказа").click()
    page.locator("#grid_form4_ValueList").get_by_text("Аукцион").click()
    page.locator("a").filter(has_text=re.compile(r"^ОК$")).click()
    page.get_by_role("textbox", name="Без НДС:").type("50000,00")
    page.get_by_role("textbox", name="Без НДС:").press("Enter")
    page.get_by_role("textbox", name="с НДС:").click()
    expect(page.get_by_role("textbox", name="с НДС:")).to_have_value("60 000,00")
    page.locator("[id=\"form3_АдресСтрока0_CB\"]").click()
    page.get_by_text("Ул. Островского, 22-").first.dblclick()
    page.locator("[id=\"form3_Груз0_DLB\"]").click()
    page.get_by_role("listitem").filter(has_text="Арбузы").click()
    expect(page.locator("[id=\"form3_КонтрагентСтрока0_i0\"]")).to_have_value("ООО \"ПОГРУЗКА\"");
    expect(page.locator("[id=\"form3_Город0_i0\"]")).to_have_value("г Москва, Россия");
    expect(page.get_by_role("textbox", name="Вес, т.:")).to_have_value("150,000");
    expect(page.get_by_role("textbox", name="Объем, м³:").first).to_have_value("10,000");
    expect(page.locator("[id=\"form3_ГрузN_div\"]").get_by_role("textbox", name="Груз: Выбрать из списка")).to_have_value("Арбузы");
    expect(page.get_by_role("textbox", name="Вес, т:")).to_have_value("150,000");
    expect(page.locator("[id=\"form3_ОбъемN_div\"]").get_by_role("textbox", name="Объем, м³:")).to_have_value("10,000");
    page.locator("[id=\"form3_АдресСтрокаN_CB\"]").click()
    page.get_by_text("Ул. Маяковского, 22-").nth(1).dblclick()
    expect(page.locator("[id=\"form3_КонтрагентСтрокаN_i0\"]")).to_have_value("ООО \"РАЗГРУЗКА\"");
    expect(page.locator("[id=\"form3_ГородN_div\"]").get_by_label("")).to_have_value("г Березники, Пермский край, Россия");
    page.wait_for_timeout(30000)

