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

# Inject custom CSS for layout and image styling
st.markdown(
    """
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(2, 1fr);
        gap: 10px;
        padding: 10px;
    }
    .grid-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 2px solid #ddd;
        border-radius: 8px;
        background-color: #f9f9f9;
        padding: 10px;
    }
    .grid-item img {
        max-height: 300px; /* Set a fixed maximum height */
        width: auto; /* Maintain aspect ratio */
        border: 2px solid #ddd;
        border-radius: 8px;
    }
    .product-info {
        text-align: center;
    }
    .product-info button {
        padding: 10px 20px;
        font-size: 16px;
        margin-top: 10px;
        cursor: pointer;
        border: none;
        background-color: #007bff;
        color: white;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a grid layout with 4 equal parts
st.markdown('<div class="grid-container">', unsafe_allow_html=True)

for i in range(4):
    st.markdown(f"""
    <div class="grid-item">
        <img src="{image_urls[i]}" alt="Product Image">
        <div class="product-info">
            <p><strong>Name:</strong> {names[i]}</p>
            <p><strong>Price:</strong> {prices[i]}</p>
            <button>Add to Cart</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
