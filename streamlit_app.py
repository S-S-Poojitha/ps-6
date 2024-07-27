import streamlit as st
import requests
import json

st.title('Online Store')

# Function to fetch all products
def fetch_products():
    response = requests.get('http://localhost:5000/products')
    return response.json()

# Function to fetch a single product
def fetch_product(product_id):
    response = requests.get(f'http://localhost:5000/product/{product_id}')
    return response.json()

# Function to add a new product
def add_product(product):
    response = requests.post('http://localhost:5000/product', json=product)
    return response.status_code

# Sidebar for product addition
with st.sidebar:
    st.header('Add New Product')
    name = st.text_input('Name')
    description = st.text_area('Description')
    price = st.number_input('Price', min_value=0)
    available = st.checkbox('Available', value=True)
    image = st.text_input('Image URL')
    manufacturer_location = st.text_input('Manufacturer Location')
    manufacturing_video = st.text_input('Manufacturing Video URL')
    videos = st.text_area('Video URLs (comma separated)').split(',')

    if st.button('Add Product'):
        product = {
            'name': name,
            'description': description,
            'price': price,
            'available': available,
            'image': image,
            'manufacturerLocation': manufacturer_location,
            'manufacturingVideo': manufacturing_video,
            'videos': videos
        }
        status_code = add_product(product)
        if status_code == 201:
            st.success('Product added successfully!')
        else:
            st.error('Failed to add product.')

# Main section to display products
products = fetch_products()
for product in products:
    st.header(product['name'])
    st.image(product['image'])
    st.write(f"Price: ${product['price']}")
    st.write(product['description'])
    st.write(f"Availability: {'In Stock' if product['available'] else 'Out of Stock'}")
    st.write(f"Manufacturer Location: {product['manufacturerLocation']}")
    st.video(product['manufacturingVideo'])
    
    if st.button(f"Show More Videos for {product['name']}"):
        for video in product['videos']:
            st.video(video)

