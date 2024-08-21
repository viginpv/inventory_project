// App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AddStock from './assets/AddStock';
import ProductForm from './assets/ProductForm';
import ProductList from './assets/ProductList';
import RemoveStock from './assets/RemoveStock';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<ProductForm />} />
      <Route path="/addstock" element={<AddStock />} />
      <Route path="/productlist" element={<ProductList />} />
      <Route path="/removestock" element={<RemoveStock />} />
    </Routes>
  </Router>
);

export default App;
