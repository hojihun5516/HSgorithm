# [프로그래머스] 방금 그곡

# 1. 문제명 및 난이도

## ▶ 문제명

    방금 그곡

## ▶ 난이도

    Level 2

---

## 2. 출처

### [프로그래머스](https://programmers.co.kr/learn/courses/30/lessons/17683)

<img src="https://programmers.co.kr/assets/icons/apple-icon-6eafc2c4c58a21aef692d6e44ce99d41f999c71789f277317532d0a9c6db8976.png" width="100px" height="100px" title="px(픽셀) 크기 설정" alt="main1"></img><br/>

---

## 3. 알고리즘 [풀이]

### Hojihoon

    check_shop 이라는 함수를 만들어서 #이 붙은 영역을 다른 문자열로 대체하였습니다.
    during_time 이라는 함수를 만들어서 총 몇분이 걸렸는지를 계산해주었습니다.
    during_time이 melody의 길이보다 작을때는 melody를 during_time만큼 잘라주어야합니다 (해당 케이스때문에 테스트케이스-30의 부분이 해결이 안됐었어요 ㅎㅎ..)
    melody의 길이가 더 작을경우에는 melody의 길이를 넉넉하게 늘려줍니다.
    만들어진 data의 melody에 m이 있으면 answer에 추가하여 데이터를 생성해주고
    return 조건을 문제에 맞게 섞어 줍니다.

### Sonbyeongil

    #이 붙은것을 replace를 사용해 바꿔준다.
    시간을 계산하는 로직을 만들고 시간동안의 리듬을 만들어준다.
    (남아있는 시간이 있을수있다. while에서 break로 끝나기 떄문에
    0까지 리듬을 추가해준다.)
    String.contains를 사용해 m이 포함되어있는것은 모두 answerList에
    저장해준다. 리스트 정렬을 한다. 문제 조건의 시간을 기준으로 시간이 같을시
    먼저 저장된것을 기준으로 0번째 곡명을 리턴해준다.
    
