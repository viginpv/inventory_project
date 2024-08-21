import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import ProductForm from './assets/ProductForm';
import ProductList from './assets/ProductList';
import RemoveStock from './assets/RemoveStock';

const App = () => {
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/create-product">Create Product</Link>
                        </li>
                        <li>
                            <Link to="/products">Product List</Link>
                        </li>
                        <li>
                            <Link to="/manage-stock">Manage Stock</Link>
                        </li>
                    </ul>
                </nav>

                <Routes>
                    <Route path="/create-product" element={<ProductForm />} />
                    <Route path="/products" element={<ProductList />} />
                    <Route path="/manage-stock" element={<RemoveStock />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
