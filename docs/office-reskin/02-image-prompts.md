# 야근 탈출 개편: 이미지 지시문 (GPT 아스트라용)

작성일: 2026-09-29. 이름과 설정은 `01-names.md` 를 따른다.

## 1. 쓰는 방법

| 순서 | 할 일 |
|---|---|
| 1 | 아래 "공통 스타일 문장" 을 복사한다 |
| 2 | 그 뒤에 그림별 "주제 문장" 을 붙여서 아스트라에 넣는다 |
| 3 | 받은 그림을 표에 적힌 파일 이름으로 `assets/office/` 폴더에 저장한다 |
| 4 | 저장했다고 알려 주면 게임에 연결한다 |

기존 `assets/` 의 그림은 지우지 않는다. 새 그림은 `assets/office/` 에 따로 모은다.

지시문이 영어인 이유: 이미지 도구는 보통 영어 지시를 더 정확히 따른다. 아스트라에서 한국어로도 잘 되는지는 시험해 보지 않았다.

## 2. 먼저 3장만 만든다

| 순서 | 그림 | 파일 이름 | 이유 |
|---|---|---|---|
| 1 | 김 과장 (주인공) | player.png | 가장 오래 보는 그림 |
| 2 | 안 읽은 메일 | enemy_mail.png | 가장 많이 나오는 적 |
| 3 | 5층 사무실 바닥 | floor_5f.png | 캐릭터가 배경 위에서 잘 보이는지 확인 |

이 3장을 게임에 넣어 보고 화풍을 확정한 뒤 나머지를 만든다. 한 번에 전부 만들면 방향이 틀렸을 때 다시 만들어야 한다.

## 3. 그림 규격

| 항목 | 값 | 이유 |
|---|---|---|
| 형식 | PNG, 투명 배경 | 바닥 위에 겹쳐 그림 |
| 크기 | 정사각형. 256 x 256 이상 | 게임이 줄여서 씀. 화면에서는 약 40픽셀 |
| 여백 | 그림이 칸의 약 85% 를 채움 | 너무 작으면 게임에서 더 작아 보임 |
| 그림자 | 넣지 않음 | 바닥과 겹치면 지저분함 |
| 글자 | 넣지 않음 | 작아지면 읽을 수 없음 |
| 상표와 로고 | 넣지 않음 | 공개 배포 중 |

투명 배경이 안 나오면 순수한 초록색 (#00FF00) 단색 배경으로 받는다. 배경은 나중에 지울 수 있다.

### 방향 규칙 (게임 코드에서 확인함)

| 종류 | 그리는 방향 | 이유 |
|---|---|---|
| 주인공과 적 | 정면 또는 오른쪽을 봄 | 왼쪽으로 갈 때는 게임이 좌우를 뒤집음 |
| 날아가는 무기 | 끝이 위쪽을 향함 | 게임이 날아가는 방향으로 돌림 |
| 아이콘, 아이템 | 정면 | 돌리지 않음 |
| 바닥 | 위에서 내려다봄 | |

## 4. 공통 스타일 문장

모든 캐릭터, 적, 무기, 아이템 그림 앞에 붙인다.

```
Flat sticker-style game sprite. Thick black outline of even width, solid flat colors,
no gradients, no shading, no drop shadow, no text, no logos. Simple chunky shapes that
stay readable at 40 pixels. Slightly exaggerated cartoon proportions, big head, small body.
Single subject centered, filling about 85 percent of a square canvas.
Transparent background. Muted office color palette: navy, grey, beige, white,
with one bright accent color per subject.
```

바닥 그림에는 아래 문장을 대신 쓴다.

```
Seamless tileable top-down floor texture for a 2D game. Flat colors, very low contrast,
no objects, no shadows, no text. The pattern must repeat without visible seams on all
four edges. Dark and muted so that characters drawn on top stand out. Square image.
```

## 5. 주인공

| 파일 이름 | 주제 문장 |
|---|---|
| player.png | `A tired middle-aged Korean office worker, dark circles under half-closed eyes, loosened necktie, wrinkled white shirt with rolled sleeves, holding a paper cup of coffee, slouching. Full body, facing right.` |

## 6. 적

| 새 이름 | 파일 이름 | 주제 문장 |
|---|---|---|
| 안 읽은 메일 | enemy_mail.png | `A small flying envelope with tiny wings and angry eyes, a red notification dot on its corner.` |
| 회의 | enemy_meeting.png | `A round meeting table with stubby legs and an angry face, a few sticky notes stuck on it.` |
| 후속 회의 | enemy_meeting_small.png | `A tiny folding chair with an angry face, running.` |
| 메신저 | enemy_messenger.png | `A floating speech bubble with three dots inside and pleading eyes, ghost-like tail.` |
| 전화기 | enemy_phone.png | `A desk phone with a curly cord, legs, and an angry face, its handset shaking as if ringing.` |
| 분기 보고서 | enemy_report.png | `A huge heavy stack of paper documents with a binder clip, thick arms, one tired eye.` |
| 회식 | enemy_soju.png | `A green glass soju bottle monster, plain blank white label with no text and no logo, flushed cheeks, tipsy grin, holding up a small shot glass.` |
| 추가 업무 | enemy_fakebox.png | `A snack gift box opened like a mouth with sharp paper teeth, documents spilling out.` |

## 7. 보스

| 새 이름 | 파일 이름 | 주제 문장 |
|---|---|---|
| 옆 팀 팀장 | boss_5f.png | `An office team leader in a vest, wide fake smile, holding out a thick folder with both hands. Full body.` |
| 끝나지 않는 주간 회의 | boss_4f.png | `A giant whiteboard on wheels with a stern face, covered in scribbled arrows and boxes, marker pens as arms.` |
| 인사팀장 | boss_3f.png | `A neat HR manager with a clipboard and a polite cold smile, glasses glinting. Full body.` |
| 감사팀장 | boss_2f.png | `A stern auditor in a dark suit holding a magnifying glass and a long trailing receipt. Full body.` |
| 부장님 | boss_bujang.png | `A big middle-aged department head in a suit, jacket over shoulders, cheerful red face, one arm raised in invitation. Full body, imposing.` |

## 8. 무기 12개

| 새 이름 | 파일 이름 | 방향 | 주제 문장 |
|---|---|---|---|
| 볼펜 | w_pen.png | 위 | `A blue ballpoint pen, tip pointing straight up.` |
| 스테이플러 | w_stapler.png | 정면 | `A red desk stapler, side view.` |
| 스테이플러 심 | w_staple.png | 위 | `A single metal staple flying, points facing straight up.` |
| 키보드 | w_keyboard.png | 위 | `A computer keyboard held like a sword, long side vertical, pointing straight up.` |
| 사원증 목걸이 | w_lanyard.png | 정면 | `An employee ID card on a blue lanyard, the card has a blank photo square.` |
| 커피 향 | w_coffee.png | 정면 | `A steaming mug of coffee, big swirling steam.` |
| 컵라면 국물 | w_ramen.png | 정면 | `An open cup of instant noodles, hot soup splashing out, plain cup with no label.` |
| 반려된 결재 서류 | w_rejected.png | 정면 | `A paper document with a big red round stamp mark on it, slightly bent like a boomerang.` |
| 종이비행기 | w_plane.png | 위 | `A white paper airplane, nose pointing straight up.` |
| 레이저 포인터 | w_pointer.png | 위 | `A slim silver laser pointer with a red glowing tip, pointing straight up.` |
| 에어컨 리모컨 | w_remote.png | 정면 | `A white air conditioner remote control with a snowflake icon on its screen.` |
| 칸막이 | w_partition.png | 정면 | `A grey office cubicle partition panel, front view, like a shield.` |
| 전체 선택 후 삭제 | w_delete.png | 정면 | `A large keyboard Delete key, red, glowing.` |

스테이플러는 아이콘 (w_stapler) 과 날아가는 심 (w_staple) 이 따로 필요하다. 지금 코드는 아이콘과 발사체가 같은 그림을 쓰므로 연결할 때 코드를 조금 고쳐야 한다.

진화 무기는 지금 기본 무기와 같은 그림을 쓴다. 진화 전용 그림은 나중에 추가할 수 있다.

## 9. 아이템 (패시브) 16개

파일 이름은 지금 코드의 키를 그대로 쓴다.

| 새 이름 | 파일 이름 | 주제 문장 |
|---|---|---|
| 에너지 드링크 | passive_might.png | `A small brown glass energy tonic bottle, plain label.` |
| 무릎 담요 | passive_armor.png | `A folded checkered lap blanket.` |
| 든든한 점심 | passive_maxhp.png | `A lunch box with rice and side dishes, top view.` |
| 비타민 | passive_regen.png | `A yellow vitamin tablet bottle with two tablets beside it.` |
| 단축키 | passive_cooldown.png | `Two keyboard keys side by side with a lightning bolt between them.` |
| 스탠드 조명 | passive_area.png | `A desk lamp with a cone of light.` |
| 손목 보호대 | passive_projspeed.png | `A black wrist brace.` |
| 업무 매뉴얼 | passive_duration.png | `A thick ring binder with colored tabs.` |
| 복사기 | passive_amount.png | `An office photocopier with two identical sheets coming out.` |
| 사무실 슬리퍼 | passive_move.png | `A pair of plain rubber office slippers.` |
| 화이트보드 자석 | passive_magnet.png | `A round red whiteboard magnet.` |
| 복권 | passive_luck.png | `A lottery ticket with a four-leaf clover, no numbers readable.` |
| 자격증 | passive_growth.png | `A certificate with a gold seal and ribbon.` |
| 일 욕심 | passive_curse.png | `A tall leaning tower of folders with a small flame on top.` |
| 반차 | passive_revival.png | `A calendar page with half of one day colored in, a small sun.` |
| 점심 메뉴판 | passive_choices.png | `A small standing menu board with three blank lines.` |

## 10. 바닥에 떨어지는 것과 화면 단추

| 새 이름 | 파일 이름 | 주제 문장 |
|---|---|---|
| 커피콩 | bean.png | `A single shiny coffee bean, green glow outline.` |
| 아이스 아메리카노 | item_heal.png | `A clear plastic cup of iced black coffee with a straw, plain cup.` |
| 대형 자석 | item_magnet.png | `A big red and silver horseshoe magnet.` |
| 정전 | item_wipe.png | `A power switch turned off, with a dark light bulb.` |
| 점심시간 | item_freeze.png | `A wall clock showing twelve, with a spoon and chopsticks crossed behind it.` |
| 간식 상자 (닫힘) | box.png | `A closed cardboard snack gift box tied with a ribbon.` |
| 간식 상자 (열림) | box_open.png | `The same cardboard snack box opened, snacks and gold sparkle inside.` |
| 도움말 단추 | help.png | `A yellow sticky note with a big question mark.` |
| 엘리베이터 (쓰지 않음. 비상계단 문 stairs.png 로 바꿈, 14장 참고) | elevator.png | `Elevator doors, top-down slightly angled view, a green down arrow lit above.` |

## 11. 배경

바닥용 스타일 문장 (4장 참고) 을 앞에 붙인다.

| 층 | 파일 이름 | 주제 문장 |
|---|---|---|
| 5F 사무실 | floor_5f.png | `Dark grey-blue office carpet tiles.` |
| 4F 회의실 | floor_4f.png | `Dark brown wood laminate flooring.` |
| 3F 탕비실 | floor_3f.png | `Dim beige linoleum with small speckles.` |
| 2F 서버실 | floor_2f.png | `Dark raised-floor metal panels with small vent holes.` |
| 1F 로비 | floor_1f.png | `Dark polished marble tiles.` |
| 벽 | wall.png | `Office wall segment seen from above, grey, with a thin baseboard.` |

### 장식 (선택)

바닥 위에 드문드문 놓는 물건이다. 공통 스타일 문장을 쓰고, 위에서 비스듬히 내려다본 모습으로 그린다. 충돌 없이 장식으로만 쓴다.

| 층 | 물건 |
|---|---|
| 5F | 책상과 모니터, 사무용 의자, 화분 |
| 4F | 긴 회의 탁자, 빔 프로젝터, 화이트보드 |
| 3F | 정수기, 커피 머신, 전자레인지 |
| 2F | 서버 랙, 서류 캐비닛, 복합기 |
| 1F | 안내 데스크, 회전문, 큰 화분 |

## 12. 이야기 그림 (큰 그림 3장)

크기 1280 x 720, 배경 있음. 공통 스타일 문장에서 "Transparent background" 와 "Single subject centered" 부분을 빼고 쓴다.

| 장면 | 파일 이름 | 주제 문장 |
|---|---|---|
| 시작 | story_open.png | `Night office, rows of desks, one lit monitor. The tired office worker stands with his bag in hand, looking at a glowing mail notification. Wall clock shows six.` |
| 게임오버 | story_over.png | `The tired office worker asleep face-down on his desk, monitor still on, empty paper cups around.` |
| 클리어 | story_clear.png | `Inside a nearly empty late-night subway car, the tired office worker asleep leaning on the window, city lights outside.` |

## 13. 개수

| 종류 | 개수 |
|---|---|
| 주인공 | 1 |
| 적 | 8 |
| 보스 | 5 |
| 무기 | 13 |
| 아이템 (패시브) | 16 |
| 바닥 아이템과 단추 | 9 |
| 배경 (바닥 5 + 벽 1) | 6 |
| 이야기 그림 | 3 |
| 합계 (장식 제외) | 61 |

## 14. 계단 개편 그림 (2026-09-30 추가)

엘리베이터를 비상계단으로 바꾸고 결말을 홀케이크 장면으로 바꾸면서 만든 그림이다. 이 문서의 12장, 13장 개수는 처음 계획 때의 숫자이고, 지금 실제 개수는 `03-review.md` 1장에 있다.

앞에 붙인 공통 문장:

`Create one wide landscape illustration, 3:2 aspect ratio, opaque with a full background scene (this one is NOT a sprite, so it has a background). Same bold cartoon sticker art style as the office night scenes you made before: very thick black outlines, solid flat colors, no gradients, no text, no logos, absolutely no letters or numbers anywhere (screens, signs, calendars and clocks show only simple icons or plain marks). The main character is the same tired middle-aged Korean office worker as before: messy black hair, heavy dark bags under droopy eyes, loosened red necktie, white shirt, navy trousers, brown leather briefcase.`

(story_stairs 는 사람이 없는 배경이라 "In this scene NO character appears at all" 문장을 더 넣었다.)

| 장면 | 파일 이름 | 주제 문장 |
|---|---|---|
| 시작 4: 점검 중인 엘리베이터 | story_noelev.png | `the elevator hall of the office floor in the evening. The elevator doors are closed and blocked: a yellow folding caution sign with a simple black wrench icon stands in front of the doors, and yellow-and-black striped tape is stretched across them. The floor indicator above the doors is dark. The main character stands in front of the blocked elevator holding his briefcase, shoulders dropped, sighing, head turned toward the side where a grey door stands half open with a green lit panel above it showing a simple staircase icon. Elevator under maintenance scene.` |
| 계단을 걸어 내려가는 배경, 옆에서 본 모습 (쓰지 않음. `_old/story_stairs_side.jpg`) | story_stairs.png | `a flat SIDE VIEW cross-section of the same grey concrete emergency stairwell, like a side-scrolling game background. One single straight flight of about eight big chunky steps goes DOWN from a flat landing in the upper LEFT of the image to a flat landing in the lower RIGHT of the image. A closed grey door stands on each landing. A metal handrail follows the steps. One warm wall lamp and one small window with the night city. Empty side view staircase background scene.` |
| 계단 1: 문자 | story_stair1.png | `inside the grey concrete emergency stairwell of an office building, metal handrail, plain walls, one small green lit panel with a simple staircase icon on the wall. The main character is walking DOWN the stairs, seen from the front, looking at the phone in his hand with a small tired smile; a small speech bubble with a red heart pops out of the phone. He holds his brown briefcase in the other hand. Stairwell text message scene.` |
| 계단 2: 부재중 전화 | story_stair2.png | `inside the same grey concrete emergency stairwell as your previous image (metal handrail, plain concrete walls, warm wall lamp). Close-up: his hand holds the phone toward the viewer; the phone screen shows two red round missed-call telephone icons. His face behind the phone looks guilty and worried with one sweat drop. He grips his brown briefcase in the other hand. Stairwell missed calls scene.` |
| 계단 4: 1층 문 앞 | story_stair4.png | `the bottom landing of the same grey concrete emergency stairwell. He is seen from behind, standing in front of a heavy grey metal door, briefcase in hand, shoulders squared and determined. Above the door a green lit panel shows a simple running-figure icon, and warm light leaks from under the door. The last steps of the staircase are visible behind him on the left. Stairwell ground floor door scene.` |
| 결말 3: 식탁에서 함께 촛불 | story_home.png | `late at night at home, in the SAME dining room as your earlier image of the little girl waiting at the table: a wooden dining table with a pink checkered table runner, a pink gift box with a yellow ribbon, warm lamp light, night city outside the window. In the middle of the table stands a WHOLE round white cream birthday cake with strawberries on top and exactly six thin striped candles, all six lit with small flames. The cake is whole and uncut: no cake slice and no cut piece anywhere. The little daughter (black bob hair, pink bunny pajamas, pink polka-dot party hat) was just woken up: sleepy half-open eyes but a big happy smile, cheeks puffed, leaning toward the cake and blowing out the candles. The father sits right beside her at the table with one arm around her shoulders, smiling warmly with tired eyes; his brown briefcase rests on the floor next to his chair. Both faces are clearly visible. Whole cake ending scene.` |

| 김 과장의 눈으로 본 계단 (지금 쓰는 story_stairs) | story_stairs_pov.png | `FIRST-PERSON point of view, seen through the main character's own eyes while he walks DOWN the grey concrete emergency stairwell of the office building. The camera looks slightly downward: one straight flight of big chunky concrete steps goes down and away from the viewer toward a flat landing below with a closed grey metal door and a small green lit panel with a simple staircase icon. A metal handrail runs along the right wall in strong perspective. One warm wall lamp, plain concrete walls, a small window with the night city. At the bottom edge of the image, his own right hand and arm in a white shirt sleeve hold the brown leather briefcase, partly visible, so it is clear we see through his eyes. No face, no other person. First person stairwell descent scene.` |

| 그 밖의 것 | 설명 |
|---|---|
| story_stair3.jpg | 새로 만들지 않았다. 예전 story_elev3 (케이크를 꺼내 놓은 집) 의 이름만 바꿨다 |
| stairs.png | 보스를 잡으면 나타나는 비상계단 문 아이콘. 쓴 지시문은 이 문서에 남기지 못했다 |
| 쓰지 않게 된 그림 | elevator.png, story_elev1, story_elev2, story_elev4, 예전 story_home 은 `assets/office/_old/` 로 옮겼다 |

## 15. 움직임 시트 (2026-09-30 추가)

김 과장과 적 8종의 걷기·펄럭임 프레임. 한 장에 4칸을 가로로 그리게 하고, 배경을 마젠타(#FF00FF) 단색으로 지정해 나중에 지운다. 검정 배경으로 나오면 외곽선과 구분이 안 되어 못 쓴다 (김 과장 1차 시도가 그랬음).

공통 문장 (앞에 붙임):

`Create one wide landscape image, 3:2 aspect ratio. It is a SPRITE SHEET: exactly 4 figures in ONE horizontal row (a 4x1 grid), all of them the SAME subject: <누구>. Same bold cartoon sticker art style as before: very thick black outlines, solid flat colors, no gradients, no text, no labels, no numbers, no grid lines, no boxes. The background is one flat solid MAGENTA color (#FF00FF) everywhere, with no shadow on the ground and nothing else. Read left to right, the four figures are: <4칸 설명>. All four have exactly the same size and drawing style and sit on the same invisible floor line so their bottoms are at the same height; each is fully inside the image with clear magenta space between neighbours and nothing touching or overlapping. Sprite sheet.`

| 대상 | 파일 (assets/office/_src) | 4칸 설명 |
|---|---|---|
| 김 과장 | sheet_player_walk.png | 1 서 있음(발 모음) / 2 오른발 앞 / 3 다리 교차 / 4 왼발 앞 |
| 안 읽은 메일 | sheet_enemy_mail_walk.png | 날개 위 / 수평 / 아래 / 수평 |
| 회의 | sheet_enemy_meeting_walk.png | 왼쪽 기울임 / 바로 / 오른쪽 기울임 / 바로 |
| 메신저 | sheet_enemy_messenger_walk.png | 납작 / 보통 / 길쭉 / 보통 |
| 전화기 | sheet_enemy_phone_walk.png | 수화기 들림(왼쪽 울림선) / 내림 / 들림(오른쪽) / 내림 |
| 분기 보고서 | sheet_enemy_report_walk.png | 왼쪽 기울임 / 바로 / 오른쪽 기울임 / 맨 위 장 들림 |
| 후속 회의(접이식 의자) | sheet_enemy_meeting_small_walk.png | 뒤로 기울임 / 바로 / 앞으로 기울임 / 바로 |
| 회식(소주병) | sheet_enemy_soju_walk.png | 왼쪽 / 바로 / 오른쪽 / 바로 + 물방울 |
| 추가 업무(가짜 상자) | sheet_enemy_fakebox_walk.png | 뚜껑 닫힘 / 살짝 / 활짝 / 살짝 |

자르기: `uv run --with pillow tools/make_walk_frames.py player enemy_mail ...` (1번 칸이 기본 그림이 되고, 예전 기본 그림은 `_old/<이름>.before-walk.png`).

## 16. 게임오버 그림 (2026-09-30 추가)

죽은 이유마다 다른 그림. 공통 문장(14장의 SCENE)을 앞에 붙였다. 예전 story_over(책상에 엎드려 잠듦)는 쓰지 않는다.

| 이유 | 파일 | 주제 문장 (요약) |
|---|---|---|
| 일반 적 | story_over_work.png | 서류 눈사태에 파묻힌 채 책상에 엎드림, 바닥의 휴대폰이 켜져 있음, 자정 시계 |
| 5층 옆 팀 팀장 | story_over_5f.png | 옆 팀 팀장이 어깨 너머로 모니터를 가리키며 서류 더미를 들고 있음, 모니터 테두리에 포스트잇 열 장 |
| 4층 주간 회의 | story_over_4f.png | 빈 회의실, 프로젝터 빔, 종이컵, 의자에서 고개 젖히고 잠듦 |
| 3층 인사팀장 | story_over_3f.png | 좁은 면담실, 인사팀장이 두꺼운 서류철을 읽고 김 과장은 의자에 푹 꺼져 있음 |
| 2층 감사팀장 | story_over_2f.png | 문서 상자 창고, 돋보기로 영수증을 뒤지고 감사팀장이 손전등을 비춤 |
| 1층 부장님 | story_over_1f.png | 고깃집, 빈 소주병 세 개, 부장님이 술을 따르고 휴대폰엔 부재중 표시 |

## 17. 굿엔딩 그림 (2026-09-30 추가)

| 장면 | 파일 | 주제 문장 (요약) |
|---|---|---|
| 굿엔딩 | story_home_good.png | 현관을 열자마자 깨어 있는 딸이 안겨 웃음, 뒤 식탁에 초 6개 켜진 홀케이크와 선물, 시계는 이른 저녁 |

## 18. 층 전용 물건과 믹스커피 (2026-09-30 추가)

스프라이트 공통 문장(SPRITE_HEAD) + 물건용 문장(얼굴·눈·팔다리 없음) 을 앞에 붙였다. 적(얼굴 있는 물건)과 헷갈리지 않게 물건에는 얼굴을 넣지 않는다. 가구는 모두 "위에서 비스듬히 내려다본 모습, 사람 없음". 회의 탁자는 4층 적(갈색 탁자 + 의자)과 다르게 밝은 회색에 의자 없이.

| 층 | 파일 | 주제 문장 (요약) |
|---|---|---|
| 5층 | prop_desk.png | 회색 사무 책상, 모니터·키보드·서류 더미 |
| 4층 | prop_table.png | 밝은 회색 긴 회의 탁자, 닫힌 노트북과 물병, 의자 없음 |
| 3층 | prop_coffee.png | 크림색·갈색 탕비실 커피 자판기, 버튼과 종이컵 |
| 3층 | item_coffee.png | 뜨거운 커피가 든 흰 종이컵 + 노란 믹스커피 봉지 (바닥 아이템) |
| 2층 | prop_copier.png | 회색 복합기, 옆 종이 받침과 튀어나온 종이 |
| 2층 | prop_cabinet.png | 회색 3단 서류 캐비닛, 맨 위 서랍이 살짝 열려 색색 폴더 |
| 1층 | prop_infodesk.png | 로비 안내 데스크, 나무 앞판·흰 상판, 종과 스탠드 |
| 1층 | prop_plant.png | 큰 회색 화분에 넓은 초록 잎 |

후처리: `tools/process_sprites.py` 가 `prop_` 이름은 정사각형으로 채우지 않고 비율 그대로 긴 쪽 384픽셀로 줄인다 (게임이 `FLOORS` 표의 w × h 로 그림).

## 19. 일시정지 버튼과 계단 휴대폰 장면 (2026-10-01 추가)

| 쓰는 곳 | 파일 | 주제 문장 (요약) |
|---|---|---|
| 화면 왼쪽 위, ? 버튼 옆의 일시정지 버튼 | pause.png | 도움말 단추(help.png)와 같은 노란 포스트잇에 굵은 검은 일시정지 막대 두 개. 스프라이트 공통 문장을 앞에 붙임 |
| 계단 장면의 휴대폰 | phone_hand.png | 김 과장의 눈으로 본 왼손(걷어 올린 흰 셔츠 소매)이 큰 검은 스마트폰을 세로로 든 모습. 화면은 글자 없는 흰 단색 (게임이 그 위에 알림과 문자를 씀) |
| 휴대폰 화면의 딸 사진 | avatar_kid.png | 새로 만들지 않았다. 굿엔딩 그림 story_home_good 에서 딸 얼굴을 오려 192픽셀로 줄임 |

후처리: `tools/process_sprites.py` 가 `phone_` 이름은 정사각형으로 채우지 않고 비율 그대로 긴 쪽 768픽셀로 줄인다 (화면에 크게 나오므로). phone_hand.png 는 654 × 768.

쓰지 않게 된 그림: 계단 이야기 그림 story_stair1~4 (14장) 는 휴대폰 장면으로 바뀌어 `assets/office/_old/` 로 옮겼다.

## 20. 스토리 A 그림 (2026-10-01 추가)

스토리를 "눈치 게임"으로 바꾸며 만든 그림이다. 장면은 14장의 공통 문장(SCENE), 아이콘은 스프라이트 공통 문장(SPRITE_HEAD, 물건은 ITEM 문장 추가)을 앞에 붙였다. 둘 다 `.omo/gpt_helpers.mjs` 에 들어 있다.

| 쓰는 곳 | 파일 | 주제 문장 (요약) |
|---|---|---|
| 시작 2 | story_stare.png | 저녁 6시 사무실. 가방을 들고 일어선 김 과장(식은땀 한 방울)을 주변 동료 모두가 같은 순간 고개를 돌려 동그란 눈으로 쳐다봄 |
| 결말 2 | story_exodus.png | 밤, 회사 건물 회전문으로 사람들이 우르르 쏟아져 나오며 환호, 종이가 날리고 창문 불이 층마다 꺼져 감. 맨 앞에서 두 팔을 든 부장님(대머리, 둥근 안경, 파란 넥타이), 옆에서 놀라 웃는 김 과장 |
| 결말 3 굿엔딩 | story_home_chicken.png | 작은 거실, 소파에서 닭다리를 들고 활짝 웃는 김 과장. 김이 나는 치킨 상자(무늬 없음)와 거품 맥주, TV 는 킥오프 직전 축구장(글자·점수판 없음), 벽시계는 12시 직전 |
| 결말 3 노말엔딩 | story_home_cold.png | 같은 거실, 조금 어둡게. 식은 치킨과 김 빠진 맥주, 지친 쓴웃음, TV 는 하프타임, 벽시계는 12시 넘음 |
| 휴대폰 사진: 회사 단톡방 | avatar_group.png | 겹친 말풍선 셋 (노랑, 흰색, 회색), 안에 점 세 개 |
| 휴대폰 사진: 치킨집 | avatar_chicken.png | 바삭한 닭다리 하나 |
| 휴대폰 사진: 친구 | avatar_friend.png | 거꾸로 쓴 빨간 모자, 회색 후드티, 손을 흔들며 활짝 웃는 친구 |

쓰지 않게 된 그림 (`assets/office/_old/daughter-story/` 로): story_gift, story_promise, story_clear, story_home, story_home_good, avatar_kid.
