$('.add_to_favorites').click(function() {
    let prod_id = this.getAttribute('data-itemid')
    $.ajax({
      method: "GET",
      url: window.location.host + "/favorites/add_to_favorite" + prod_id,
      data: 'somedata', 
    });

//    $.ajax({
//        url: window.location.host + '/favorites/add_to_favorite' + prod_id,
//        data: { "product_id": prod_id},
//        async: false,
//        success: function( data ){
//        console.log(data)
//        }
//    })
})
