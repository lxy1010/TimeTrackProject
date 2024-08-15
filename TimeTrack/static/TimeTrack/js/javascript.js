let timerId = null;
let minutes = 25;
let seconds = 0;
let isRunning = false;

function updateDisplay() {
    const totalSeconds = minutes * 60 + seconds;
    const hours = Math.floor(totalSeconds / 3600);
    minutes = Math.floor((totalSeconds - (hours * 3600)) / 60);
    seconds = totalSeconds % 60;

    document.getElementById('timeDisplay').textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

    if (seconds === 0 && minutes === 0) {
        stopTimer();
        alert('Pomodoro完成!');
    }
}

function startTimer() {
    if (!isRunning) {
        isRunning = true;
        document.getElementById('startBtn').disabled = true;
        document.getElementById('pauseBtn').disabled = false;

        timerId = setInterval(function() {
            seconds--;
            updateDisplay();

            if (seconds < 0) {
                seconds = 59;
                minutes--;
            }
        }, 1000);
    }
}

function pauseTimer() {
    if (isRunning) {
        isRunning = false;
        clearInterval(timerId);
        document.getElementById('startBtn').disabled = false;
        document.getElementById('pauseBtn').disabled = true;
    }
}

function stopTimer() {
    pauseTimer();
    minutes = 25;
    seconds = 0;
    updateDisplay();
    document.getElementById('resetBtn').disabled = false;
}

console.log(document.getElementById('startBtn'))
document.getElementById('startBtn').addEventListener('click', startTimer);
document.getElementById('pauseBtn').addEventListener('click', pauseTimer);
document.getElementById('resetBtn').addEventListener('click', function() {
    stopTimer();
    document.getElementById('resetBtn').disabled = true;
});

// 初始化显示
updateDisplay();


// -----------------------------------------------------------

var toastElList = [].slice.call(document.querySelectorAll('.toast'));
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl, option);
});

toastList.forEach(toast => toast.show());