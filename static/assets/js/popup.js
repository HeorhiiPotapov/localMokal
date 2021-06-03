let bg_for_popup = document.createElement('div')
bg_for_popup.classList.add('bg-for-popup')


document.querySelector('#content').append(bg_for_popup)

function popup_open(selector_popup) {
  let popup_window = document.querySelector(selector_popup),
    bg_popup = document.querySelector('.bg-for-popup')
  popup_window.classList.add('_open')
  bg_popup.classList.add('_open')
  bg_popup.addEventListener('click', close_popup_on_bg.bind(this, bg_popup, popup_window), false)
}

function popup_close(selector_popup) {
  let popup_window = document.querySelector(selector_popup),
    bg_popup = document.querySelector('.bg-for-popup')
  popup_window.classList.remove('_open')
  bg_popup.classList.remove('_open')
  bg_popup.removeEventListener('click', close_popup_on_bg.bind(this, bg_popup, popup_window), false)

}

function close_popup_on_bg(bg_el, popup_el) {
  bg_el.classList.remove('_open')
  popup_el.classList.remove('_open')
}