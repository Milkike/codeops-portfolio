/* ==========================================
   1. STATE MANAGEMENT & CONSTANTS
   ========================================== */
const state = {
  baseCurrency: 'ETB',
  rates: {},
  watchlist: [],
  history: [],
  selectedCurrency: '',
  lastAmount: '',
  status: { type: 'info', message: '' }
};

const STORAGE_KEY = 'etb_pro_app_state';
const API_URL = 'https://open.er-api.com/v6/latest/ETB';

/* ==========================================
   2. DOM ELEMENTS
   ========================================== */
const statusLine = document.getElementById('status-line');
const conversionForm = document.getElementById('conversion-form');
const amountInput = document.getElementById('amount-input');
const currencySelect = document.getElementById('currency-select');
const convertBtn = document.getElementById('convert-btn');
const resultBox = document.getElementById('conversion-result');
const addWatchlistBtn = document.getElementById('add-watchlist-btn');
const watchlistContainer = document.getElementById('watchlist-container');
const historyContainer = document.getElementById('history-container');
const clearHistoryBtn = document.getElementById('clear-history-btn');

/* ==========================================
   3. HELPER FUNCTIONS
   ========================================== */
function setStatus(type, message) {
  state.status = { type, message };
  statusLine.className = `status-message ${type}`;
  statusLine.querySelector('.status-text').textContent = message;
}

function saveStateToStorage() {
  const payload = {
    watchlist: state.watchlist,
    history: state.history,
    selectedCurrency: currencySelect.value,
    lastAmount: amountInput.value
  };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
}

function loadStateFromStorage() {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (!saved) return;

  try {
    const parsed = JSON.parse(saved);
    if (Array.isArray(parsed.watchlist)) state.watchlist = parsed.watchlist;
    if (Array.isArray(parsed.history)) state.history = parsed.history;
    if (parsed.selectedCurrency) state.selectedCurrency = parsed.selectedCurrency;
    if (parsed.lastAmount) {
      state.lastAmount = parsed.lastAmount;
      amountInput.value = parsed.lastAmount;
    }
  } catch (err) {
    console.error('Failed to load stored state:', err);
  }
}

/* ==========================================
   4. API DATA FETCHING
   ========================================== */
async function fetchRates() {
  setStatus('info', 'Updating exchange rates...');

  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`);

    const data = await response.json();
    if (data.result !== 'success' || !data.rates) throw new Error('Invalid rate data.');

    state.rates = data.rates;

    renderDropdown();
    renderWatchlist();
    renderHistory();

    // Enable interactive elements
    currencySelect.disabled = false;
    convertBtn.disabled = false;
    addWatchlistBtn.disabled = false;

    setStatus('success', 'Live exchange rates updated successfully.');
  } catch (error) {
    console.error('Fetch error:', error);
    setStatus('error', 'Unable to fetch exchange rates. Check connection.');
    currencySelect.innerHTML = '<option value="">Unavailable</option>';
  }
}

/* ==========================================
   5. UI RENDER FUNCTIONS
   ========================================== */
function renderDropdown() {
  currencySelect.innerHTML = '';
  const currencies = Object.keys(state.rates).sort();

  currencies.forEach(code => {
    const option = document.createElement('option');
    option.value = code;
    option.textContent = `${code}`;
    currencySelect.appendChild(option);
  });

  if (state.selectedCurrency && state.rates[state.selectedCurrency]) {
    currencySelect.value = state.selectedCurrency;
  } else if (state.rates['USD']) {
    currencySelect.value = 'USD';
  }
}

function renderWatchlist() {
  watchlistContainer.innerHTML = '';

  if (state.watchlist.length === 0) {
    watchlistContainer.innerHTML = '<li class="empty-list">Watchlist is currently empty.</li>';
    return;
  }

  state.watchlist.forEach(code => {
    const rate = state.rates[code];
    const li = document.createElement('li');
    li.className = 'list-item';
    const rateDisplay = rate ? rate.toFixed(4) : 'N/A';

    li.innerHTML = `
      <div class="list-info">
        <strong>1 ETB</strong> = <span>${rateDisplay} ${code}</span>
      </div>
      <button class="delete-btn" data-currency="${code}" title="Remove">&times;</button>
    `;

    watchlistContainer.appendChild(li);
  });
}

function renderHistory() {
  historyContainer.innerHTML = '';

  if (state.history.length === 0) {
    historyContainer.innerHTML = '<li class="empty-list">No conversion history available.</li>';
    return;
  }

  state.history.slice().reverse().forEach(item => {
    const li = document.createElement('li');
    li.className = 'list-item';
    li.innerHTML = `
      <div class="list-info">
        <div><strong>${item.amount} ETB</strong></div>
        <span>${item.result} ${item.currency}</span>
      </div>
      <span class="timestamp">${item.timestamp}</span>
    `;
    historyContainer.appendChild(li);
  });
}

/* ==========================================
   6. EVENT HANDLERS
   ========================================== */
function handleConversion(event) {
  event.preventDefault();

  const amount = parseFloat(amountInput.value);
  const targetCurrency = currencySelect.value;

  if (isNaN(amount) || amount <= 0) {
    setStatus('error', 'Please enter a valid amount greater than zero.');
    resultBox.classList.add('hidden');
    return;
  }

  const rate = state.rates[targetCurrency];
  if (!rate) {
    setStatus('error', `Exchange rate unavailable for ${targetCurrency}`);
    return;
  }

  const convertedTotal = (amount * rate).toFixed(2);

  resultBox.innerHTML = `
    ${convertedTotal} ${targetCurrency}
    <small>for ${amount.toLocaleString()} ETB (Rate: ${rate.toFixed(4)})</small>
  `;
  resultBox.classList.remove('hidden');

  // Record into history
  const historyRecord = {
    amount: amount.toLocaleString(),
    result: convertedTotal,
    currency: targetCurrency,
    timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  };

  state.history.push(historyRecord);
  renderHistory();

  setStatus('success', 'Conversion completed successfully.');
  saveStateToStorage();
}

function handleAddToWatchlist() {
  const targetCurrency = currencySelect.value;
  if (!targetCurrency) return;

  if (state.watchlist.includes(targetCurrency)) {
    setStatus('info', `${targetCurrency} is already in your watchlist.`);
    return;
  }

  state.watchlist.push(targetCurrency);
  renderWatchlist();
  saveStateToStorage();
  setStatus('success', `Added ${targetCurrency} to watchlist.`);
}

function handleWatchlistClick(event) {
  if (event.target.classList.contains('delete-btn')) {
    const currencyToRemove = event.target.getAttribute('data-currency');
    state.watchlist = state.watchlist.filter(code => code !== currencyToRemove);
    renderWatchlist();
    saveStateToStorage();
    setStatus('info', `Removed ${currencyToRemove} from watchlist.`);
  }
}

function handleClearHistory() {
  state.history = [];
  renderHistory();
  saveStateToStorage();
  setStatus('info', 'Conversion history cleared.');
}

/* ==========================================
   7. INITIALIZATION
   ========================================== */
function init() {
  loadStateFromStorage();

  conversionForm.addEventListener('submit', handleConversion);
  addWatchlistBtn.addEventListener('click', handleAddToWatchlist);
  watchlistContainer.addEventListener('click', handleWatchlistClick);
  clearHistoryBtn.addEventListener('click', handleClearHistory);

  amountInput.addEventListener('input', saveStateToStorage);
  currencySelect.addEventListener('change', saveStateToStorage);

  fetchRates();
}

document.addEventListener('DOMContentLoaded', init);