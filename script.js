window.location.href = 'https://jdh-dev-993.github.io/Svetlana/im/not_f';
console.log('Сайт запущен!');
console.log('The site was created with the support of Murka Technologies');
function copyText(text) {
  navigator.clipboard.writeText(text)
    .then(() => showNotification())
    .catch(err => console.error("Ошибка копирования: ", err));
}
function showNotification() {
  const notification = document.getElementById("copyNotification");
  notification.style.display = "block";
  setTimeout(() => {
    notification.style.display = "none";
  }, 2500);
}

function err() {
alert("Данная страница в процессе разработки! Вы не можете на неё зайти")
}

function showBlock() {
      document.getElementById('overlay').style.display = 'flex';
}

function hideBlock() {
      document.getElementById('overlay').style.display = 'none';
}
