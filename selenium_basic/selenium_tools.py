from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

#========================================================
# 1. Navigation 네이게이션 관련 툴
# 웹 사이트 검색, URL 변경된다든과 관련된 것.페이지 불러오기. 새로고침. 뒤로가기. 
# driver.get("https://www.naver.com")
# time.sleep(1) 
# ## 1-1. get() - 원하는 페이지로 이동하는 함수.
# driver.get("https://google.com")

# ## 1-2. back() - 뒤로가기
# driver.back()
# time.sleep(2)

# ## 1-3. forward() - 앞으로가기
# driver.forward()
# time.sleep(2)

# ## 1-4. refresh() - 페이지 새로고침
# driver.refresh()
# time.sleep(2)

#========================================================
# 2. browser information 
# 브라우저 정보에 대해서 가지고 올 수 있다.
# driver.get("https://naver.com")
# time.sleep(1)
# ## 2-1. title, current_url
# ### title : 웹사이트의 title를 가지고 온다.
# title = driver.title
# print(title, "이 타이틀이다")

# ### current_url : 주소창을 그대로 가지고옴
# curUrl = driver.current_url
# print(curUrl, "가 현재 주소다.")

# if "nid.naver.com" in curUrl:
#     print("지금은 로그인 하는 로직이 필요함")
# else:
#     print("내가 계획한 로직 그대로 실행하면됨")


#========================================================

# 3. Driver Wait

driver.get("https://www.naver.com")
## time.sleep(초)를 줬는데 원래 이런식으로는 하는게 아니다. 각 컴퓨터 네트워크 속도에 따라 다름. 속도가 느리면 1초만 기다려서 원하는 엘리먼트가 나타나지 않았을 수 있다.

### 2가지가 필요.
### from selenium.webdriver.support.ui import WebDriverWait
### from selenium.webdriver.support import expected_conditions as EC

### WebDriverWait(driver, 10) : driver를 10초동안 기다린다.
### .until(언제까지?)
### EC 기대되는 조건 안에 presence_of_element_located와 같은 함수가 들어있음.
#### presence_of_element_located : 특정 찾고자하는 요소가 웹 페이지에 위치할 때 까지 10초까지는 기다림.

## 3-1. 3초때 로딩이 끝나서, element가 찾아짐
## 3-2. 10초까지는 기다림
## 3-3. 10초 넘어가면 에러던짐
try:
    selector = "#shortcutArea > ul > li:nth-child(5) > a"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        By.CSS_SELECTOR, selector
    ))
except:
    print("예외 발생, 예외 처리 코드 실행하기")

print("엘리먼트 로딩 끝")

## 일찍 끝나면 다음 코드 실행
print("다음 코드 실행")


#========================================================



print('동작 끝 ㅅㄱ~')
input()