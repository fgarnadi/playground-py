def passwd_to_dict(path: str = "/etc/passwd") -> dict:
    result = {}
    with open(path, "r") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                username, _, id, *_ = line.split(":")
                result[username] = id

    return result
