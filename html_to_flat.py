from bs4 import BeautifulSoup

#改行やスペースを消して、htmlをリストにする
def html_to_flat_array(element, array):
    if element.name is None:
        if element.string and element.string.strip() and element.string != "力":  # 空の要素でない場合のみ追加
            array.append(element.string.strip())
    else:
        for child in element.children:
            html_to_flat_array(child, array)