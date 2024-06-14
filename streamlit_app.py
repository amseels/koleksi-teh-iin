import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Title of the app
st.title('📗 Koleksi Teh Iin')
st.write("#### organized by 1000 Lentera")

url = "https://docs.google.com/spreadsheets/d/1ERvukhKnlhVBA3-0SIX8hc-gMt0NWk3tW-3QJoR75Js/edit?gid=0#gid=0"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
books = conn.read(spreadsheet=url)

sort_options = ['Judul', 'Penulis']
sort_by = st.selectbox('Sort by', sort_options)
sorted_books = books.sort_values(by=sort_by)

# st.dataframe(books)

tab1, tab2 = st.tabs(["Seluruh Koleksi", "Cari Buku"])

# Gallery view
with tab1:
  st.write("### Book List")
  st.dataframe(sorted_books[['Judul', 'Penulis', 'Kategori']])  # Display book titles and authors in a table


# Book details view
with tab2:
    selected_book_title = st.selectbox("Cari Judul Buku", sorted_books['Judul'], index = None)

    if selected_book_title is not None:
      book = books[books['Judul'] == selected_book_title].iloc[0]
      # st.image(book['Foto'], width=200)
      st.subheader(book['Judul'])
      st.write(f"**Author:** {book['Penulis']}")
      st.write(book['Deskripsi'])