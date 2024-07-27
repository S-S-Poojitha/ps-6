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

# Inject Bootstrap CSS and custom styling
st.markdown(
    """
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
    .card-img-top {
        max-height: 200px; /* Set a fixed maximum height */
        width: auto; /* Maintain aspect ratio */
        object-fit: cover; /* Ensure images fit properly */
    }
    .card {
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 20px;
    }
    .card-body {
        text-align: center;
    }
    .btn-primary {
        background-color: #007bff;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a 2x2 grid layout using Bootstrap
st.markdown('<div class="container mt-4"><div class="row">', unsafe_allow_html=True)

for i in range(4):
    st.markdown(f"""
    <div class="col-md-6 col-lg-3 mb-4">
        <div class="card">
            <img src="{image_urls[i]}" class="card-img-top" alt="Product Image">
            <div class="card-body">
                <h5 class="card-title">{names[i]}</h5>
                <p class="card-text">{prices[i]}</p>
                <a href="#" class="btn btn-primary">Add to Cart</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)
