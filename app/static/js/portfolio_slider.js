document.addEventListener("DOMContentLoaded", function () {
    const slideContainers = ["cctv1", "cctv2", "papercup"];
    let slideIndexes = { cctv1: 0, cctv2: 0, papercup: 0 };

    function changeSlide(direction, slideId) {
        const slides = document.querySelectorAll(`#${slideId} .slide`);
        const totalSlides = slides.length;

        if (totalSlides === 0) return; // 슬라이드가 없으면 종료

        let currentIndex = slideIndexes[slideId];
        let nextIndex = (currentIndex + direction + totalSlides) % totalSlides;

        slides[currentIndex].classList.remove("active");
        slides[nextIndex].classList.add("active");

        slideIndexes[slideId] = nextIndex;
    }

    function autoSlide(slideId) {
        setInterval(() => {
            changeSlide(1, slideId);
        }, 5000);
    }

    slideContainers.forEach((slideId) => {
        const slides = document.querySelectorAll(`#${slideId} .slide`);
        if (slides.length > 0) {
            slides[0].classList.add("active"); // 첫 번째 슬라이드 활성화
            autoSlide(slideId);
        }

        // 왼쪽/오른쪽 버튼 이벤트 리스너 추가
        document.querySelector(`#${slideId} .prev`).addEventListener("click", function () {
            changeSlide(-1, slideId);
        });

        document.querySelector(`#${slideId} .next`).addEventListener("click", function () {
            changeSlide(1, slideId);
        });
    });
});
