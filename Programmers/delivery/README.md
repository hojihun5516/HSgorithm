# [프로그래머스] 배달

# 1. 문제명 및 난이도

## ▶ 문제명

    배달

## ▶ 난이도

    Level 2

---

## 2. 출처

### [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/12978)

<img src="https://programmers.co.kr/assets/icons/apple-icon-6eafc2c4c58a21aef692d6e44ce99d41f999c71789f277317532d0a9c6db8976.png" width="100px" height="100px" title="px(픽셀) 크기 설정" alt="main1"></img><br/>

---

## 3. 알고리즘 [풀이]

### Hojihoon

    dist라는 변수에 해당 마을까지 가는 비용을 저장합니다.
    nodes라는 변수에 {from:[[to,val],[to,val]]} 이렇게 저장합니다.
    cur_node가 갈 수 있는 곳(to)의 val과 dist의 to를 비교해서 더 낮으면 업데이트해주고 que에 넣어줍니다.

### Sonbyeongil

    대기중
