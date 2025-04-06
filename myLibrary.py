# My personal library manager application
import streamlit as st
import json
import os

st.set_page_config(page_title="📚Library", layout='wide')
file_name = "books.json"

# to load data from json file
def load_books():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    else:
        return []
    
# to save data in json file
def save_book(library):
    with open(file_name, "w") as file:
        json.dump(library, file, indent=4)
        
#load books
library = load_books()

st.title("📚 Personal Library Manager")
st.write("👨‍💻Created by Danish Zohaib")

menu = ["Add Book", "Show All Books", "Search Book", "Delete Book"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Book":
    st.header("➕Please Add New Book")
    title = st.text_input("Please Enter Book Name:")
    author = st.text_input("Please Enter Author Name:")
    year = st.text_input("Please Enter Year:")
    
    if st.button("Add"):
        book = {"title":title, "author":author, "year":year}
        library.append(book)
        save_book(library)
        st.success("💾Book has been saved successfully")
        
elif choice == "Show All Books":
    st.subheader("All books in my library")
    if library:
        for i, book in enumerate(library):
            st.write(f"{i+1}. **{book['title']}** - {book['author']} ({book['year']})")
    else:
        st.info("❌There is no book saved in library")
        
elif choice == "Search Book":
    st.subheader("🔎Find a book here.")
    search_title = st.text_input("Please Enter Book Name:")
    if st.button("Search"):
        found = False
        for book in library:
            if book['title'].lower()==search_title.lower():
                st.success(f"Book Found: {book['title']} - {book['author']} ({book['year']})")
                found=True
                break
        if not found:
            st.error("Book not found in library")
            
elif choice == "Delete Book":
    st.subheader("📕Book you want to delete from library")
    delete_title = st.text_input("Enter Book Name:")
    if st.button("Delete Book"):
        for book in library:
            if book['title'].lower() == delete_title.lower():
                library.remove(book)
                save_book(library) # to update json
                st.success("Book Deleted Successfully")
                break
        else:
            st.error("Book not Found")
                