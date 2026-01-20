k, m, n = map(int, input().split())

T = k + m + n

#cap ba me
p_aa_aa = (n / T) * ((n - 1) / (T - 1))
p_Aa_aa = (m / T) * (n / (T - 1)) + (n / T) * (m / (T - 1))
p_Aa_Aa = (m / T) * ((m - 1) / (T - 1))

con_lan = (
    p_aa_aa
    + 0.5 * p_Aa_aa
    + 0.25 * p_Aa_Aa
)

print(1 - con_lan)
