# soharang

This project provides a simple GUI tool to scrape posts from a specific Naver Cafe board, save them to an Excel file, and also export each post to a text file.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`
- `pandas`

Install dependencies with:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

1. Edit `cafe_manager.py` and update the `CAFE_URL` variable and parsing logic in `scrape_cafe()` to match the target board (e.g. the "정회원 신청해요" board in the "소하랑" cafe).
2. Run the script:

```bash
python cafe_manager.py
```

3. Click **Fetch Posts**. The program will attempt to download posts, store them in `members.xlsx`, and also write text files to `D:\CODING\txt`.

Note: Accessing Naver Cafe may require authentication or additional headers. This example does not handle login; you'll need to adjust the code if the board is not publicly accessible.
