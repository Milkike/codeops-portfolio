import PropTypes from 'prop-types';
import { Dish } from './Dish';

export function Menu({ dishes = [], selectedCategory = 'All' }) {
  // Filter menu items by selected category
  const filteredDishes = selectedCategory === 'All'
    ? dishes
    : dishes.filter((dish) => dish.category === selectedCategory);

  return (
    <section className="menu-section">
      <h2>Addis Eats Menu ({selectedCategory})</h2>

      {filteredDishes.length === 0 ? (
        <p className="empty-state">No dishes found in this category.</p>
      ) : (
        <div className="dish-grid">
          {filteredDishes.map((dish) => (
            <Dish
              key={dish.id}
              name={dish.name}
              price={dish.price}
              spicy={dish.spicy}
            />
          ))}
        </div>
      )}
    </section>
  );
}

Menu.propTypes = {
  dishes: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      category: PropTypes.string.isRequired,
      spicy: PropTypes.bool,
    })
  ).isRequired,
  selectedCategory: PropTypes.string,
};