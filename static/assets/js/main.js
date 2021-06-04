window.onload = function () {

	(function () {

		// burger header menu
		// if(document.querySelector('.wrapper-menu-hamburger')) {
		// 	$('.wrapper-menu-hamburger').on('click', function() {
		// 		$('.wrapper-menu-hamburger__hamburger-menu').toggleClass('animate');
		// 	})
		// }
		// /burger header menu
		if ($('body').width() < 768 && document.querySelector('.header-main')) {
			document.querySelector('#page').style.paddingTop = '153px'
		} else if (document.querySelector('.header-main')) {
			document.querySelector('#page').style.paddingTop = '97px'
		}

		fixed_block_from('.header-main', 99999, 'top')
		fixed_block_from('.mobile_menu_on_bottom', 992, 'bottom')



		// slider home page
		if (document.querySelector('.slider-temp-wrapper__slider-temp')) {
			$('.slider-temp-wrapper__slider-temp').slick({
				speed: 1000,
				slidesToShow: 1,
				// autoplay: true,
				dots: true,
				arrows: true,

				responsive: [{
					breakpoint: 992,
					settings: {
						arrows: false,
					}
				}]
			});
		}
		// /slider home page


		// categories
		if (document.querySelector('.category')) {
			$('.category').hover(function () {
				let path = this.querySelector('.category__top-icon svg path')
				if (path) {
					path.setAttribute('fill', '')
				}
			}, function () {
				let path = this.querySelector('.category__top-icon svg path')
				if (path) {
					path.setAttribute('fill', 'url(#icon_gradient)')
				}
			})

			let all_cat = document.querySelectorAll('.category')
			all_cat.forEach(cat => {
				let sub_cat = cat.querySelector('.category__subcat')
				if (sub_cat) {
					cat.addEventListener('click', function () {
						$(sub_cat).toggleClass('_open')
					})
					sub_cat.addEventListener('mouseleave', function () {
						$(this).toggleClass('_open')
					})
				}
			})

			// categories mobile
			let slider_on_categories_set = 0

			window.addEventListener('resize', function () {
				slider_on_categories_set = set_categories_slider(slider_on_categories_set)
			})
			slider_on_categories_set = set_categories_slider(slider_on_categories_set)
			// /categories mobile

		}
		// categories

		// страница товара
		if (document.querySelector('.product-page')) {
			$('#content').css('padding', '0')
			$('.header-main').css('display', 'none')

			window.addEventListener('resize', function () {
				if ($('body').width() <= 992) { // на моб
					$('.product-page__content').css({
						'max-height': 'inherit',
						'height': 'auto'
					})
					$('.product-page__images-block').css({
						'max-height': '300px',
						'height': '300px'
					})
					$('.product-page').css('margin-top', '80px')

				} else {
					$('.product-page').css('margin-top', '0')
					set_full_height_product_page()
				}
			})
			if ($('body').width() <= 992) { // на пк запустить при загрузке страницы
				$('.product-page__content').css({
					'max-height': 'inherit',
					'height': 'auto'
				})
				$('.product-page__images-block').css({
					'max-height': '300px',
					'height': '300px'
				})
				$('.product-page').css('margin-top', '80px')
			} else {
				$('.product-page').css('margin-top', '0')
				set_full_height_product_page()
			}

			$('.product-page__images-block').slick({
				speed: 1000,
				slidesToShow: 1,
				// autoplay: true,
				dots: true,
				arrows: true,
				responsive: [{
					breakpoint: 992,
					settings: {
						arrows: false,
					}
				}]
			});


			// подробнее
			// скрыть кнопку если текст занимает меньше 90px height
			window.addEventListener('resize', function () {
				hide_or_show_expand_btn()
				// page__content__header вылезает за полосу прокрутки при position: fixed... Поправляю
				if ($('body').width() > 992) {
					$('.product-page__content__header').css('width', $('.product-page__content').width() - 17 + "px")
				} else {
					$('.product-page__content__header').css('width', '100%')
				}
			})
			if ($('body').width() > 992) {
				$('.product-page__content__header').css('width', $('.product-page__content').width() - 17 + "px")
			} else {
				$('.product-page__content__header').css('width', '100%')
			}


			hide_or_show_expand_btn()
			// /скрыть кнопку если пекст занимает меньше 90px height

			// развирнуть при клике
			$('.product-page__content__product-info__description__expand').on('click', function () {
				$('.product-page__content__product-info__description__text', ).toggleClass('open')
				$('.product-page__content__product-info__description__expand').toggleClass('open')
			})
			// /развирнуть при клике

			// подробнее

			// скрыть шапку если скролится вниз и показать если скролится наверх
			fixed_block_from('.product-page__content__header', 992, 'top')
			if ($('body').width() < 992) {
				// кнопки позвонить и сообщения переместить в футер
				$('.product-page__content__header__buttons button').appendTo('.mobile_menu_on_bottom')
				// share переместить в шапку
				$('.product-page__content__product-info__price-and-favorites__share').appendTo('.product-page__content__header__buttons')
			}

		} else {

		}
		// раздел с номерами
		$('#btn_call, .product-page__content__header__phones__close-btn').on('click', function () {
			$('.product-page__content__header').toggleClass('active')
			$('.product-page__content__header__phones').toggleClass('active')
		})
		// страница товара



		// поля с паролем
		// if(document.querySelector('.view-password')) {
		// 	let all_passw_block = document.querySelectorAll('.view-password')
		// 	all_passw_block.forEach(block => {
		// 		let eye = block.querySelector('._show-passw'),
		// 			inp = block.querySelector('input')
		// 		eye.addEventListener('click', function () {
		// 			let inp_type = inp.getAttribute('type')
		// 			console.log(inp_type)
		// 			if (inp_type == 'password') {
		// 				inp.setAttribute('type', 'text')
		// 				eye.classList.remove('fa-eye')
		// 				eye.classList.add('fa-eye-slash')
		// 			} else {
		// 				inp.setAttribute('type', 'password')
		// 				eye.classList.add('fa-eye')
		// 				eye.classList.remove('fa-eye-slash')
		// 			}
		// 		})
		// 	})
		// }
		
		// поля с паролем

		// поиск в шапке
		dropdown_input('region-inp')
		// страница подписки
		if (document.querySelector('form#subscription-to-shares')) {
			dropdown_input('subscription-to-shares__region')
			let all_cat = document.querySelectorAll('.subscription-to-shares .categories-wrapper .category_h')
			all_cat.forEach(cat => {
				cat.addEventListener('click', function () {
					// поставить флажок
					let this_checkbox = cat.querySelector('.subscription-to-shares__category-checkbox')
					if (this_checkbox.checked) {
						this_checkbox.checked = false
					} else {
						this_checkbox.checked = true
					}
					// /поставить флажок

					$(cat).toggleClass('_active')
				})
			})
		}
		// страница подписки

		// tmp checkbox
		if(document.querySelector('.temp-checkbox')) {
			let all_tmp_checkbox = document.querySelectorAll('.temp-checkbox')
			all_tmp_checkbox.forEach(checkbox => {
				let img_active = checkbox.querySelector('.icon_active'),
					just_img = checkbox.querySelector('.just_icon'),
					inp = checkbox.parentNode.querySelector('input[type="checkbox"')
				just_img.addEventListener('click', function() {
					img_active.style.display = 'block'
					just_img.style.display = 'none'
					inp.setAttribute('checked', 'true')


				})
				img_active.addEventListener('click', function() {
					just_img.style.display = 'block'
					img_active.style.display = 'none'
					inp.setAttribute('checked', 'false')
				})
			})
		}
		// /tmp checkbox


		// nav bar
		if (document.querySelector('.right-bar')) {

			$('.wrapper-menu-hamburger').on('click', function () {
				$('.right-bar').toggleClass('_open')
				$('.bg-for-open-mob-menu').toggleClass('_active')
			})
			$('.right-bar').mouseleave(function () {
				$('.right-bar').toggleClass('_open')
				$('.bg-for-open-mob-menu').toggleClass('_active')

			})
			$('._open-right-bar').on('click', function () {
				$('.right-bar').toggleClass('_open')
				$('.bg-for-open-mob-menu').toggleClass('_active')
			})
			$('.bg-for-open-mob-menu').on('touchstart', function () {
				$('.right-bar').toggleClass('_open')
				$('.bg-for-open-mob-menu').toggleClass('_active')
			})
			$('.bg-for-open-mob-menu').on('click', function () {
				$('.right-bar').toggleClass('_open')
				$('.bg-for-open-mob-menu').toggleClass('_active')
			})
			document.querySelector('.right-bar').addEventListener('scroll', function () {
				console.log('scroll')
			});
			let sub_menu_btns = document.querySelectorAll('.right-bar__menu__item._with-sub-menu > a')
			sub_menu_btns.forEach(btn => {
				btn.addEventListener('click', function () {

					// открыть текущее
					let sub_menu = btn.parentNode.querySelector('.right-bar__menu__item__sub-menu')
					$(sub_menu).toggleClass('_open')
					$(btn.parentNode).toggleClass('_active')
					// получить приведущее открытое меню
					let prev_open_menu = document.querySelector('.right-bar__menu__item__sub-menu._prev_open_menu')
					// добавить к текущему класс открытого
					sub_menu.classList.add('_prev_open_menu')
					// удалить у приведущего класс _open и _prev. У родителя забираю класс _active
					if (prev_open_menu != null) {
						prev_open_menu.parentNode.classList.remove('_active')
						prev_open_menu.classList.remove('_prev_open_menu')
						prev_open_menu.classList.remove('_open')
					}

				})
			})
		}
		// nav bar


		// search form
		if (document.querySelector('#search-inp')) {
			let searh_timeout;
			$('.search-form__input-block img').on('click', function () {
				$('#search-form').submit()
			})
			$('#search-inp').on('input', function () {
				clearTimeout(searh_timeout);
				searh_timeout = setTimeout(function () {
					let val = document.querySelector('#search-inp').value,
						city = document.querySelector('#region-inp').value

					if (val.length >= 3) {
						$.ajax({
							url: "/products/search/",
							data: {
								"query": val,
								"region": city
							},

							async: false,
							success: function (data) {
								let json_parse = JSON.parse(data)
								let inner_block = document.querySelector('.search-form__search-issue')
								inner_block.innerHTML = ''

								for (key in json_parse) {
									let name = json_parse[key]['name'],
										link = json_parse[key]['link']

									let li = document.createElement('li'),
										a = document.createElement('a')
									a.setAttribute('href', link)
									a.textContent = name
									li.append(a)
									inner_block.append(li)
								}
								// json_parse[0].forEach(el => {
								// 	console.log(el['name'])
								// })
							}
						})
					}
				}, 500)
			})
		}
		// search form
		// $('#search-inp').on('input', function(){
		// 	let val = document.querySelector('#search-inp').value,
		// 		city = document.querySelector('#region-inp').value

		// 	if(val.length >= 3) {
		// 		$.ajax({
		// 			url: "https://2426c4087ccb.ngrok.io/search/",
		// 			data: { "q": val, "city": city },
		// 			async: false,
		// 			success: function( data ){
		// 				console.log('ssend::', data )
		// 			}
		// 		})
		// 	}
		// })
	})();
}

function fixed_block_from(selector, max_width, position) {

	if ($('body').width() < max_width) {

		let prev_offset_y;
		document.querySelector('body').addEventListener('scroll', function (e) {
			if (prev_offset_y > document.body.scrollTop) { // это скрол наверх
				// показать при скроле наверх
				$(selector).css(position, '0')
			} else { // это скрол вниз
				// скриывать шапку при скроле вниз
				$(selector).css(position, '-50%')
			}
			prev_offset_y = document.body.scrollTop
		})
	}
}

function dropdown_input(for_input) { // for_input - id скрытого инпута, куда выводить значение
	let dropdown_items = document.querySelectorAll(`.dropdown-menu[data-for="${for_input}"] .dropdown-item`)
	dropdown_items.forEach(item => {
		// при клике изменить value скритого инпута, на значение текущего item
		item.addEventListener('click', function () {
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
	$(".block-for-calculate-height").text('')
	$(".product-page__content__product-info__description__text").clone().appendTo('.block-for-calculate-height');
	let description_text_height = $(".block-for-calculate-height").height()
	if (description_text_height <= 90) {
		$('.product-page__content__product-info__description__expand').css('display', 'none')
	} else {
		$('.product-page__content__product-info__description__expand').css('display', 'inline-block')
	}
}

function set_full_height_product_page() {
	if ($('.product-page__images-block')) {
		// let header_height = $('.header-main').height() + parseInt($('.header-main').css('padding-top')) + parseInt($('.header-main').css('padding-bottom'))
		$('.product-page__images-block').css({
			'max-height': document.documentElement.clientHeight + 'px',
			'height': document.documentElement.clientHeight + 'px'
		})
		$('.product-page__content').css({
			// - header_height
			'max-height': document.documentElement.clientHeight + 'px',
			'height': document.documentElement.clientHeight + 'px'
		})
	}
}

function set_categories_slider(slider_on_cat_set) {
	if ($('body').width() <= 992) { // на моб
		if (slider_on_cat_set) { // если слайдер установлен не продолжать
			return slider_on_cat_set
		}
		$('.categories').slick({ // добавить слайдер
			speed: 1000,
			slidesToShow: 3,
			// autoplay: true,
			arrows: false,

			dots: false,
		});
		slider_on_cat_set = 1 // пометить что слайдер есть
	} else { // на пк
		if (!slider_on_cat_set) { // если слайдер не установлен не продолжать
			return slider_on_cat_set
		}
		$('.categories').slick('unslick'); // удалить слайдер
		slider_on_cat_set = 0 // пометить что слейдер убрали
	}
	return slider_on_cat_set
}