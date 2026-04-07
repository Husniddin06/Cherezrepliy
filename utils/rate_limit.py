import time
from collections import defaultdict
from typing import Dict, Tuple

_requests: Dict[int, list] = defaultdict(list)

RATE_LIMIT  = 5
RATE_WINDOW = 60


def check_rate_limit(user_id: int, bypass_ids: set = None) -> Tuple[bool, int]:
    if bypass_ids and user_id in bypass_ids:
        return True, 0
    now = time.time()
    _requests[user_id] = [ts for ts in _requests[user_id] if now - ts < RATE_WINDOW]
    if len(_requests[user_id]) >= RATE_LIMIT:
        wait = int(RATE_WINDOW - (now - _requests[user_id][0])) + 1
        return False, wait
    _requests[user_id].append(now)
    return True, 0


def reset_user(user_id: int):
    _requests.pop(user_id, None)


def get_request_count(user_id: int) -> int:
    now = time.time()
    return len([ts for ts in _requests.get(user_id, []) if now - ts < RATE_WINDOW])
