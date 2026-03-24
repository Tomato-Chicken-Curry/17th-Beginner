const pwInput = document.getElementById('pwInput');
const msg = document.getElementById('msg');
const bar = document.getElementById('strengthBar');

pwInput.addEventListener('input', () => {
    const val = pwInput.value;
    let score = 0;

    // 1. 길이 체크
    if (val.length >= 8) { score++; document.getElementById('len').classList.add('valid'); }
    else { document.getElementById('len').classList.remove('valid'); }

    // 2. 숫자 포함 체크
    if (/[0-9]/.test(val)) { score++; document.getElementById('num').classList.add('valid'); }
    else { document.getElementById('num').classList.remove('valid'); }

    // 3. 특수문자 포함 체크
    if (/[!@#$%^&*]/.test(val)) { score++; document.getElementById('special').classList.add('valid'); }
    else { document.getElementById('special').classList.remove('valid'); }

    // 등급 표시
    const colors = ["#ff4b2b", "#ff9068", "#00ff41"];
    const labels = ["위험", "보통", "안전"];
    
    if (val.length === 0) {
        bar.style.width = "0%";
        msg.innerText = "비밀번호를 입력하세요.";
    } else {
        bar.style.width = (score + 1) * 25 + "%";
        bar.style.backgroundColor = colors[score] || colors[0];
        msg.innerText = `보안 등급: ${labels[score] || "위험"}`;
    }
});