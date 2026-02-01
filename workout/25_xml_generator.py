def myxml(tag, content="", **kwargs) -> str:
    attr = " ".join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f"<{tag} {attr.strip()}>{content}</{tag}>"
