import React, { useState } from 'react';
import axios from 'axios';

const RemoveStock = () => {
    const [subvariantId, setSubvariantId] = useState('');
    const [stock, setStock] = useState('');

    const handleSubvariantIdChange = (e) => setSubvariantId(e.target.value);
    const handleStockChange = (e) => setStock(e.target.value);

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post(`/api/stock/remove/${subvariantId}/`, { stock })
            .then(response => alert('Stock removed successfully!'))
            .catch(error => alert('Error removing stock.'));
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
                <label>Stock to Remove:</label>
                <input
                    type="number"
                    value={stock}
                    onChange={handleStockChange}
                    required
                />
            </div>
            <button type="submit">Remove Stock</button>
        </form>
    );
};

export default RemoveStock;

