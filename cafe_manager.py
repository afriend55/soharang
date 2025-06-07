import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


class CafeManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Naver Cafe Manager")

        self.fetch_button = tk.Button(master, text="Fetch Posts", command=self.fetch_posts)
        self.fetch_button.pack(padx=10, pady=10)

    def fetch_posts(self):
        try:
            posts = self.scrape_cafe()
            if posts:
                self.save_to_excel(posts)
                self.save_to_txt(posts)
                messagebox.showinfo("Success", f"Fetched {len(posts)} posts.")
            else:
                messagebox.showinfo("Info", "No posts found or unable to fetch posts.")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def scrape_cafe(self):
        """Scrape posts from Naver Cafe.

        This example uses placeholder URLs and parsing logic. You must
        update `CAFE_URL` with the actual board URL and adjust the
        BeautifulSoup selectors based on the page structure.
        """
        CAFE_URL = "https://cafe.naver.com/soharang"  # Replace with real URL
        response = requests.get(CAFE_URL)
        if not response.ok:
            return []
        soup = BeautifulSoup(response.text, "html.parser")
        # Example parsing logic - adjust as needed for actual page structure
        post_elems = soup.select("div.board_list li a.article")
        posts = []
        for elem in post_elems:
            title = elem.get_text(strip=True)
            link = elem.get("href")
            posts.append({"title": title, "link": link})
        return posts

    def save_to_excel(self, posts):
        df = pd.DataFrame(posts)
        df.to_excel("members.xlsx", index=False)

    def save_to_txt(self, posts):
        folder = r"D:\\CODING\\txt"
        os.makedirs(folder, exist_ok=True)
        for i, post in enumerate(posts, start=1):
            filename = os.path.join(folder, f"post_{i}.txt")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(post["title"] + "\n" + post.get("link", ""))


if __name__ == "__main__":
    root = tk.Tk()
    app = CafeManagerApp(root)
    root.mainloop()
