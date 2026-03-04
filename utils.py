def normalize_name(name: str) -> str:
    """Normalize user-provided name."""
    name = (name or "").strip()
    return name if name else "world"

def format_greeting(name: str, caps: bool = False) -> str:
    """Return a greeting string."""
    msg = f"Hello, {name}!"
    return msg.upper() if caps else msg
