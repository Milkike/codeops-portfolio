import { dishes } from './data';
import { Menu } from './Menu';

export default function App() {
  return (
    <main className="app-container">
      <h1>Addis Eats</h1>
      {/* Change selectedCategory to 'Main', 'Breakfast', 'Beverage', or 'Dessert' to test filtering */}
      <Menu dishes={dishes} selectedCategory="Main" />
    </main>
  );
}