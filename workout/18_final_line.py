def get_final_line(path: str) -> str:
   final = ""
   for line in open(path, "r"):
       final = line

   return final.strip()
