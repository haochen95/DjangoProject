
$(document).ready(function () {

    document.getElementById("btn").onclick = function () {
        $.ajax({
            type: "get",
            url: "/studentsinfo/",
            dataType: "json",
            success: function (data, status) {
                console.log(data)
            }
        })

    }
})