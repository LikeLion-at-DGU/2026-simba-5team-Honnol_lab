# Soload URL / API 명세서

| Method | URL | name | 인증 | 요청 데이터 | 응답 |
|---|---|---|---|---|---|
| GET | `/` | main | 필요 | - | 메인(레벨별 추천 장소·지도) |
| GET/POST | `/login/` | login | - | username, password | 성공→메인 / 실패→에러 |
| GET/POST | `/signup/` | signup | - | email, username, password, confirm | 성공→테스트 / 실패→에러 |
| GET | `/logout/` | logout | - | - | 시작 페이지 |
| GET | `/placeinfo/<place_id>/` | placeinfo | - | (GET) same_level | 장소 상세(통계·후기·지도) |
| GET/POST | `/createreview/<place_id>/` | createreview | 필요 | 후기 항목 + images(multipart) | 작성 후 상세로 |
| GET/POST | `/review/<review_id>/update/` | review_update | 작성자 | 후기 항목 | 수정 후 상세로 |
| POST | `/review/<review_id>/delete/` | review_delete | 작성자 | - | 마이페이지 |
| POST | `/review/<review_id>/like/` | review_like | 필요 | - | JSON `{success, liked, count}` |
| GET | `/mypage/` | mypage | 필요 | - | 내 찜·후기 |
| GET | `/profile/<user_id>/` | user_profile | 필요 | - | 유저 프로필(본인이면 mypage로 redirect) |
| POST | `/profile/<user_id>/follow/` | follow | 필요 | - | 프로필로 redirect (팔로우 토글) |
| GET/POST | `/profile/edit/` | edit_profile | 필요 | nickname, profile_image(multipart) | 수정 후 마이페이지 |
| GET/POST | `/testpage/` | testpage | 필요 | score | 점수→레벨 저장 후 결과로 |
| GET | `/lastpage/` | lastpage | 필요 | - | 테스트 결과 |
| POST | `/place/<place_id>/like/` | place_like | 필요 | - | JSON `{success, liked}` |
| POST | `/place/create-or-get/` | create_place | 필요 | kakao_id, name, address, latitude, longitude, category, phone, confirm | 존재시 상세 redirect / 신규시 생성→후기작성 / JSON `{exists:false}` |

## 주요 JSON 응답
- `place_like` / `review_like` : `{"success": true, "liked": true/false}` (fetch 토글)
- `review_like` 는 추가로 `"count"`(좋아요 수) 반환
- `create_place` : 미확인 시 `{"exists": false}` → 프론트 confirm 후 `confirm=yes`로 재요청