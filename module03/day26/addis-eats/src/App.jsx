import Dish from "./Dish.jsx";
import Header from "./Header.jsx";

const menu = [
  { id: 1, name: "Doro Wat", price: 240 },
  { id: 2, name: "Shiro", price: 120 },
  { id: 3, name: "Tibs", price: 280 },
];

function App() {
  return (
    <main>
      <Header />

      <section>
        {menu.map((dish) => (
          <Dish
            key={dish.id}
            name={dish.name}
            price={dish.price}
          />
        ))}
      </section>
    </main>
  );
}

export default App;