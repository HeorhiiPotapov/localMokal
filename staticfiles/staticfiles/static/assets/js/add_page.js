if (document.querySelector('form#form_add_page')) {
	let all_cat = document.querySelectorAll('.subscription-to-shares .categories-wrapper .category_h')
	all_cat.forEach(cat => {
		cat.addEventListener('click', function () {
			let this_checkbox = cat.querySelector('.subscription-to-shares__category-checkbox')
			// убрать флажок с приведущего
			all_cat.forEach(cat_ => {
				let this_checkbox = cat_.querySelector('.subscription-to-shares__category-checkbox')

				this_checkbox.checked = false
				cat_.classList.remove('_active')
				// console.log(this_checkbox.checked)
			})
			// поставить флажок
			if (this_checkbox.checked) {
				this_checkbox.checked = false
			} else {
				this_checkbox.checked = true
			}
			// /поставить флажок
			$(cat).toggleClass('_active')

			// показывать только те подрубрики которые входят в эту рубрику
			let sub_cat = document.querySelector('#sub-cat-select'),
				sub_cat_options = document.querySelectorAll('#sub-cat-select option'),
				main_cat_name = this_checkbox.value
			sub_cat_options.forEach(option => {
				let name_parent_cat = option.getAttribute('data-main-cat')


				if (name_parent_cat != main_cat_name) { // скрыть подрубрики которые пренадлежат другой родительской группе
					option.style.display = 'none'
				} else {
					option.style.display = 'block'
				}

				// сменить value(подкатегорию) в select на ту подкатегорию которая имеется у родительской группы
				if (this_checkbox.value == name_parent_cat) {
					sub_cat.value = option.value
				}
			})

		})
	})

	let form_add_page = document.querySelector('form#form_add_page')
    let token = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    form_add_page.addEventListener('submit', function (e) {
		// e.preventDefault()
		console.log(form_add_page.querySelector('.subscription-to-shares__category-checkbox').value)
		var formData = new FormData();
		formData.append("myFile", document.querySelector('input[name="image_product_0"]').files[0], 'chris1.jpg');

		$.ajax({
			method: "POST",
			url: "https://b9a733906ba7.ngrok.io/products/create/",
			dataType: "script",
			data: formData
		});
	})


	// ЗАГРУЗКА КАРТИНКУ ИЛИ УРЛ НА YOUTUBE
	let load_photo_btn = document.querySelector('.load_photo_btn'),
		load_url_ytb_btn = document.querySelector('.load_url_ytb_btn'),
		container_btn = document.querySelector('.add-page__photo__load-image-or-urlYouT')

	let container_for_inner_block = document.querySelector('.add-page__photo__container-for-loaded-files')

	// при клике на кнопку загрузки картинки
	load_photo_btn.addEventListener('click', function () {
		// получить количество загруженых картикок/url
		let alredy_loaded_count = get_count_loaded_files_or_url('.add-page__photo__container-for-loaded-files')
		if (alredy_loaded_count >= 0) {
			let new_block_loaded_image = document.querySelector('.tmp_block_add_photo_for_clone').cloneNode(true)

			// добавляю блоку с картинкой и инпутом нужные классы
			new_block_loaded_image.classList.remove('tmp_block_add_photo_for_clone')
			new_block_loaded_image.classList.add('add-page__photo__container-for-loaded-files__image')

			// добавляю атрибут name инпуту
			let input_file = new_block_loaded_image.querySelector('input')
			input_file.setAttribute('name', 'image_product_' + alredy_loaded_count)

			// активировать окно загрузки файлов
			input_file.click()

			// выполнитсяы только после загрузки файла
			input_file.addEventListener('change', function () {
				let new_block = insert_loaded_image_intu_block(new_block_loaded_image, input_file)

				// добавить возможность удалить блок 
				let del_btn = new_block.querySelector('.del_block')
				del_btn.addEventListener('click', function () {
					this.offsetParent.remove()
				})

				// вывести блок
				container_for_inner_block.appendChild(new_block)

				// если количество блоков +1 будет больше 7
				if (alredy_loaded_count + 1 >= 7) {
					container_btn.style.display = 'none'
				} else {
					container_btn.style.display = 'flex'
				}
			})
		}
	})
	// end при клике на кнопку загрузки картинки

	// при клике на кнопку загрузки url youtobe
	load_url_ytb_btn.addEventListener('click', function () {
		let alredy_loaded_count = get_count_loaded_files_or_url('.add-page__photo__container-for-loaded-files')
		if (alredy_loaded_count == 0) { // если это первый загрузочный блок
			let new_block_loaded_url = document.querySelector('.tmp_block_add_url_ytb_for_clone').cloneNode(true)

			// добавляю нужные классы			
			new_block_loaded_image.classList.remove('tmp_block_add_photo_for_clone')
			new_block_loaded_image.classList.add('add-page__photo__container-for-loaded-files__image')

			// добавляю атрибут name инпуту
			let input_url = new_block_loaded_image.querySelector('input')
			input_url.setAttribute('name', 'url_youtube_product_' + alredy_loaded_count)
		}
	})

	// end при клике на кнопку загрузки url youtobe

	get_free_count_for_foaded_block('.add-page__photo__container-for-loaded-files')
	function insert_loaded_image_intu_block(new_block, input_with_files) {

		let curFiles = input_with_files.files;
		if (curFiles.length != 0) { // если файл загрузили 
			// добавить картинку в new_block
			let image = new_block.querySelector('img');
			image.src = window.URL.createObjectURL(curFiles[0]);

			return new_block
		} else { // если файл не был загружен
			return false
		}
	}
	function get_count_loaded_files_or_url(selector) {
		let container = document.querySelector(selector)
		return container.querySelectorAll('div').length
	}
	function get_free_count_for_foaded_block(selector) {
		let container = document.querySelector(selector),
			container_elements = container.childNodes,
			container_blocks = []
		container_elements.forEach(el => {
			if (el.nodeName == 'DIV') {
				container_blocks.push(el)
			}
		})
		container_blocks.forEach(block => {

		})

	}
}
