if (document.querySelector("form#form_add_page")) {
  let all_cat = document.querySelectorAll(
    ".subscription-to-shares .categories-wrapper .category_h"
  );
  all_cat.forEach((cat) => {
    cat.addEventListener("click", function () {
      let this_checkbox = cat.querySelector(
        ".subscription-to-shares__category-checkbox"
      );
      // убрать флажок с приведущего
      all_cat.forEach((cat_) => {
        let this_checkbox = cat_.querySelector(
          ".subscription-to-shares__category-checkbox"
        );

        this_checkbox.checked = false;
        cat_.classList.remove("_active");
        // console.log(this_checkbox.checked)
      });
      // поставить флажок
      if (this_checkbox.checked) {
        this_checkbox.checked = false;
      } else {
        this_checkbox.checked = true;
      }
      // /поставить флажок
      $(cat).toggleClass("_active");

      // показывать только те подрубрики которые входят в эту рубрику
      let sub_cat = document.querySelector("#sub-cat-select"),
        sub_cat_options = document.querySelectorAll("#sub-cat-select option"),
        main_cat_name = this_checkbox.value;
      sub_cat_options.forEach((option) => {
        let name_parent_cat = option.getAttribute("data-main-cat");

        if (name_parent_cat == '-1') {
          return
        }

        if (name_parent_cat != main_cat_name) {
          // скрыть подрубрики которые пренадлежат другой родительской группе
          option.classList.add('_display_none')
        } else {
          option.classList.remove('_display_none')
        }

        // скріть value(подкатегорию)
        sub_cat.value = ''
      });
    });

  });

  let form_add_page = document.querySelector("form#form_add_page");
  // form_add_page.addEventListener("submit", function (e) {
  //   e.preventDefault();
  //   let form_data = new FormData(form_add_page);
  //   let file_inputs = document.querySelectorAll(
  //     ".add-page__photo__container-for-loaded-files .file_input"
  //   );

  //   // let name_pr = document.querySelector('#name_product'),
  //   // 	cat_pr = document.querySelector('.subscription-to-shares__category-checkbox').checked,
  //   // 	subcat_pr = document.querySelector('#sub-cat-select'),
  //   // 	price = document.querySelector('#price'),
  //   // 	discount_from = document.querySelector('#discount_from'),
  //   // 	discount_to = document.querySelector('#discount_to'),
  //   // 	discount_percent = document.querySelector('#discount_percent'),
  //   // 	discount_description = document.querySelector('#discount_description')

  //   // form_data.append(
  //   //   "csrfmiddlewaretoken",
  //   //   form_add_page.querySelector('input[name="csrfmiddlewaretoken"]').value
  //   // );
  //   var request = new XMLHttpRequest();
  //   request.open("post", "http://127.0.0.1:8000/products/create/");
  //   request.send(form_data);
  // });

  // ЗАГРУЗКА КАРТИНКУ ИЛИ УРЛ НА YOUTUBE
  let load_photo_btn = document.querySelector(".load_photo_btn"),
    load_url_ytb_btn = document.querySelector(".load_url_ytb_btn"),
    container_btn = document.querySelector(
      ".add-page__photo__load-image-or-urlYouT"
    );
  let id_for_inp = 0;
  let container_for_inner_block = document.querySelector(
    ".add-page__photo__container-for-loaded-files"
  );

  // при клике на кнопку загрузки картинки
  load_photo_btn.addEventListener("click", function () {
    id_for_inp += 1;
    // получить количество загруженых картикок/url
    let _pos_for_block = get_pos_for_block(
      ".add-page__photo__container-for-loaded-files"
    );
    if (_pos_for_block >= 0) {
      let new_block_loaded_image = document
        .querySelector(".tmp_block_add_photo_for_clone")
        .cloneNode(true);

      // добавляю блоку с картинкой и инпутом нужные классы
      new_block_loaded_image.classList.remove("tmp_block_add_photo_for_clone");
      new_block_loaded_image.classList.add(
        "add-page__photo__container-for-loaded-files__image"
      );

      // добавляю атрибут name инпуту
      let input_file = new_block_loaded_image.querySelector("input");

      input_file.setAttribute("name", "image_product_" + id_for_inp);
      new_block_loaded_image.setAttribute("data-pos", _pos_for_block);

      input_file.removeAttribute("disabled");

      // активировать окно загрузки файлов
      input_file.click();

      // выполнитсяы только после загрузки файла
      input_file.addEventListener("change", function () {
        let new_block = insert_loaded_image_intu_block(
          new_block_loaded_image,
          input_file
        );

        // добавить возможность удалить блок
        let del_btn = new_block.querySelector(".del_block");
        del_btn.addEventListener("click", function () {
          this.offsetParent.remove();
          set_new_pos_for_all_block(
            ".add-page__photo__container-for-loaded-files"
          );
          toggle_yout_btn();
        });

        // добавляю возможность перетаскивания
        drag_element(new_block);

        // вывести блок
        container_for_inner_block.appendChild(new_block);

        // если количество блоков +1 будет больше 7
        if (_pos_for_block + 1 >= 7) {
          container_btn.style.display = "none";
        } else {
          container_btn.style.display = "flex";
        }

        toggle_yout_btn();
      });
    }
  });
  // end при клике на кнопку загрузки картинки

  // при клике на кнопку загрузки url youtobe
  load_url_ytb_btn.addEventListener("click", function () {
    let alredy_loaded_count = get_pos_for_block(
      ".add-page__photo__container-for-loaded-files"
    );
    let _pos_for_block = get_pos_for_block(
      ".add-page__photo__container-for-loaded-files"
    );
    if (alredy_loaded_count == 0 && _pos_for_block >= 0) {
      // если это первый загрузочный блок
      let new_block_loaded_url = document
        .querySelector(".tmp_block_add_url_ytb_for_clone")
        .cloneNode(true);

      // добавляю нужные классы
      new_block_loaded_url.classList.remove("tmp_block_add_url_ytb_for_clone");
      new_block_loaded_url.classList.add(
        "add-page__photo__container-for-loaded-files__youTub-url"
      );

      // добавляю атрибут name инпуту
      let input_url = new_block_loaded_url.querySelector("input");
      input_url.setAttribute(
        "name",
        "video"
      );
      input_url.removeAttribute("disabled");

      // получаю от пользователя url на виде и достаю параметны из ссыдки
      let url_yout_vid = prompt("Вставьте URL на видео YouTube");
      url_param = get_param_from_link(url_yout_vid);

      if (url_param.v != "") {
        let url_to_preview = `https://img.youtube.com/vi/${url_param.v}/hqdefault.jpg`;
        new_block_loaded_url
          .querySelector("img")
          .setAttribute("src", url_to_preview);
        new_block_loaded_url
          .querySelector("input")
          .setAttribute("value", url_yout_vid);

        // добавить возможность удалить блок
        let del_btn = new_block_loaded_url.querySelector(".del_block");
        del_btn.addEventListener("click", function () {
          this.offsetParent.remove();
          set_new_pos_for_all_block(
            ".add-page__photo__container-for-loaded-files"
          );
          toggle_yout_btn();
        });

        // вывести блок
        container_for_inner_block.appendChild(new_block_loaded_url);

        // если количество блоков +1 будет больше 7
        if (_pos_for_block + 1 >= 7) {
          container_btn.style.display = "none";
        } else {
          container_btn.style.display = "flex";
        }

        toggle_yout_btn();
      }
    }
  });

  // end при клике на кнопку загрузки url youtobe

  function drag_element(elmnt) {
    let blocks_container = document.querySelector(
      ".add-page__photo__container-for-loaded-files"
    );

    elmnt.onmousedown = dragMouseDown;

    let tem_el_posY, tem_el_posX;
    let el_posY, el_posX;
    let cursorY, cursorX;

    function dragMouseDown(e) {
      // запомнить изначальное положение
      tem_el_posY = elmnt.offsetTop;
      tem_el_posX = elmnt.offsetLeft;
      e = e || window.event;
      // get the mouse cursor position at startup:
      cursorX = e.clientX;
      cursorY = e.clientY;

      // если не нажато на dek_block
      if (e.target != elmnt.querySelector(".del_block")) {
        $(elmnt).toggleClass("dragged");
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
      }
    }

    function elementDrag(e) {
      e = e || window.event;
      // calculate the new cursor position:
      el_posX = cursorX - e.clientX;
      el_posY = cursorY - e.clientY;
      // console.log(elmnt.offsetLeft, '---', elmnt.offsetTop)

      cursorX = e.clientX;
      cursorY = e.clientY;
      // set the element's new position:
      elmnt.style.top = elmnt.offsetTop - tem_el_posY - el_posY + "px";
      elmnt.style.left = elmnt.offsetLeft - tem_el_posX - el_posX + "px";

      // получаю data-pos на какое место поставить текущий елемент
      let elem_on_the_cursor_id = Math.floor(
        get_pos_cursor_to_the_parent(e).x / 160
      );
      // получаю на какой стороне находится курсор, на левой или правой
      let part_on_el = parseInt(
        (get_pos_cursor_to_the_parent(e).x / 160 + "")
        .split(".")[1]
        .substr(0, 1)
      );
      // получаю елемен, поторый в данный момент назодится под этим data-pos
      let elem_on_the_cursor = document.querySelector(
        `.add-page__photo__container-for-loaded-files__image[data-pos="${elem_on_the_cursor_id}"]`
      );

      // удалить приведущее подсказки
      let all_help_line = document.querySelectorAll(
        ".help_line_left, .help_line_right"
      );
      all_help_line.forEach((el) => el.classList.remove("active"));

      if (elem_on_the_cursor != null) {
        if (part_on_el >= 5) {
          // right
          elem_on_the_cursor
            .querySelector(".help_line_right")
            .classList.add("active");
          elem_on_the_cursor
            .querySelector(".help_line_left")
            .classList.remove("active");
        } else {
          // left
          elem_on_the_cursor
            .querySelector(".help_line_left")
            .classList.add("active");
          elem_on_the_cursor
            .querySelector(".help_line_right")
            .classList.remove("active");
        }
      }
    }

    function closeDragElement(e) {
      /* stop moving when mouse button is released:*/
      document.onmouseup = null;
      document.onmousemove = null;

      let count_elem_in_container_for_inner =
        get_pos_for_block(".add-page__photo__container-for-loaded-files") - 1;

      $(elmnt).toggleClass("dragged");
      elmnt.style.top = 0;
      elmnt.style.left = 0;
      // получаю data-pos на какое место поставить текущий елемент
      let elem_on_the_cursor_id = Math.floor(
        get_pos_cursor_to_the_parent(e).x / 160
      );

      // получаю елемен, поторый в данный момент назодится под этим data-pos
      let elem_on_the_cursor = document.querySelector(
        `.add-page__photo__container-for-loaded-files__image[data-pos="${elem_on_the_cursor_id}"]`
      );
      // получаю на какой стороне находится курсор, на левой или правой
      var part_on_el = parseInt(
        (get_pos_cursor_to_the_parent(e).x / 160 + "")
        .split(".")[1]
        .substr(0, 1)
      );
      let clone_elmnt = elmnt.cloneNode(true);

      // удалить приведущее подсказки
      let all_help_line = document.querySelectorAll(
        ".help_line_left, .help_line_right"
      );
      all_help_line.forEach((el) => el.classList.remove("active"));

      let available_pos = 0;

      // если ютуб видео загружено не позволить переместить картинку на первое место
      let youtube_block_ = blocks_container.querySelector(
        ".add-page__photo__container-for-loaded-files__youTub-url"
      );
      if (youtube_block_) {
        available_pos = 1;
      } else {
        available_pos = 0;
      }

      console.log(youtube_block_, elem_on_the_cursor);
      if (elem_on_the_cursor == elmnt) {
        // не продолжать если этот тот же елемент
        return;
      }

      if (
        elem_on_the_cursor_id >= available_pos &&
        elem_on_the_cursor != null &&
        elem_on_the_cursor != youtube_block_
      ) {
        // вставить елемент после определенного елемента
        if (part_on_el >= 5) {
          // right
          console.log("вставить елемент после определенного елемента right");
          elem_on_the_cursor.after(clone_elmnt);
        } else {
          // left
          console.log("вставить елемент после определенного елемента left");

          elem_on_the_cursor.before(clone_elmnt);
        }
      } else if (
        elem_on_the_cursor != null &&
        elem_on_the_cursor_id < available_pos &&
        elem_on_the_cursor != youtube_block_
      ) {
        // вставить елемент в начало
        console.log("вставить елемент в начало");

        container_for_inner_block.prepend(clone_elmnt);
      } else if (elem_on_the_cursor == null && youtube_block_) {
        youtube_block_.after(clone_elmnt);
      } else if (
        elem_on_the_cursor == null &&
        elem_on_the_cursor_id > count_elem_in_container_for_inner
      ) {
        // вставить в конец
        console.log("вставить в конец");
        container_for_inner_block.append(clone_elmnt);
      }

      drag_element(clone_elmnt);
      elmnt.remove();
      set_new_pos_for_all_block(".add-page__photo__container-for-loaded-files");
    }

    function get_pos_cursor_to_the_parent(event) {
      var bounds = event.target.parentNode.getBoundingClientRect();
      var x = event.clientX - bounds.left;
      var y = event.clientY - bounds.top;
      return {
        x: x,
        y: y
      };
    }
  }

  function toggle_yout_btn() {
    let alredy_loaded_count = get_pos_for_block(
      ".add-page__photo__container-for-loaded-files"
    );
    if (alredy_loaded_count == 0) {
      load_url_ytb_btn.style.display = "block";
    } else {
      load_url_ytb_btn.style.display = "none";
    }
  }

  function set_new_pos_for_all_block(selector) {
    // устанавливает нормальный порядок для всех блоков внутри селектора
    let container = document.querySelector(selector),
      container_elements = container.childNodes,
      pos = 0;
    container_elements.forEach((el) => {
      if (el.nodeName == "DIV") {
        el.setAttribute("data-pos", pos);
        pos += 1;
      }
    });
  }

  function insert_loaded_image_intu_block(new_block, input_with_files) {
    let curFiles = input_with_files.files;
    if (curFiles.length != 0) {
      // если файл загрузили
      // добавить картинку в new_block
      let image = new_block.querySelector("img");
      image.src = window.URL.createObjectURL(curFiles[0]);

      return new_block;
    } else {
      // если файл не был загружен
      return false;
    }
  }

  function get_count_loaded_files_or_url(selector) {
    let container = document.querySelector(selector);
    return container.querySelectorAll("div").length;
  }

  function get_pos_for_block(selector) {
    let container = document.querySelector(selector),
      container_elements = container.childNodes,
      container_blocks = [];
    container_elements.forEach((el) => {
      if (el.nodeName == "DIV") {
        container_blocks.push(el);
      }
    });
    return container_blocks.length;
  }

  function get_param_from_link(url) {
    let url_ = url.split("?").pop();
    var qa = [];
    for (var prs of url_.split("&")) {
      var pra = prs.split("=");
      qa[pra[0]] = pra[1];
    }
    return qa;
  }
}