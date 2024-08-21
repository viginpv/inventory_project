import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('/api/products/')
            .then(response => setProducts(response.data))
            .catch(error => alert('Error fetching products.'));
    }, []);

    return (
        <div>
            <h2>Product List</h2>
            <ul>
                {products.map(product => (
                    <li key={product.id}>
                        {product.ProductName} - Variants: {product.variants.map(v => `${v.name}`).join(', ')}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
