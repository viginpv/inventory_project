import React, { useState } from 'react';
import axios from 'axios';

const ProductForm = () => {
    const [productName, setProductName] = useState('');
    const [variants, setVariants] = useState([]);
    const [variantName, setVariantName] = useState('');
    const [options, setOptions] = useState('');

    const handleProductNameChange = (e) => setProductName(e.target.value);

    const handleVariantNameChange = (e) => setVariantName(e.target.value);

    const handleOptionsChange = (e) => setOptions(e.target.value);

    const handleAddVariant = () => {
        setVariants([
            ...variants,
            { name: variantName, options: options.split(',').map(option => option.trim()) }
        ]);
        setVariantName('');
        setOptions('');
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/products/create/', {
            ProductName: productName,
            variants: variants
        })
        .then(response => alert('Product created successfully!'))
        .catch(error => alert('Error creating product.'));
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Product Name:</label>
                <input
                    type="text"
                    value={productName}
                    onChange={handleProductNameChange}
                    required
                />
            </div>
            <div>
                <label>Variant Name:</label>
                <input
                    type="text"
                    value={variantName}
                    onChange={handleVariantNameChange}
                />
            </div>
            <div>
                <label>Options (comma separated):</label>
                <input
                    type="text"
                    value={options}
                    onChange={handleOptionsChange}
                />
            </div>
            <button type="button" onClick={handleAddVariant}>Add Variant</button>
            <button type="submit">Create Product</button>
        </form>
    );
};

export default ProductForm;
