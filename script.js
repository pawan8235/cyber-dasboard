const passwordForm = document.getElementById('passwordForm');
const passwordInput = document.getElementById('passwordInput');
const passwordResult = document.getElementById('passwordResult');

// URL form aur result elements ko select karna
const urlForm = document.getElementById('urlForm');
const urlInput = document.getElementById('urlInput');
const urlResult = document.getElementById('urlResult');

// Password Strength Analyzer Event Listener
passwordForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Page refresh hone se roknay ke liye
    const pwd = passwordInput.value;
    
    let strengthText = "";
    let colorCode = "";

    // Password validation logic
    if (pwd.length >= 8 && /[A-Z]/.test(pwd) && /[0-9]/.test(pwd) && /[^A-Za-z0-9]/.test(pwd)) {
        strengthText = "Strong 🛡️ (Secure Password)";
        colorCode = "#3fb950"; // Green
    } else if (pwd.length >= 6) {
        strengthText = "Moderate ⚠️ (Needs Special Characters/Numbers)";
        colorCode = "#d29922"; // Yellow
    } else {
        strengthText = "Weak ❌ (Too short, make it 8+ chars)";
        colorCode = "#f85149"; // Red
    }

    // Screen par result show karna
    passwordResult.style.color = colorCode;
    passwordResult.innerHTML = `Analysis: <strong>${strengthText}</strong>`;
});

// URL Safety Checker Event Listener
urlForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const url = urlInput.value.trim();

    let urlStatus = "Safe to visit ✅ (HTTPS Enabled)";
    let color = "#3fb950";

    if (!url.startsWith("https://")) {
        urlStatus = "Warning ⚠️: Insecure HTTP protocol detected!";
        color = "#d29922";
    }

    urlResult.style.color = color;
    urlResult.innerHTML = `Status: <strong>${urlStatus}</strong>`;
});