from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 강의 정리
# 1. URL로 1페이지 방문
page_index = 1
search_query = "꿀사과"
shop_link = f"https://msearch.shopping.naver.com/search/all?adQuery={search_query}&frm=NVSCTAB&origQuery={search_query}&pagingIndex={page_index}&pagingSize=40&productSet=total&query={search_query}&sort=rel&viewType=list"

driver.get(shop_link)
time.sleep(10)


# 2. 페이지 4-5번 밑으로 내리기(상품 더 불러오기)
MAX_SCROLL_ATTEMPTS = 2

for i in range(MAX_SCROLL_ATTEMPTS):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

# 3. 타겟 상품이 페이지에 노출되고 있는지 확인하기
# 4. 없다면 -> URL로 Next Page 방문
try:
    ## 모바일버전 상품 고유 아이디 #_sr_lst_86716488026 , data-i="86716488026"
    target_code = "86716488026"
    target_product_selector = f"a[data-shp-contents-id='{target_code}']"    # data-i 고유값으로 상품 순위 찾기
    target_element = driver.find_element(By.CSS_SELECTOR, target_product_selector)
    # elements = driver.find_elements(By.CSS_SELECTOR, selector)

    # data-i와 data-ms 속성이 target_code인 a 태그 중, href="#"가 아닌 것 선택
    # target_element = None
    # for el in elements:
    #     if el.get_attribute("href") != "#":
    #         target_element = el
    #         break

    ## 해당 상품 고유 아이디 > a태그에 "data-shp-contents-rank" 랭킹이 보임.
    # if target_element:
    print("랭킹 : ", target_element.get_attribute("data-shp-contents-rank"))
    print("contentsData : ", target_element.get_attribute("data-shp-contents-dtl"))
    print("href : ", target_element.get_attribute("href"))


except:
    print("타겟 상품을 못찾음")
    # Next Page 방문

input()