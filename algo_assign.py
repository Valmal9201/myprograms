def egcd(a, b): #O(log(min(a,b)))
    if b == 0:
        return abs(a), (1 if a >= 0 else -1), 0
    g, x1, y1 = egcd(b, a % b) z #O(log(min(b,a % b)))
    return g, y1, x1 - (a // b) * y1 # ax+by=g

def solve(a, b, c):
    if a == 0 and b == 0: #O(1)
        if c == 0: #O(1)
            return "infinite" # 0x + 0y = 4
        else:
            return None
    g, xg, yg = egcd(a, b) # O(log(min(a, b)))
    if c % g != 0: # O(1)
        return None
    k = c // g # O(1)
    x0, y0 = xg * k, yg * k # O(1)
    final = (f"({x0}t, {y0}t)") # O(log(n))
    return final

# Example
ans = solve(47, 30, 1) 
print(ans)