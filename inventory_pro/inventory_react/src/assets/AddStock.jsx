import React, { useState } from 'react';
import axios from 'axios';

const AddStock = () => {
    const [subvariantId, setSubvariantId] = useState('');
    const [stock, setStock] = useState('');

    const handleSubvariantIdChange = (e) => setSubvariantId(e.target.value);
    const handleStockChange = (e) => setStock(e.target.value);

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post(`http://127.0.0.1:8000/api/stock/add/${subvariantId}/`, { stock })
            .then(response => alert('Stock added successfully!'))
            .catch(error => {
                console.error('Error details:', error);
                const errorMessage = error.response?.data?.error || error.message;
                alert('Error adding stock: ' + errorMessage);
            });
    };
    

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>SubVariant ID:</label>
                <input
                    type="text"
                    value={subvariantId}
                    onChange={handleSubvariantIdChange}
                    required
                />
            </div>
            <div>
                <label>Stock to Add:</label>
                <input
                    type="number"
                    value={stock}
                    onChange={handleStockChange}
                    required
                />
            </div>
            <button type="submit">Add Stock</button>
        </form>
    );
};

export default AddStock;
