// ProductForm.jsx
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
        if (variantName && options) {
            setVariants([...variants, { name: variantName, options: options.split(',').map(option => option.trim()) }]);
            setVariantName('');
            setOptions('');
        } else {
            alert('Please provide both a variant name and options.');
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const productData = {
            ProductName: productName,
            variants: variants
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/products/create/', productData);
            alert('Product created successfully!');
            setProductName('');
            setVariants([]);
        } catch (error) {
            console.error('Error response:', error.response?.data || error.message);
            alert('Error creating product. Please check the logs for more details.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Product Name:</label>
                <input type="text" value={productName} onChange={handleProductNameChange} required />
            </div>
            <div>
                <label>Variant Name:</label>
                <input type="text" value={variantName} onChange={handleVariantNameChange} />
            </div>
            <div>
                <label>Options (comma separated):</label>
                <input type="text" value={options} onChange={handleOptionsChange} />
            </div>
            <button type="button" onClick={handleAddVariant}>Add Variant</button>

            <h3>Variants:</h3>
            <ul>
                {variants.map((variant, index) => (
                    <li key={index}>
                        {variant.name}: {variant.options.join(', ')}
                    </li>
                ))}
            </ul>

            <button type="submit">Create Product</button>
        </form>
    );
};

export default ProductForm;
