# Extract_Package 
PLAYDATA 데이터엔지니어링 부트캠프 32기 팀 프로젝트 1
팀 LeeChungBae의 extract_package 모듈 레포지토리 입니다.

## dev/1.0.0 branch
본 브랜치의 패키지는 https://github.com/LeeChungBae/Airflow_dags 레포지토리의 `dev/d1.0.0` 버전에 사용된 패키지이며,

자매 패키지로 
- `load_package dev/d1.0.0`: https://github.com/LeeChungBae/Load_package/tree/dev/d1.0.0
- `transform_package dev/d1.0.0`: https://github.com/LeeChungBae/Transform_package/dev/d1.0.0
가 있습니다.


## 모듈별 기능
- `extract_package.py`:
to be implemented.
본 branch에서는 아직 개발되지 않은 기능입니다.

- `ice_breaking.py`:
팀원의 사진을 출력하는 아이스브레이킹용 프로그램 입니다. 
코드 내부적으로 각 멤버 사진의 ascii 문자열이 저장되어 있으며
이를 순차적으로 print() 함수를 통해 이름과 번갈아가며 출력되게 되어 있습니다.

Airflow_dags 1일차 dev/1.0.0 branch 기준, 모든 dags가 태스크 완료시에 한 번씩 ice_breaking()을 부르도록 되어 있습니다.

