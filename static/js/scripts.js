document.addEventListener("DOMContentLoaded", function() {
    var signInBtn = document.getElementById("signInBtn");
    var signUpBtn = document.getElementById("signUpBtn");
    var signInForm = document.getElementById("signInForm");
    var signUpForm = document.getElementById("signUpForm");
    var messageBlock = document.querySelector('.messages');
    const tabButtons = document.querySelectorAll(".tab-button");
    const tabContents = document.querySelectorAll(".tab-content");

    if (signInBtn && signUpBtn && signInForm && signUpForm) {
        signInBtn.addEventListener("click", function() {
            signInForm.classList.remove("hidden");
            signUpForm.classList.add("hidden");
            this.classList.add("active");
            signUpBtn.classList.remove("active");
        });

        signUpBtn.addEventListener("click", function() {
            signUpForm.classList.remove("hidden");
            signInForm.classList.add("hidden");
            this.classList.add("active");
            signInBtn.classList.remove("active");
        });
    } else {
        console.error("Не удалось найти элементы для обработки событий.");
    }

    function openTab(tabName) {
        tabContents.forEach(tab => tab.classList.remove("active"));
        tabButtons.forEach(button => button.classList.remove("active"));

        document.getElementById(tabName).classList.add("active");
        document.querySelector(`[data-tab="${tabName}"]`).classList.add("active");
    }

    tabButtons.forEach(button => {
        button.addEventListener("click", () => openTab(button.dataset.tab));
    });

    const getMoneyBtn = document.querySelector(".get-money-btn");
    if (getMoneyBtn) {
        getMoneyBtn.addEventListener("click", (event) => {
            event.preventDefault();  // Предотвращаем стандартную отправку формы
            fetch(getMoneyBtn.closest("form").action, {
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
                }
            }).then(response => {
                if (response.ok) {
                    location.reload();  // Обновляем страницу после успешного запроса
                }
            });
        });
    }

    if (messageBlock) {
        // Показываем блок с сообщениями
        messageBlock.style.display = "block";
        
        // Через 3 секунды скрываем сообщение
        setTimeout(function() {
            messageBlock.style.opacity = "0"; // Плавное исчезновение
        }, 3000); // 3000 миллисекунд = 3 секунды

        // Через 4 секунды скрываем полностью
        setTimeout(function() {
            messageBlock.style.display = "none";
        }, 4000); // 4000 миллисекунд = 4 секунды (после полного исчезновения)
    }
});