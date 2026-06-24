# 🐤 Soload (솔로드)

> 나의 **혼놀 레벨**에 맞는 장소를 추천하고, 후기로 함께 성장하는 20대 혼놀 서비스

멋쟁이사자처럼 동국대 14기 5팀 — Honnol_lab

---

## 🛠 기술 스택
- Python 3.12 / Django 6.0
- SQLite3
- 카카오 지도 API (장소 검색·지도)
- HTML / CSS / JavaScript (MTV 템플릿)

---

## 🚀 실행 방법 (git clone 후)

> 프로젝트는 `Soload/` 폴더 안에 있습니다. 모든 명령은 `Soload/`에서 실행하세요.

### 1. 클론 & 이동
```bash
git clone <레포지토리 주소>
cd <레포지토리 폴더>/Soload
```

### 2. 가상환경 생성 & 활성화
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. `.env` 파일 생성 (카카오 키)
`Soload/` 폴더 안(= `manage.py`가 있는 위치)에 **`.env`** 파일을 만들고,
**노션에 공유된 내용을 그대로 복붙**하세요.

`.env` 예시:
```
KAKAO_APP_KEY=노션에_공유된_키값
```
> `.env`는 보안상 git에 포함되지 않아 직접 생성해야 합니다.
> 키가 없으면 지도·장소검색만 비활성화되고 나머지 기능은 정상 동작합니다.

### 5. 서버 실행
```bash
python manage.py runserver
```
→ 브라우저에서 **http://127.0.0.1:8000** 접속

> 데이터베이스(db.sqlite3)와 사진(media)이 레포에 포함되어 있어, **바로 장소·후기 데이터가 보입니다.**
> 혹시 DB 관련 에러가 나면 `python manage.py migrate`를 한 번 실행하세요.

### (선택) 관리자 페이지
```bash
python manage.py createsuperuser
```
→ `http://127.0.0.1:8000/admin/` 에서 데이터 관리

---

## 🧭 주요 기능
- 회원가입 → **혼놀 테스트**로 레벨 부여(병아리 캐릭터)
- **레벨별 장소 추천** + 카카오 지도 마커
- 카카오 검색으로 **장소 직접 등록**
- 후기 작성(사진·태그·체류시간) → **경험치/레벨업 + 장소 정보 자동 보정**
- 후기 **좋아요 / 수정 / 삭제**, 같은 레벨 후기 필터
- 장소 **찜**, 마이페이지(찜·후기·성장단계), **프로필 수정**
- **유저 프로필 / 팔로우·팔로잉**
- 레벨·장소별 **혼놀 도움말 팁**

---

## ⚠️ 참고
- Python **3.12** 권장
- DB·사진이 레포에 포함되어 있어 별도 데이터 세팅 없이 바로 실행됩니다.
- 카카오 키(`.env`)가 없으면 지도/검색만 빠지고 나머지는 그대로 동작합니다.
