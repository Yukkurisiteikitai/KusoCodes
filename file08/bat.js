const divup = document.createElement('div');
divup.classList.add('spinner');
document.body.appendChild(divup);

// CSSスタイルの追加
const style = document.createElement('style');
style.textContent = `
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
    }
    .spinner {
        border: 8px solid #f3f3f3; /* 背景色 */
        border-top: 8px solid #3498db; /* スピナーの色 */
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
        display: none; /* 初期状態で非表示 */
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
`;
document.head.appendChild(style);

// JavaScriptのコー
function showSpinner() {
    document.querySelector('.spinner').style.display = 'block';
}

function hideSpinner() {
    document.querySelector('.spinner').style.display = 'none';
}

// スピナーを表示
showSpinner();

// スピナーを隠すタイミングで呼び出す
setTimeout(hideSpinner, 5000); // 5秒後にスピナーを隠す
