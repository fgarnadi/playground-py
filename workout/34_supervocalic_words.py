def get_sv(file: str) -> set[str]:
    vowels = set("aiueo")
    
    return {word.strip() for word in open(file) if vowels < set(word)}
