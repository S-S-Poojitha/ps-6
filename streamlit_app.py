import streamlit as st

# URLs of the handcrafted furniture and art images
image_urls = [
    "https://content.jdmagicbox.com/comp/def_content/handicraft-item-dealers/d189618293-handicraft-item-dealers-4-q52mt.jpg",
    "https://content.jdmagicbox.com/comp/ahmedabad/c8/079pxx79.xx79.101225102212.k3c8/catalogue/toran-art-satellite-ahmedabad-handicraft-item-manufacturers-26qy14nsz2.jpg",
    "https://th-i.thgim.com/public/incoming/ikjulw/article67682621.ece/alternates/FREE_1200/03Tribals.jpg",
    "https://m.media-amazon.com/images/I/61D83qJYjDL._AC_UF894,1000_QL80_.jpg"
]

# Create a 2x2 grid of images
cols = st.columns(2)
for i in range(2):
    with cols[i]:
        st.image(image_urls[i * 2], width=300)
        st.image(image_urls[i * 2 + 1], width=300)
