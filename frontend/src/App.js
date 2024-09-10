import React, { useState } from 'react';
import axios from 'axios';

const products = [
  "iPhone 15 Plus",
  "iPad 12.9",
  "MacBook Pro 16",
  "AirPods Pro",
  "Apple Watch Series 8",
  "iMac 27",
  "Mac Mini",
  "Apple TV 4K",
  "HomePod",
  "Magic Keyboard",
  "Magic Mouse",
  "Apple Pencil",
  "AirTag",
  "MagSafe Charger",
  "Pro Display XDR"
];

function App() {
  const [product, setProduct] = useState('');
  const [quantity, setQuantity] = useState(1);
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5001/order', { product, quantity });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Error placing order');
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '500px', margin: '0 auto' }}>
      <h1>E-Commerce Order System</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        <select 
          value={product} 
          onChange={(e) => setProduct(e.target.value)}
          style={{ padding: '5px' }}
        >
          <option value="">Select a product</option>
          {products.map((prod, index) => (
            <option key={index} value={prod}>{prod}</option>
          ))}
        </select>
        <input 
          type="number" 
          value={quantity} 
          onChange={(e) => setQuantity(e.target.value)}
          min="1"
          style={{ padding: '5px' }}
        />
        <button type="submit" style={{ padding: '10px', backgroundColor: '#4CAF50', color: 'white', border: 'none' }}>
          Place Order
        </button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;