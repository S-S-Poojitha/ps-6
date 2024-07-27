import streamlit as st

# URLs of the handcrafted furniture and art images
image_urls = [
    "https://cdn.shopify.com/s/files/1/0260/6111/products/Handcrafted_Wooden_Furniture.jpg",
    "https://cdn.shopify.com/s/files/1/0250/5922/products/Handcrafted_Chair_1.jpg",
    "https://cdn.pixabay.com/photo/2017/08/30/01/53/handmade-2688934_960_720.jpg",
    "https://cdn.pixabay.com/photo/2017/08/31/10/32/handcraft-2689458_960_720.jpg"
]

# Create a 2x2 grid of images
cols = st.columns(2)
for i in range(2):
    with cols[i]:
        st.image(image_urls[i * 2], width=300)
        st.image(image_urls[i * 2 + 1], width=300)
