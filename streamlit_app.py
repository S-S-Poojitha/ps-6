import streamlit as st

# URLs of the handcrafted furniture and art images
image_urls = [
    "https://content.jdmagicbox.com/comp/def_content/handicraft-item-dealers/d189618293-handicraft-item-dealers-4-q52mt.jpg",
    "https://content.jdmagicbox.com/comp/ahmedabad/c8/079pxx79.xx79.101225102212.k3c8/catalogue/toran-art-satellite-ahmedabad-handicraft-item-manufacturers-26qy14nsz2.jpg",
    "https://th-i.thgim.com/public/incoming/ikjulw/article67682621.ece/alternates/FREE_1200/03Tribals.jpg",
    "https://m.media-amazon.com/images/I/61D83qJYjDL._AC_UF894,1000_QL80_.jpg"
]

# Updated prices in Indian Rupees
prices = [
    "₹1,500",
    "₹750",
    "₹1,200",
    "₹900"
]

# Names for the products
names = [
    "Handcrafted Vase",
    "Decorative Toran",
    "Tribal Art",
    "Handcrafted Table"
]

# Inject custom CSS for spacing
st.markdown(
    """
    <style>
    .image-container {
        margin-bottom: 20px;
    }
    .image-container img {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a 2x2 grid of images with prices and names
cols = st.columns(2)
for i in range(2):
    with cols[i]:
        st.markdown(f'<div class="image-container"><img src="{image_urls[i * 2]}" width="300"></div>', unsafe_allow_html=True)
        st.write(f"**Name:** {names[i * 2]}")
        st.write(f"**Price:** {prices[i * 2]}")
        st.button("Add to Cart", key=f"btn{i * 2}")
        
        st.markdown(f'<div class="image-container"><img src="{image_urls[i * 2 + 1]}" width="300"></div>', unsafe_allow_html=True)
        st.write(f"**Name:** {names[i * 2 + 1]}")
        st.write(f"**Price:** {prices[i * 2 + 1]}")
        st.button("Add to Cart", key=f"btn{i * 2 + 1}")
