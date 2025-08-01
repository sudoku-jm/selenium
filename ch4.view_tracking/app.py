from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

#==================
#여러개의 타켓 블로그 찾기 + 타켓 블로그 30위내에 없을때 -> 스크롤해서 찾기
#==================

##검색쿼리들 배열
search_querys = ["python flask","python selenium"]
##타켓 블로그 링크들 배열
target_blog_links = ["https://blog.naver.com/et0709/223621484130","https://blog.naver.com/ergosphere29/223164321902"]



#=========내 방식=====================

BLOG_FOUND = False
MAX_SCROLL_ATTEMPTS = 7

for search_query, target_blog_link in zip(search_querys, target_blog_links):
    search_link = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={search_query}"
    driver.get(search_link)
    time.sleep(2)
    for i in range(MAX_SCROLL_ATTEMPTS):
        try:
            link_selector = f'a[data-url^="{target_blog_link}"]'
            # 1️⃣ 타겟 블로그의 링크가 있는 a 요소 찾기 시도
            element = driver.find_element(By.CSS_SELECTOR, link_selector)

            print('element 존재함')

            # 2️⃣ 조상 li.bx 요소 추적 (안전한 방식)
            while True:
                if element.tag_name.lower() == "html":
                    raise NoSuchElementException("li.bx 조상 요소를 찾지 못했음 (html까지 도달)")
                element = element.find_element(By.XPATH, "./..")
                if element.tag_name.lower() == "li" and "bx" in (element.get_attribute("class") or ""):
                    li_element = element
                    break

            # 3️⃣ 전체 리스트 중 몇 번째인지 계산
            li_list = driver.find_elements(By.CSS_SELECTOR, "ul.lst_view > li.bx")
            now_rank = li_list.index(li_element) + 1

            print(f"✅ {search_query} : 타겟 블로그의 랭크는 {now_rank}위입니다.")
            BLOG_FOUND = True
            break

        except NoSuchElementException:
            print(f"❌ {i+1}차 시도: 아직 타겟 블로그를 찾지 못했습니다. 스크롤 시도 중...")

        except ValueError:
            print("❌ li 리스트 안에 해당 요소가 없습니다. 비동기 로딩 실패 가능성 있음.")

        except Exception as e:
            print(f"❌ 알 수 없는 에러 발생: {type(e).__name__} - {e}")

        # ⏬ 못 찾았으니 스크롤 내리기
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)

    # 7회 스크롤 해도 못찾은 경우
    if not BLOG_FOUND:
        print(f"❗ {search_query} : 타겟 블로그의 랭크를 찾지 못했습니다.")

#====================================

# =========강의 방식==================
## 파이썬의 zip()을 활용해서 두개의 배열을 쌍으로 묶어 반복하는 구조.
# for search_query, target_blog_link in zip(search_querys, target_blog_links):
#     search_link = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={search_query}"
#     driver.get(search_link)
#     time.sleep(2)

#     link_selector = f'a[data-url^="{target_blog_link}"]'
#     now_rank = -1 
#     BLOG_FOUND = False
#     for _ in range(7): 
#         # 최대 7번 하위 랭크 블로그 글을 불러오겠음.
#         try : 
#             element = driver.find_element(By.CSS_SELECTOR, link_selector)
#             while True:
#                 #By.XPATH : 부모 엘리먼트 단계. 위로 찾기
#                 # . 점은 현재 위치 , .. 점점은 한단계위로, ./.. 나의 바로 위에 있는 부모 엘리먼트를 찾기.
#                 new_element = element.find_element(By.XPATH, "./..")
#                 now_rank = new_element.get_attribute("data-cr-rank")
#                 if now_rank != None:
#                     # print("현재랭크 찾음 : ", now_rank)
#                     BLOG_FOUND = True
#                     break
#                 # print("현재랭크 못찾음")
#                 element = new_element
#             if BLOG_FOUND : 
#                 #for문을 굳이 더 실행시켜줄 필요가 없음.
#                 break
#         except:
#             #예외처리
#             print("타겟 블로그를 못 찾음. => 스크롤하겠습니다.")
#             driver.execute_script("window.scrollBy(0, 1000);")
#             time.sleep(3) #새로운 글 로딩하는데 좀 기다려줌
#     print(f"{search_query} / {now_rank}등 : 타켓 블로그의 랭크를 찾았습니다.")
#====================================
input()