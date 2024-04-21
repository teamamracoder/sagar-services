const chatboxToggle = document.querySelector('.chatbox-toggle')
const chatboxMessageWrapper = document.querySelector('.chatbox-message-wrapper')

chatboxToggle.addEventListener('click', function () {
    chatboxMessageWrapper.classList.toggle('show')
})
