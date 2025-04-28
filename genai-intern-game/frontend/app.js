async function submitGuess() {
  const guess = document.getElementById('guess').value;
  const response = await fetch('/api/v1/game/guess', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ seed: 'Rock', guess: guess })
  });
  const data = await response.json();
  document.getElementById('result').innerText = data.message;
}