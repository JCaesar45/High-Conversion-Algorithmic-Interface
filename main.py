import warnings
from typing import List, Tuple, Any, Optional

SENTINEL = object()

def deprecated_decorator(func):
    def wrapper(*args, **kwargs):
        warnings.warn(
            f"Call to deprecated function {func.__name__}.",
            DeprecationWarning,
            stacklevel=2
        )
        return func(*args, **kwargs)
    return wrapper

def process_mutable_data(data_list: List[int]) -> List[int]:
    """Use list when data requires modification (appending/removing)."""
    data_list.append(0)
    return data_list

def process_immutable_data(data_tuple: Tuple[int, ...]) -> Tuple[int, ...]:
    """Use tuple for fixed collections, ensuring data integrity and memory efficiency."""
    return data_tuple

@deprecated_decorator
def legacy_fetch_item(identifier: str) -> Any:
    """Deprecated: Use fetch_item_with_sentinel instead."""
    return fetch_item_with_sentinel(identifier)

def fetch_item_with_sentinel(identifier: str) -> Any:
    """
    Return SENTINEL for 'not found' to distinguish from None.
    Raise exceptions only for truly exceptional, unexpected conditions.
    """
    database_mock = {"item_1": "data"}
    
    if not isinstance(identifier, str):
        raise TypeError("Identifier must be a string.")
        
    return database_mock.get(identifier, SENTINEL)
