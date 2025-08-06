# main.py
from schema import InterestInput
from agent import get_book_recommendations
from dotenv import load_dotenv
load_dotenv()
import os

def main():
    print("📚 Welcome to the AI Book Recommender!")
    interest = input("Enter your interest (e.g., science fiction, psychology, entrepreneurship): ")

    try:
        validated_input = InterestInput(interest=interest)
    except Exception as e:
        print(f"❌ Invalid input: {e}")
        return

    print("\n🔍 Searching for book recommendations...")
    books = get_book_recommendations(validated_input)

    print("\n✅ Recommended Books:")
    for i, book in enumerate(books, start=1):
        print(f"\n{i}. 📖 {book.title}")
        print(f"   ✍️ Author: {book.author}")
        print(f"   📝 {book.description}")

if __name__ == "__main__":
    main()
