import PropTypes from 'prop-types';
import { Card } from './Card';

export function Dish({ name, price, currency = 'ETB', spicy }) {
  // Guard non-booleans explicitly so truthy/falsy non-booleans don't render unexpectedly
  const isSpicy = Boolean(spicy);

  return (
    <Card>
      <div className="dish-header">
        <h3>{name}</h3>
        {isSpicy && <span className="badge spicy-badge">🌶️ Spicy</span>}
      </div>
      <p className="price">
        {price} {currency}
      </p>
    </Card>
  );
}

Dish.propTypes = {
  name: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
  currency: PropTypes.string,
  spicy: PropTypes.bool,
};