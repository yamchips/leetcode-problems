# Assessment from DataAnnotation
import requests
from bs4 import BeautifulSoup

def decode_google_doc(url: str) -> None:
    # Fetch HTML from the Google Doc
    resp = requests.get(url)
    resp.raise_for_status()
    html = resp.text

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find the table
    tables = soup.find_all("table")
    if not tables:
        raise ValueError("No table found in the document.")

    # Take the first table
    table = tables[0]

    coords = []
    for row in table.find_all("tr")[1:]:  # skip header row
        cols = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
        if len(cols) < 3:
            continue
        x = int(cols[0])
        char = cols[1]
        y = int(cols[2])
        coords.append((x, y, char))

    if not coords:
        raise ValueError("No coordinates parsed from table.")

    # Grid bounds
    max_x = max(x for x, _, _ in coords)
    max_y = max(y for _, y, _ in coords)

    # Fill with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place chars
    for x, y, c in coords:
        grid[y][x] = c

    # Print
    for y in range(max_y, -1, -1):
        print("".join(grid[y]))


if __name__=='__main__':
    decode_google_doc('https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub')

# Example usage:
# decode_google_doc("https://docs.google.com/document/d/EXAMPLE_ID/pub")
