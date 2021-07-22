$(document).ready(function () {
    $('#id_replacement_employee').prop('disabled', true);
    $('#id_work_status').change(function() {
        let sel = $('#id_work_status option:selected').html()
        console.log(sel);
        if(sel === 'В отпуске'){
            $('#id_replacement_employee').prop('disabled', false);
            console.log($('#id_replacement_employee option:selected').html());
        }else{
            $('#id_replacement_employee').prop('disabled', true);
            $('#id_replacement_employee option:contains("---------")').prop('selected', true);
        }
        console.log($('#id_replacement_employee option:selected').html());
    })
})
