window.onload = function() {

	(function () {
		// burger header menu
		// if(document.querySelector('.wrapper-menu-hamburger')) {
		// 	$('.wrapper-menu-hamburger').on('click', function() {
		// 		$('.wrapper-menu-hamburger__hamburger-menu').toggleClass('animate');
		// 	})
		// }
		// /burger header menu

		// slider home page
		if( document.querySelector('.slider-temp-wrapper__slider-temp') ) {
			$('.slider-temp-wrapper__slider-temp').slick({
				speed: 1000,
				slidesToShow: 1,
				// autoplay: true,
				dots: true,
				arrows: true,

				responsive: [
					{
						breakpoint: 992,
						settings: {
							arrows: false,
						}
					}
				]
			});
		}
		// /slider home page


		// categories
		if(document.querySelector('.category')) {
			$('.category').hover(function() {
				let path = this.querySelector('.category__top-icon svg path')
				if(path) {
					path.setAttribute('fill','')
				}
				}, function() {
				let path = this.querySelector('.category__top-icon svg path')
				if(path) {
					path.setAttribute('fill','url(#icon_gradient)')
				}
			})

			// categories mobile
			let slider_on_categories_set = 0

			window.addEventListener('resize', function() {
				slider_on_categories_set = set_categories_slider( slider_on_categories_set )
			})
			slider_on_categories_set = set_categories_slider( slider_on_categories_set )
			// /categories mobile

		}
		// categories

		// страница товара 
		if(document.querySelector('.product-page')) {
			$('#content').css('padding','0')
			$('.header-main').css('display','none')

			window.addEventListener('resize',function() {
				if( $('body').width() <= 992 ) {  // на моб
					$('.product-page__content').css({
						'max-height': 'inherit',
						'height': 'auto'
					})
					$('.product-page__images-block').css({
						'max-height': '300px',
						'height': '300px'
					})
					$('.product-page').css('margin-top', '80px')

				}else { 
					$('.product-page').css('margin-top', '0')
					set_full_height_product_page()
				}
			})
			if( $('body').width() <= 992 ) { // на пк запустить при загрузке страницы
				$('.product-page__content').css({
					'max-height': 'inherit',
					'height': 'auto'
				})
				$('.product-page__images-block').css({
					'max-height': '300px',
					'height': '300px'
				})
				$('.product-page').css('margin-top', '80px')
			}else {
				$('.product-page').css('margin-top', '0')
				set_full_height_product_page()
			}

			$('.product-page__images-block').slick({
				speed: 1000,
				slidesToShow: 1,
				// autoplay: true,
				dots: true,
				arrows: true,
				responsive: [
					{
						breakpoint: 992,
						settings: {
							arrows: false,
						}
					}
				]
			});


			// подробнее
				// скрыть кнопку если текст занимает меньше 90px height
				window.addEventListener('resize', function() {
					hide_or_show_expand_btn()
					// page__content__header вылезает за полосу прокрутки при position: fixed... Поправляю
					if($('body').width() > 992) {
						$('.product-page__content__header').css('width', $('.product-page__content').width() -17 + "px")
					}else {
						$('.product-page__content__header').css('width', '100%')

					}
				})
				if($('body').width() > 992) {
					$('.product-page__content__header').css('width', $('.product-page__content').width() -17 + "px")
				}else {
					$('.product-page__content__header').css('width', '100%')
				}


				hide_or_show_expand_btn()
				// /скрыть кнопку если пекст занимает меньше 90px height
				
				// развирнуть при клике 
				$('.product-page__content__product-info__description__expand').on('click',function() {
					$('.product-page__content__product-info__description__text').toggleClass('open')
					$('.product-page__content__product-info__description__expand').toggleClass('open')
				})
				// /развирнуть при клике 

			// подробнее
			
			// скрыть шапку если скролится вниз и показать если скролится наверх
		
			if($('body').width() < 992) {
				let prev_offset_y;
				document.querySelector('body').addEventListener('scroll', function(e) {
					let header_pos_top = parseInt($('.product-page__content__header').css('top'))
					
					if(prev_offset_y > document.body.scrollTop) { // это скрол наверх
						// показать шапку при скроле наверх
						if(header_pos_top < 0) { 
							$('.product-page__content__header').css('top', header_pos_top +3 + 'px')
						}
					}else { // это скрол вниз
						// скриывать шапку при скроле вниз
						if(header_pos_top > -90) { 
							$('.product-page__content__header').css('top', header_pos_top -3 + 'px')
						}
					}

					prev_offset_y = document.body.scrollTop
				})

				// кнопки позвонить и сообщения переместить в футер
				$('.product-page__content__header__buttons button').appendTo('.mobile_menu_on_bottom')

				// share переместить в шапку
				$('.product-page__content__product-info__price-and-favorites__share').appendTo('.product-page__content__header__buttons')
			}
		}else {
			
		}
		// страница товара 



		// поля с паролем 
		let all_passw_block = document.querySelectorAll('.view-password')
		all_passw_block.forEach( block => {
			let eye = block.querySelector('._show-passw'),
				inp = block.querySelector('input')
			eye.addEventListener('click',function() {
				let inp_type = inp.getAttribute('type')
				console.log(inp_type)
				if(inp_type =='password') {
					inp.setAttribute('type','text')
					eye.classList.remove('fa-eye')
					eye.classList.add('fa-eye-slash')
				}else {
					inp.setAttribute('type','password')
					eye.classList.add('fa-eye')
					eye.classList.remove('fa-eye-slash')
				}
			})
		})
		// поля с паролем

		// поиск в шапке
		dropdown_input( 'region' )
		// поиск в шапке

		// nav bar
		$('.wrapper-menu-hamburger').on('click', function() {
			$('.right-bar').toggleClass('_open')
		})
		$('.right-bar').mouseleave(function(){
			$('.right-bar').toggleClass('_open')
		})
		let sub_menu_btns = document.querySelectorAll('.right-bar__menu__item._with-sub-menu > a')
		sub_menu_btns.forEach( btn => {
			btn.addEventListener('click', function(){
				
				// открыть текущее 
				let sub_menu = btn.parentNode.querySelector('.right-bar__menu__item__sub-menu')
				$(sub_menu).toggleClass('_open')
				$(btn.parentNode).toggleClass('_active')

				// получить приведущее открытое меню
				let prev_open_menu = document.querySelector('.right-bar__menu__item__sub-menu._prev_open_menu')
				// добавить к текущему класс открытого
				sub_menu.classList.add('_prev_open_menu')
				// удалить у приведущего класс _open и _prev. У родителя забираю класс _active
				if(prev_open_menu != null) {
					prev_open_menu.parentNode.classList.remove('_active')
					prev_open_menu.classList.remove('_prev_open_menu')
					prev_open_menu.classList.remove('_open')
				}
				
			})
		})
		// nav bar

	})();
}

function dropdown_input( for_input ) { // for_input - id скрытого инпута, куда выводить значение
	let dropdown_items = document.querySelectorAll(`.dropdown-menu[data-for="${for_input}"] .dropdown-item`)
	dropdown_items.forEach( item => {
		// при клике изменить value скритого инпута, на значение текущего item
		item.addEventListener('click', function() {
			let item_value = item.getAttribute('data-value'),
			hidden_input = document.querySelector(`input#${for_input}`)
			hidden_input.value = item_value

			// сменить самой кнопки содержимое кнопки 
			let button_dropdown = document.querySelector(`.dropdown-menu[data-for="${for_input}"]`).parentNode.querySelector('button')
			button_dropdown.innerHTML = item_value
		})
	})
}

function hide_or_show_expand_btn() {
	$( ".block-for-calculate-height").text('')
	$( ".product-page__content__product-info__description__text" ).clone().appendTo('.block-for-calculate-height');
	let description_text_height = $( ".block-for-calculate-height" ).height()
	if(description_text_height <= 90) {
		$('.product-page__content__product-info__description__expand').css('display','none')
	}else {
		$('.product-page__content__product-info__description__expand').css('display','inline-block')
	}
}
function set_full_height_product_page() {
	if($('.product-page__images-block')) {
		// let header_height = $('.header-main').height() + parseInt($('.header-main').css('padding-top')) + parseInt($('.header-main').css('padding-bottom'))
		$('.product-page__images-block').css({
			'max-height': document.documentElement.clientHeight  + 'px',
			'height' : document.documentElement.clientHeight  + 'px'
		})
		$('.product-page__content').css({
			// - header_height
			'max-height': document.documentElement.clientHeight  + 'px',
			'height' : document.documentElement.clientHeight  + 'px'
		})
	}
}
function set_categories_slider( slider_on_cat_set ) {
	if($('body').width() <= 992) {  // на моб
		if(slider_on_cat_set) { // если слайдер установлен не продолжать
			return slider_on_cat_set
		}
		$('.categories').slick({ // добавить слайдер
			speed: 1000,
			slidesToShow: 3,
			// autoplay: true,
			arrows: false,

			dots: false,
		});
		slider_on_cat_set = 1  // пометить что слайдер есть
	}else { // на пк
		if(!slider_on_cat_set) { // если слайдер не установлен не продолжать
			return slider_on_cat_set
		}
		$('.categories').slick('unslick'); // удалить слайдер
		slider_on_cat_set = 0 // пометить что слейдер убрали
	}
	return slider_on_cat_set
}