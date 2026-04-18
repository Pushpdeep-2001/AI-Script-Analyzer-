def validate_script(script: str):
    if not script or len(script.strip()) < 20:
        raise ValueError("Script is too short")

    if "Title" not in script:
        raise ValueError("Script must include a Title")

    return True