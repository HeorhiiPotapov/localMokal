(function() {
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
			// share переместить в шапку
		}

		// перенести кнопки позвонить и сообщение в нижнее меню
		window.addEventListener('resize', function () {
			chenge_product_page_html()
		})
		chenge_product_page_html()

		// раздел с номерами
		$('#btn_call, .product-page__content__header__phones__close-btn').on('click', function () {
			$('.product-page__content__header').toggleClass('active')
			$('.product-page__content__header__phones').toggleClass('active')
		})
	}
	// страница товара
})()


function chenge_product_page_html() {
	// на моб устройствах если кнопок еще нету в нижнем меню
	if ($('body').width() < 992  && !document.querySelector('.mobile-menu-on-bottom button')) {
		$('.mobile-menu-on-bottom').empty();
		$('.product-page__content__header__buttons button').appendTo('.mobile-menu-on-bottom')
		$('.product-page__content__product-info__price-and-favorites__share').appendTo('.product-page__content__header__buttons')
	// если это пк и кнопки находятся в нижнем меню 
	}else if($('body').width() > 992 && !document.querySelector('.mobile-menu-on-bottom button')) {
		console.log(document.querySelector('.product-page__content__header__buttons button'))
		$('.mobile-menu-on-bottom button').appendTo('.product-page__content__header__buttons')
		$('.product-page__content__product-info__price-and-favorites__share').appendTo('.product-page__content__product-info__price-and-favorites')
	}
}