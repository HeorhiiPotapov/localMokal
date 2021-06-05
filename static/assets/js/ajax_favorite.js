$(".add_to_favorites").click(function (e) {
	e.preventDefault();
	let prod_id = this.getAttribute("data-itemid");
	let img = $("#item-img-" + prod_id);
	let navIcon = $("#nav_fav_img");

	$.ajax({
		url: "/favorites/add_to_favorite/" + prod_id + "/",
		data: {
			product_id: prod_id
		},
		success: function (data) {
			let n = parseInt(favCount.text());
			if (data["is_favorite"] === true) {
				img.attr("src", imgLocation + "favorites_fill.svg");
				navIcon.attr("src", imgLocation + "favorites_fill.svg");
				favCount.text((n += 1));
			} else {
				if (window.location.pathname == '/favorites/favorite-list/') {
					// console.log(this)
					// deletion from favorite products list on render
				}
				img.attr("src", imgLocation + "favorites.svg");
				favCount.text((n -= 1));
			}
			if (n === 0) {
				navIcon.attr("src", imgLocation + "favorites.svg");
			}
		},
	});
});