$("#add_coin").on("click", function () {
    $.get("/rpg/add_coin", function (data) {
        location.reload()
    })
});

$("#add_exp").on("click", function () {
    $.get("/rpg/add_exp", function (data) {
        location.reload()
    })
});

$("#give_coin").on("click", function () {
    console.log($(this).attr('data-to'))
    $.get("/rpg/"+$(this).attr('data-to')+"/give_coin", function (data) {
        location.reload()
    })
});