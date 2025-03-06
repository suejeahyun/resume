document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        document.querySelectorAll(".btn").forEach(btn => {
            btn.classList.add("show");
        });
    }, 2000); // 2초 후 실행
});
