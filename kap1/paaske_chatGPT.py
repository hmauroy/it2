def calculate_easter(year):
    # Gaussian algorithm constants
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31  # Month of Easter
    day = ((h + l - 7 * m + 114) % 31) + 1  # Day of Easter

    return day, month


# Calculate Easter for the year 2024
for year in range(2000,2025):
    easter = calculate_easter(year)
    print(f"Easter in {year} is on: {easter[0]}.{easter[1]}")
