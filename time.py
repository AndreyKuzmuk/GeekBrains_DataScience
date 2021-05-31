TypedSec = int(input("Type some seconds: "))
hrs = TypedSec // 3600
minutes = TypedSec % 3600 // 60
sec = TypedSec % 60
print(f"{hrs:02d} : {minutes:1d} : {sec:02d}")
