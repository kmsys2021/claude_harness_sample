"""
logger.py — 에이전트 실행 결과를 logs/ 폴더에 저장합니다.

사용법:
  python logger.py <시나리오_id> <결과_텍스트>

예시:
  python logger.py example_01 "작업 완료. 파일 3개 분석함."

또는 코드에서 직접 import 해서 사용:
  from logger import save_result
  save_result("example_01", result_text, success=True)
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def save_result(scenario_id: str, result: str, success: bool = True, notes: str = "") -> Path:
    """
    실행 결과를 logs/<날짜시간>_<시나리오id>.json 에 저장합니다.
    저장된 파일 경로를 반환합니다.
    """
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = logs_dir / f"{timestamp}_{scenario_id}.json"

    log_data = {
        "scenario_id": scenario_id,
        "timestamp": datetime.now().isoformat(),
        "success": success,
        "result": result,
        "notes": notes,
    }

    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

    print(f"로그 저장 완료: {log_path}")
    return log_path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("사용법: python logger.py <시나리오_id> <결과>")
        sys.exit(1)

    scenario_id = sys.argv[1]
    result_text = sys.argv[2]
    save_result(scenario_id, result_text)
