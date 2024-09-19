document.addEventListener('DOMContentLoaded', function() {
    const usernameInput = document.getElementById('username');
    let clickedOnce = 0;
    let previousDirection = null;
    let currentX = 0;  // X축 위치 저장
    let currentY = 0;  // Y축 위치 저장

    // 난수를 뽑아 중복되지 않도록 배열에서 선택
    function getRandomDirection(excludeDirection) {
        const availableDirections = [1, 2, 3, 4].filter(d => d !== excludeDirection);  // 이전 방향 제외
        const randomIndex = Math.floor(Math.random() * availableDirections.length);
        return availableDirections[randomIndex];
    }

    // 애니메이션 적용 및 위치 누적
    function applyAnimation(direction) {
        switch (direction) {
            case 1:  // 오른쪽으로 이동
                currentX += 400;
                usernameInput.style.transform = `translate(${currentX}px, ${currentY}px)`;
                break;
            case 2:  // 왼쪽으로 이동
                currentX -= 400;
                usernameInput.style.transform = `translate(${currentX}px, ${currentY}px)`;
                break;
            case 3:  // 위로 이동
                currentY -= 200;
                usernameInput.style.transform = `translate(${currentX}px, ${currentY}px)`;
                break;
            case 4:  // 아래로 이동
                currentY += 300;
                usernameInput.style.transform = `translate(${currentX}px, ${currentY}px)`;
                break;
        }
    }

    // username 입력창이 클릭될 때 애니메이션 실행
    usernameInput.addEventListener('focus', function() {
        if (clickedOnce < 2) {  // 두 번만 실행되도록 제어
            clickedOnce++;

            // 포커스를 해제하고, 새로운 방향으로 애니메이션 실행
            setTimeout(function() {
                usernameInput.blur();  // 포커스 해제

                // 첫 번째 클릭 시 난수 선택, 두 번째는 중복되지 않는 방향으로
                const direction = getRandomDirection(previousDirection);
                previousDirection = direction;  // 이전 방향 저장
                applyAnimation(direction);  // 애니메이션 적용
            }, 100);  // 100ms 후 애니메이션 적용
        }
    });
});
