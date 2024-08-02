# Extract_Package
PLAYDATA 데이터엔지니어링 부트캠프 32기 팀 프로젝트 1
팀 LeeChungBae의 extract_package 모듈 레포지토리 입니다.

# 모듈별 기능
## extract_package.py
to be implemented

## ice_breaking.py
팀원의 사진을 출력하는 아이스브레이킹용 프로그램 입니다. 
코드 내부적으로 각 멤버 사진의 ascii 문자열이 저장되어 있으며
이를 순차적으로 print() 함수를 통해 이름과 번갈아가며 출력되게 되어 있습니다.

Airflow_dags 1일차 dev/1.0.0 branch 기준, 모든 dags가 태스크 완료시에 한 번씩 ice_breaking()을 부르도록 되어 있습니다.

# 함수별 상세
## extract_package.py
### func
```
dummy code
```

## ice_breaking.py
### ice_breaking()
```
ascii_1 = 정세현 사진 아스키아트 
ascii_2 = 배주영 사진 아스키아트
ascii_2 = 이상우 사진 아스키아트
def ice_breaking():
    print(ascii_1)
    print("Sehyeon")
    print(ascii_2)
    print("Jooyoung")
    print(ascii_3)
    print("Sangwoo")

ice_breaking() # testing code

```
