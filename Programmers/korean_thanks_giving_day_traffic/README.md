# [프로그래머스] 추석 트래픽

# 1. 문제명 및 난이도

## ▶ 문제명

    추석 트래픽

## ▶ 난이도

    Level 3

---

## 2. 출처

### [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/17676)

<img src="https://programmers.co.kr/assets/icons/apple-icon-6eafc2c4c58a21aef692d6e44ce99d41f999c71789f277317532d0a9c6db8976.png" width="100px" height="100px" title="px(픽셀) 크기 설정" alt="main1"></img><br/>

---

## 3. 알고리즘 [풀이]

### Hojihoon

주어진 end_time을 millisecond로 바꿔줍니다. (초로 변환 후 1000을 곱함)
문제에 주어진 방법으로 start_time을 계산하고 requests(List)에 [start_time, end_time]을 이중배열로 추가해줍니다.
데이터 세팅을 끝내고, 1초에 맞는 max값을 구하기 위해 모든 requests의 시작시간과 끝시간만을 999(1초)를 더해서 count_request함수에 넣어줍니다.
이렇게 하면 1초라는 시작시간 앞과 끝나는 시간 후를 제외한 모든 곳에서 발생된 request를 count할 수 있습니다.

### Sonbyeongil
