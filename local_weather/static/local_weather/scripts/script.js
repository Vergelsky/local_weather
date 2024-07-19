$(function () {

    $('[name="city"]').fias({
		type: $.fias.type.city,
        change: function (obj) {
            var address = $.fias.getAddress('.bs-component');

            $('#address').text(address);
        },
        'withParents' : true

    });


});