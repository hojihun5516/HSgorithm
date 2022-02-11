[프로그래머스] n진수 게임
======================
# 1. 문제명 및 난이도
## ▶ 문제명
	n 진수 게임

## ▶ 난이도
	Level 2

****
## 2. 출처
### [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/17687)
<img src="https://programmers.co.kr/assets/icons/apple-icon-6eafc2c4c58a21aef692d6e44ce99d41f999c71789f277317532d0a9c6db8976.png" width="100px" height="100px" title="px(픽셀) 크기 설정" alt="main1"></img><br/>
****
## 3. 알고리즘 [풀이]
### Hojihoon
    진행중

### Sonbyeongil
    찾아야될 길이까지 num을 n진수화 해준다.
    찾아야될 길이 구하는 점화식 찾는데 시간좀 걸렸다.
    t=1, m=1, p=1 len=1
    t=2, m=2, p=1 len=2
    t=3, m=3, p=1 len=6
    t=4 m =2 p=2 len=7
    하 노가다(결론적으로 t * m + p - 1 이렇게 풀었는데 일부러 변수명 TMP로 한건가 해서 신기했다.)
    여튼 p는 나중에 생각하자 그냥 t*m 하는게 쉽다.
    그 이후는 그냥 p-1번째 추가해주고
    p는 m만큼 증가시면서 t만큼 하면된다.