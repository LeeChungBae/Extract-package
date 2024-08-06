# Extract_Package 
PLAYDATA 데이터엔지니어링 부트캠프 32기 팀 LeeChungBae의 extract_package 모듈 레포지토리 입니다.

## dev/1.0.0 branch
본 브랜치의 패키지는 https://github.com/LeeChungBae/Airflow_dags/tree/dev/d1.0.0 레포지토리의 `dev/d1.0.0` 버전에 사용된 패키지이며,

자매 패키지로 
- `load_package dev/d1.0.0`: https://github.com/LeeChungBae/Load_package/tree/dev/d1.0.0
- `transform_package dev/d1.0.0`: https://github.com/LeeChungBae/Transform_package/dev/d1.0.0

가 있습니다.


## 모듈별 기능
- `extract_package.py`:
본 branch에서는 개발중인 기능입니다.

영화진흥위원회 오픈 API 기능을 통해 지정한 년도의 박스오피스 데이터를 `request`받아 저장하는 모듈입니다.

- `ice_breaking.py`:

팀원의 사진을 출력하는 아이스브레이킹용 모듈입니다.

코드 내부적으로 각 멤버 사진의 ascii 문자열이 저장되어 있으며
이를 `ice_breaking()` 함수를 통해 순차적으로 `print()` 하여 이름과 번갈아가며 출력하게 되어 있습니다.

Airflow_dags 1일차 dev/1.0.0 branch 기준, 모든 dags가 태스크 완료시에 한 번씩 ice_breaking()을 부르도록 되어 있습니다.

