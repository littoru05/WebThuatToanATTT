// ==================== TAB SWITCHING ====================

function switchTab(tabName) {
    // Hide all tab contents
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));
    
    // Remove active from all buttons
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Mark button as active
    event.target.classList.add('active');
}

// ==================== PLAYFAIR CIPHER ====================

async function playfairEncrypt() {
    const plaintext = document.getElementById('playfair-plaintext').value;
    const key = document.getElementById('playfair-key').value;
    
    try {
        const response = await fetch('/api/playfair/encrypt', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ plaintext, key })
        });
        
        const data = await response.json();
        const resultDiv = document.getElementById('playfair-encrypt-result');
        
        if (data.success) {
            document.getElementById('playfair-encrypt-text').textContent = data.result;
            resultDiv.style.display = 'block';
            document.getElementById('playfair-ciphertext').value = data.result;
        } else {
            alert('Lỗi: ' + data.error);
        }
    } catch (e) {
        alert('Lỗi kết nối: ' + e.message);
    }
}

async function playfairDecrypt() {
    const ciphertext = document.getElementById('playfair-ciphertext').value;
    const key = document.getElementById('playfair-key').value;
    
    try {
        const response = await fetch('/api/playfair/decrypt', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ciphertext, key })
        });
        
        const data = await response.json();
        const resultDiv = document.getElementById('playfair-decrypt-result');
        
        if (data.success) {
            document.getElementById('playfair-decrypt-text').textContent = data.result;
            resultDiv.style.display = 'block';
        } else {
            alert('Lỗi: ' + data.error);
        }
    } catch (e) {
        alert('Lỗi kết nối: ' + e.message);
    }
}

// ==================== MODULO OPERATIONS ====================

async function apiCall(endpoint, params) {
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(params)
        });
        return await response.json();
    } catch (e) {
        alert('Lỗi kết nối: ' + e.message);
        return null;
    }
}

async function moduloEx1() {
    const a = parseInt(document.getElementById('mod-ex1-a').value);
    const m = parseInt(document.getElementById('mod-ex1-m').value);
    const n = parseInt(document.getElementById('mod-ex1-n').value);
    
    const data = await apiCall('/api/modulo/exercise1', { a, m, n });
    if (data && data.success) {
        document.getElementById('modulo-ex1-result').innerHTML = `<strong>Kết quả:</strong> ${data.formula}`;
        document.getElementById('modulo-ex1-result').style.display = 'block';
    }
}

async function moduloEx2() {
    const a = parseInt(document.getElementById('mod-ex2-a').value);
    const n = parseInt(document.getElementById('mod-ex2-n').value);
    
    const data = await apiCall('/api/modulo/exercise2', { a, n });
    if (data && data.success) {
        document.getElementById('modulo-ex2-result').innerHTML = `<strong>Kết quả:</strong> ${data.formula}`;
        document.getElementById('modulo-ex2-result').style.display = 'block';
    }
}

async function moduloEx3() {
    const a = parseInt(document.getElementById('mod-ex3-a').value);
    const m = parseInt(document.getElementById('mod-ex3-m').value);
    const n = parseInt(document.getElementById('mod-ex3-n').value);
    
    const data = await apiCall('/api/modulo/exercise3', { a, m, n });
    if (data && data.success) {
        document.getElementById('modulo-ex3-result').innerHTML = `<strong>Fermat Theorem:</strong> ${a}^${m} mod ${n} = ${data.result}`;
        document.getElementById('modulo-ex3-result').style.display = 'block';
    }
}

async function moduloEx4() {
    const n = parseInt(document.getElementById('mod-ex4-n').value);
    
    const data = await apiCall('/api/modulo/exercise4', { n });
    if (data && data.success) {
        document.getElementById('modulo-ex4-result').innerHTML = `<strong>Kết quả:</strong> ${data.formula}`;
        document.getElementById('modulo-ex4-result').style.display = 'block';
    }
}

async function moduloEx5() {
    const a = parseInt(document.getElementById('mod-ex5-a').value);
    const m = parseInt(document.getElementById('mod-ex5-m').value);
    const n = parseInt(document.getElementById('mod-ex5-n').value);
    
    const data = await apiCall('/api/modulo/exercise5', { a, m, n });
    if (data && data.success) {
        document.getElementById('modulo-ex5-result').innerHTML = `<strong>Euler Theorem:</strong> ${a}^${m} mod ${n} = ${data.result}`;
        document.getElementById('modulo-ex5-result').style.display = 'block';
    }
}

async function moduloEx6() {
    const a = parseInt(document.getElementById('mod-ex6-a').value);
    const k = parseInt(document.getElementById('mod-ex6-k').value);
    const n = parseInt(document.getElementById('mod-ex6-n').value);
    
    const data = await apiCall('/api/modulo/exercise6', { a, k, n });
    if (data && data.success) {
        document.getElementById('modulo-ex6-result').innerHTML = `<strong>CRT Power:</strong> ${a}^${k} mod ${n} = ${data.result}`;
        document.getElementById('modulo-ex6-result').style.display = 'block';
    }
}

async function moduloEx7() {
    const m1 = parseInt(document.getElementById('mod-ex7-m1').value);
    const a1 = parseInt(document.getElementById('mod-ex7-a1').value);
    const m2 = parseInt(document.getElementById('mod-ex7-m2').value);
    const a2 = parseInt(document.getElementById('mod-ex7-a2').value);
    const m3 = parseInt(document.getElementById('mod-ex7-m3').value);
    const a3 = parseInt(document.getElementById('mod-ex7-a3').value);
    
    const data = await apiCall('/api/modulo/exercise7', { m1, a1, m2, a2, m3, a3 });
    if (data && data.success) {
        document.getElementById('modulo-ex7-result').innerHTML = `<strong>Giải CRT:</strong> x = ${data.result}`;
        document.getElementById('modulo-ex7-result').style.display = 'block';
    }
}

async function moduloEx8() {
    const a = parseInt(document.getElementById('mod-ex8-a').value);
    const n = parseInt(document.getElementById('mod-ex8-n').value);
    
    const data = await apiCall('/api/modulo/exercise8', { a, n });
    if (data && data.success) {
        document.getElementById('modulo-ex8-result').innerHTML = `<strong>Kết quả:</strong> ${data.message}`;
        document.getElementById('modulo-ex8-result').style.display = 'block';
    }
}

async function moduloEx9() {
    const a = parseInt(document.getElementById('mod-ex9-a').value);
    const b = parseInt(document.getElementById('mod-ex9-b').value);
    const n = parseInt(document.getElementById('mod-ex9-n').value);
    
    const data = await apiCall('/api/modulo/exercise9', { a, b, n });
    if (data && data.success) {
        document.getElementById('modulo-ex9-result').innerHTML = `<strong>Kết quả:</strong> ${data.formula}`;
        document.getElementById('modulo-ex9-result').style.display = 'block';
    }
}

async function moduloEx10() {
    const a = parseInt(document.getElementById('mod-ex10-a').value);
    const b = parseInt(document.getElementById('mod-ex10-b').value);
    const x = parseInt(document.getElementById('mod-ex10-x').value);
    const y = parseInt(document.getElementById('mod-ex10-y').value);
    const n = parseInt(document.getElementById('mod-ex10-n').value);
    
    const data = await apiCall('/api/modulo/exercise10', { a, b, x, y, n });
    if (data && data.success) {
        const res = data.result;
        let html = `<strong>Kết quả:</strong><br>`;
        html += `A1 = (${a}*${x} + ${b}*${y}) mod ${n} = ${res.A1}<br>`;
        html += `A2 = (${a}*${x} - ${b}*${y}) mod ${n} = ${res.A2}<br>`;
        html += `A3 = (${a}*${x} * ${b}*${y}) mod ${n} = ${res.A3}<br>`;
        html += `A4 = (${b}*${y})^-1 mod ${n} = ${res.A4}<br>`;
        html += `A5 = (${a}*${x} / ${b}*${y}) mod ${n} = ${res.A5}`;
        document.getElementById('modulo-ex10-result').innerHTML = html;
        document.getElementById('modulo-ex10-result').style.display = 'block';
    }
}

// ==================== RSA ENCRYPTION ====================

async function rsaGenerate() {
    const p = parseInt(document.getElementById('rsa-p').value);
    const q = parseInt(document.getElementById('rsa-q').value);
    const e = parseInt(document.getElementById('rsa-e').value);
    
    const data = await apiCall('/api/rsa/generate', { p, q, e });
    if (data && data.success) {
        const n = data.n;
        const d = data.d;
        const phi = data.phi;
        
        document.getElementById('rsa-encrypt-e').value = e;
        document.getElementById('rsa-encrypt-n').value = n;
        document.getElementById('rsa-decrypt-d').value = d;
        document.getElementById('rsa-decrypt-n').value = n;
        
        let html = `<strong>Kết quả tạo khóa RSA:</strong><br>`;
        html += `n = p×q = ${p}×${q} = <strong>${n}</strong><br>`;
        html += `φ(n) = (p-1)×(q-1) = ${p-1}×${q-1} = <strong>${phi}</strong><br>`;
        html += `e = <strong>${e}</strong><br>`;
        html += `d = e^-1 mod φ(n) = <strong>${d}</strong><br><br>`;
        html += `<strong>Khóa Công Khai:</strong> {e=${e}, n=${n}}<br>`;
        html += `<strong>Khóa Riêng Tư:</strong> {d=${d}, n=${n}}`;
        
        document.getElementById('rsa-generate-result').innerHTML = html;
        document.getElementById('rsa-generate-result').style.display = 'block';
    }
}

async function rsaEncrypt() {
    const plaintext = document.getElementById('rsa-plaintext').value;
    const e = parseInt(document.getElementById('rsa-encrypt-e').value);
    const n = parseInt(document.getElementById('rsa-encrypt-n').value);
    
    const data = await apiCall('/api/rsa/encrypt', { plaintext, e, n });
    if (data && data.success) {
        document.getElementById('rsa-encrypt-result').innerHTML = `<strong>Mã hóa:</strong> M=${plaintext} → C = ${data.result}`;
        document.getElementById('rsa-encrypt-result').style.display = 'block';
        document.getElementById('rsa-ciphertext').value = data.result;
    }
}

async function rsaDecrypt() {
    const ciphertext = document.getElementById('rsa-ciphertext').value;
    const d = parseInt(document.getElementById('rsa-decrypt-d').value);
    const n = parseInt(document.getElementById('rsa-decrypt-n').value);
    
    const data = await apiCall('/api/rsa/decrypt', { ciphertext, d, n });
    if (data && data.success) {
        document.getElementById('rsa-decrypt-result').innerHTML = `<strong>Giải mã:</strong> C=${ciphertext} → M = ${data.result}`;
        document.getElementById('rsa-decrypt-result').style.display = 'block';
    }
}

// ==================== DES ENCRYPTION ====================

async function desEncrypt() {
    const plaintext = document.getElementById('des-plaintext').value;
    const key = document.getElementById('des-key').value;
    
    const data = await apiCall('/api/des/encrypt', { plaintext, key });
    if (data && data.success) {
        document.getElementById('des-encrypt-result').innerHTML = `<strong>Mã hóa DES:</strong><br>${data.result}`;
        document.getElementById('des-encrypt-result').style.display = 'block';
        document.getElementById('des-ciphertext').value = data.result;
    }
}

async function desDecrypt() {
    const ciphertext = document.getElementById('des-ciphertext').value;
    const key = document.getElementById('des-key').value;
    
    const data = await apiCall('/api/des/decrypt', { ciphertext, key });
    if (data && data.success) {
        document.getElementById('des-decrypt-result').innerHTML = `<strong>Giải mã DES:</strong><br>${data.result}`;
        document.getElementById('des-decrypt-result').style.display = 'block';
    }
}

// ==================== AES ENCRYPTION ====================

async function aesEncrypt() {
    const plaintext = document.getElementById('aes-plaintext').value;
    const key = document.getElementById('aes-key').value;
    
    const data = await apiCall('/api/aes/encrypt', { plaintext, key });
    if (data && data.success) {
        document.getElementById('aes-encrypt-result').innerHTML = `<strong>Mã hóa AES:</strong><br>${data.result}`;
        document.getElementById('aes-encrypt-result').style.display = 'block';
        document.getElementById('aes-ciphertext').value = data.result;
    }
}

async function aesDecrypt() {
    const ciphertext = document.getElementById('aes-ciphertext').value;
    const key = document.getElementById('aes-key').value;
    
    const data = await apiCall('/api/aes/decrypt', { ciphertext, key });
    if (data && data.success) {
        document.getElementById('aes-decrypt-result').innerHTML = `<strong>Giải mã AES:</strong><br>${data.result}`;
        document.getElementById('aes-decrypt-result').style.display = 'block';
    }
}
