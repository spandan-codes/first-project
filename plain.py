red={
    "1":"one",
"2":"two",
"3":"three",
"4":"four",
"5":"five",
"6":"six",
"7":"seven",
"8":"eight",
"9":"nine",
"10":"ten"
}
rock=input("anything ")
h=""
for r in rock:
    h+=red.get(r,r)
print(h)
