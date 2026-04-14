# Agent Harness

Claude Code를 에이전트로 사용하는 작업 실행 템플릿입니다.

```
나(사용자)             → 시나리오 작성  →  scenarios/
Claude Code(에이전트)  → 시나리오 실행
→ 결과                 → 로그 저장     →  logs/
```

API 키 없음. 설치 없음. Claude.ai Pro 구독만 있으면 됩니다.

---

## 요구사항

- Claude.ai Pro 구독
- Python 3.8+

## 폴더 구조

```
Harness_sample/
├── scenarios/           ← 에이전트 작업 정의 (여기만 수정)
│   └── example.yaml
├── logs/                ← 실행 결과 자동 저장 (건드리지 않음)
│   └── .gitkeep
├── logger.py            ← 결과 저장 헬퍼 (그대로 사용)
└── README.md            ← 이 파일
```

---

## 시작하기 (3단계)

### 1단계 — 시나리오 정의

`scenarios/` 폴더에 YAML 파일을 만들어 에이전트가 할 일을 씁니다.

```yaml
scenario_id: "내_첫_작업"
task: |
  README.md 파일을 읽고 이 프로젝트가 무엇인지 한 문장으로 요약해줘.
success_criteria:
  - "요약이 한 문장인가?"
```

### 2단계 — Claude Code에서 실행

Claude Code 채팅창에서 이렇게 말하면 됩니다:

```
scenarios/내_파일.yaml 시나리오를 실행해줘
```

### 3단계 — 결과 저장 (선택)

```bash
python logger.py 내_첫_작업 "요약 완료: 이 프로젝트는 ..."
```

결과가 `logs/` 폴더에 JSON으로 저장됩니다.

---

## 새 프로젝트에 적용

1. 이 폴더 전체를 복사
2. `scenarios/example.yaml`을 복사해서 내용 수정
3. `logs/` 폴더는 `.gitkeep`만 남기고 비우기
