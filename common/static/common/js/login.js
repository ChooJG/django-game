document.addEventListener('DOMContentLoaded', function() {
    // username 입력창 요소 가져오기
    const usernameInput = document.getElementById('username');

    // username 입력창이 클릭될 때 감지하는 이벤트
    usernameInput.addEventListener('focus', function() {
        console.log('사용자ID 입력창이 클릭되었습니다.');
        // 여기에 필요한 다른 작업을 추가할 수 있습니다.
    });
});