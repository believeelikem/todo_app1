
  // --- Password check logic ---
  const p1 = document.getElementById('p1');
  const p2 = document.getElementById('p2');
  const msg = document.getElementById('pwMatchMsg');
  const submitBtn = document.getElementById('submitBtn');

  function checkPasswords() {
    const v1 = p1.value;
    const v2 = p2.value;

    // No input yet
    if (!v1 && !v2) {
      msg.textContent = '';
      submitBtn.disabled = true;
      return;
    }

    // Too short
    if (v1.length < 8) {
      msg.textContent = 'Password must be at least 8 characters.';
      msg.style.color = '#c92a2a';
      submitBtn.disabled = true;
      return;
    }

    // Match check
    if (v1 === v2) {
      msg.textContent = 'Passwords match ✔️';
      msg.style.color = '#2b8a3e';
      submitBtn.disabled = false;
    } else {
      msg.textContent = 'Passwords do not match.';
      msg.style.color = '#c92a2a';
      submitBtn.disabled = true;
    }
  }

  p1.addEventListener('input', checkPasswords);
  p2.addEventListener('input', checkPasswords);

  // --- Show/hide password toggles ---
  function toggle(input, btn) {
    btn.addEventListener('click', () => {
      const type = input.type === 'password' ? 'text' : 'password';
      input.type = type;
      btn.textContent = type === 'text' ? '🙈' : '👁️';
    });
  }

  toggle(p1, document.getElementById('toggleP1'));
  toggle(p2, document.getElementById('toggleP2'));


