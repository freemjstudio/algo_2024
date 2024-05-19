from __future__ import annotations
from functools import wraps
from inspect import iscoroutinefunction
from typing import Callable, ParamSpec, TypeVar

__all__: list[str] = ["run_once"]

_UnSet = object()
_P = ParamSpec("_P") # 함수 매개변수 타입 캡처
_T = TypeVar("_T")

def run_once(f: Callable[_P, _T]) -> Callable[_P, _T]:
    # 비동기 함수 처리
    if iscoroutinefunction(f):
        @wraps(f)
        async def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            v:object = _UnSet
            if v is _UnSet:
                v: Any = await f(*args, **kwargs)
    else:
        @wraps(f)
        def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            v:object = _UnSet
            if v is _UnSet:
                v: _T = f(*args, **kwargs)
            return v

    return wrapped