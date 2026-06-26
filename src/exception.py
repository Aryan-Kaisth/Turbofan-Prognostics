# src/exception.py
from __future__ import annotations
from types import TracebackType
from typing import TypeAlias

# Type alias for sys.exc_info()
ExcInfo: TypeAlias = tuple[type[BaseException], BaseException, TracebackType | None]

def get_detailed_error_message(
    error: BaseException,
    exc_info: ExcInfo,
) -> str:
    _, _, traceback = exc_info

    if traceback is None:
        return f"Reason: {error}"

    frame = traceback.tb_frame

    return (f"Failure in [{frame.f_code.co_filename}] at line [{traceback.tb_lineno}] | Reason: {error}")

class CustomException(Exception):
    def __init__(
        self,
        error: BaseException,
        exc_info: ExcInfo,
    ) -> None:
        super().__init__(str(error))
        self.error_message = get_detailed_error_message(error, exc_info)

    def __str__(self) -> str:
        return self.error_message