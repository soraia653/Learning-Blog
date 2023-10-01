$(document).ready(function () {
    $('#photo').change(function () {
        var input = this;
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#user-photo')
                .attr('src', e.target.result)
                .attr('width', '150')
                .attr('height', '150')
                ;
            }

            reader.readAsDataURL(input.files[0]);
        }
    });
});