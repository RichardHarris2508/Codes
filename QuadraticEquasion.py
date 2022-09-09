n = 4800
a = 80

for i in range(-n, n+1):
    if i != 0 :
        if n%i==0:
            n1 = i 
            n2 = int(n/i)

            print(f"{n1} {n2}")

            g = max(n1, n2)
            s = min(n1, n2)

            print(f"{g} {s}\n")
            if g-s == a:
                print(f"{g} * {s}")